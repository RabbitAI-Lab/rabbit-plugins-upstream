
一个 WorkBuddy/CodeBuddy Skill，实现多市场投资策略管理框架。覆盖美股、A股、港股，按资产分类执行差异化规则，组合层风控 + 纪律执行协议。

**当前版本**: v2.3.15（2026-09-16）

## 核心能力

- **资产三层分类**（A 类平台核心 / B 类高弹性周期 / C 类低波动收益），不同资产用不同退出逻辑
- **组合层 7 红线**（单标的≤25%、单行业≤35%、AI 叙事≤50%、回撤梯度防御、VIX 熔断）
- **多市场覆盖**（美股 A/B/C 分级、A 股三条件引擎、港股警戒线框架）
- **四种入场模式**（模式 A 恐慌错杀 / 模式 B 趋势确认 / 模式 C 再平衡 / 模式 D A 类候选区间建仓）
- **QMS 4 因子评分**（盈利趋势、行业相对强度、EPS 修正、价格结构）

## 快速开始

```bash
cp -r invassistant-skill ~/.workbuddy/skills/invassistant
pip install -r requirements.txt
```

然后对 WorkBuddy 说：「检查持仓」

> ⚠️ **数据外送说明**：可选的 `scripts/send_*.py` 会把报告内容推送到你自行配置的 webhook 端点（企业微信/钉钉/飞书）。未配置前完全静默，除报告正文外不发送任何数据；启用前请先核对端点配置。

> ⚠️ **非投资建议**：本框架仅作决策支持，所有输出需人工复核；作者不对交易损失承担责任。

## 版本历史

| 版本 | 日期 | 核心改动 |
|------|------|----------|
| v2.3.15 | 2026-09-16 | 收紧加固（估值门 + 量能门 fail-closed）；Framework Scope 边界章节；数据外送说明；依赖版本锁定 |
| v2.3.14 | 2026-09-11 | 清除示例配置与代码注释中的真实持仓标的（§13 D8 / P10） |
| v2.3.1 | 2026-06-06 | 重大清理：英文 SKILL.md、清理 frontmatter、双语 README、移除个股脚本 |
| v2.1.1 | 2026-06-04 | 新增模式 D：A 类候选池区间建仓（不带观察延迟） |
| v2.1 | 2026-05-18 | A/B/C 资产分类；7 红线；4 因子 QMS；A 类移除追踪止损 |
| v2.0 | 2026-05-18 | 完全重构：决策金字塔、5 因子 QMS、10 红线（已被 v2.1 取代） |
| v1.5.x | 2026 Q1-Q2 | 三条件引擎、双模式入场、追踪止损、行为补丁迭代 |
| v1.0 | 2026-01 | 初始版本：三条红线入场 + 多层退出引擎 |

## 架构

```
invassistant/
├── SKILL.md                    # 核心定义（触发词、工作流、策略规则）
├── README.md                   # 英文文档
├── README_zh.md                # 本文件（中文文档）
├── references/                 # 详细策略参考
│   ├── us_stock_strategy.md    # 美股 A/B/C 规则 + 模式 D
│   ├── a_share_strategy.md     # A 股三条件引擎
│   └── risk_control_and_overrides.md  # 7 红线、QMS、Override 协议
└── scripts/                    # 执行引擎（Python，可选辅助工具）
    ├── portfolio_checker.py    # 组合检查主程序
    ├── redline_engine.py       # 入场过滤引擎（fail-closed 门控）
    ├── exit_engine.py          # 退出引擎（止损、趋势破位、动量）
    ├── init_config.py          # 首次运行配置生成器（通用示例标的）
    ├── data_fetcher.py         # 行情数据获取辅助
    └── send_*.py               # 企微/钉钉/飞书 webhook 推送（默认关闭，需自行配置）
```

## 协议

MIT License — 见 [LICENSE](LICENSE)
