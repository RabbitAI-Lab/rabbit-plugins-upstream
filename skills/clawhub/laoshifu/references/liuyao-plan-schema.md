# 六爻会谈计划

起卦后、答复前生成 `liuyao-plan.json`，只在内部使用。

```json
{
  "schemaVersion": "aceworld-liuyao-consultation.v1",
  "stage": "reading",
  "intent": "decision",
  "question": {
    "text": "这个月底前，甲方会不会签下这份合同？",
    "category": "career",
    "answerNeed": "outcome",
    "desiredOutcome": "确认月底前能否签约",
    "knownContext": ["合同已经发给甲方", "用户正在等待签署"]
  },
  "evidenceBalance": {
    "texts": 0.3,
    "structure": 0.7
  },
  "conclusions": [
    {
      "id": "contract-outcome",
      "appliesTo": "月底前甲方签署这份合同",
      "verdict": "这份合同能成，但月底前还定不下来。",
      "timing": "真正松动在下一个时间窗口。",
      "conditions": ["对方内部还要过一道确认", "关键条款不宜临时再改"],
      "guidance": ["先追确认人，不要只催经办人"],
      "delivery": "firm",
      "textual_evidence_ids": ["liuyao-text-primary-gua"],
      "structural_evidence_ids": ["从 chart 中选择的结构 ID 之一", "从 chart 中选择的结构 ID 之二"],
      "counter_evidence_ids": []
    }
  ],
  "soulNote": "有些事不是不能成，只是催错了门。"
}
```

## 规则

- `question.text` 必须与起卦时写入 chart 的问题完全一致，不能起卦后偷换问题。
- `knownContext` 只写用户明确说过的现实，不从反馈偷造信息。
- `appliesTo` 明确每条判断对应的人、事、期限或结果，禁止泛泛而谈。
- 每条结论至少引用一条卦辞或爻辞依据、两条结构依据；结构依据占比保持约六至八成。
- `firm` 只在用神、世应、动变、月日等主要层面方向清楚且没有同级反证时使用；必须直接回答能不能、成不成或有没有转机。
- 有直接反证时写入 `counter_evidence_ids`，并用 `probable` 或 `tentative` 说明条件。
- 时间只来自盘内应期边界；没有明确应期就说阶段，不编具体日子。
- `soulNote` 不超过断事正文四分之一。
