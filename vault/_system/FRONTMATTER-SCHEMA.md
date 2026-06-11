# 프론트매터 스키마 레퍼런스

vault의 모든 노드는 마크다운 파일 상단에 프론트매터 블록을 포함해야 한다. **필수(required)** 로 표시된 필드는 의무이며, **선택(optional)** 필드는 생략할 수 있지만 가능하면 채워야 한다.

---

## 전체 필드 명세

### id
- **타입:** string
- **형식:** 케밥 케이스의 `타입-슬러그` (예: `hyp-creators-will-pay-29mo`)
- **필수:** 예
- **비고:** vault 전체에서 유일해야 한다. 노드 타입 접두사와 설명적 슬러그를 조합한다. 공백 금지, 대문자 금지(슬러그 내 약어 제외).

### title
- **타입:** string
- **필수:** 예
- **비고:** 사람이 읽을 수 있는 5–80자. 같은 타입의 노드 사이에서 구별 가능해야 한다.

### type
- **타입:** string
- **필수:** 예
- **허용 값:** 다음 중 정확히 하나: `pillar`, `decision`, `concept`, `question`, `playbook`, `task`, `event`, `pattern`, `hypothesis`, `fact`, `source`, `bookmark`, `note`, `contact`, `reference`, `custom`, `log`
- **비고:** `NODE-TYPES.md`의 정식 명칭과 정확히 일치해야 한다 (소문자, 단수).

### namespace
- **타입:** string
- **필수:** 예
- **비고:** 프로젝트·팀·도메인 영역을 나타낸다. 케밥 케이스 사용 (예: `product-ops`, `growth`, `infra`). 범위 필터링을 가능하게 하고 네임스페이스 간 충돌을 줄인다.

### visibility
- **타입:** string
- **필수:** 예
- **허용 값:** 다음 중 정확히 하나: `public`, `namespace`, `private`, `system`
- **기본값:** `namespace`
- **비고:** AI 에이전트가 검색 시 노드를 사용할 수 있는 시점을 제어한다. 폭넓게 재사용 가능한 지식은 `public`, 해당 네임스페이스 안에서만 쓸 콘텐츠는 `namespace`, 민감하거나 개인적인 자료는 `private`, vault 지침이나 에이전트용 운영 규칙은 `system`.

### summary
- **타입:** string
- **필수:** 예
- **길이:** 최대 1–2문장 (200자 이내 권장)
- **비고:** 그래프를 스캔하는 AI 에이전트를 위해 작성한다. 핵심 아이디어를 한눈에 전달해야 한다. concept 노드에 정의되지 않은 전문용어는 피한다.

### auto_inject
- **타입:** boolean
- **필수:** 예
- **허용 값:** `true` 또는 `false`
- **비고:** `true`이면 시스템이 이 노드에 관련 콘텐츠나 트리거를 자동 삽입할 수 있다. 자동화 훅 용도로 명시 설계된 경우가 아니면 `false`를 기본값으로.

### applicable_when
- **타입:** string
- **기본값:** `"Empty"`
- **비고:** 이 노드가 유의미해지는 맥락이나 트리거 조건을 기술한다. 노드가 보편적으로 적용되거나 맥락 독립적이면 `"Empty"`를 사용한다.

### confidence
- **타입:** float
- **범위:** 0.0 ~ 1.0
- **필수:** 예
- **비고:** 노드의 정확성·유효성에 대한 저자의 확신을 반영한다. 1.0 = 확실, 0.0 = 순수 추측. 증거가 쌓이면 재검토하고 갱신한다.

### verified_at
- **타입:** string (날짜)
- **형식:** `MM/DD/YYYY`
- **기본값:** `"Empty"`
- **비고:** 사람이 노드의 내용이나 결론을 마지막으로 검토·확인한 날짜. 첫 검증 전까지는 `"Empty"`.

### verified_by
- **타입:** string
- **기본값:** `"Empty"`
- **비고:** 이 노드를 마지막으로 검증한 사람의 이름 또는 id. 검증 전까지는 `"Empty"`.

### staleness_signal
- **타입:** string
- **필수:** 예
- **비고:** 충족되면 이 노드가 낡았거나 틀렸거나 무효화되었을 수 있음을 나타내는, 구체적이고 관측 가능한 조건. 조건문 형태로 작성한다 (예: "매출 성장률이 두 분기 연속 5% 아래로 떨어지면 이 가정을 재평가"). 에이전트는 staleness signal을 모니터링해야 한다.

### tags
- **타입:** string 배열
- **필수:** 예
- **비고:** 배열 문법: `["태그-하나", "태그-둘"]`. 태그는 소문자 케밥 케이스. 관련 태그 2–8개를 포함한다. 필터링과 상호 참조에 사용된다.

### edges
- **타입:** JSON 객체 배열
- **필수:** 예
- **구조:** 각 객체는 정확히 4개의 키를 가져야 한다:

| 키 | 타입 | 비고 |
|---|---|---|
| `target` | string | 대상 노드의 `id` |
| `type` | string | `EDGE-TYPES.md`의 10개 엣지 타입 중 하나 |
| `weight` | float | 관계 강도, 0.0 ~ 1.0 |
| `note` | string | 연결에 대한 간단한 설명 |

- **예:**

