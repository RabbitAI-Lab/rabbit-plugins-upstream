# 内部会谈计划

每次实质性断语前生成 JSON 文件。它是后台工件，不得展示给用户。以下只演示结构，不是现成断语；日期、状态、判断和ID必须按实际输入与盘面重写。

```json
{
  "schemaVersion": "bazi-ziwei-consultation.v1",
  "stage": "calibration|reading|deepening|closure",
  "intent": "curiosity|comfort|decision|learning",
  "topic": "career",
  "focus": {
    "status": "resolved",
    "domain": "career",
    "coreQuestion": "今年主动换工作能不能成？",
    "answerNeed": "outcome",
    "knownContext": ["目前在职", "正在考虑主动换工作"],
    "blockingUnknowns": []
  },
  "calibrationState": {
    "rejectionStreak": 0,
    "confirmedFacts": [],
    "rejectedHypotheses": []
  },
  "calibration": [
    {
      "hypothesis_type": "past-event|current-status|timing|relationship-pattern|input-boundary",
      "statement": "你很能扛事，但责任一多就容易把自己压得太紧。",
      "question": "这几年工作上的责任明显压重了，对不对？",
      "evidence_ids": ["内部 ID"]
    }
  ],
  "conclusions": [
    {
      "id": "career-2026",
      "topic": "career",
      "verdict": "填写有实际依据的主判断，不保证具体事件必然发生。",
      "timing": "有时间依据才填写窗口，否则说明无法定时。",
      "conditions": ["主动整理合作边界，变化会更顺。"],
      "guidance": ["不要在旧承诺上继续加码。"],
      "bazi_evidence_ids": ["内部 bazi ID"],
      "ziwei_evidence_ids": ["内部 ziwei ID"],
      "counter_evidence_ids": [],
      "agreement": "same",
      "bazi_level": "high",
      "ziwei_level": "high",
      "delivery": "direct"
    }
  ],
  "soulNote": ""
}
```

## 字段规则

- `calibration` 每轮最多 1 条；不是所有轮次都需要。
- `conclusions` 每轮最多 4 条，优先只处理用户当前议题。
- `focus.status`：`calibrating|resolved`。校盘阶段可保留未知项；有实质结论时必须为 `resolved`。
- `focus.coreQuestion` 必须是可以直接回答的具体问题；“婚姻、事业、财运怎么样”不合格。
- `focus.answerNeed`：`outcome|timing|turning-point|cause|decision|overview`。
- `focus.knownContext` 在 `resolved` 时至少记录一项已经确认的现实事实；`calibrating` 时可以为空。
- 有实质结论时 `focus.blockingUnknowns` 必须为空；缺少会改变答案的事实就先追问。
- `calibration.hypothesis_type` 说明本轮核对的是过去事件、当前状态、时机、关系模式或输入边界。
- 校盘必须先陈述判断，再用“对不对、对吗、是不是这样”等确认式问句收尾，不得直接问用户现实状态。
- `calibrationState.rejectionStreak` 记录连续明确否认；“不记得、不确定”不增加。
- `rejectionStreak >= 2` 时禁止继续下结论，下一轮 `hypothesis_type` 必须为 `input-boundary`，核对日期、历法、时辰或出生地边界。
- `agreement`：`same` 同向，`complementary` 互补，`conflict` 冲突，`single` 单一体系。
- `*_level`：只能为 `high|medium|low|none`，必须由所列内部证据支持。
- `delivery`：`direct|firm|probable|tentative`。
- `agreement=same` 且两边均为 `high` 且无反证时，`delivery` 强制为 `direct`。
- `direct` 只允许用于双高同断：主判断直接说清，断语不带"大概率、可能、也许、多半"这类含糊措辞；条件与局限可如实交代。
- 两边至少 `medium`、方向不相左且无反证时才可用 `probable`，并要写明余地；任一为 `low`、方向相左或存在反证时必须降为 `tentative` 并列两种可能。
- `counter_evidence_ids` 主动记录同题反证；有同级直接冲突时不得标为 `same`。
- `soulNote` 为兼容保留的可选字段，默认留空或省略。不要为填字段另编点命金句；有必要的提醒直接融入正文。

V4.1：用户可见字段允许体系名与真实术语解释；内部ID和算法细节仍不外露。公开术语附独立public-notes.json，遵循 paid-consultation-standard.md。
