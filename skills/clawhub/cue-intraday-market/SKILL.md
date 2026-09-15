---
name: cue-intraday-market
description: 用 Cue 做大盘盘中分析——聚合早盘核心行情，穿透指数表象识别市场真实情绪与资金流向，定位逆势主线与风险雷区，输出盘中观察评论。
description_zh: Cue 大盘盘中分析：穿透指数看情绪/资金/主线/风险，输出盘中观察评论。
version: 1.1.0
author: sensedeal
tags: [cue, intraday, market-overview, panel-analysis, 盘中分析, 盘面透视, 市场情绪, 资金流向, 主线]
---

# 大盘盘中分析

> 聚合早盘核心行情数据，穿透指数表象识别市场真实情绪与资金流向，定位逆势主线与风险雷区，输出盘中观察评论。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_mb_OZI`，传入关注角度 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付，来源链接不丢失 | 禁止概括/改数字 |
| 6 | 交付时**同时附带 Cue 原始报告链接** | 禁止编造链接 |
| 7 | 遇 `INSUFFICIENT_CREDITS` 主动提示邀请链接 | 禁止只丢错误码 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 盘中看盘 | 交易日盘中快速了解大盘真实情绪和资金动向 |
| 早盘概览 | 开盘后快速聚合当日核心行情 |
| 主线捕捉 | 定位当日逆势走强的主线和板块 |
| 风险识别 | 提前发现当日的风险雷区 |

## 核心能力

1. **早盘行情聚合** — 指数涨跌、涨跌家数、成交额等核心数据一览
2. **市场情绪识别** — 穿透指数表象，判断真实情绪和赚钱效应
3. **资金流向** — 板块资金、主力资金进出方向
4. **主线与风险** — 定位逆势主线，标出风险雷区
5. **盘中操作建议** — 输出盘中观察评论（含操作方向）

## 试试这样问

- "今天盘面怎么样？"
- "现在市场情绪如何，资金在往哪走？"
- "今天有什么主线板块值得关注？"
- "早盘有哪些风险要注意？"

## 输出形式

结构化盘中观察评论：早盘行情概览 → 市场情绪 → 资金流向 → 主线板块 → 风险雷区 → 操作建议 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/XXXXX)（示例链接，待替换为真实分享链接）

## 交付规范（必须执行）

把最终报告发送给用户时，**必须同时附带 Cue 原始报告链接**，方便用户回到网页端查看完整原文、继续追问或转发同事。

**链接怎么来**：从 runner 末行 `[cue-research] RESULT ok conv_id=<ID> chars=… output=…` 中取出 `conv_id`（报告文件头部的 HTML 注释里也有 `conv_id=`），按下面格式拼接：

```
https://cuecue.cn/share/<conv_id>
```

交付模板（照此结构输出）：

```
报告已完成 ✅

<报告正文……>

---
**Cue 原始报告**：https://cuecue.cn/share/<conv_id>
**本地副本**：~/cue-reports/<文件名>.md
```

规则：
- `conv_id` 必须取自实际输出，**禁止编造**或使用文档示例里的 id。
- 末行为 `RESULT empty`（无 conv_id 或报告为空）时**不要拼链接**，如实告知未取到报告并给后续建议。
- 用户明确说不要链接时可不附。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "盘中盘面透视：早盘行情 + 市场情绪 + 资金流向 + 主线与风险" \
  --template-id template_mb_OZI \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-intraday-market.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 关注角度（如"今日盘面""早盘主线"），**必填** |
| `--template-id` | 固定为 `template_mb_OZI` |
| `--output` | 落盘路径 |

---

## 格式转换

Cue 输出 Markdown。安装 pandoc 后可转换为 Word 或 PDF：

```bash
# .md → .docx（Word）
pandoc report.md -o report.docx

