# 旧技术报告数据（仅限内部审计）

此格式会暴露后台推断结构，已经退出用户流程。不得生成、展示或交付给用户。只有内部回归测试可以传 `--internal=true` 调用旧校验器和渲染器。

只输出合法 JSON，不要 Markdown 代码块。所有核心对象必须带 `evidence_ids`，ID 必须来自 `chart.interpretation.evidence`。

```json
{
  "meta": {
    "archetype_name": "3-7字",
    "axis_oneliner": "30字以内",
    "evidence_ids": ["至少1个ID"]
  },
  "axes": {
    "bazi_main": "45字以内",
    "ziwei_main": "45字以内",
    "bazi_evidence_ids": ["bazi ID"],
    "ziwei_evidence_ids": ["ziwei ID"]
  },
  "consistency": "同向印证|互补印证|存在矛盾",
  "strengths": [
    {"title":"6字以内","desc":"25字以内","evidence_ids":["ID"]}
  ],
  "weaknesses": [
    {"title":"6字以内","desc":"25字以内","evidence_ids":["ID"]}
  ],
  "section_01": {
    "text": "180-250字主轴印证",
    "word_count": 200,
    "evidence_ids": ["ID"]
  },
  "section_02": {
    "conclusion": "100字以内阶段结论",
    "evidence_ids": ["timing ID"]
  },
  "dim": {
    "career": {"bazi":"30字以内","ziwei":"30字以内","verdict":"🟢 同向|⚠ 部分冲突|🔴 矛盾","verdict_class":"verdict-yes|verdict-partial|verdict-no","fused":"30字以内","evidence_ids":["ID"]},
    "wealth": "字段同 career",
    "marriage": "字段同 career",
    "children": "字段同 career",
    "family": "字段同 career",
    "health": "字段同 career"
  },
  "conflicts": [
    {"point":"8字以内","bazi":"25字以内","ziwei":"25字以内","impact":"低|中|高","impact_class":"low|mid|high","advice":"30字以内","evidence_ids":["ID"]}
  ],
  "final": {
    "life_axis": "30字以内",
    "nodes": [
      {"age":27,"year":2026,"event":"40字以内的阶段主题，不虚构具体事件","evidence_ids":["timing ID"]}
    ],
    "risks": [
      {"range":"年份与年龄","desc":"40字以内","evidence_ids":["timing ID"]}
    ],
    "leverage": [
      {"title":"10字以内","desc":"40字以内","evidence_ids":["ID"]}
    ],
    "advice": ["25字以内","25字以内","25字以内","25字以内"]
  },
  "certainty": {
    "bazi_level":"很有把握|比较有把握|仍需观察",
    "ziwei_level":"很有把握|比较有把握|仍需观察",
    "consistency_level":"高度一致|大体一致|各有侧重",
    "stability_level":"很稳定|较稳定|会随阶段变化",
    "note":"80字以内"
  }
}
```

固定数量：`strengths` 3 项、`weaknesses` 3 项、`conflicts` 3 项、`nodes` 5 项、`risks` 3 项、`leverage` 2 项、`advice` 4 项。`dim` 六个维度都必须完整填写。

时间节点只能描述大运或流年“主题与风险窗口”，不能在缺少证据时断言升职、结婚、患病、破财等具体事件。健康字段不得写疾病诊断。所有展示文字不得出现 evidence ID、内部权重、小数分数或“置信度”这个术语。
