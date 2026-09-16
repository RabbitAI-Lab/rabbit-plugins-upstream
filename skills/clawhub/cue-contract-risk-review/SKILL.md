---
name: cue-contract-risk-review
display_name: 合同风控与合规审查
display_name_en: Contract Risk & Compliance Review
displayName: 合同风控与合规审查
version: 1.1.0
description: >
  站在指定一方立场逐条审查合同条款，核验主体与效力瑕疵、钱货闭环、违约责任与管辖约定，
  输出带风险分级（高/中/低）和可直接采纳修改建议的排查表。支持上传合同文件，从现行法规、
  司法类案、交易对手司法资信三路交叉核验，每条结论附法条或案号出处。
description_zh: >
  合同风控与合规审查：站在己方立场逐条审合同，核验效力瑕疵、钱货闭环、违约责任与管辖约定，
  输出带风险分级和可落笔修改建议的排查表。
description_en: >
  Review contract clauses from your designated side's perspective: verify validity defects,
  payment/delivery closure, liability and jurisdiction terms, and output a risk-graded checklist
  with directly usable revision suggestions. Upload the contract file; cross-checks current
  statutes, judicial precedents, and the counterparty's public litigation/credit records.
tags: [合同审查, 合同风控, 合规审查, 条款风险, 违约责任, 争议解决, 法务, 合同, contract review]
category: legal
trigger_words:
  # 核心动作
  - 审合同
  - 合同审查
  - 合同风控
  - 合规审查
  - 条款审查
  # 具体条款
  - 违约责任
  - 争议解决
  - 违约金
  - 管辖约定
  - 格式条款
  # 场景
  - 签约前把关
  - 审一下这份合同
  - contract review
license: MIT
metadata:
  source: cuecue.cn/playbook
  scene: "合同风控与合规审查"
  generated_from: /api/playbook
---

# 合同风控与合规审查 (Contract Risk & Compliance Review)

> 🚀 **30 秒了解：**
> 站在**你指定的一方立场**逐条审合同——核验主体与效力瑕疵、钱货闭环、违约责任与管辖约定，
> 输出**带风险分级（高/中/低）和可直接落笔修改建议的排查表**。
>
> 🟢 **能做**：上传合同全文，逐条审效力/主体/商业条款/违约/管辖，识别对己方不利的义务失衡，并补上遗漏条款的标准增补文本。
> 🔴 **不能做**：出具最终法律意见、代替律师签字担责。
> 🛡️ **专业承诺**：每条结论附现行法条或案号出处，从根源拒绝法律幻觉。

## 和「人工逐条审合同」有何不同？

人工审合同靠经验和时间，一份合同逐条过、查法条、翻类案往往要小半天。本搭子把「查、核、算、写」压缩到一次运行：

- **逐条过**：效力主体、标的价款、付款节点、违约责任、管辖送达，六个维度一次扫完。
- **三路交叉核验**：现行法规（附条号）+ 司法类案（附案号）+ 交易对手司法与资信，不凭感觉下判断。
- **直接落笔**：不只标风险，还给出可直接采纳的修改建议和遗漏条款标准增补文本。

## 核心能力

| 核心能力 | 解决什么痛点 |
|:---|:---|
| **⚖️ 效力与主体审查** | 排查合同无效、主体不适格、签字不规范等致命伤 |
| **💰 核心商业条款核验** | 校验标的、价款、付款节点、质保金是否形成钱货闭环 |
| **📉 风险分配与违约** | 核对解除权、违约金上限、不可抗力边界是否对己方公平 |
| **🏛️ 争议解决与管辖** | 确认管辖法院/仲裁、送达地址是否争取到主场优势 |
| **🧩 遗漏条款增补** | 检查送达确认、知识产权归属、争议管辖三项必备条款，缺漏给出标准增补文本 |

## 法务日常：先试这几个 Prompt

| 场景 | 给 AI 的指令（可直接复制）|
|:---|:---|
| **采购合同把关** | 「我方是采购方，帮我审这份采购合同，重点看付款节点、验收标准和违约责任是否对等。」 |
| **服务合同审查** | 「我方是服务提供方，审一下这份合同的知识产权归属、保密条款和责任上限，避免背无限责任。」 |
| **劳动合同核验** | 「我方是用人单位，帮我核验这份劳动合同的解除条款、竞业限制和违约金是否触碰劳动法强制性规定。」 |

## 使用前配置（全自动装配）

