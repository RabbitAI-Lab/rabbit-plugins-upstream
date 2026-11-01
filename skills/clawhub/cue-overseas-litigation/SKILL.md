---
name: cue-overseas-litigation
slug: cue-overseas-litigation
displayName: 境外诉讼案例库
version: 1.3.2
description: >
  境外诉讼案例库 — 围绕一个主题检索主要法域的公开判例与监管公告，归纳诉因、判决倾向与对中国主体的合规启示。
  Triggers: 境外诉讼、海外官司、跨境诉讼、海外判例、境外监管公告、国际诉讼案例、制裁案例、出口管制案例、涉外法律检索、overseas litigation、cross-border litigation
license: MIT
metadata:
  source: cuecue.cn/playbook
  scene: "涉外法律"
  buddy: "境外诉讼案例库"
---

# 境外诉讼案例库

> 围绕任意主题检索美国、欧盟、新加坡等主要法域的公开判例与监管公告，归纳诉因、判决倾向与对中国出海主体的合规启示。多源交叉验证，结论带来源链接。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 健康检查：Key / 服务 / 搭子三样全过再跑 | 禁止跳过 |
| 2 | 告知用户耗时 3-15 分钟 | 禁止中途取消 |
| 3 | 确认 credits，一条命令阻塞等待 | 禁止连发多条 |
| 4 | stdout `[cue-research] RESULT ok` = 完成 | 无 RESULT = 未完成 |
| 5 | 原样交付报告 + 告知落盘路径 | 禁止自行概括 |
| 6 | 交付时**同时附带 Cue 原始报告链接** | 禁止编造链接 |
| 7 | 遇 `INSUFFICIENT_CREDITS` 主动提示邀请链接 | 禁止只丢错误码 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 出海合规自查 | 企业在目标法域是否有类似诉讼先例、常见诉因 |
| 行业诉讼风险扫描 | 某行业（光伏/新能源/AI/电商）在海外被诉的典型案例 |
| 制裁与管制监控 | OFAC、BIS 实体清单、欧盟制裁名单的最新动态 |
| 跨境投资尽调 | 目标公司或实控人在海外是否有诉讼/处罚记录 |
| 专利/知产纠纷 | 特定技术领域的海外专利诉讼趋势 |

## 核心能力

1. **多法域判例检索** — 美国联邦法院（PACER）、欧盟法院（CURIA）、新加坡最高法院
2. **监管公告监控** — OFAC 制裁名单、BIS 实体清单、欧盟制裁、ITC 337 调查
3. **诉因归类与判决倾向** — 胜诉/败诉/和解趋势、罚金金额（公开数据）
4. **合规启示归纳** — 对中国出海主体的影响评估
5. **逐条可溯源** — 每个结论附原始出处链接

## 试试这样问

- "查一下新能源行业在美国的专利诉讼案例"
- "检索 TikTok 在海外的监管处罚案例"
- "看看中国光伏企业在欧盟的反倾销判例"
- "比亚迪在海外有没有被起诉过"
- "跨境电商最近在美国的集体诉讼有哪些"
- "最近中国 AI 企业被列入 BIS 实体清单的情况"

## 输出形式

结构化报告：相关案例列表 → 诉因归纳 → 判决倾向 → 罚金/赔偿 → 合规启示 → 来源链接。中文报告，关键判例名/法条保留原文。

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

## 数据覆盖

美国联邦法院（PACER）、欧盟法院（CURIA）、新加坡最高法院、OFAC SDN List、BIS Entity List、欧盟制裁名单、ITC 337 调查、各法域证券监管公告、ICSID 国际仲裁。以公开数据为限。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

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

