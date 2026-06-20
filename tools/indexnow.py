#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 등 IndexNow 참여 엔진에 URL을 통보한다.

IndexNow 는 한 번의 요청으로 참여 검색엔진 전체에 전파된다(빙·네이버·얀덱스·Seznam 등).
구글은 IndexNow 미참여이므로 tools/google_index.py 를 별도로 사용한다.

사용법:
    python tools/indexnow.py                 # sitemap.xml 의 모든 URL 통보(첫 일괄 통보)
    python tools/indexnow.py URL [URL ...]   # 지정한 URL만 통보(글 1건 올렸을 때)

키 파일: 빌드 시 루트에 {INDEXNOW_KEY}.txt 가 생성되어 배포돼야 한다.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ENDPOINT = "https://api.indexnow.org/indexnow"
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE)


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python build.py 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls: list) -> None:
    if not urls:
        sys.exit("통보할 URL이 없습니다.")
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow → {ENDPOINT}")
    print(f"  host={HOST}  key=...{INDEXNOW_KEY[-6:]}  urls={len(urls)}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  HTTP {resp.status} {resp.reason}  ✅ (빙·네이버·얀덱스로 전파)")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")
        # 200/202 = 정상, 400=형식오류, 403=키불일치, 422=URL/키 위치 불일치
        print(f"  HTTP {e.code} {e.reason}\n  {body}")
        if e.code not in (200, 202):
            sys.exit(1)
    except urllib.error.URLError as e:
        sys.exit(f"  네트워크 오류: {e.reason}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    submit(args or urls_from_sitemap())
