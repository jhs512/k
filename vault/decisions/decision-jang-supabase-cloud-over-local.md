---
id: decision-jang-supabase-cloud-over-local
title: "Supabase 작업 시 로컬 CLI보다 클라우드 환경을 선호"
type: decision
namespace: personal
visibility: namespace
summary: "수파베이스 프로젝트는 로컬 CLI 대신 Supabase 클라우드를 기본 작업 환경으로 사용한다."
auto_inject: false
applicable_when: "Supabase를 사용하는 프로젝트 세팅 및 개발 환경 결정 시"
confidence: 0.95
verified_at: "06/10/2026"
verified_by: "jang-heeseong"
staleness_signal: "로컬 CLI의 기능이 클라우드와 동등해지거나, 오프라인 개발 필요성이 생기면 재검토"
tags: ["supabase", "cloud", "cli", "환경설정", "데이터베이스"]
edges: [
  {"target": "contact-jang-heeseong", "type": "authored_by", "weight": 1.0, "note": "장희성의 개인 기술 선호 결정"},
  {"target": "pattern-jang-supabase-schema-env", "type": "followed_by", "weight": 0.9, "note": "클라우드 기반이기 때문에 스키마 분리 패턴을 바로 적용 가능"}
]
related: ["[[pattern-jang-supabase-schema-env]]", "[[pattern-jang-supabase-members-table]]"]
source_url: "Empty"
---

# Supabase 작업 시 로컬 CLI보다 클라우드 환경을 선호

Supabase 프로젝트를 시작하거나 작업할 때, 로컬 Docker 기반의 Supabase CLI 환경보다 **Supabase 클라우드(supabase.com)**를 기본 작업 공간으로 사용한다.

## 결정 근거

- 로컬 CLI는 Docker 설치와 초기 세팅에 시간이 걸리고, 팀 협업 시 환경 차이가 발생할 수 있다.
- 클라우드 환경은 대시보드에서 스키마, 테이블, RLS 정책, 트리거 등을 시각적으로 관리할 수 있어 생산성이 높다.
- Supabase 클라우드의 무료 티어로도 개발/테스트 환경을 충분히 운영할 수 있다.
- 스키마 기반 환경 분리(public/dev/test)를 단일 Supabase 프로젝트 안에서 구현할 수 있다.

## 트레이드오프

로컬 CLI는 완전한 오프라인 작업과 CI/CD 파이프라인 자동화에 유리하지만, 개인 프로젝트나 강의 목적에서는 클라우드의 편의성이 더 크다.
