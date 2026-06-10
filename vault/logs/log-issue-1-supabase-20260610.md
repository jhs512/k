---
id: log-issue-1-supabase-20260610
type: log
operation: manual-node-creation
date: "2026-06-10T00:00:00"
namespace: personal
summary: "이슈 #1 처리: 수파베이스 작업 선호도 지식 3개 노드 생성 (decision×2, pattern×1)"
affected_nodes: ["decision-jang-supabase-cloud-over-local", "decision-jang-supabase-schema-env", "pattern-jang-supabase-members-table"]
tags: ["log", "supabase", "issue"]
---

이슈 #1 요청에 따라 수파베이스 관련 지식을 vault에 추가했다. 수파베이스 클라우드 선호 decision, 스키마 기반 환경 분리(public/dev/test) decision, public.members 테이블 중심 아키텍처 + auth.users 트리거 동기화 pattern 3개를 생성했다. 모든 노드는 authored_by로 contact-jang-heeseong에, 상호 related_to/followed_by 엣지로 연결했다. INDEX 갱신 완료.
