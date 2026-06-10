---
id: pattern-jang-supabase-members-table
title: "수파베이스 public.members 테이블 중심 아키텍처 + auth.users 트리거 동기화"
type: pattern
namespace: personal
visibility: public
summary: "public 스키마의 모든 테이블은 auth.users 대신 public.members에 의존하도록 설계하고, auth.users와 public.members 간 동기화는 트리거로 처리한다."
auto_inject: false
applicable_when: "수파베이스 프로젝트에서 사용자 참조 테이블 및 FK 설계를 결정할 때"
confidence: 0.9
verified_at: "06/10/2026"
verified_by: "jang-heeseong"
staleness_signal: "수파베이스 Auth 구조가 크게 변경되거나 public.members 추상화 방식이 비효율적으로 판명될 때"
tags: ["supabase", "postgresql", "members", "auth", "trigger", "foreign-key", "architecture"]
edges: [
  {"target": "contact-jang-heeseong", "type": "authored_by", "weight": 1.0, "note": "장희성의 수파베이스 사용자 테이블 설계 패턴"},
  {"target": "decision-jang-supabase-cloud-over-local", "type": "related_to", "weight": 0.8, "note": "클라우드 환경에서 이 패턴을 적용한다"},
  {"target": "decision-jang-supabase-schema-env", "type": "related_to", "weight": 0.8, "note": "각 스키마(public/dev/test)에서 동일한 members 패턴을 사용한다"}
]
related: ["[[수파베이스 클라우드 환경 선호]]", "decision-jang-supabase-cloud-over-local", "decision-jang-supabase-schema-env"]
source_url: "Empty"
---

# 수파베이스 public.members 테이블 중심 아키텍처 + auth.users 트리거 동기화

## 핵심 원칙

수파베이스의 `auth.users` 테이블은 인증 전용으로만 남겨두고, 비즈니스 로직에 필요한 사용자 참조는 모두 `public.members`를 통해 처리한다.

## 구조

```sql
-- public.members: auth.users를 래핑하는 비즈니스 사용자 테이블
create table public.members (
  id uuid primary key references auth.users(id) on delete cascade,
  -- 비즈니스 필드 (nickname, role, created_at 등)
);

-- 다른 테이블의 FK는 public.members를 가리킴
create table public.posts (
  author_id uuid references public.members(id) on delete cascade,
  ...
);
```

## auth.users → public.members 트리거 동기화

```sql
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.members (id)
  values (new.id);
  return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();
```

## 이유

- `auth.users`는 수파베이스 내부 스키마로 직접 조인하면 RLS·권한 관리가 복잡해진다.
- `public.members`를 중간 레이어로 두면 비즈니스 필드 추가, 소프트 딜리트, 역할 관리 등을 자유롭게 확장할 수 있다.
- 트리거로 동기화하면 회원가입 직후 자동으로 `members` 레코드가 생성되어 FK 무결성이 보장된다.

## 주의사항

- `handle_new_user` 함수는 `security definer`로 선언해야 `auth.users` 접근 권한 문제를 피할 수 있다.
- `auth.users`에서 사용자가 삭제될 때 `on delete cascade`로 `members` 레코드도 함께 삭제된다.
