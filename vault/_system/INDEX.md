# Knowledge Graph Vault — Master Index

> **Entry point for AI agents.** This index lists every node in the vault, grouped by type, with summary and edge count for rapid scanning.

---

## pillar

| ID | Summary | Edges |
|---|---|---|
| `pillar-personal-foundation` | 신중하게 내리고 기록한 의사결정이 즉흥적인 대응보다 장기적으로 더 나은 결과를 만든다는 이 vault의 기초 원칙. | 1 |
| `pillar-jang-causality` | 장희성의 핵심 세계관. 인과율을 믿으며, 행동의 결과는 뿌린 대로 돌아온다고 본다. 베풂과 성실함의 근거가 되는 가치 축. | 2 |

---

## decision

| ID | Summary | Edges |
|---|---|---|
| `decision-personal-first` | 모호한 문제에 시간 압박이 있을 때는, 되돌릴 수 있는 행동을 기본값으로 선택해 추진력을 유지하면서 선택지를 보존한다. | 1 |
| `decision-jang-security-defaults` | 스프링 시큐리티 초기 설정은 모든 요청 허용, H2 콘솔 정상 작동 보장, CSRF 전체 비활성화로 한다. | 1 |
| `decision-jang-rest-over-thymeleaf` | 뷰 레이어는 타임리프 같은 서버사이드 템플릿보다 REST API 방식을 선호한다. | 1 |
| `decision-jang-test-strategy` | 테스트는 H2 메모리 DB 위에서 실제 HTTP 요청을 날리고, 각 테스트 후 트랜잭션 롤백으로 상태를 초기화하는 방식을 선호한다. | 2 |
| `decision-jang-sql-logging` | 모든 SQL은 포맷팅된 형태로 자세히 출력하고, 바인딩 파라미터와 추출 값까지 로그에 보이게 설정한다. | 1 |
| `decision-jang-supabase-cloud-over-local` | 수파베이스 프로젝트는 로컬 CLI 대신 Supabase 클라우드를 기본 작업 환경으로 사용한다. | 2 |

---

## concept

*No nodes created yet.*

---

## question

*No nodes created yet.*

---

## playbook

| ID | Summary | Edges |
|---|---|---|
| `playbook-jang-springboot-setup` | 장희성의 스프링부트 프로젝트 초기 세팅 표준. yaml 설정, 최신 안정 버전, JDK 25+, Group com / Artifact back, Gradle KTS, 필수 의존성 목록 포함. | 3 |
| `playbook-jang-springboot-profiles` | application-dev.yml은 H2 파일 모드(데이터 유지), application-test.yml은 H2 메모리 모드(휘발)로 구성한다. | 1 |

---

## task

*No nodes created yet.*

---

## event

*No nodes created yet.*

---

## pattern

| ID | Summary | Edges |
|---|---|---|
| `pattern-jang-supabase-schema-env` | 단일 Supabase 프로젝트 안에서 public=production, dev=개발, test=테스트 스키마로 환경을 분리한다. | 3 |
| `pattern-jang-supabase-members-table` | public 스키마의 거의 모든 테이블이 auth.users 대신 public.members를 참조하며, 두 테이블은 트리거로 동기화한다. | 3 |

---

## hypothesis

*No nodes created yet.*

---

## fact

*No nodes created yet.*

---

## source

*No nodes created yet.*

---

## bookmark

*No nodes created yet.*

---

## note

| ID | Summary | Edges |
|---|---|---|
| `note-jang-money-attitude` | 장희성은 돈 버는 것을 좋아하지만 인색하지는 않다. 베풂은 인과율 신념(뿌린 대로 거둔다)에서 비롯된다. | 2 |
| `note-jang-tastes` | 장희성은 풋살과 한식을 좋아하고, 대중문화(연예·트렌드)에는 관심이 없다. | 1 |

---

## contact

| ID | Summary | Edges |
|---|---|---|
| `contact-jang-heeseong` | 1986년생 한국 남성. IT 강사로 스프링부트 강의를 주력으로 한다. 이 vault의 소유자이자 모든 personal 노드의 1차 저자. | 3 |

---

## reference

*No nodes created yet.*

---

## custom

*No nodes created yet.*

---

## log

> Log nodes are not indexed here. They live in `logs/` and are self-contained. To review recent operations, scan `logs/` directly.

---

## Adding New Nodes

When you create a new node:

1. Add a frontmatter block with all required fields per `_system/FRONTMATTER-SCHEMA.md`.
2. Assign a unique `id` in `type-slug` format.
3. Populate `edges` with at least one relationship to another node.
4. Update this index by inserting a row into the appropriate table.
5. Use `related` for informal wikilinks that don't need a formal edge.
6. `log` nodes are never added to this index — they are self-contained in `logs/`.

---

*Last updated: 06/10/2026 (issue-1: Supabase 선호도 노드 3개 추가 — decision 1, pattern 2)*
