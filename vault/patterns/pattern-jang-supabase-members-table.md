---
id: pattern-jang-supabase-members-table
title: "Supabase public.members 테이블을 auth.users 대신 외래키 기준으로 사용"
type: pattern
namespace: personal
visibility: namespace
summary: "public 스키마의 거의 모든 테이블이 auth.users 대신 public.members를 참조하며, 두 테이블은 트리거로 동기화한다."
auto_inject: false
applicable_when: "Supabase 프로젝트에서 사용자 참조 테이블 설계 시"
confidence: 0.9
verified_at: "06/10/2026"
verified_by: "jang-heeseong"
staleness_signal: "Supabase auth 스키마가 공개 확장을 공식 지원하거나, RLS 정책이 auth.users 직접 참조를 강제하는 상황이 되면 재검토"
tags: ["supabase", "members", "auth", "트리거", "외래키", "사용자관리", "데이터베이스설계"]
edges: [
  {"target": "pattern-jang-supabase-schema-env", "type": "part_of", "weight": 0.85, "note": "스키마 환경 분리 패턴과 함께 적용되는 사용자 테이블 설계 패턴"},
  {"target": "decision-jang-supabase-cloud-over-local", "type": "depends_on", "weight": 0.8, "note": "Supabase 클라우드 환경에서 트리거와 테이블을 관리하는 방식"},
  {"target": "contact-jang-heeseong", "type": "authored_by", "weight": 1.0, "note": "장희성의 Supabase 사용자 테이블 설계 선호"}
]
related: ["[[pattern-jang-supabase-schema-env]]", "[[decision-jang-supabase-cloud-over-local]]"]
source_url: "Empty"
---

# Supabase public.members 테이블을 auth.users 대신 외래키 기준으로 사용

## 핵심 원칙

`public` 스키마의 거의 모든 테이블은 `auth.users`를 직접 참조하지 않고, **`public.members`** 테이블을 외래키 대상으로 사용한다.

## 테이블 구조

```sql
-- public.members: auth.users의 공개 미러 테이블
CREATE TABLE public.members (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT,
  -- 추가 프로필 컬럼들
  created_at TIMESTAMPTZ DEFAULT now()
);
```

다른 테이블들은 `auth.users(id)` 대신 `public.members(id)`를 참조한다.

```sql
-- 예시: posts 테이블
CREATE TABLE public.posts (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  member_id UUID REFERENCES public.members(id) ON DELETE CASCADE,
  content TEXT
);
```

## auth.users ↔ public.members 동기화 (트리거)

```sql
-- 신규 가입 시 members에 자동 삽입
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.members (id, email)
  VALUES (NEW.id, NEW.email);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

## 이 패턴을 선호하는 이유

- `auth` 스키마는 Supabase 내부 스키마라 RLS 정책 작성이나 JOIN이 불편하다.
- `public.members`를 통하면 커스텀 컬럼 추가, RLS 정책 관리, 타 테이블과의 JOIN이 자연스럽다.
- 사용자 데이터와 인증 데이터를 분리해 마이그레이션 및 유지보수가 쉬워진다.
