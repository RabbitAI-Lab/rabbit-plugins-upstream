# 黄金追踪 (Gold Tracker)

面向 AI 智能体的轻量级金价追踪和分析技能。
自动化数据获取、验证和日志记录的重复工作，
让智能体专注于市场推理。

## 功能特性

- **零第三方依赖** — 仅使用 Python 标准库
- **自动化数据获取** — 金价 + 汇率，带范围验证和缓存
- **格式标准化** — 所有运行的日志结构一致
- **提醒去重** — 防止重复的价格提醒条目
- **摘要生成** — 一键生成简报或完整摘要
- **健康验证** — 检查项目完整性和数据质量
- **灵活新闻来源** — 智能体可自由研究当前影响市场的因素

## 系统要求

- Python 3.8+
- 无需 `pip install`

## 快速开始

```bash
# 获取当前金价和汇率
python scripts/fetch.py

# 检查项目状态
python scripts/validate.py

# 生成简报
python scripts/summary.py brief

# 生成完整摘要
python scripts/summary.py full

# 标准化所有日志格式
python scripts/normalize.py

# 去重提醒记录
python scripts/dedup.py
```

## 项目结构

```
gold-tracker/
├── skill.yaml          # 技能元数据（ClawHub 兼容）
├── SKILL.md            # 智能体操作手册
├── README.md           # 本文件
├── config.yaml         # 所有可配置参数
├── scripts/            # 自动化脚本（零依赖）
│   ├── fetch.py        # 数据获取 + 验证 + 状态更新
│   ├── validate.py     # 项目健康检查器
│   ├── normalize.py    # 日志格式标准化器
│   ├── dedup.py        # 提醒去重器
│   └── summary.py      # 摘要生成器（简报/完整）
├── logs/               # 当日分析日志（运行时）
├── archive/            # 历史日志（运行时）
├── alerts/             # 价格提醒记录（运行时）
├── analysis.md         # 当前完整分析（运行时）
└── state.json          # 最新价格快照（运行时）
```

## 配置

编辑 `config.yaml` 调整：
- 数据源 URL 和超时时间
- 价格验证范围
- 缓存 TTL
- 提醒阈值
- 输出偏好

## 智能体使用指南

阅读 `SKILL.md` 获取完整操作手册。简短版本：

1. 运行 `python scripts/fetch.py` 获取最新价格
2. 读取 `state.json` 获取当前快照
3. 进行新闻研究 — 不要局限于固定来源
4. 将分析写入 `analysis.md`，并追加 YAML 条目到 `logs/`
5. 运行 `python scripts/validate.py` 和 `python scripts/summary.py brief` 验证

## 许可证

MIT