Cue API Key：在 [cuecue.cn](https://cuecue.cn/api-key?src=clawhub-overseas-litigation) 注册后免费创建，新账号送 500 积分 + 每天 10 积分。点击「创建 API Key」，生成 API Key 后一定要点击「复制」并粘贴发送给您正在使用的智能体。写入 `~/.cue/config.json`：

```bash
mkdir -p ~/.cue
echo '{"api_key": "sk你的key"}' > ~/.cue/config.json
```

单次研究消耗约 3-8 credits。

> **API Key 只能由用户本人创建**：Agent 既不能代生成、也无权查看用户的 Key。检测到未配置或失效时，按以下话术告知用户：**「点击『创建 API Key』，生成 API Key 后一定要点击『复制』并粘贴发送给我。」** 然后等待用户提供，**禁止声称"我去生成/查看"**。

---

## 调用说明

Agent 会自动匹配「涉外法律」场景下的「境外诉讼案例库」搭子。固定写法：

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "<用户问题原话>" \
  --template-id <运行时的搭子 template_id> \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-overseas-litigation.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 用户原话，不要改写 |
| `--template-id` | 从 `/api/playbook` 拉取当前可用的搭子 ID |
| `--output` | 落盘路径，格式 `~/cue-reports/日期-overseas-litigation.md` |

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

本 Skill **不在本地执行检索**。流程是 Agent → Cue 服务端 → 外部数据源：

```
你的 Agent ──→ Cue API（cuecue.cn）──→ PACER / CURIA / OFAC 等
```

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 用户本人 | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/api-key?src=clawhub-overseas-litigation) 生成后点「复制」并粘贴发送给您正在使用的智能体，再由 Agent 写入 ~/.cue/config.json（Agent 不能代生成，也无权查看） |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',[]);buddy=[b for s in scenes if s.get('secondary_category')=='涉外法律' for b in s.get('buddies',[])];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | **由用户本人**前往 [cuecue.cn/hub/api-key](https://cuecue.cn/api-key?src=clawhub-overseas-litigation) 生成后点「复制」并粘贴发送给您正在使用的智能体（Agent 无法代生成，也无权查看） |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

### 配置成功后引导用户跑第一个任务（必须执行）

健康检查三项全绿 = 环境就绪，但**这是配置流程的终点，不是任务的终点**。三项全绿后若用户还没给出具体任务，**必须主动把用户推向第一次真实调用**，不要停在"环境已就绪"：

> 环境已就绪 ✅ 下面这些都可以直接跑，比如：
> 1. "查一下新能源行业在美国的专利诉讼案例"
> 2. "检索 TikTok 在海外的监管处罚案例"
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
| `RESULT empty` | 公开源无匹配 | 缩小范围（法域/时段），换关键词 |
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
└─ 结果空 → 缩窄关键词 → 单法域 → 确认该主题有公开判例
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
| [PACER](https://pacer.uscourts.gov) | 美国联邦法院 | 按页，<$30/季免费 |
| [Google Scholar](https://scholar.google.com) | 美国联邦+州法院 | 免费 |
| [CURIA](https://curia.europa.eu) | 欧盟法院 | 免费 |
| [OFAC SDN](https://sanctionssearch.ofac.treas.gov) | 美国制裁名单 | 免费 |
| [BIS Entity List](https://www.bis.gov/entity-list) | 出口管制实体清单 | 免费 |
| [ICSID](https://icsid.worldbank.org/cases) | 国际投资仲裁 | 免费 |

---

## FAQ

**Q: 和 Cue 网页端有什么区别？**
A: 在 Claude Code 里直接用自然语言触发，Agent 自动匹配搭子、确认、取报告，不用切网页。

**Q: 能查国内诉讼吗？**
A: 不能。本 Skill 专注境外法域，国内诉讼有另外的搭子。

**Q: 报告语言？**
A: 中文报告，判例名/法条保留原文附摘要。

**Q: 积分不够？**
A: 打开 [https://cuecue.cn/](https://cuecue.cn/)，点击页面**左下角**「获取专属邀请链接」，好友加入后再得 500 积分；也可前往 [cuecue.cn/pay](https://cuecue.cn/pay) 订阅（首次订阅有优惠），或等次日免费额度。每天登录还送 10 积分，单次约 3-8 积分。

**Q: 查不到怎么办？**
A: 先跑健康检查。三个环节任一断了都会失败——见上方「自救指引」。

**Q: 结果可靠吗？**
A: 结论带来源链接可回查。注意：覆盖以联邦法院/欧盟/主要监管公告为主；州法院、仲裁非公开裁决、非英语法域覆盖不全；不构成法律意见。

---

> 本 Skill 基于 Cue 平台（cuecue.cn）「境外诉讼案例库」搭子。搭子模板由服务端动态维护。Skill 本身 MIT 开源。

---

## 参考

- Cue 平台：https://cuecue.cn
- Playbook 页面：https://cuecue.cn/playbook
- API Key 管理：https://cuecue.cn/api-key?src=clawhub-overseas-litigation
