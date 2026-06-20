# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 방문형 사이트라 LocalBusiness Schema는 쓰지 않고 Organization·WebPage·FAQPage만 사용한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "logo": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/icon-512.png",
    "width": 512,
    "height": 512
  }},
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "서울 양천구 목동·신월동·신정동 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 양천구"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "양천구 출장마사지｜목동·신월·신정 홈타이 지역 안내",
  "url": "{BASE_URL}/",
  "description": "양천구 출장마사지·홈타이 예약 전 목동, 신월동, 신정동, 오목교, 신정네거리 생활권을 확인하세요.",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "publisher": {{ "@type": "Organization", "name": "{BRAND}", "url": "{BASE_URL}/" }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "양천구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 목동, 신월동, 신정동 대표 동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "오목교역이나 신정네거리역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "오목교역, 목동역, 신정역, 신정네거리역, 양천구청역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "목1동, 신정5동처럼 번호 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "목1~5동, 신월1~7동, 신정1·2·3·4·6·7동은 각각 목동·신월동·신정동 대표 페이지에서 통합 안내합니다. 신정5동은 행정동 목록에서 제외했습니다. 중복 페이지 위험을 줄이기 위한 운영 기준입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "신월동처럼 역이 먼 지역도 방문되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "역과의 거리는 방문 가능 여부와 무관합니다. 신월동은 차량 이동으로 방문하며, 위치에 따라 추가 이동비가 있을 수 있어 예약 시 총비용으로 먼저 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "홈타이는 집에서 받는 타이마사지를 가리키는 말로 출장마사지의 대표 형태입니다. 자세한 차이와 이용 기준은 양천구 홈타이 이용 가이드에서 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 양천구 전지역</p>
    <h1>양천구 출장마사지 · 양천구 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>목동·신월동·신정동 자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/seoul/yangcheon-gu/">지역별 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>3개</strong><span>대표 지역</span></li>
      <li><strong>7개</strong><span>역세권 안내</span></li>
      <li><strong>10개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>양천구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>양천구 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 양천구는 서울 서남권 자치구로, 목동 학원가와 목동아파트 중심 생활권, 오목교역과 목동역 주변 역세권, 신정네거리역과 양천구청역을 중심으로 한 신정동 생활권, 신월동 주거지와 서서울호수공원 인접 생활권이 함께 있는 지역입니다. 그래서 이 사이트는 "양천 전지역 가능"만 적는 방식 대신 목동·신월동·신정동을 나누어 안내합니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 분명하게 안내해 드립니다. 방문 가능 여부는 행정동 경계가 아니라 실제 위치와 예약 시간으로 판단하므로, 예약 시 정확한 도로명 주소만 알려주시면 됩니다.</p>
</section>

<section id="diff">
<h2>목동·신월동·신정동 생활권 차이</h2>
<p>같은 양천구라도 동마다 주거 형태와 생활 리듬이 다릅니다. 목동은 학원가와 대단지 아파트, 오목교역·목동역 역세권이 모인 양천구의 대표 생활권으로 역세권 접근성이 좋습니다. 신월동은 지하철보다 도로 이동이 중심인 서남부 주거 생활권이라 차량 이동 기준과 추가 이동비를 조금 더 분명하게 안내합니다. 신정동은 신정역·신정네거리역·양천구청역을 끼고 있는 행정·주거 생활권으로 역세권이 여러 갈래로 분산되어 있습니다. 본인 생활권과 가까운 대표 동 페이지를 고르시면 방문 환경과 예약 기준을 한 번에 확인하실 수 있습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 양천구 대표 동 기준으로 구성됩니다. 각 페이지에서는 생활권 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간, 어울리는 테마를 동마다 고유한 내용으로 설명합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/seoul/yangcheon-gu/mok-dong/">목동</a></li>
<li><a href="/seoul/yangcheon-gu/sinwol-dong/">신월동</a></li>
<li><a href="/seoul/yangcheon-gu/sinjeong-dong/">신정동</a></li>
</ul>
<p>목동은 양천구에서 검색 의도가 가장 넓은 대표 생활권으로 <a href="/seoul/yangcheon-gu/mok-dong/">목동 출장마사지 방문 관리 안내</a>에서 학원가·아파트·운동장 생활권을 함께 다룹니다. 서남부 주거지는 <a href="/seoul/yangcheon-gu/sinwol-dong/">신월동 출장마사지 방문 관리 안내</a>에서 서서울호수공원·까치산 인접권을, 행정·주거 생활권은 <a href="/seoul/yangcheon-gu/sinjeong-dong/">신정동 출장마사지 방문 관리 안내</a>에서 신정네거리역·양천구청역 생활권을 확인하실 수 있습니다. 양천구 전체 구조는 <a href="/seoul/yangcheon-gu/">양천구 지역별 안내</a>에서 한눈에 보실 수 있습니다.</p>
</section>

<section id="stations">
<h2>오목교역·목동역·신정네거리역·양천구청역 역세권 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 편하시면 역세권 안내를 참고하세요. 양천구를 지나는 5호선(오목교·목동·신정)과 2호선(신정네거리·양천구청)을 중심으로 역마다 한 페이지씩 안내하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 까치산역과 등촌역은 강서구 경계 성격이 강해 양천구에서는 인접 생활권으로만 다룹니다.</p>
<ul class="card-grid">
<li><a href="/seoul/yangcheon-gu/station/omokgyo-station/">오목교역</a></li>
<li><a href="/seoul/yangcheon-gu/station/mok-dong-station/">목동역</a></li>
<li><a href="/seoul/yangcheon-gu/station/sinjeong-station/">신정역</a></li>
<li><a href="/seoul/yangcheon-gu/station/sinjeongnegeori-station/">신정네거리역</a></li>
<li><a href="/seoul/yangcheon-gu/station/yangcheon-gu-office-station/">양천구청역</a></li>
<li><a href="/seoul/yangcheon-gu/station/kkachisan-nearby-area/">까치산역 인접</a></li>
<li><a href="/seoul/yangcheon-gu/station/deungchon-nearby-area/">등촌역 인접</a></li>
</ul>
<p>역세권 전체 구성은 <a href="/seoul/yangcheon-gu/station/">양천구 역세권별 방문 관리 안내</a>에서, 학원가·아파트·운동장처럼 더 세밀한 위치 기준은 <a href="/seoul/yangcheon-gu/area/">양천구 생활권별 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>양천구 홈타이 예약 전 확인사항</h2>
<p>양천구 출장마사지·홈타이 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하는 것이 좋습니다. 오목교역과 목동역처럼 접근성이 좋은 지역도 있지만, 신월동 일부 주거지와 서서울호수공원 인접권은 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 양천구 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 홈타이와 출장마사지의 차이, 코스 선택 기준, 처음 이용 안내는 <a href="/massage/">양천구 홈타이 이용 가이드</a>에서, 예약 절차는 <a href="/reservation/">예약안내</a>에서, 준비사항은 <a href="/guide/">이용 전 확인사항</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="dedup">
<h2>양천구 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 검색 노출용 페이지를 무리하게 늘리는 대신 중복을 줄이는 구조로 운영합니다. 목1동부터 목5동, 신월1동부터 신월7동, 신정1·2·3·4·6·7동을 각각 만들지 않고 목동·신월동·신정동 대표 페이지로 통합하며, 신정5동은 행정동 목록에서 제외했습니다. 역은 역명 기준 1개 URL만 두고 출구별·노선별로 쪼개지 않으며, 지역·역·테마를 조합한 도어웨이 페이지도 만들지 않습니다. 메뉴명과 URL에는 키워드를 반복하지 않고, 같은 본문에서 지역명만 바꾸는 방식도 쓰지 않습니다. 페이지 수보다 페이지당 정확도를 택한 구조입니다.</p>
</section>

<section id="how">
<h2>양천구 출장마사지 사이트 이용 방법</h2>
<p>양천구 메인페이지는 구 전체 안내를 담당하고, 대표동 페이지는 목동·신월동·신정동 검색을, 역세권 페이지는 오목교역·목동역·신정역·신정네거리역·양천구청역 검색을 담당합니다. 생활권 페이지는 목동 학원가, 목동아파트, 신월동 주거지, 신정네거리, 양천구청 인근처럼 사용자가 위치를 더 쉽게 찾도록 돕습니다. 관리 유형이 먼저 궁금하시면 <a href="/themes/">테마별 안내</a>와 <a href="/courses/">코스안내</a>를, 운영 기준과 작성 원칙이 궁금하시면 <a href="/about/">운영자 소개</a>를 참고해 주세요. 고민되시면 예약 전화에서 상태를 말씀해 주시면 함께 정해 드립니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>양천구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 목동, 신월동, 신정동 대표 동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>오목교역이나 신정네거리역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>목1동, 신정5동처럼 번호 동은 왜 따로 없나요?</h3>
<p>목1~5동, 신월1~7동, 신정1·2·3·4·6·7동은 각각 대표 동 페이지에서 통합 안내합니다. 신정5동은 행정동 목록에서 제외했습니다. 중복 페이지 위험을 줄이기 위한 기준입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>양천구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "양천구 출장마사지｜목동·신월·신정 홈타이 지역 안내",
    "desc": "양천구 출장마사지·홈타이 예약 전 목동, 신월동, 신정동, 오목교, 신정네거리 생활권을 확인하세요.",
    "h1": "양천구 출장마사지 · 양천구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
