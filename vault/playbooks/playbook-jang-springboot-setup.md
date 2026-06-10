---
id: playbook-jang-springboot-setup
title: 스프링부트 신규 프로젝트 표준 세팅
type: playbook
namespace: personal
visibility: public
summary: 장희성의 스프링부트 프로젝트 초기 세팅 표준. yaml 설정, 최신 안정 버전, JDK 25+, Group com / Artifact back, Gradle KTS, 필수 의존성 목록 포함.
auto_inject: false
applicable_when: 새 스프링부트 프로젝트를 생성하거나 강의 예제를 세팅할 때
confidence: 1.0
verified_at: 06/10/2026
verified_by: 장희성 (본인 구술)
staleness_signal: JDK 25를 초과하는 새 LTS가 표준이 되거나 본인이 다른 세팅을 지시하면 갱신
tags: ["spring-boot", "project-setup", "gradle-kts", "jdk-25", "teaching", "playbook"]
edges: [
  {"target": "contact-jang-heeseong", "type": "authored_by", "weight": 0.9, "note": "본인의 강의 표준 세팅"},
  {"target": "decision-jang-security-defaults", "type": "related_to", "weight": 0.9, "note": "세팅 직후 적용하는 시큐리티 기본 설정"},
  {"target": "playbook-jang-springboot-profiles", "type": "related_to", "weight": 0.9, "note": "세팅에 포함되는 dev/test 프로파일 구성"}
]
related: ["[[decision-jang-security-defaults]]", "[[playbook-jang-springboot-profiles]]", "[[decision-jang-rest-over-thymeleaf]]", "[[decision-jang-sql-logging]]", "[[decision-jang-test-strategy]]"]
source_url: "Empty"
---

# 스프링부트 신규 프로젝트 표준 세팅

## 프로젝트 생성 기준

| 항목 | 값 |
|---|---|
| 설정 파일 형식 | **yaml** (`application.yml` — properties 아님) |
| 스프링부트 버전 | **최신 안정(stable) 버전** |
| JDK | **25 이상** |
| Group | `com` |
| Artifact | `back` |
| 빌드 도구 | **Gradle — Kotlin DSL(KTS)** |

## 필수 의존성

- Spring Web
- Spring Security
- H2 Database
- Spring Data JPA
- Spring Boot DevTools
- Lombok — **자바+스프링 조합일 때만** (코틀린이면 불필요)

## 후속 설정 (별도 노드)

- 시큐리티/H2 콘솔/CSRF: [[decision-jang-security-defaults]]
- dev/test 프로파일: [[playbook-jang-springboot-profiles]]
- 뷰 레이어 방침: [[decision-jang-rest-over-thymeleaf]]
- SQL 로깅: [[decision-jang-sql-logging]]
- 테스트 전략: [[decision-jang-test-strategy]]

---

*2026-06-10 본인 구술을 /convert-note로 분해하여 생성.*
