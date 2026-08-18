---
name: multi-agent-team
version: 1.0.0
description: |
  多智能体协作（整合与进阶·元能力）。给定一项任务/一个待决问题，自动完成：
  角色分工(提议者/批判者/事实核查/综合裁决) → 任务派发 → 多视角作答 →
  交叉验证(reason-verify) → 投票聚合/辩论择优 → 输出带置信度的共识结论。
  对标一线大模型智能体的「多 agent 辩论/自一致性」能力，且把每个 agent 的产出
  都过一遍可靠自验证、按可靠度加权投票。当复杂决策需要多视角、且要
  抑制单点幻觉时使用。
agent_created: true
visibility: public
---

# multi-agent-team —— 多智能体协作

把「一个大脑拍板」升级为「多角色 deliberation + 加权投票」。
这是目前一线大模型智能体重点攻关的协作范式，本技能把它做成可离线验证的真实算法。

## 闭环（team.py 真实实现）

| 阶段 | 动作 |
|------|------|
| ① 分工 | 默认 4 角色：提议者 / 批判者 / 事实核查 / 综合裁决 |
| ② 派发 | 同一任务派给各角色，各自产出「立场 + 依据 + 置信度」 |
| ③ 交叉验证 | 每个 agent 的产出都过 `reason-verify`（真实子进程调用），按可靠度打分 |
| ④ 聚合 | 多数投票 + 按可靠度加权；胜出方即共识，附异议摘要 |
| ⑤ 置信度 | 共识置信度 = 对胜出方的一致比例 × 平均可靠度 |

## 使用

```bash
python multi-agent-team/scripts/team.py \
  --task "AIDC 数据中心该优先上 HVDC 还是传统 UPS？" \
  --out team_report.json --agents 4
```

## 输出 `team_report.json`

```json
{
  "task": "...",
  "roles": ["提议者","批判者","事实核查","综合裁决"],
  "stances": [{"role":"批判者","stance":"...","reliability":0.85}],
  "vote_tally": {"HVDC":3,"UPS":1},
  "consensus": "HVDC",
  "agreement": 0.75,
  "confidence": 0.79,
  "dissent": "UPS 派认为初期成本与改造成本更高"
}
```

## 自我进化

自带 `learner.py`（由 `skill-self-improve` 注入）。每次协作后把
「哪类任务角色间最易分歧 / 哪个角色可靠度最低」记入 `learned_patterns.json`，
下一次自动调优角色构成与加权策略。
