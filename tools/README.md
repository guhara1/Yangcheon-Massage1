# 색인 자동화 (IndexNow · Google Indexing API)

생성되는 색인 파일(빌드 시 자동):

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 전체 색인 URL + `lastmod` (구글·네이버 공통) |
| `rss.xml` | RSS 2.0 피드 — HTML `<head>`에 자동발견 링크 포함 |
| `robots.txt` | 전체 허용 + `Sitemap:` 위치 명시 |
| `7b1e4a9c…a4b8.txt` | IndexNow 키 파일 (루트에 배포돼야 함) |

키는 `content/site.py`의 `INDEXNOW_KEY`. 바꾸면 `python build.py` 재실행 시 새 키 파일이 생성됩니다.

---

## 가장 빠른 색인 흐름

### 1. 첫 일괄 통보 (배포 직후 1회)
```bash
python build.py            # sitemap·rss·robots·키파일 생성
python tools/indexnow.py   # 모든 URL을 빙·네이버·얀덱스에 즉시 통보
```

### 2. 글/페이지를 새로 올릴 때마다
```bash
python tools/publish.py "https://yangcheon-massage1.pages.dev/magazine/새글/"
```
→ 빌드 + 해당 URL을 빙·네이버에 즉시 통보까지 한 줄로 끝.
인자를 비우면(`python tools/publish.py`) 전체 URL을 통보합니다.

### 3. 구글까지 (선택)
구글은 IndexNow에 참여하지 않습니다. 두 가지 경로가 있습니다.

- **정석:** Google Search Console에 사이트 등록 → `sitemap.xml` 제출 (가장 안정적)
- **API:** Indexing API (아래 준비 후) `python tools/google_index.py`
  ```bash
  python tools/publish.py --google      # IndexNow + 구글 한 번에
  ```

---

## IndexNow (빙·네이버·얀덱스)
- 한 번의 요청이 IndexNow 참여 엔진 전체로 전파됩니다(빙·네이버·얀덱스·Seznam 등).
- 키 파일(`{KEY}.txt`)이 사이트 루트에서 200으로 응답해야 인증됩니다. 배포 후
  `https://yangcheon-massage1.pages.dev/7b1e4a9c2d8f43e6b0a5c9d1e7f2a4b8.txt` 접속 확인.
- 의존성 없음(파이썬 표준 라이브러리만 사용).

## Google Indexing API
> 공식 대상은 JobPosting·BroadcastEvent 페이지입니다. 일반 페이지에도 호출은
> 되지만 효과가 보장되지 않으므로, 일반 페이지는 Search Console + sitemap이 정석입니다.

준비:
1. Google Cloud → **Indexing API** 사용 설정
2. 서비스 계정 생성 → JSON 키 다운로드 → `tools/service-account.json` 저장
   (또는 env `GOOGLE_APPLICATION_CREDENTIALS`에 경로 지정). 이 파일은 `.gitignore` 처리됨.
3. Search Console 속성 → 설정 → 사용자 및 권한 → 서비스 계정 이메일을 **소유자**로 추가
4. `pip install google-auth requests`
5. `python tools/google_index.py`

---

## sitemap ping 관련 (중요)
- **구글·빙의 `ping?sitemap=` 엔드포인트는 2023년에 모두 폐기**되었습니다(404 응답).
  더 이상 동작하지 않으므로 별도 ping 스크립트를 두지 않았습니다.
- 그 자리를 대체하는 실시간 통보가 **IndexNow**(빙·네이버)와 **Indexing API**(구글)입니다.
- 구글에 sitemap을 알리는 현재 방법은 **Search Console에서 sitemap 직접 제출**입니다.

## 수동으로 한 번 해두면 좋은 것
- **Naver Search Advisor**(searchadvisor.naver.com): 사이트 등록 + 사이트맵/RSS 제출.
  메인페이지에 네이버 인증 메타태그는 이미 삽입돼 있습니다.
- **Google Search Console**: 사이트 등록 + `sitemap.xml` 제출.
