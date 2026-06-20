#!/usr/bin/env python3
"""원클릭 발행 — 빌드 후 IndexNow(빙·네이버)로 즉시 색인 통보.

사용법:
  python tools/publish.py                 # 빌드 + 전체 URL IndexNow 통보
  python tools/publish.py URL [URL ...]   # 빌드 + 지정 URL만 통보(글 1건 추가 시)
  python tools/publish.py --google        # 위 + 구글 Indexing API 통보(자격증명 필요)

글을 새로 올렸다면: content/ 수정 → python tools/publish.py "<새 글 URL>" 한 줄이면
빌드와 빙·네이버 색인 통보가 한 번에 끝납니다.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    return subprocess.call([sys.executable, *cmd], cwd=ROOT)


if __name__ == "__main__":
    args = sys.argv[1:]
    use_google = "--google" in args
    urls = [a for a in args if a.startswith("http")]

    if run(["build.py"]) != 0:
        sys.exit("빌드 실패")

    run(["tools/indexnow.py", *urls])
    if use_google:
        run(["tools/google_index.py", *urls])
