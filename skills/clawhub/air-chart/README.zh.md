<div align="center">

# Air-chart

**一句话，让 AI 给你画出全球空气质量专业图表。**

[English](README.md) | 简体中文

![Claude Code](https://img.shields.io/badge/Claude%20Code-native-blue)
![Cursor](https://img.shields.io/badge/Cursor-native-blue)
![Codex CLI](https://img.shields.io/badge/Codex%20CLI-compatible-blue)
![ClawHub](https://img.shields.io/badge/ClawHub-publishable-green)
![skills.sh](https://img.shields.io/badge/skills.sh-installable-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## 这个 Skill 能干嘛？

你在 AI 对话里随口一句话，它就能**自动找站点、拉数据、画图表**，几秒钟交回一张可以直接贴进报告的高清 SVG 图：

> 💬 "看看北京最近一周 PM2.5 走势"
> 💬 "对比东京和首尔过去 7 天的空气质量"
> 💬 "德里过去 30 天 PM10，和 WHO 标准对比一下"
> 💬 "新加坡最近 48 小时臭氧的小时变化"
> 💬 "北京各个监测点现在谁最脏？"

背后发生的是一条全自动管道：解析城市 → 在全球最大的开放空气质量平台 **OpenAQ**（100+ 国家的政府参考级监测数据）里挑选**仍在正常更新**的监测站 → 清洗异常值与缺失时段 → 渲染成专业图表。

**为什么值得用：**

- **专业可信**：优先选用政府参考级监测站，图上直接标注物理浓度（µg/m³）和 **WHO 安全基准线**（超标红色、达标绿色），一眼看出空气达不达标——不是花哨的 AQI 指数，是可写进报告的数据。
- **零安装负担**：不需要 Python、不需要 Matplotlib，只要 `bash`/`jq`/`awk` 就能跑，任何 Agent 沙箱、任何裸机即装即用。
- **全球覆盖 + 智能纠错**：内置 200+ 城市坐标库，模糊输入（`delhi`、`tOKyo`）都能识别，还支持直接传经纬度。
- **真实世界数据，不是玩具**：自动剔除停更的"僵尸站点"和传感器故障尖峰，数据缺失时段折线断开而不是瞎补零。

## 效果演示

| 多城对比（7 日 PM2.5） | 单城 48h 臭氧 |
| --- | --- |
| ![beijing vs tokyo](examples/beijing_vs_tokyo.svg) | ![london o3](examples/london_48h_o3.svg) |

| 同城多站点快照 | 单城多指标（深色主题） |
| --- | --- |
| ![delhi snapshot](examples/delhi_snapshot.svg) | ![beijing dark](examples/beijing_pm25_pm10_dark.svg) |

## 特性

- **零重型依赖**：仅需 `bash` / `jq` / `awk` / `curl`，渲染器为纯 awk 实现的 SVG 生成器——不需要 Python、Matplotlib 或 Node.js。
- **全球覆盖**：内置 200+ 全球主要城市坐标库，也支持直接传入 `lat,lon`。
- **智能站点优选**：25km 半径检索 → 剔除 24h（必要时 72h）未更新的僵尸站点 → 优先选择政府参考级监测站（Reference-grade）。
- **专业视觉**：醒目标注物理浓度单位（µg/m³），默认叠加 WHO 空气质量指南 24 小时基准虚线（PM2.5=15 / PM10=45 / O3=100 / NO2=25 / SO2=40 / CO=4），浅/深双主题。
- **工程化**：本地缓存（小时级 20min / 日级 2h TTL）、429 限流指数退避、数据断点（缺失时段折线断开而非错误插值）、UTC→站点当地时间自动对齐。

## 快速开始

### 1. 配置 API Key（免费，约 1 分钟）

1. 打开 [OpenAQ Explorer 注册页](https://explore.openaq.org/register) 注册或[直接登录](https://explore.openaq.org/login)。
2. 登录后打开[账户页](https://explore.openaq.org/account)，页面下方即可看到并复制你的 API Key。
3. 任选其一配置：

```bash
export OPENAQ_API_KEY="你的key"                                # 临时 / CI
echo 'OPENAQ_API_KEY=你的key' > ~/.config/air-chart/config     # 持久
```

> 凭证策略刻意保持轻量：OpenAQ Key 属免费公共服务凭证，无需系统钥匙串，明文配置文件即可。
> 没有 Key 也能用 `--demo` 演示模式预览完整效果。

### 2. 运行

```bash
# 单城市 7 天 PM2.5 趋势
./scripts/air_chart.sh --city Beijing --param pm25 --period 7d

# 多城市对比（最多 4 城）
./scripts/air_chart.sh --city Tokyo --city Seoul --param pm25 --period 7d

# 单城市多指标（如 PM2.5 + PM10）
./scripts/air_chart.sh --city Beijing --param pm25 --param pm10 --period 30d

# 48 小时小时级曲线（观察昼夜规律）
./scripts/air_chart.sh --city Singapore --param o3 --period 48h

# 同城多站点实时快照（柱状图）
./scripts/air_chart.sh --city Delhi --param pm10 --snapshot

# 深色主题 + 指定输出
./scripts/air_chart.sh --city London --param no2 --period 14d --theme dark -o london.svg
```

### 3. 作为 AI Agent Skill 安装

将本仓库（或其中 `SKILL.md` + `scripts/` + `data/`）放入你的 Agent skills 目录即可，例如：

```bash
git clone https://github.com/qiakai/air-chart.git ~/.claude/skills/air-chart
# 或: npx skills add qiakai/air-chart
```

之后对 Agent 说"对比东京和首尔过去 7 天的 PM2.5 走势"即可自动调用。

`SKILL.md` 为英文版（兼容各平台收录与路由），中文版见 `SKILL.zh.md`。

## 命令参数

| 参数 | 说明 | 取值 |
| --- | --- | --- |
| `--city, -c` | 城市名（可重复，≤4 个）或坐标 `"lat,lon"` | `Beijing`、`New Delhi`、`39.9,116.4` |
| `--param, -p` | 污染物指标（默认 `pm25`） | `pm25` `pm10` `o3` `no2` `so2` `co` |
| `--period, -t` | 时间跨度（默认 `7d`） | `24h` `48h`（小时级）· `7d` `14d` `30d`（日级） |
| `--snapshot` | 同城多站点实时快照柱状图 | 开关 |
| `--theme` | 主题 | `light` / `dark` |
| `--lang` | 输出语言（图表 + 提示文案） | `en` / `zh`（默认按系统 locale 自动检测） |
| `--out, -o` | 输出 SVG 路径 | 默认 `./air-chart-<时间戳>.svg` |
| `--demo` | 演示模式（免 API Key） | 开关 |

## 架构

```text
[城市/指标/时间跨度]
   │
   ▼
geo_resolve.sh      城市名 → 坐标+时区（内置坐标库 / 坐标直传）
   │
   ▼
openaq_client.sh    OpenAQ API v3：鉴权、User-Agent 标识、md5 缓存、
                    429 指数退避、活性过滤(24h/72h)、按参数固定 ID
                    匹配传感器、参考级站点优选
   │
   ▼
data_transform.awk  清洗(负值/超物理上限尖峰)、断点检测(缺失时段
                    断开, 严禁填 0)、统计聚合、当地时区标签
   │
   ▼
render_draw.sh      纯 awk SVG 渲染（折线/柱状 + WHO 基准虚线 + 图例）
```

`data/parameters.tsv` 为静态参数字典（对齐 openaq-api 污染物固定 ID）：slug / param_id / 名称 / 单位 / WHO 24h 基准 / 物理上限 / 指标专属色，消除冗余 `/parameters` 探测。视觉规范对齐 openaq-explorer：指标专属色板（PM2.5 `#E65100`、PM10 `#6A1B9A`、O3 `#0277BD`、NO2 `#00838F`）、多城色盲友好色板、WHO 基准线达标绿 `#10B981` / 超标红 `#EF4444`；站点单位与默认单位不一致时自动隐藏 WHO 线以防量纲误导。

## 退出码

| 码 | 含义 |
| --- | --- |
| 3 | 未配置 API Key（附注册引导） |
| 4 | 网络 / API 异常 / 限流重试耗尽 |
| 5 | 无活性站点或无有效数据 |
| 2 | 城市名无法解析（附相近候选） |

## 延伸阅读

- [技术解析文章](docs/article-zh.md)：零依赖 CLI 数据管道 + Agent Skill 视觉交付的架构实践

## License

MIT
