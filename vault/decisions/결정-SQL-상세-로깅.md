---
id: 결정-SQL-상세-로깅
title: SQL 로깅 — 예쁘게 포맷하고 바인딩 파라미터까지 출력
type: decision
namespace: personal
visibility: public
summary: 모든 SQL은 포맷팅(format_sql)된 형태로 자세히 출력하고, 바인딩 파라미터(binding) 값과 추출(extract) 값까지 로그에 보이게 설정한다.
auto_inject: false
applicable_when: 스프링부트 프로젝트의 JPA/하이버네이트 로깅을 설정할 때
confidence: 0.95
verified_at: 06/10/2026
verified_by: 장희성 (본인 구술)
staleness_signal: 운영 환경 로그 정책이 별도로 정해지거나 본인이 로깅 수준 변경을 지시하면 갱신
tags: ["SQL-로깅", "JPA", "하이버네이트", "SQL-포맷", "바인딩-파라미터", "스프링부트"]
edges: [
  {"target": "플레이북-스프링부트-표준-세팅", "type": "part_of", "weight": 0.8, "note": "표준 세팅의 로깅 설정 단계"}
]
related: ["[[플레이북-스프링부트-표준-세팅]]", "[[플레이북-스프링부트-프로파일-구성]]"]
source_url: "Empty"
---

# SQL 로깅 — 예쁘게 포맷하고 바인딩 파라미터까지 출력

## 결정 내용

JPA/하이버네이트가 실행하는 **모든 SQL을 자세히, 보기 좋게** 출력한다:

1. **SQL 출력 + 포맷팅** — `show-sql` 성격의 출력에 `hibernate.format_sql: true`를 더해 들여쓰기된 형태로 보이게 한다.
2. **바인딩 파라미터 표시** — `?`로만 보이는 값을 실제 값으로 확인할 수 있게 트레이스 로깅을 켠다 (예: `org.hibernate.orm.jdbc.bind: trace`, 구버전은 `BasicBinder`).
3. **추출(extract) 값까지** — 조회 결과 추출 로깅(`org.hibernate.orm.jdbc.extract: trace`)도 함께 켜서 값의 입출력 양쪽을 모두 본다.

## 근거

강의에서 JPA가 실제로 어떤 SQL을 어떤 값으로 실행하는지 학생이 눈으로 확인하는 것이 핵심 학습 포인트다. dev/test 프로파일([[플레이북-스프링부트-프로파일-구성]]) 양쪽에 적용한다.

---

*2026-06-10 본인 구술을 /convert-note로 분해하여 생성.*
