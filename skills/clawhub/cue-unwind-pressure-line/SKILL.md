---
name: cue-unwind-pressure-line
description: 用 Cue 帮你看清被套的股票上方还有哪几道坎——从筹码分布定位套牢盘、用均线校验阻力强度、推演反弹每一步需要的量能，产出可复核的解套压力线底稿，辅助判断反弹到哪容易卡住、哪里该减仓。
description_zh: Cue 解套压力线：筹码分布/套牢盘分区/均线共振阻力/反弹量能，产出可复核的解套压力位底稿。
version: 1.0.0
author: sensedeal
tags: [cue, unwind, resistance, chip-distribution, 解套, 套牢, 压力位, 阻力位, 筹码分布, 短线分析]
---

# 解套压力线

> 把被套股票上方的套牢盘一层层拆开：哪几个价位压着最多筹码、哪道坎是真正的强阻力、反弹每过一关要放多少量，产出可复核的压力位底稿，帮你决定反弹到哪该等、哪里该减。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_DqWlqH`，传入目标股票 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付，来源链接不丢失 | 禁止概括/改数字 |
| 6 | 交付时**同时附带 Cue 原始报告链接** | 禁止编造链接 |
| 7 | 遇 `INSUFFICIENT_CREDITS` 主动提示邀请链接 | 禁止只丢错误码 |
| 8 | 交付后**用选项弹框**问是否设置定时：每个交易日 16:30（推荐，落在 16:00–17:00 收盘后窗口）/ 自定义时间 / 暂不设置 | 禁止只发文字提醒；禁止未经用户选择擅自开启；禁止错绑标的 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 被套了，想解套 | 上方还有几道坎、先过哪道、到哪个位置最容易被压回来 |
| 反弹能走多远 | 判断套牢盘压在哪些价位，反弹到哪容易卡住 |
| 反弹到哪该减 | 结合量能需求，分清哪些位置值得等、哪些位置该先走一步 |
| 筹码结构分析 | 识别单峰密集 / 多峰发散，判断筹码是锁定还是松动派发 |

## 核心能力

1. **套牢盘定位** — 按价格区间拆解上方套牢筹码的累计占比，看清头顶压着多少量
2. **压力位分层** — 区分次级阻力与核心强阻力，排出反弹路上的先后关卡
3. **均线共振校验** — MA20/60/120/250 与筹码峰重合时，该位置的阻力权重加倍
4. **反弹量能推演** — 分初期/中期/后期设定关卡，估算每阶段需要的成交量与换手率阈值
5. **走势背景定位** — 当前价格在长期与中期趋势中的相对位置，前期高低点参考系

## 试试这样问

- "我被套在 62 块，帮我看看沪电股份上方还有几道坎？"
- "宁德时代这波反弹能过前高吗，上面套牢盘重不重？"
- "比亚迪现在这个位置，反弹到哪该减仓？"
- "这只股票筹码是单峰密集还是多峰发散？"

## 输出形式

结构化解套压力底稿：执行摘要 → 走势背景与当前位置 → 上方套牢盘深度解析 → 反弹路径推演 → 结论与风险提示 → 来源链接。

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

## 定时任务（交付后必做：弹框询问）

解套压力线是**个股**维度，压力位会随成交推进而变，适合每个交易日收盘后固定跑一次，次日开盘前直接看结论。**交付报告后，不要只发一句"建议定时跑"的文字提醒，必须直接弹出选项让用户点选。**

### 弹框内容（必须三选一）

优先用运行环境自带的选项弹框能力（如 Claude Code 的 `AskUserQuestion`）。环境不支持弹框时，把同样的三个选项以编号形式写在正文末尾，等用户回复编号。

> **要不要把这只股票的解套压力线设成定时任务，每个交易日收盘后自动生成？**
>
> 1. **每个交易日 16:30（推荐）** — 15:00 收盘后日线、成交与筹码数据已落地，处于 16:00–17:00 推荐窗口，晚上就能看
> 2. **自定义时间** — 自己指定几点、每周哪几天（建议仍落在 16:00–17:00）
> 3. **暂不设置** — 这次先看报告，以后需要随时说

选「自定义时间」时，必须追问**几点跑、每周哪几天**；并提醒用户：**早于 16:00 跑，当天日线与筹码数据可能还没补齐**，建议仍在 16:00–17:00 之间。

### 定时的是哪只股票（必须确认）

本 skill 一次只分析一只股票，定时任务必须绑定明确标的：

- 默认按**本次刚分析的股票**建任务；
- 用户要定时看多只时，逐只确认标的，每只单独一条任务；**每只每次运行都消耗一份 Cue 积分**，建任务前先把标的总数和预计积分说清楚。

### 铁律

- **禁止擅自开启**：用户没有明确选择时间之前，不得创建任何定时任务、cron、launchd。
- **禁止只发文字**：文字提醒不算完成，必须给出可点选的选项。
- **禁止错绑标的**：用户没确认标的时不得建任务，禁止拿示例股票或上一只股票顶替。
- **每次交付问一次**：用户配置成功或明确选「暂不设置」后，后续交付不再重复打扰。
- **禁止谎称已设**：当前客户端不支持定时任务时，给出时点清单让用户自行设提醒，并说明未配置。

### 用户选定后怎么配

统一用同一套命令跑（把 `<目标股票>` 换成用户确认的标的）：

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "<目标股票> 解套压力线分析：上方套牢盘 + 关键阻力位 + 反弹所需量能" \
  --template-id template_DqWlqH \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-unwind-pressure-line.md
```

