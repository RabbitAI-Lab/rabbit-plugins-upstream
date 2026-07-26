# 🏦 银行流水自动对账 (Bank Reconciliation)

银行流水自动对账引擎 — 导入银行流水和账面记录，自动核销，生成可视化对账报告。

## 核心功能

- 📥 **智能导入** — 支持 Excel/CSV，自动识别 30+ 列名别名，覆盖工行/建行/农行/中行/招行/兴业/浦发等主流银行
- 🎯 **三层匹配** — 精确匹配(金额+日期) → 模糊匹配(金额百分比+摘要相似度) → 关联匹配(同户名批量)
- 📊 **可视化报告** — 交互式 HTML 报告，含仪表盘、匹配明细、待确认列表、导出功能
- 🔄 **方向自处理** — 自动处理银行视角(贷方=收入)与会计视角(借方=收入)的差异

## 快速开始

```bash
# 安装依赖
pip install pandas openpyxl rapidfuzz

# 运行对账
python scripts/reconcile.py --bank 银行流水.xlsx --books 账面记录.csv

# 查看报告
# 打开 reconciliation_report.html
```

## 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--bank` | (必填) | 银行流水文件路径 |
| `--books` | (必填) | 账面记录文件路径 |
| `--date-tolerance` | 1 | 精确匹配日期容差天数 |
| `--amount-tolerance` | 0.01 | 精确匹配金额容差(元) |
| `--fuzzy-date-tolerance` | 3 | 模糊匹配日期容差天数 |
| `--fuzzy-amount-pct` | 0.05 | 模糊匹配金额百分比容差 |
| `--output` | reconciliation_result.json | JSON 结果路径 |
| `--report` | reconciliation_report.html | HTML 报告路径 |

## 文件结构

```
├── SKILL.md                    # WorkBuddy Skill 定义
├── README.md
├── scripts/
│   └── reconcile.py            # 核心对账引擎
└── references/
    └── matching_rules.md       # 匹配规则与银行格式参考
```

## License

MIT