```yaml
edges: [
  {"target": "pillar-example-philosophy", "type": "related_to", "weight": 0.7, "note": "이 결정의 근거를 제공"}
]
```

### related
- **타입:** string 배열
- **필수:** 아니오
- **비고:** 정식 엣지까지는 필요 없는 가벼운 상호 참조용 위키링크(`[[노드 제목]]`) 또는 노드 id. 탐색과 브라우징에 유용하다.

### source_url
- **타입:** string
- **기본값:** `"Empty"`
- **비고:** 이 노드의 출처가 된 외부 리소스의 URL. 출처가 없으면 `"Empty"`.

---

## 프론트매터 블록 예시

```yaml
---
id: hyp-creators-will-pay-29mo
title: 크리에이터는 29개월 후 분석 도구에 돈을 낸다
type: hypothesis
namespace: product-ops
visibility: namespace
summary: 29개월 이상 꾸준히 게시해 온 크리에이터는 신규 크리에이터보다 유료 분석 티어로 전환할 가능성이 높다.
auto_inject: false
applicable_when: 크리에이터 수익화 전략을 평가할 때
confidence: 0.65
verified_at: 03/15/2026
verified_by: Alice Chen
staleness_signal: 무료 티어 리텐션이 12개월 시점에 60%를 넘으면 재평가
tags: ["크리에이터-이코노미", "수익화", "분석", "전환"]
edges: [
  {"target": "fact-cohort-retention-q4", "type": "derived_from", "weight": 0.8, "note": "코호트 데이터가 이 가설의 직접 근거"},
  {"target": "decision-analytics-pricing", "type": "contradicts", "weight": 0.5, "note": "가격 모델은 더 짧은 전환 기간을 가정"}
]
related: ["[[fact-cohort-retention-q4]]", "decision-analytics-pricing"]
source_url: "Empty"
---
```

---

---

## 로그 노드 스키마

`log` 노드는 토큰 비용을 최소화하도록 설계된 축소 스키마를 사용한다. 로그 노드에는 전체 프론트매터 체크리스트를 적용하지 **않는다**.

### 필드

| 필드 | 타입 | 비고 |
|---|---|---|
| `id` | string | 형식: `log-[작업]-[YYYYMMDD-HHmmss]` (예: `log-convert-note-20260515-143022`) |
| `type` | string | 항상 `log` |
| `operation` | string | 다음 중 하나: `convert-note`, `query-vault`, `organize-vault`, `vault-health`, `init-vault` |
| `date` | string | ISO 8601: `"YYYY-MM-DDTHH:MM:SS"` |
| `namespace` | string | 영향받은 네임스페이스, 전역이면 `"vault"` |
| `summary` | string | 한 문장, 150자 이내 |
| `affected_nodes` | array | 생성·수정된 노드 ID. 없으면 빈 배열 `[]`. |
| `tags` | array | 항상 `"log"`와 작업 이름을 포함 |

### 예시

```yaml
---
id: log-convert-note-20260515-143022
type: log
operation: convert-note
date: "2026-05-15T14:30:22"
namespace: personal
summary: "raw/karpathy-llm-wiki.md 처리 → 노드 3개 생성 (concept, source, fact)"
affected_nodes: ["concept-llm-wiki-pattern", "source-karpathy-llm-wiki", "fact-rag-vs-compounding"]
tags: ["log", "convert-note"]
---
```

### 본문

로그 본문은 30–80단어. 무엇이 실행됐고, 무엇이 바뀌었고, 특기할 발견이나 오류가 있었는지를 다룬다. 마크다운 헤더 없이 평문으로.

### 규칙

- 로그 노드는 생성 후 **절대 편집하지 않는다**.
- 로그 노드는 `_system/INDEX.md`에 **인덱싱하지 않는다** — `logs/` 폴더는 자기완결적이다.
- 로그 노드는 `/vault-health`의 **confidence 감쇠 대상이 아니다**.
- 로그 노드는 암묵적으로 `visibility: system`이다 — 에이전트는 질의 답변에 사용하지 않는다.

---

## 필드별 검증 체크리스트

- [ ] `id`가 유일하고, 케밥 케이스이며, 타입 접두사가 있다
- [ ] `title`이 비어 있지 않고 사람이 읽을 수 있다
- [ ] `type`이 16개 정식 타입 중 하나와 일치한다
- [ ] `namespace`가 케밥 케이스다
- [ ] `visibility`가 `public`, `namespace`, `private`, `system` 중 하나다
- [ ] `summary`가 1–2문장, 200자 이내다
- [ ] `auto_inject`가 boolean이다
- [ ] `applicable_when`이 문자열 또는 `"Empty"`다
- [ ] `confidence`가 0.0과 1.0 사이다
- [ ] `verified_at`이 MM/DD/YYYY 또는 `"Empty"`다
- [ ] `verified_by`가 문자열 또는 `"Empty"`다
- [ ] `staleness_signal`이 비어 있지 않은 조건문이다
- [ ] `tags`가 비어 있지 않은 케밥 케이스 문자열 배열이다
- [ ] `edges`가 `target`, `type`, `weight`, `note`를 가진 객체의 비어 있지 않은 배열이다
- [ ] `related`가 위키링크 또는 id 배열이다 (선택)
- [ ] `source_url`이 URL 문자열 또는 `"Empty"`다
