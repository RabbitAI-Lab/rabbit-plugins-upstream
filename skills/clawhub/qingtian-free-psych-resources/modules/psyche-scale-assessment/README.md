# 心理量表测评与报告生成 — 说明文档

一个**数据驱动**的心理自评量表测评引擎。所有量表以结构化 JSON 存放于 `scales/`，计分与报告逻辑通用，新增量表只需加数据文件。

---

## 目录结构

```
psyche-scale-assessment/
├── SKILL.md                  # 技能主入口（触发、流程、安全、扩展）
├── README.md                # 本文件
├── scales/                  # 量表数据（每个量表一个 JSON）
├── scripts/
│   ├── scoring_engine.py    # 通用计分引擎
│   └── report_generator.py  # 中文报告渲染
├── references/
│   ├── safety_protocol.md   # 安全护栏与求助资源
│   └── scale_authority.md   # 量表来源、版权、常模
└── examples/
    └── sample_report.md     # 示例报告
```

---

## 量表数据 Schema（统一结构）

```json
{
  "id": "PHQ-9",
  "name": "患者健康问卷抑郁量表（PHQ-9）",
  "short_name": "PHQ-9 抑郁自评",
  "category": "抑郁",
  "target_population": "成年人（≥12岁）",
  "estimated_time": "约 2 分钟",
  "item_count": 9,
  "description": "国际通用的抑郁症状筛查工具……",
  "source": "Spitzer et al., 1999",
  "license": "公开学术工具，非商业用途免费",
  "scoring_type": "sum",
  "items": [
    {
      "id": "q1",
      "text": "题目文字",
      "reverse": false,
      "crisis": false,
      "options": [
        {"label": "完全不会", "score": 0},
        {"label": "好几天", "score": 1},
        {"label": "一半以上天数", "score": 2},
        {"label": "几乎每天", "score": 3}
      ]
    }
  ],
  "dimensions": [
    {"name": "抑郁总分", "items": ["q1", ...], "max": 27, "min": 0}
  ],
  "standard_score": null,
  "interpretation": {
    "bands": [
      {"min": 0, "max": 4, "level": "无/极轻度", "summary": "...", "advice": "..."}
    ]
  },
  "safety": {
    "crisis_items": ["q9"],
    "crisis_rule": "q9 得分 ≥ 1 即触发",
    "high_risk_rule": "总分 ≥ 15 或 q9 ≥ 1"
  }
}
```

### Schema 关键字段说明

| 字段 | 作用 |
|------|------|
| `items[].reverse` | `true` 表示反向计分题，引擎按选项分值端点自动翻转 |
| `items[].crisis` | `true` 表示该题为自伤/危机题 |
| `dimensions[].method` | `sum`（默认）或 `average` |
| `dimensions[].cap` | 维度封顶值（如 PSQI 成分封顶 3）|
| `standard_score` | `{"slope":1.25}` 表示维度分 ×1.25 得到标准分 |
| `interpretation.bands[].dimension` | 指定该判级区间归属维度；省略表示匹配所有维度 |
| `safety` | 危机题列表与触发/高风险规则 |

---

## 计分逻辑要点

1. **反向计分**：对 `reverse` 题，翻转分 = `选项最小分 + 选项最大分 - 原分`（适用于任意等距 Likert）。
2. **标准分**：SAS / SDS 等中国常模量表，原始分 ×1.25 得标准分，再按标准分判级。
3. **维度聚合**：子量表求和或平均，可封顶。
4. **判级**：总分/维度分落入 `bands` 区间即对应分级。
5. **危机检测**：危机题非零或高风险规则满足时，`crisis_flag=true`。

---

## 量表库（19 个）

| 领域 | id | 题数 | 备注 |
|------|-----|------|------|
| 抑郁 | PHQ-9 | 9 | 危机题 q9 |
| 抑郁(中国常模) | SDS | 20 | 10 反向，标准分 ×1.25 |
| 焦虑 | GAD-7 | 7 | — |
| 焦虑(中国常模) | SAS | 20 | 15 反向，标准分 ×1.25 |
| 压力 | PSS-10 | 10 | 4 反向 |
| 睡眠 | PSQI | 19→7成分 | 成分封顶 3，>7 差 |
| 正念 | MAAS | 15 | 全反向 |
| 正念 | FFMQ | 39 | 5 因子，含反向 |
| 自尊 | Rosenberg | 10 | 5 反向 |
| 情绪 | PANAS | 20 | 积极/消极 |
| 生活满意 | SWLS | 5 | 7 点 |
| 抑郁(社区) | CES-D | 20 | 4 反向 |
| 心理韧性 | CD-RISC | 10 | 5 点 |
| 职业倦怠 | MBI | 22 | 3 维度 |
| 综合症状 | SCL-90 | 90 | 9 因子+附加 |
| 社会支持 | SSRS | 10 | 3 维度 |
| 注意缺陷 | ASRS | 6 | 成人 ADHD |
| 依恋 | ECR | 36 | 两维，反向 |
| 网络成瘾 | IAT | 20 | 5 点 |

---

## 安装与使用

- 本技能位于用户级目录 `~/.workbuddy/skills/psyche-scale-assessment/`，跨项目可用。
- 触发后由 AI 走 SKILL.md 定义的工作流程；也可直接调用脚本做批处理：
  ```bash
  python scripts/scoring_engine.py PHQ-9 answers.json
  python scripts/report_generator.py GAD-7 answers.json
  ```
- 报告默认保存到当前工作目录的 `reports/`。

---

## 版本

- v0.1.0：初始版本，19 个量表 + 通用引擎 + 报告生成 + 安全护栏。
