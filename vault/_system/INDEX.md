# Knowledge Graph Vault — Master Index

> **Entry point for AI agents.** This index lists every node in the vault, grouped by type, with summary and edge count for rapid scanning.

---

## pillar

| ID | Summary | Edges |
|---|---|---|
| `pillar-personal-foundation` | 신중하게 내리고 기록한 의사결정이 즉흥적인 대응보다 장기적으로 더 나은 결과를 만든다는 이 vault의 기초 원칙. | 1 |

---

## decision

| ID | Summary | Edges |
|---|---|---|
| `decision-personal-first` | 모호한 문제에 시간 압박이 있을 때는, 되돌릴 수 있는 행동을 기본값으로 선택해 추진력을 유지하면서 선택지를 보존한다. | 1 |

---

## concept

*No nodes created yet.*

---

## question

*No nodes created yet.*

---

## playbook

*No nodes created yet.*

---

## task

*No nodes created yet.*

---

## event

*No nodes created yet.*

---

## pattern

*No nodes created yet.*

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

*No nodes created yet.*

---

## contact

*No nodes created yet.*

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

*Last updated: 06/10/2026*