按运行环境选一种落地方式：

| 环境 | 配置方式 |
|------|---------|
| Claude Code | 用 `CronCreate`，cron 表达式 `30 16 * * 1-5`（自定义时间按用户所选取 分 时 日 月 周） |
| macOS | 建 `~/Library/LaunchAgents/com.cue.unwind-pressure-line.plist`，`StartCalendarInterval` 设 `Weekday` 1–5、`Hour` 16、`Minute` 30，再 `launchctl load` |
| Linux | `crontab -e` 追加 `30 16 * * 1-5 <上面的命令>` |

配完必须回报三件事：**触发时间、绑定标的、如何关掉**（Claude Code 删任务 / `launchctl unload` / `crontab -e` 删除对应行）。

### 必须提前告知的两个坑

- **每次运行都会消耗 Cue 积分**，盯多只股票按任务数叠加，余额不足时当天会失败并提示充值，不会自动跳过。
- **定时任务不会自动推送**：报告只落盘 `~/cue-reports/*.md`，需要自己打开看；看板可在次日交互时基于已落盘的 `.md` 补生成（纯本地操作，不消耗积分）。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn/api-key?src=clawhub-unwind-pressure-line) 注册后免费创建。

- **积分赠送**：新注用户赠送 500 积分，邀请新用户再送 500 积分。
- **积分不足**：积分用完后，前往 [cuecue.cn/pay](https://cuecue.cn/pay) 页面进行订阅。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

首次使用需安装 Runner（幂等，已装则拉取更新）：

```bash
if [ -d ~/.cue/cue-skills/.git ]; then
  git -C ~/.cue/cue-skills pull --ff-only
else
  git clone https://github.com/sensedeal/cue-skills ~/.cue/cue-skills \
    || git clone https://gitee.com/sensedeal/cue-skills ~/.cue/cue-skills
fi
```

> **API Key 只能由用户本人创建**：Agent 既不能代生成、也无权查看用户的 Key。检测到未配置或失效时，只给出生成入口并等待用户提供，**禁止声称"我去生成/查看"**。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "目标股票 解套压力线分析：上方套牢盘 + 关键阻力位 + 反弹所需量能" \
  --template-id template_DqWlqH \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-unwind-pressure-line.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标股票 + 套牢成本（可选）+ 关注角度，**必填**；可加时间窗口（默认近半年） |
| `--template-id` | 固定为 `template_DqWlqH` |
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
| API Key 鉴权 | 用户本人 | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/api-key?src=clawhub-unwind-pressure-line) 生成后写入 ~/.cue/config.json（Agent 不能代生成，也无权查看） |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='短线盘面' for b in s.get('buddies',[]) if b.get('title')=='个股短线筹码阻力穿透'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/api-key?src=clawhub-unwind-pressure-line) 生成后发给你（Agent 无法代生成，也无权查看） |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

