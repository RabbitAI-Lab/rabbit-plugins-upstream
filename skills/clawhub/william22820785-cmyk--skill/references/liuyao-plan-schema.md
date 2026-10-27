# 六爻+奇门双法会谈计划 (V3)

起卦后、答复前从 fusion.json 读取内部数据。本文件定义 v3 schema、证据回指规则与交付口径。

```json
{
  "schemaVersion": "aceworld-liuyao-qimen-fusion.v3",
  "stage": "reading",
  "timeBasis": "local",
  "basisComparison": {
    "localPillars": "丙午 丙申 乙亥 辛巳",
    "beijingPillars": "丙午 丙申 乙亥 丙戌",
    "diverges": true,
    "differences": ["时柱 当地 辛巳 / 北京 丙戌"]
  },
  "timeBasisDisclosure": "本次起卦按local时基排盘；当地与北京四柱存在差异（时柱 当地 辛巳 / 北京 丙戌），跨时区案例以当地时基为准，边界情形需另行核对。",
  "question": {
    "text": "这个月底前，甲方会不会签下这份合同？",
    "category": "career",
    "answerNeed": "outcome",
    "desiredOutcome": "确认月底前能否签约",
    "knownContext": ["合同已经发给甲方", "用户正在等待签署"]
  },
  "methods": {
    "liuyao": {
      "本卦": "水山蹇",
      "变卦": "水地比",
      "动爻": [],
      "世爻": {},
      "应爻": {},
      "direction": "吉",
      "level": "medium",
      "evidence": {"items": [{"kind": "用神", "label": "六爻用神", "text": "本次用神取事业用神；盘面匹配本卦2爻官鬼丑土"}]}
    },
    "qimen": {
      "局数": "阴遁4局",
      "节气": "大暑下元",
      "值符": "天冲(落8宫)",
      "值使": "伤门(落8宫)",
      "空亡": "申、酉",
      "direction": "吉",
      "level": "medium",
      "evidence": {"items": [{"kind": "格局", "label": "格局", "text": "开门临日干宫"}]}
    }
  },
  "evidence": [
    {
      "id": "ly-01",
      "system": "liuyao",
      "label": "六爻用神",
      "kind": "用神",
      "sourcePath": "/methods/liuyao/evidence/items/0/text",
      "value": "本次用神取事业用神；盘面匹配本卦2爻官鬼丑土"
    },
    {
      "id": "qm-01",
      "system": "qimen",
      "label": "格局",
      "kind": "格局",
      "sourcePath": "/methods/qimen/evidence/items/0/text",
      "value": "开门临日干宫"
    }
  ],
  "agreement": {
    "overall": "same",
    "points": [
      {
        "dimension": "总体吉凶",
        "verdict": "六爻偏吉，奇门偏吉",
        "delivery": "probable",
        "detail": "六爻：本卦2爻官鬼丑土发动；奇门：开门临日干宫，两法方向一致"
      }
    ],
    "conflicts": []
  },
  "conclusions": [
    {
      "id": "outcome",
      "appliesTo": "月底前甲方签署这份合同",
      "verdict": "多半能成，但不是板上钉钉……取决于对方是否按期回话。",
      "timing": "盘面没给明确应期；具体还要看条件是否出现",
      "conditions": ["把节点、交付物和对方要签的字先落成书面"],
      "guidance": ["按节点跟进书面确认"],
      "delivery": "probable",
      "liuyao_evidence_ids": ["ly-01"],
      "qimen_evidence_ids": ["qm-01"],
      "counter_evidence_ids": [],
      "liuyao_level": "medium",
      "qimen_level": "medium",
      "agreement": "same"
    }
  ],
  "diagram": "旧版Markdown，仅供历史审计",
  "diagramData": {},
  "soulNote": "有些事不是不能成，只是催错了门。"
}
```

## 判据与证据回指

- `evidence[]` 是本次盘面判据清单，每条含 `id`、`system`、`label`、`kind`、`sourcePath`、`value`。`sourcePath` 必须指向本文档内的真实字段，校验器逐条回指比对该值，不存在的编号或对不上的取值一律判失败。
- 结论里的 `liuyao_evidence_ids`、`qimen_evidence_ids`、`counter_evidence_ids` 只能引用 `evidence[]` 中已有的编号；引用空清单视为没有分别取证。
- 两法的证据编号不得共用同一组：六爻用 `ly-` 前缀，奇门用 `qm-` 前缀；两法引用完全相同的编号集合会被判失败。
- `agreement.points[].detail` 必须写出两法各自的判据摘要，不得留空；方向相左时必须写入 `agreement.conflicts`，并给出 `resolution`。

## 强度分级（每法独立评）

- `high`：用神或候选已与盘面匹配，有明确得助判据，且没有结构性反证（回头克、化空、化退、月破、日破、入墓、未匹配），也没有空亡、伏吟这类延后判据。
- `medium`：有得助判据但带延后或状态偏弱判据（空亡、伏吟、休囚），或判据只落在单一一处。
- `low`：未见可用候选、用神未匹配到盘面，或出现结构性反证。
- 分级只看判据性质，不把判据条数换算成准确率、成功率或吉凶分；`level` 不是现实命中率。

## 交付口径

同一套门禁写在 `scripts/validate-liuyao-qimen-consultation.cjs`，脚本会硬校验：

- `firm`：两法都是 `high`、方向一致、无 `counter_evidence_ids`。语气斩钉截铁，直接说能或不能；不得出现「大概率、可能、也许、多半」这类给判断本身留余地的措辞（条件、边界和免责仍要如实交代）。
- `probable`：两法至少 `medium`、方向不相左、无反证。给出主要倾向，同时写出余地与触发条件，断语中必须出现「多半、可能、取决于、要看」一类词。
- `tentative`：任一法为 `low`，或方向相左，或存在反证。必须并列两种可能，不强行统一。
- `id = "outcome"` 的结论在双高同向且无反证时必须给 `firm`；给不出就说清是哪一侧依据不足。

## 时基（跨时区）

- `timeBasis` 取值 `local|beijing`，默认 `local`：按求测者所在地墙钟排四柱、定节气，六爻与奇门必须用同一时基，否则两法比较的是不同日柱时柱。
- `basisComparison` 记录当地与北京四柱的差异；`diverges` 为真时必须给出 `timeBasisDisclosure`，并在答复正文中原样出现。
- 非东八区案例以当地时基为准；节气取自天文节气时刻换算，边界情形仍以披露为准，不对外声称全球时区精确换算。

## 保留旧规则

- `question.text` 与起卦时一致，不偷换问题；`knownContext` 只写用户明确说过的现实。
- `appliesTo` 明确每条判断对应的人、事、期限或结果。
- 时间只来自盘内应期边界，不编具体日期。
- `soulNote` 为历史字段，不强制展示，不为凑收尾照抄。
- 有 `counter_evidence_ids`：降为 `tentative`，不得写成灾祸或必然结果。

## V4.1 公开依据与解释

- `diagramData` 由原始六爻数据生成，不由模型手填。按 [diagram-display.md](diagram-display.md) 展示 PNG 或逐爻备用文本，再给详解；旧 `diagram` 仅供历史兼容。
- 允许体系名称与少量真实术语，首次出现口语解释，并记录 public-notes.json。
- 不公开完整奇门九宫格、内部ID、评分权重和融合计算过程。
- `firm` 是表达风格，不是现实命中率。细致度不以凑字数或保证应验来实现。
- 完整规则见 [paid-consultation-standard.md](paid-consultation-standard.md)。
