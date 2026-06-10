---
id: pattern-jang-supabase-schema-env
title: "Supabase 스키마로 환경(production/dev/test) 분리"
type: pattern
namespace: personal
visibility: namespace
summary: "단일 Supabase 프로젝트 안에서 public=production, dev=개발, test=테스트 스키마로 환경을 분리한다."
auto_inject: false
applicable_when: "Supabase 클라우드 프로젝트에서 환경별 DB 분리가 필요할 때"
confidence: 0.9
verified_at: "06/10/2026"
verified_by: "jang-heeseong"
staleness_signal: "Supabase가 공식적으로 여러 환경을 지원하는 브랜치 기능을 안정화하면 재검토"
tags: ["supabase", "schema", "환경분리", "production", "dev", "test", "데이터베이스"]
edges: [
  {"target": "decision-jang-supabase-cloud-over-local", "type": "depends_on", "weight": 0.9, "note": "클라우드 기반 작업 결정의 구체적 구현 패턴"},
  {"target": "pattern-jang-supabase-members-table", "type": "related_to", "weight": 0.85, "note": "members 테이블 패턴도 이 스키마 분리 위에서 적용됨"},
  {"target": "contact-jang-heeseong", "type": "authored_by", "weight": 1.0, "note": "장희성의 Supabase 운영 패턴"}
]
related: ["[[decision-jang-supabase-cloud-over-local]]", "[[pattern-jang-supabase-members-table]]"]
source_url: "Empty"
---

# Supabase 스키마로 환경(production/dev/test) 분리

하나의 Supabase 클라우드 프로젝트 안에서 **PostgreSQL 스키마**를 활용해 환경을 분리한다.

## 스키마 구조

| 스키마 | 역할 |
|---|---|
| `public` | **Production** — 실제 서비스 데이터 |
| `dev` | **Development** — 개발 중 실험 및 기능 구현 |
| `test` | **Test** — 자동화 테스트 및 QA |

## 구현 방식

- 각 스키마에 동일한 테이블 구조를 복제하거나, 스키마별 필요에 따라 다르게 관리한다.
- 애플리케이션 연결 시 `search_path`를 환경에 맞게 설정하거나, 쿼리에서 `schema.table` 형식으로 명시한다.
- Supabase 대시보드의 Schema Editor에서 스키마를 생성하고 테이블을 관리한다.

## 장점

- 별도의 Supabase 프로젝트를 여러 개 만들 필요 없이 한 프로젝트에서 환경 분리가 가능하다.
- 무료 티어 제한(프로젝트 수 제한) 안에서 효율적으로 운영할 수 있다.
- 스키마 간 데이터를 쿼리로 직접 비교하거나 마이그레이션할 수 있다.
