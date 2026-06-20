#!/usr/bin/env python3
"""Google Indexing API 색인 통보 (구글은 IndexNow 미참여).

주의: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 마크업 페이지를
대상으로 합니다. 일반 페이지에도 호출은 가능하나 효과는 보장되지 않으며, 일반
페이지의 정석 경로는 Search Console 등록 + sitemap.xml 제출입니다.

사전 준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드 → tools/service-account.json 로 저장
     (또는 환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 경로 지정)
  3) Search Console 속성 설정 → 사용자/소유자에 서비스 계정 이메일을 '소유자'로 추가
  4) 의존성:  pip install google-auth requests

사용법:
  python tools/google_index.py                # sitemap.xml 의 모든 URL
  python tools/google_index.py URL [URL ...]  # 지정 URL
  python tools/google_index.py --delete URL   # URL_DELETED 통보
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
CRED = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS",
                      os.path.join(ROOT, "tools", "service-account.json"))


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python build.py 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main(urls: list, notif_type: str) -> None:
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 누락: pip install google-auth requests")
    if not os.path.exists(CRED):
        sys.exit(f"서비스 계정 키가 없습니다: {CRED}\n  README(tools/README.md) 의 사전 준비를 참고하세요.")

    creds = service_account.Credentials.from_service_account_file(CRED, scopes=SCOPES)
    session = AuthorizedSession(creds)
    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": notif_type}, timeout=30)
        flag = "✅" if r.status_code == 200 else "⚠"
        print(f"  {flag} {r.status_code}  {u}")
        ok += r.status_code == 200
    print(f"\n{ok}/{len(urls)} 건 통보 완료 (type={notif_type})")
    print("일일 쿼터 기본 200건. 효과는 Search Console > URL 검사에서 확인하세요.")


if __name__ == "__main__":
    args = sys.argv[1:]
    notif = "URL_DELETED" if "--delete" in args else "URL_UPDATED"
    targets = [a for a in args if a.startswith("http")]
    main(targets or urls_from_sitemap(), notif)