🔑 **获取调用密钥**：在 [cuecue.cn](https://cuecue.cn/hub/api-key) 免费注册获取 API key（新注用户赠送 500 积分）。

*(获取密钥后，直接将其发送给当前的 AI 助手，并对它说：“**这是我的 key，请帮我配好环境。**” 助手会自动为你拉取底层脚本、写入配置文件。)*

## 标准工作流 (SOP)

1. **上传合同 + 说明立场**：提供合同文件（Word/PDF），并说明「我方是哪一方」——甲方还是乙方、供货方还是采购方。立场决定风险判断方向。
2. **交互澄清**：若关键信息缺失（如立场未说明、合同类型不明），AI 会主动追问。
3. **获取审查报告**：等待 3-15 分钟，输出带风险分级、法条/案号出处和修改建议的排查表。

> 🛡️ **客户隐私保护声明**：系统默认开启高密级保护，服务端解析后不留存任何源文件或结果缓存。

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

## 能力边界

- ✅ **胜任**：条款逐条风险识别、效力瑕疵核验、违约金/利率法定边界核算、遗漏条款增补。
- ❌ **无法替代**：最终法律意见签发、合同签署与担责、证据真实性实质审查。
- ⚠️ **使用规范**：AI 产出基于公开法规、司法案例与工商司法公开记录交叉比对，**不构成正式法律意见**；签署前请由执业律师做最终人工审查。

---

<details>
<summary>⚙️ Agent 执行摘要（AI 执行，默认收起）</summary>

本节供 Agent（Workbuddy/Claude Code/Claude Desktop）执行使用，不对普通用户展示。搭子模板由服务端动态维护，template_id 以运行时 live 为准。

**【一】执行前置与环境准备：**

用户提供 API key 后，Agent 需自行完成运行环境准备。

1. **检查与写入 API Key**：如果 `~/.cue/config.json` 不存在，使用用户的 key 自动生成并写入。
2. **确认 Runner 就绪**：若无 runner 脚本，自动克隆开源仓：
   ```bash
   if [ -d ~/.cue/cue-skills/.git ]; then
     git -C ~/.cue/cue-skills pull --ff-only
   else
     git clone https://github.com/sensedeal/cue-skills ~/.cue/cue-skills \
       || git clone https://gitee.com/sensedeal/cue-skills ~/.cue/cue-skills
   fi
   ```

**【二】文件处理与上传（核心）：**

合同审查以**上传合同文件**为前提。用户提供本地合同（docx/pdf/txt/md 等），**不要尝试自己在本地读取文本**，直接使用 runner 原生 `--material <文件路径>` 参数把文件传给平台处理。

- 若用户只粘贴了合同**文本**（无文件），则把合同正文放进 `--query`，并明确标注「以下是合同原文」。
- 必填的第二项是**己方立场**（甲方/乙方、供货方/采购方等），写进 `--query`；用户未说明时先追问。

**【三】预期管理与防焦虑（必须执行）：**

执行前必须向用户发送提示：「🚀 正在启动合同审查，需核验现行法规与司法案例，大约需要 3 到 15 分钟。我会后台为您执行，完成后立即向您汇报。」

**【四】容错与错误提示：**

- **超时与重试**：报连接失败时，自动重试最多 2 次（间隔 10s → 30s 递增）。
- **凭据错误**：提示「积分不足或 key 失效，请检查」，不要重试。
- **结果为空**：末行 `RESULT empty` 时改用自由式兜底或请用户补充背景。
- **禁止静默吞错**：明确向用户转述具体的报错环节。

### 积分不足专项提示（必须执行）

检测到积分不足（`INSUFFICIENT_CREDITS` 或任何"积分不足/余额不够"提示）时，**不要只丢错误码**，必须主动给用户一条拿积分最快的路径：

> 你的 Cue 积分不足，本次任务未能启动。两个办法：
> 1. **邀请好友得 500 积分（推荐）**：打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」，分享给好友——好友加入后你再得 **500 积分**。
> 2. **直接充值**：前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅（首次充值有优惠）；或等次日免费额度。

规则：
- 提示要**主动、简短、可点**——把「首页」和「左下角」两个关键动作说清楚，不要让用户自己找入口。
- 积分不足**不要重试**（`retryable: false`），也不要换 query 绕。
- 用户回复已充值/已邀请后，用**完全相同的命令**重跑。

**【五】搭子路由（提取 template_id）：**

| 适用场景 | template_id |
| :--- | :--- |
| 合同风控与合规审查（唯一搭子） | template_BFSwVa |

**【六】最终执行命令格式：**

场景 A：上传合同文件（标准用法）
```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "我方是<甲方/乙方>，<可选:重点审查某类条款>，请审查这份合同并输出风险排查表" \
  --material "<本地合同文件绝对路径>" \
  --template-id template_BFSwVa \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-contract-review.md
```

场景 B：用户仅粘贴合同文本（无文件）
```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "我方是<甲方/乙方>，以下是合同原文：\n<合同全文>\n请审查并输出风险排查表" \
  --template-id template_BFSwVa \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-contract-review.md
```

执行后读末行 `RESULT ok`，原样交付报告并提供本地 md 文件路径；末行 `RESULT empty` 时走容错。

</details>

## FAQ

**Q: 报告能在网页端看原文吗？**
A: 能。交付时会同时附上 Cue 原始报告链接 `https://cuecue.cn/share/<conv_id>`，可回网页端查看完整原文、继续追问或转发同事。

**Q: 提示积分不足怎么办？**
A: 打开 [cuecue.cn](https://cuecue.cn/)，点击页面左下角「获取专属邀请链接」，好友加入后你再得 500 积分；也可前往 [cuecue.cn/pay](https://cuecue.cn/pay) 充值（首次有优惠），或等次日免费额度。积分不足不要重试。
