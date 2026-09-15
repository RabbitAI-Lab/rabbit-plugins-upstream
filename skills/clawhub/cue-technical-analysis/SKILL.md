---
name: cue-technical-analysis
description: 用 Cue 对个股做短线走势与技术面分析——从量价关系、资金流向、趋势结构入手，计算波动率与最大回撤，产出可复核的走势分析底稿，辅助判断短线的买卖节奏和关键价位。
description_zh: Cue 短线走势与技术面分析：穿透量价关系/资金流向/趋势结构/支撑压力位，产出可复核的走势底稿。
version: 1.1.0
author: sensedeal
tags: [cue, technical-analysis, short-term-trading, quantity-price, 短线分析, 技术分析, 量价分析, 资金流向, 支撑压力位]
---

# 短线走势与技术面分析

> 围绕个股的历史行情、量价与强弱趋势，计算波动率、最大回撤与趋势结构，产出可复核的走势分析底稿，帮你看清短线的买卖节奏和支撑压力位。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_L1YwFU`，传入目标股票 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付，来源链接不丢失 | 禁止概括/改数字 |
| 6 | 交付时**同时附带 Cue 原始报告链接** | 禁止编造链接 |
| 7 | 遇 `INSUFFICIENT_CREDITS` 主动提示邀请链接 | 禁止只丢错误码 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 短线交易决策 | 判断个股短期的买卖节奏和关键价位 |
| 量价关系分析 | 识别放量突破、缩量回调、量价背离等信号 |
| 技术面复盘 | 复盘个股近期走势的技术结构 |
| 支撑压力判断 | 找出关键支撑位和压力位 |

## 核心能力

1. **量价关系分析** — 成交量与价格走势的配合/背离，识别放量突破、缩量回调
2. **资金流向** — 主力资金进出、筹码分布，判断资金态度
3. **趋势结构** — 均线、趋势线、技术形态，判断当前强弱与趋势方向
4. **波动率与回撤** — 波动率、最大回撤等风险度量，评估短线波动
5. **支撑压力位** — 关键支撑位、压力位，作为买卖参考

## 试试这样问

- "帮我分析一下宁德时代短线的量价走势"
- "比亚迪现在短线能买吗，支撑位在哪？"
- "茅台最近的量价关系怎么样？"
- "这只股票放量了，是突破还是出货？"

## 输出形式

结构化技术面底稿：行情概览 → 量价关系 → 资金流向 → 趋势结构 → 波动率与回撤 → 支撑压力位 → 风险提示 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/buddy-test-81a83d14ba86)

> 上例中的 token 是示例，**不可复制到实际交付中**。

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

- **积分赠送**：新注用户赠送 500 积分，邀请新用户再送 500 积分。
- **积分不足**：积分用完后，前往 [cuecue.cn/pay](https://cuecue.cn/pay) 页面进行订阅。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "目标股票 短线量价与技术面分析：量价关系 + 资金流向 + 趋势结构 + 支撑压力位" \
  --template-id template_L1YwFU \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-technical-analysis.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标股票 + 关注角度，**必填** |
| `--template-id` | 固定为 `template_L1YwFU` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='短线盘面' for b in s.get('buddies',[]) if b.get('title')=='短线资金量价与技术面分析'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [同花顺](https://www.10jqka.com.cn) | 个股行情、技术指标、资金流向 | 免费 |
| [东方财富](https://www.eastmoney.com) | 行情数据、资金流向、技术指标 | 免费 |
| [雪球](https://xueqiu.com) | 个股讨论、资金面观点 | 免费 |
| [TradingView](https://www.tradingview.com) | 图表、技术分析工具 | 免费版 |

---

## FAQ

**Q: 能给出具体买卖点吗？**
A: 报告给出支撑压力位、量价信号和趋势判断，不喊具体买卖指令，决策在你。

**Q: 适合什么周期的短线？**
A: 以日线为主，可在 query 中指定时间窗口（如"近 20 个交易日"）调整。

**Q: 和技术指标类工具（如 MACD/KDJ）有什么区别？**
A: 这个搭子不止看单一指标，而是把量价、资金、趋势、波动回撤放在一起交叉看，输出一份可复核的底稿，而非单个指标信号。

**Q: 报告能在网页端看原文吗？**
A: 可以。交付时会同时附上 Cue 原始报告链接 `https://cuecue.cn/share/<conv_id>`，点开即可回到网页端查看完整原文、继续追问或转发同事。

**Q: 提示积分不足怎么办？**
A: 打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」，分享给好友——好友加入后你再得 **500 积分**（推荐）；也可前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅充值（首次充值有优惠），或等次日免费额度。

## 参考

- Cue 平台首页：https://cuecue.cn
- API Key 管理：https://cuecue.cn/api-key
- 付费订阅页面：https://cuecue.cn/pay
