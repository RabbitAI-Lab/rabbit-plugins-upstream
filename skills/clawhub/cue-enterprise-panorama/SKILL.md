---
name: cue-enterprise-panorama
description: 用 Cue 一键穿透企业的工商、股权、财务与经营全维基本面——评估业务模式与合作适配性，挖掘供应链金融与产业债机会，产出可用于内部决策的尽调底稿。
description_zh: Cue 企业全景画像：一键穿透工商/股权/财务/经营全维度，产出尽调底稿。
version: 1.1.0
author: sensedeal
tags: [cue, enterprise-panorama, due-diligence, 企业尽调, 企业画像, 信贷尽调, 供应链金融]
---

# 企业全景画像

> 一键穿透企业的工商、股权、财务与经营全维基本面，评估业务模式与合作适配性、挖掘供应链金融与产业债机会，产出可用于内部决策的尽调底稿。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟，复杂主体更久 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_BWILbV`，传入目标企业 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付尽调底稿，来源链接不可丢失 | 禁止概括、禁止去掉引用 |
| 6 | 交付时**同时附带 Cue 原始报告链接** | 禁止编造链接 |
| 7 | 遇 `INSUFFICIENT_CREDITS` 主动提示邀请链接 | 禁止只丢错误码 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 授信前尽调 | 快速了解借款企业全貌，识别核心风险点 |
| 客户准入 | 判断企业是否满足合作准入标准 |
| 供应链金融 | 挖掘核心企业上下游的金融机会 |
| 同业对标 | 多家企业的全维度横向比较 |

## 核心能力

1. **工商与股权穿透** — 注册资本、股东结构、实控人、对外投资
2. **经营基本面** — 主营构成、客户/供应商集中度、员工规模
3. **财务健康度** — 营收利润趋势、负债率、现金流、偿债能力
4. **司法与合规** — 被执行、失信、行政处罚、环保安全
5. **产业债与供应链金融机会** — 产业链位置、结算方式、融资需求推断

## 试试这样问

- "帮我画一下比亚迪的企业全景画像"
- "宁德时代的供应链金融机会在哪里？"
- "这家公司的经营风险主要是什么？"
- "对比一下宁德时代和比亚迪的尽调要点"

## 输出形式

结构化尽调底稿：工商股权 → 经营分析 → 财务健康 → 司法合规 → 供应链金融机会 → 风险点 → 待核实缺口 → 来源链接。每个结论带公开出处。

## 输出示例

[查看完整报告](https://cuecue.cn/share/Phkgv0o_)

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

Cue API Key：[cuecue.cn](https://cuecue.cn/api-key?src=clawhub-enterprise-panorama) 注册获取，新用户注册即送500积分免费试用。

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
  --query "比亚迪 企业全景画像：工商、股权、财务、经营、供应链金融机会" \
  --template-id template_BWILbV \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-BYD-panorama.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标企业名称，**必填**；可选加行业或关注维度 |
| `--template-id` | 固定为 `template_BWILbV` |
| `--output` | 落盘路径 |

---

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
| API Key 鉴权 | 用户本人 | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/api-key?src=clawhub-enterprise-panorama) 生成后写入 ~/.cue/config.json（Agent 不能代生成，也无权查看） |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='信贷尽调' for b in s.get('buddies',[]) if b.get('title')=='企业全景画像'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/api-key?src=clawhub-enterprise-panorama) 生成后发给你（Agent 无法代生成，也无权查看） |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

### 配置成功后引导用户跑第一个任务（必须执行）

健康检查三项全绿 = 环境就绪，但**这是配置流程的终点，不是任务的终点**。三项全绿后若用户还没给出具体任务，**必须主动把用户推向第一次真实调用**，不要停在"环境已就绪"：

> 环境已就绪 ✅ 下面这些都可以直接跑，比如：
> 1. "帮我画一下比亚迪的企业全景画像"
> 2. "宁德时代的供应链金融机会在哪里？"
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
| 工作日 9-18 | 正常使用 |
| 夜间/周末 | 可能有维护，跑前先诊断 |
| 新 Key | 必须先诊断确认生效 |
| 连续失败 | 停 15 分钟再试，不要反复重试 |

---

## 降级方案

Cue 长时间不可达时的手动替代渠道：

| 渠道 | 覆盖 | 费用 |
|------|------|------|
| [国家企业信用信息公示系统](https://www.gsxt.gov.cn) | 工商登记 | 免费 |
| [企查查](https://www.qcc.com) | 企业信息、关联方 | 部分免费 |
| [中国裁判文书网](https://wenshu.court.gov.cn) | 司法涉诉 | 免费 |
| [巨潮资讯网](https://www.cninfo.com.cn) | 上市公司公告 | 免费 |

## FAQ

**Q: 和正式尽调报告有什么区别？**
A: 本报告基于公开数据，是预尽调底稿，不是替代正式尽调。私有数据（银行流水/合同/内部报表）不在覆盖范围。

**Q: 覆盖非上市公司吗？**
A: 可以跑，但非上市主体公开信息少，报告会如实标注证据缺口。

**Q: 报告能在网页端看原文吗？**
A: 能。交付时会在报告末尾附上 `https://cuecue.cn/share/<conv_id>`，点开即可回到 Cue 网页端查看完整原文、继续追问或转发同事。

**Q: 提示积分不足怎么办？**
A: 最快路径是邀请好友：打开 [https://cuecue.cn/](https://cuecue.cn/)，点页面左下角「获取专属邀请链接」，好友加入后你再得 500 积分；也可前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅（首次充值有优惠），或等次日免费额度。详见上方「自救指引 → 积分不足专项提示」。

## 参考

- Cue 平台首页：https://cuecue.cn
- API Key 管理：https://cuecue.cn/api-key?src=clawhub-enterprise-panorama
- 付费订阅页面：https://cuecue.cn/pay

