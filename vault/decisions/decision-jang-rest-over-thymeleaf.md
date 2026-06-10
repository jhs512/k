---
id: decision-jang-rest-over-thymeleaf
title: 타임리프보다 REST API 방식 선호
type: decision
namespace: personal
visibility: public
summary: 뷰 레이어는 타임리프 같은 서버사이드 템플릿보다 REST API 방식을 선호한다.
auto_inject: false
applicable_when: 스프링부트 프로젝트의 컨트롤러/뷰 레이어 구조를 정할 때
confidence: 1.0
verified_at: 06/10/2026
verified_by: 장희성 (본인 구술)
staleness_signal: 본인이 특정 프로젝트에서 SSR/타임리프를 명시적으로 요구하면 해당 건은 예외
tags: ["rest-api", "thymeleaf", "architecture", "spring-boot"]
edges: [
  {"target": "playbook-jang-springboot-setup", "type": "part_of", "weight": 0.8, "note": "표준 세팅의 아키텍처 방침"}
]
related: ["[[playbook-jang-springboot-setup]]", "[[decision-jang-security-defaults]]"]
source_url: "Empty"
---

# 타임리프보다 REST API 방식 선호

## 결정 내용

스프링부트 프로젝트에서 뷰를 만들 때 타임리프(서버사이드 템플릿) 방식보다 **REST API(`@RestController`, JSON 응답)** 방식을 기본으로 한다. 프런트엔드는 별도 클라이언트가 담당하는 구조를 전제한다.

## 함의

- 컨트롤러 예제는 `@Controller` + 템플릿이 아니라 `@RestController` 기준으로 작성한다.
- CSRF를 끄는 결정([[decision-jang-security-defaults]])과 일관된다 — 세션 기반 폼 제출이 아닌 API 중심이기 때문.
- 강의 예제·과제 코드 생성 시 타임리프 의존성은 기본 포함하지 않는다.

---

*2026-06-10 본인 구술을 /convert-note로 분해하여 생성.*
