# Vault 워크플로

Infinite Brain 자동화를 위한 에이전트 비종속 워크플로 정의. 각 워크플로는 예약 작업이나 크론 실행을 지원하는 어떤 에이전트로도 트리거할 수 있다.

---

## vault-health

**트리거:** 주 1회 (권장: 월요일 아침)
**스킬:** `/vault-health`
**출력:** `notes/note-vault-health-YYYYMMDD.md` + 갱신된 `_system/INDEX.md`

**하는 일:**
1. 90일 이상 검증되지 않은 노드에 confidence 감쇠 적용
2. 고아 노드, 모순, 낡음 신호, 상호 링크 공백, 분류 체계, 가시성, summary 품질 감사
3. 구조화된 헬스 리포트를 `note` 노드로 작성
4. 수정 실행 전 우선순위 액션을 사람의 승인에 부침

**두 가지 모드:**
- `/vault-health` — 대화형: 감쇠 + 감사 + 각 수정 전에 질문
- `/vault-health auto` — 자동: 감쇠 + 감사 + 리포트 노드만, 수정 0건, 질문 0건

**에이전트별 설정:**

### Claude Code
```bash
# 주간 스케줄 등록은 1회만 실행 (auto 모드, 질문 없음):
/schedule weekly /vault-health auto
```

### GitHub Actions
`.github/workflows/vault-health.yml`을 생성 — 크론으로 Claude Code CLI를 통해 예약 에이전트를 원격 트리거한다. 아래 GITHUB-ACTIONS 섹션 참고.

### Cursor / Gemini CLI / Copilot
스킬은 이 vault 안이 아니라 ib Claude Code 플러그인에 있다. Claude 외 에이전트에는 `_system/AGENTS.md`(운영 규칙)를 알려 주고 vault-health 스킬에 기술된 감쇠 규칙을 적용하게 한다 (`/vault-health` 1단계: 미검증 91–180일 시 confidence −0.1, 181–365일 시 −0.2, 하한 0.1).

---

## convert-note (수동 실행, 비예약)

**트리거:** 수동 — `raw/`에 파일을 넣은 뒤 실행
**스킬:** `/convert-note`
**출력:** 각 폴더의 새 타입 노드 + 갱신된 `_system/INDEX.md`

자동화 비권장 — 변환은 타입 분류에 대한 사람의 검토가 필요하다.

---

## GITHUB-ACTIONS

`vault-health`를 GitHub Action으로 실행하려면 (러너에 Claude Code CLI 설치 필요):

```yaml
# .github/workflows/vault-health.yml
name: Vault Health

on:
  schedule:
    - cron: '0 8 * * 1'   # 매주 월요일 08:00 UTC
  workflow_dispatch:        # 수동 트리거

jobs:
  health:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run vault-health skill
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          npm install -g @anthropic-ai/claude-code
          claude --print --skill vault-health auto
      - name: Commit health report
        run: |
          git config user.name "vault-health[bot]"
          git config user.email "vault-health@users.noreply.github.com"
          git add notes/ _system/INDEX.md
          git diff --cached --quiet || git commit -m "chore: vault health report $(date +%Y-%m-%d)"
          git push
```

> **참고:** `--skill vault-health`는 Claude Code CLI가 플래그를 통한 스킬 호출을 지원해야 한다. 최신 CLI 문서를 확인할 것 — 대안은 스킬 내용을 `--system-prompt`로 전달하는 것이다.

---

## 워크플로 원칙

1. **자동화 단계는 절대 삭제하지 않는다.** 감쇠는 `confidence`만 수정한다. 감사는 수집만 한다. 수정에는 사람의 승인이 필요하다.
2. **모든 자동 실행은 노드를 남긴다.** `notes/`의 헬스 리포트가 vault 자체 안에 감사 기록을 만든다.
3. **워크플로는 누적적이다.** 새 자동화는 노드를 덮어쓰지 말고 새로 써야 한다. 과거 헬스 리포트는 ID에 날짜를 담아 보존된다.
