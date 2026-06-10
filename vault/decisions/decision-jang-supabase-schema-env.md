---
id: decision-jang-supabase-schema-env
title: "수파베이스 클라우드 내 스키마로 환경 분리 (public/dev/test)"
type: decision
namespace: personal
visibility: public
summary: "단일 수파베이스 클라우드 프로젝트에서 스키마를 이용해 public=production, dev=dev, test=test 로 환경을 분리한다."
auto_inject: false
applicable_when: "수파베이스 프로젝트에서 환경별 DB 구성을 설계할 때"
confidence: 0.9
verified_at: "06/10/2026"
verified_by: "jang-heeseong"
staleness_signal: "수파베이스가 프로젝트 브랜칭 기능을 정식 지원해 스키마 분리가 불필요해질 때"
tags: ["supabase", "schema", "environment", "database", "multi-env"]
edges: [
  {"target": "contact-jang-heeseong", "type": "authored_by", "weight": 1.0, "note": "장희성의 수파베이스 스키마 환경 분리 전략"},
  {"target": "decision-jang-supabase-cloud-over-local", "type": "preceded_by", "weight": 0.9, "note": "클라우드 선호 결정 이후 자연스럽게 따라오는 스키마 분리 전략"},
  {"target": "pattern-jang-supabase-members-table", "type": "related_to", "weight": 0.8, "note": "각 스키마에서 members 테이블 패턴이 동일하게 적용된다"}
]
related: ["[[수파베이스 클라우드 환경 선호]]", "decision-jang-supabase-cloud-over-local"]
source_url: "Empty"
---

# 수파베이스 클라우드 내 스키마로 환경 분리 (public/dev/test)

단일 수파베이스 클라우드 프로젝트 안에서 PostgreSQL 스키마를 활용해 환경을 분리한다.

## 스키마 매핑

| 스키마 | 환경 | 용도 |
|---|---|---|
| `public` | Production | 실제 서비스 데이터 |
| `dev` | Development | 개발 중 테이블/기능 실험 |
| `test` | Test | 자동화 테스트용 격리 데이터 |

## 이유

별도 프로젝트를 환경마다 생성하면 비용이 증가하고 관리 복잡도가 높아진다. 스키마 분리는 PostgreSQL의 기본 기능이므로 추가 비용 없이 환경 격리를 달성할 수 있다.

## 주의사항

- RLS(Row Level Security) 정책은 스키마 단위로 별도 설정해야 한다.
- 수파베이스 Auth는 `auth` 스키마를 공유하므로, 테스트 시 사용자 데이터 격리에 유의한다.
- 각 스키마의 `members` 테이블은 `auth.users` 트리거 연동 구조를 동일하게 유지한다.
