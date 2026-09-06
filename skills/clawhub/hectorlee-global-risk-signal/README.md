# 盘前雷达 · Global Risk Signal

> A 股盘前外围风险信号，30 秒看懂「今天外围有没有雷」。

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License"></a>
  <a href="#特性"><img src="https://img.shields.io/badge/deps-zero%20dependency-success" alt="零第三方依赖"></a>
  <a href="#快速开始"><img src="https://img.shields.io/badge/key-none%20required-brightgreen" alt="无需 API Key"></a>
  <img src="https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+">
  <a href="https://clawhub.ai/xiyanjun/skills/hectorlee-global-risk-signal"><img src="https://img.shields.io/badge/install-ClawHub-orange" alt="ClawHub 一键安装"></a>
</p>

一个纯 Python 标准库、**零第三方依赖、无 key 开箱即用**的盘前风险信号工具。聚合六大维度数据，做多空情景推演，输出方向判断 + 1-5 级风险分级 + 可分享信号卡，支持推送到飞书群。

> **开源免费**：MIT 协议，可自由使用、修改、商用。代码纯标准库、无 key、开箱即用，装上就能跑。

## 为什么做这个

A 股开盘前，外围市场（美股、A50、人民币、美元、VIX、美债）和地缘事件往往决定当日情绪。散户早上打开软件，需要的是一个**一眼看懂的方向 + 风险等级**，而不是一堆需要自己拼的行情数字。盘前雷达把「拉数据 → 打分 → 输出」压缩成一条命令。

## 特性

- ✅ **零依赖**：纯标准库（urllib / xml.etree / email.utils），`python3` 直接跑，无 `pip install`
- ✅ **无 key**：所有数据源免鉴权，FRED 为可选增强
- ✅ **六大维度**：外围行情 · 地缘事件 · 财经日历 · 国内新闻 · 宏观数据 · 中国资金面
- ✅ **情景推演**：多头逻辑 vs 空头逻辑，非机械打分，附反向风险条件
- ✅ **风险分级**：1-5 级琥珀色风险条，直观
- ✅ **可分享信号卡**：HTML 卡片，内置品牌 footer（可接二维码）
- ✅ **订阅推送**：本机 notify-hub + 云端 GitHub Actions 双轨，电脑关机也照常推

## 快速开始

```bash
cd scripts

# 一键：采集 → 打分 → 输出报告
python3 score_and_report.py --pretty

# 渲染 HTML 信号卡
python3 render_card.py
```

输出产物在 `output/` 目录：
- `report_YYYYMMDD.json` — 结构化报告
- `card_YYYYMMDD.html` — 可分享信号卡
- `push_card_YYYYMMDD.json` — 飞书卡片

## 数据源

| 模块 | 内容 | 数据源 |
|---|---|---|
| 外围行情 | A50 期货、纳指/标普期货、离岸/在岸人民币、美元指数、VIX、美债 10Y、黄金、原油、恒指 | 腾讯 / 新浪 / 东财（三级降级） |
| 地缘事件 | conflict / trade / mideast 三主题 | GDELT DOC 2.0 |
| 财经日历 | 当日事件 + 重磅事件 | 华尔街见闻 |
| 国内新闻 | 5 频道 + 7x24 快讯 + 滚动 | 中新网 / 东财 / 新浪 |
| 宏观数据 | 中国 PMI/CPI/PPI + 美国/中国/全球 GDP·CPI·失业率 + FRED | 东财 / World Bank / FRED |
| 中国资金面 | 两融余额、龙虎榜、沪深港通净流入、在岸人民币 | 东财 |

## 订阅推送

**方式一：本机**（需 WorkBuddy notify-hub 已配飞书通道）

```bash
python3 push_feishu.py --send
```

**方式二：云端 GitHub Actions**（推荐，电脑关机也推）

1. 仓库 `Settings → Secrets and variables → Actions` 添加两个 secret：
   - `FEISHU_WEBHOOK` — 飞书群机器人 webhook URL
   - `FEISHU_SECRET` — 机器人「加签」密钥
2. 每天 UTC 0:30（北京 8:30，周一~五）自动运行；也可在 Actions 页手动 `Run workflow` 验证。

## 目录结构

```
hectorlee-global-risk-signal/
├── SKILL.md                    # WorkBuddy / ClawHub skill 元数据
├── README.md
├── LICENSE
├── scripts/
│   ├── score_and_report.py     # 编排 + 打分 + 报告
│   ├── fetch_market.py         # 外围行情
│   ├── fetch_geopolitics.py    # 地缘事件
│   ├── fetch_calendar.py       # 财经日历
│   ├── fetch_news_cn.py        # 国内新闻
│   ├── fetch_macro.py          # 宏观数据
│   ├── fetch_funds.py          # 中国资金面
│   ├── render_card.py          # 信号卡渲染
│   ├── push_feishu.py          # 本机推送
│   ├── push_webhook.py         # 云端推送
│   └── templates/card.html     # 信号卡模板
└── .github/workflows/daily-push.yml
```

## 免责声明

本项目输出基于公开信息的分析推演，仅供参考，**不构成投资建议**。市场有风险，投资需谨慎。

## License

[MIT](./LICENSE) © 2026 hectorlee
