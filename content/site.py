# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.gandago.example.com"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 텔레그램 문의 채널 (웹사이트 제작문의·제휴문의 공용)
TELEGRAM = "https://t.me/googleseolab"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("홈타이 가이드", "/massage/", [
        ("홈타이란?", "/massage/#hometai"),
        ("출장마사지와 홈타이 차이", "/massage/#diff"),
        ("양천구 이용 기준", "/massage/#coverage"),
        ("지역별 이동 기준", "/massage/#move"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("처음 이용 안내", "/massage/#first"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/seoul/yangcheon-gu/", [
        ("양천구 전체", "/seoul/yangcheon-gu/"),
        ("목동", "/seoul/yangcheon-gu/mok-dong/"),
        ("신월동", "/seoul/yangcheon-gu/sinwol-dong/"),
        ("신정동", "/seoul/yangcheon-gu/sinjeong-dong/"),
    ]),
    ("역세권 안내", "/seoul/yangcheon-gu/station/", [
        ("역 전체", "/seoul/yangcheon-gu/station/"),
        ("오목교역", "/seoul/yangcheon-gu/station/omokgyo-station/"),
        ("목동역", "/seoul/yangcheon-gu/station/mok-dong-station/"),
        ("신정역", "/seoul/yangcheon-gu/station/sinjeong-station/"),
        ("신정네거리역", "/seoul/yangcheon-gu/station/sinjeongnegeori-station/"),
        ("양천구청역", "/seoul/yangcheon-gu/station/yangcheon-gu-office-station/"),
        ("까치산역 인접 생활권", "/seoul/yangcheon-gu/station/kkachisan-nearby-area/"),
        ("등촌역 인접 생활권", "/seoul/yangcheon-gu/station/deungchon-nearby-area/"),
    ]),
    ("생활권 안내", "/seoul/yangcheon-gu/area/", [
        ("생활권 전체", "/seoul/yangcheon-gu/area/"),
        ("목동 학원가", "/seoul/yangcheon-gu/area/mok-dong-academy/"),
        ("목동아파트", "/seoul/yangcheon-gu/area/mok-dong-apartment/"),
        ("오목교·목동운동장", "/seoul/yangcheon-gu/area/omokgyo-stadium/"),
        ("목동역·목동오거리", "/seoul/yangcheon-gu/area/mok-dong-five-way/"),
        ("신정네거리·신정동", "/seoul/yangcheon-gu/area/sinjeongnegeori-sinjeong/"),
        ("양천구청·신정동", "/seoul/yangcheon-gu/area/yangcheon-office-sinjeong/"),
        ("신월동 주거지", "/seoul/yangcheon-gu/area/sinwol-residential/"),
        ("서서울호수공원·신월", "/seoul/yangcheon-gu/area/west-seoul-lake-park-sinwol/"),
        ("까치산·신월 인접", "/seoul/yangcheon-gu/area/kkachisan-sinwol/"),
        ("안양천·목동 인접", "/seoul/yangcheon-gu/area/anyangcheon-mok-dong/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
