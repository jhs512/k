---
id: decision-personal-first
title: 되돌릴 수 있는 행동을 되돌릴 수 있는 무행동보다 우선한다
type: decision
namespace: personal
visibility: public
summary: 모호한 문제에 시간 압박이 있을 때는, 되돌릴 수 있는 행동을 기본값으로 선택해 추진력을 유지하면서 선택지를 보존한다.
auto_inject: false
applicable_when: 분석 마비에 빠졌거나 급하지 않은 선택을 두고 결론 없이 고민이 길어질 때
confidence: 0.85
verified_at: 06/10/2026
verified_by: System Bootstrap
staleness_signal: 되돌릴 수 있다고 판단한 행동이 복구 불가능한 연쇄 부작용을 일으키면 이 기본값을 재검토
tags: ["operational-decision", "reversibility", "momentum", "default-behavior"]
edges: [
  {"target": "pillar-personal-foundation", "type": "supports", "weight": 0.9, "note": "결정 자체가 기록되고 근거를 갖춘 신중한 행동의 예시로서 pillar를 뒷받침"}
]
related: ["[[pillar-personal-foundation]]"]
source_url: "Empty"
---

# 되돌릴 수 있는 행동을 되돌릴 수 있는 무행동보다 우선한다

## 맥락

모호한 문제 앞에서 인간의 기본 행동은 기다림이다 — 데이터를 더 모으고, 분석을 한 번 더 돌린다. 때로는 옳지만, 더 자주 지연 자체가 비용이 된다. 이 결정은 기본 휴리스틱을 세운다: **행동의 비용이 무행동의 비용보다 낮고 그 행동이 되돌릴 수 있다면, 행동하라**.

## 적용 범위

적용되는 경우: 긴급 상황이 아니고, 올바른 길에 대한 모호성이 있으며, 지연에 측정 가능한 비용이 있고, 행동이 최소한 부분적으로 되돌릴 수 있을 때.

적용되지 않는 경우: 되돌릴 수 없는 피해(데이터 삭제, 법적 약속)를 만들거나, 되돌리는 비용 자체가 과도하거나, 더 구체적인 playbook/decision 노드가 이미 존재할 때.

## 검토한 대안

- **확실해질 때까지 기다린다** — 기각: 시간 압박 환경에서 확실성은 제때 오지 않고, 기다림은 다른 종류의 실패(기회 상실, 누적된 우회 비용)를 만든다.
- **모호한 결정을 단일 권위자에게 위임한다** — 기각: 병목을 만들고 문제에 가장 가까운 사람에게서 맥락을 빼앗는다.

## 근거

실제 피드백은 고립된 분석보다 좋은 정보를 만들고, 추진력은 복리로 쌓이며, 되돌릴 수 있는 결정은 생각보다 흔하다. 행동 전 번복 조건을 적어 두고, 점검 시점을 정하라. 이것은 규칙이 아니라 기본값이다.

---

*이 decision 노드는 06/10/2026 vault 초기 스캐폴딩 과정에서 생성되었다.*
