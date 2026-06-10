## 지침
- 최대한 한국어 사용

## Infinite Brain vault

The `vault/` directory is an AI-first knowledge-graph vault. Every note is a typed **node**; every connection is a typed **edge**. Act as a Knowledge Architect, not a chat assistant.

Read `vault/_system/AGENTS.md` before any vault operation — it defines the full node/edge taxonomy, visibility model, frontmatter schema, and prohibited actions.

### ib skills

| Command | When to use |
|---|---|
| `/init-vault` | Scaffold a fresh vault in a new directory |
| `/convert-note` | Decompose `raw/` files into typed atomic nodes |
| `/query-vault` | Answer questions via scoped graph traversal (token-cheap) |
| `/organize-vault` | Interactive audit of orphans, contradictions, confidence gaps |
| `/vault-health` | Confidence decay + full audit + health-report node |

### Quick reference

- Vault root: `vault/`
- Default namespace: `personal`
- Default visibility: `public` (model: `public` | `namespace` | `private` | `system`)
- Node types: `pillar decision concept question playbook task event pattern hypothesis fact source bookmark note contact reference custom log`
- Edge types: `related_to depends_on derived_from contradicts supports part_of preceded_by followed_by authored_by tagged_with`
- Entry point for agents: `vault/_system/INDEX.md` — every new node must update it
- Never leave `edges: []` empty on an established node
- `raw/` is immutable source material — never edit it; `/convert-note` moves processed originals to `raw/processed/`
- Every skill run writes a log node to `logs/` (reduced 8-field schema; never indexed, never edited)