# .md → .pdf
pandoc report.md -o report.pdf --pdf-engine=xelatex
```

输出文件与输入同目录、同名、不同后缀。

### 依赖安装

| 目标格式 | 依赖 | macOS | Ubuntu |
|----------|------|-------|--------|
| Word (.docx) | pandoc | `brew install pandoc` | `sudo apt install pandoc` |
| PDF (.pdf) | pandoc + LaTeX | `brew install --cask basictex` | `sudo apt install texlive-xetex` |

---

## 架构说明

本 Skill **不在本地执行检索**。流程是 Agent → Cue API（cuecue.cn）→ 外部数据源。解析结果的质量和时效取决于 Cue 服务端和外部数据源的状态。

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 你 | 重新生成 Key，更新 ~/.cue/config.json |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='短线盘面' for b in s.get('buddies',[]) if b.get('title')=='盘中盘面透视'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | [cuecue.cn/api-key](https://cuecue.cn/api-key) 重新生成 |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

---

## 自救指引

### 错误速查

| 现象 | 原因 | 怎么修 |
|------|------|--------|
| 401 / Key 无效 | Key 过期或写错 | 重新生成 Key，更新 `~/.cue/config.json` |
| 超时 >30s | 服务维护/过载 | 等 5 分钟，跑诊断；当天内重试 |
| 搭子不可用 | 临时下线 | 网页端直接跑，或等 1 小时 |
| 积分不足 | 余额 < 消耗 | **按「积分不足专项提示」主动引导**（充值 / 邀请好友得积分 / 等次日免费额度） |
| 中途中断 | 队列满/数据源波动 | **不换 prompt**，相同命令续接 |
| `RESULT empty` | 公开源无匹配 | 缩小范围，换关键词 |
| config.json 报错 | JSON 格式不对 | `{"api_key": "sk..."}` 无多余逗号 |

### 积分不足专项提示（必须执行）

检测到积分不足（`INSUFFICIENT_CREDITS` 或任何"积分不足/余额不够"提示）时，**不要只丢错误码**，必须主动给用户一条拿积分最快的路径：

> 你的 Cue 积分不足，本次任务未能启动。两个办法：
> 1. **邀请好友得 500 积分（推荐）**：打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」，分享给好友——好友加入后你再得 **500 积分**。
> 2. **直接充值**：前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅（首次充值有优惠）；或等次日免费额度。

规则：
- 提示要**主动、简短、可点**——把「首页」和「左下角」两个关键动作说清楚，不要让用户自己找入口。
- 积分不足**不要重试**（`retryable: false`），也不要换 query 绕。
- 用户回复已充值/已邀请后，用**完全相同的命令**重跑。

### 决策树

```
出问题？
├─ Key 报错 → 重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 缩窄关键词 → 确认该主题有公开数据
```

### 调度建议

| 时段 | 建议 |
|------|------|
| 交易日盘中/盘后 | 正常使用（数据最新鲜） |
| 夜间/周末 | 可能有维护，跑前先诊断 |
| 新 Key | 必须先诊断确认生效 |
| 连续失败 | 停 15 分钟再试，不要反复重试 |

---

## 降级方案

Cue 长时间不可达时的手动替代渠道：

| 渠道 | 覆盖 | 费用 |
|------|------|------|
| [同花顺](https://www.10jqka.com.cn) | 大盘行情、板块资金、涨跌家数 | 免费 |
| [东方财富](https://www.eastmoney.com) | 行情数据、资金流向、板块异动 | 免费 |
| [雪球](https://xueqiu.com) | 盘面讨论、市场情绪 | 免费 |
| [TradingView](https://www.tradingview.com) | 指数图表、技术分析 | 免费版 |

---

## FAQ

**Q: 是实时盘中数据吗？**
A: 基于 Cue 抓取的公开行情数据，盘中时段数据更新更快，具体时效取决于数据源。

**Q: 会给具体买卖建议吗？**
A: 这个搭子会给出盘中操作方向和建议，但最终决策仍在你。

**Q: 和"短线走势与技术面分析"有什么区别？**
A: 那个是个股层面的走势分析，这个是大盘层面的盘中观察——一个看个股，一个看全局。

**Q: 报告能在网页端看原文吗？**
A: 能。交付时会附 `https://cuecue.cn/share/<conv_id>`，点开即可在网页端查看完整原文、继续追问或转发同事。

**Q: 提示积分不足怎么办？**
A: 打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」分享给好友——好友加入后你再得 **500 积分**（最快）；也可以前往 [cuecue.cn/pay](https://cuecue.cn/pay) 充值（首次充值有优惠），或等次日免费额度。