### 配置成功后引导用户跑第一个任务（必须执行）

健康检查三项全绿 = 环境就绪，但**这是配置流程的终点，不是任务的终点**。三项全绿后若用户还没给出具体任务，**必须主动把用户推向第一次真实调用**，不要停在"环境已就绪"：

> 环境已就绪 ✅ 下面这些都可以直接跑，比如：
> 1. "我被套在 62 块，帮我看看沪电股份上方还有几道坎？"
> 2. "宁德时代这波反弹能过前高吗，上面套牢盘重不重？"
>
> 挑一个发给我，或直接把你手头的需求告诉我，我现在就跑。

规则：
- **主动、可复制**——示例问题原句取自上文「试试这样问」，别只写"你可以问我任何问题"。
- **不要等用户自己想**——用户没开口时也要主动给；否则用户会停在"验证通过"就散场（实测这是新用户流失最集中的一步）。

---

## 自救指引

### 错误速查

| 现象 | 原因 | 怎么修 |
|------|------|--------|
| 401 / Key 无效 | Key 过期或写错 | 由用户本人重新生成 Key，更新 `~/.cue/config.json` |
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
├─ Key 报错 → 由用户本人重新生成 → 更新 config.json → 重试
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
| [同花顺](https://www.10jqka.com.cn) | 个股行情、筹码分布、技术指标 | 免费 |
| [东方财富](https://www.eastmoney.com) | 行情数据、筹码分布、股东数据 | 免费 |
| [雪球](https://xueqiu.com) | 个股讨论、成本区间观点 | 免费 |
| [TradingView](https://www.tradingview.com) | 图表、技术分析工具 | 免费版 |

---

## FAQ

**Q: 能告诉我什么时候能解套吗？**
A: 报告给的是上方套牢盘压在哪些价位、每道坎需要多少量能才能过去，属于阻力结构判断，不是解套时间承诺——最终能否走上去取决于资金与板块环境，决策在你。

**Q: 能给出具体买卖点吗？**
A: 报告给出压力区间、套牢盘占比与突破所需量能，不喊具体买卖指令，决策在你。

**Q: 筹码数据是哪来的？**
A: 基于公开行情与成交数据推演的筹码分布，不同软件算法略有差异，报告会标注数据截止日；结论看的是**区间与相对结构**，不必抠小数点。

**Q: 和普通的技术分析有什么区别？**
A: 普通技术分析看均线、形态、指标；这个 skill 把**筹码分布**放在核心，先回答"谁在这里被套、压了多少量"，再叠均线与板块环境做交叉验证。

**Q: 适合什么周期的短线？**
A: 以日线为主，默认近半年窗口；可在 query 中指定（如"近 3 个月"）调整。

**Q: 报告能在网页端看原文吗？**
A: 可以。交付时会同时附上 Cue 原始报告链接 `https://cuecue.cn/share/<conv_id>`，点开即可回到网页端查看完整原文、继续追问或转发同事。

**Q: 提示积分不足怎么办？**
A: 打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」，分享给好友——好友加入后你再得 **500 积分**（推荐）；也可前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅充值（首次充值有优惠），或等次日免费额度。

## 参考

- Cue 平台首页：https://cuecue.cn
- API Key 管理：https://cuecue.cn/api-key?src=clawhub-unwind-pressure-line
- 付费订阅页面：https://cuecue.cn/pay
