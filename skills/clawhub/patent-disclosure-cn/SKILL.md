---
name: patent-disclosure-cn
description: 技术交底书生成。当用户要写技术交底书、专利交底、把研发材料或技术方案整理成交底书、挖专利点、只有一个想法想看看能往哪几个方向申请，或说「帮我写个交底书」「这个能写成专利吗」时使用。无需 API Key，首次使用自动领取免费试用。Use when the user wants to turn R&D materials or an idea into a patent technical disclosure document (Word). Works without an API key: a free trial is claimed automatically on first use.
version: "1.0.0"
author: PatentMax
user-invocable: true
argument-hint: "[材料文件路径 / 技术方案描述 / 一个想法]"
allowed-tools: Bash, Read, Write, Glob
---

# 技术交底书 · PatentMax

把研发材料、技术方案，甚至只是一个想法，写成一份**可以直接交给代理人的技术交底书 Word**。附图自动画，发明点逐条和全球专利库比对，正文干净；系统推导和待补充的地方在核对说明里逐条列出，方便核对。

数据来自 PatentMax 专利库。

接口与控制台：**https://api.ip930.com**

**不需要 API Key 就能用。** 没设 `PATENTMAX_API_KEY` 时，脚本第一次运行会自动领取一份免费试用（累计 ¥40 额度、30 天有效，只开通本技能的功能），存在本机 `~/.patentmax/`，之后自动沿用。领取成功时 stderr 会打一行「[PatentMax] 已自动领取免费试用……」，**把这句话转告用户**。

试用用完、过期，或想用其他功能时，命令会返回带 `"free_trial": true` 的错误，`message` 里写着下一步怎么办（注册 PatentMax 再送 ¥50 体验额度），**原样转告用户，不要自己换写法重试**。用户设了 `PATENTMAX_API_KEY` 就一律用正式密钥，不会领试用。

## 核心原则

**材料越全，交底书越好。** 服务端是无人值守生成的，材料里缺的信息会按通行做法自动补，补得越多，要人确认的条目就越多。**先把用户手上的材料读全，再提交。**

**这是付费任务，执行前必须取得用户确认。** 命令必须显式加 `--yes`。

**只有一个模糊想法时，先出方向，别直接写。** 用 `ideas` 子命令出几个可申请的方向，用户挑一个再写，比拿一句话硬写有用得多。

**不重复提交。** 生成要几分钟到十几分钟，等得久不代表失败。重复提交就是重复扣费。

## 什么时候用

| 用户说 | 怎么做 |
| --- | --- |
| 「帮我写个技术交底书」「把这些材料整理成交底书」 | ✅ 读材料 → `create` |
| 「这个项目有什么能申请专利的」 | ✅ 读项目文档 → `create` |
| 「我有个想法，能不能申请专利」（只有一两句） | ✅ 先 `ideas` 出方向，挑一个再 `create` |
| 「交底书写好了，帮我看看有没有人做过」 | ❌ 那是查新，用专利查新 |
| 「查一下这个方向有哪些专利」 | ❌ 用全球专利检索 |

## 先读材料

**这一步决定交底书的质量。** 用户给了项目目录或文件，先自己读一遍，挑出和技术方案有关的：

- **优先读**：设计文档、技术方案、研发报告、实验记录、需求说明、README
- **代码**：不要整份塞进去。读懂之后，用文字写出**处理流程、关键判断条件、模块划分**
- **图片、图纸**：脚本读不到图。把图上的结构、连接关系、流程用文字写进 `--supplement`

`.md` / `.txt` / `.docx` 可以直接用 `--file` 交给脚本（可多次）；PDF、PPT 需要你读完后把要点写进 `--supplement`。

提交前用 `preview` 看一眼拼好的材料有多少字（**不花钱**）：

| 字数 | 情况 |
| --- | --- |
| 800 字以上 | 充分，直接提交 |
| 200–800 字 | 偏薄，能写，但推断的地方多。**先问用户两三个问题补上** |
| 200 字以下 | 脚本会拦下来。先用 `ideas` 出方向 |

材料最少要讲清三件事：**解决什么问题、具体怎么做（结构 / 步骤 / 参数）、达到什么效果**。详见 `references/materials-guide.md`。

## 命令

```bash
# 材料齐的：直接出交底书
python scripts/patentmax_disclosure.py create \
  --file ./设计方案.docx --file ./实验记录.md \
  --supplement "补充：阀门转轴上装角度和扭矩传感器……" \
  --title "阀门卡滞诊断与清理装置" \
  --wait --yes

# 只有一个想法：先出方向（默认 3 个，最多 5 个）
python scripts/patentmax_disclosure.py ideas \
  --idea "冬天水渠闸门老被冰卡住，想做个能自己判断卡滞并清理的装置" \
  --count 3 --wait --yes

# 用户挑中第 2 个方向，接着写交底书
python scripts/patentmax_disclosure.py create \
  --from-ideas <上一步的 report_id> --direction 2 --wait --yes

# 不花钱：预览拼好的材料
python scripts/patentmax_disclosure.py preview --file ./设计方案.docx

# 下载：交底书正文 + 核对说明
python scripts/patentmax_disclosure.py download --report-id <report_id> --out 技术交底书.docx
python scripts/patentmax_disclosure.py download --report-id <report_id> --kind notes --out 核对说明.docx

# 中途断了继续查 / 不跑了
python scripts/patentmax_disclosure.py status --operation-id <operation_id>
python scripts/patentmax_disclosure.py cancel --operation-id <operation_id>
```

`--idempotency-key` 不填会按材料内容自动生成，**同样的材料重试不会重复扣费**。

## 等待期间

提交后先告诉用户：**「交底书已开始生成，一般 5 到 15 分钟，排队时会更久。」**

`--wait` 会一直轮询到出结果，间隔从 10 秒逐步放宽到 60 秒，默认最多等 90 分钟。

**等得久不代表失败。** 只要状态不是 `failed`，任务就还在服务端跑，**绝对不要重新提交**。`--wait` 超时了就用 `status --operation-id` 接着查。

## 交付

跑完先把两份 Word 都下载下来，然后告诉用户：

**1. 交底书正文**（`技术交底书.docx`）：干净的正文，可以直接交给代理人。包括发明名称、背景技术、技术方案、优点、实施方式及附图、权利要求结构预览、说明书摘要、附图标号表。

**2. 核对说明**（`核对说明.docx`）：系统推导的内容、待补充信息、附图绘图说明、发明点对照、替代方案。**正文里需要确认的推导和待补充都汇总在这里。**

结果 JSON 里有几个字段要主动讲：

| 字段 | 怎么讲 |
| --- | --- |
| `pending_count` | 大于 0 时：「有 N 处是系统按通行做法推断的，请在核对说明里逐条确认」 |
| `missing_sections` | 缺哪几节，需要发明人补什么事实 |
| `figures` | `auto: true` 的是已经画好的附图；`false` 的只给了绘图说明，需要另外画 |
| `novelty.rows` | 每个发明点在专利库里有没有撞上，`hits` 里是撞上的公开号 |
| `conflicts` | 多份材料对同一参数写法不一致，要用户定一个 |

**`novelty` 是发明点比对，不是正式查新。** 要一个能不能申请的结论，用专利查新。

最后一句固定是：

> 在 https://api.ip930.com 控制台可以查看所有任务和余额。

## 创新升级的结果

`ideas` 跑完返回一组方向，每个方向有标题、概述、核心方案、创新点，以及新颖性、可行性、差异化和综合评分。

**把方向列给用户挑，不要替他选。** 每个方向用一两句话讲清楚它和原始想法的区别，附上综合分。用户挑定后再用 `--from-ideas` 写交底书。

`existing_tech_description` 写的是「未检索到」时照实说，不要包装成「很新颖」。

## 它不做什么

**不出具专利申请文件。** 交底书是给代理人的技术说明，正式的权利要求书和说明书需要专利代理师撰写并递交。

**不保证能授权。** 发明点比对只能说明在专利库里撞没撞上，不能代替审查。

**不做外观设计。** 适合发明和实用新型这类技术方案。

**材料会发送到服务端生成。** 涉及还没申请的核心参数时，提醒用户一句。

## 相关能力

同一把正式密钥、同一个余额（免费试用只开通本技能，其他功能要注册后用正式密钥）：

- **全球专利检索**：写之前先摸摸这个方向有哪些专利
- **专利查新**：交底书写完，判断能不能申请
- **企业情报分析 / 技术路线分析**：方向都还没定时先看这两个

典型顺序：**检索摸底 → 写交底书 → 查新确认 → 交给代理人**。

## 参考

- `references/materials-guide.md`：材料怎么准备，不同领域要写到什么程度
- `references/workflow.md`：完整流程：从一个想法到交底书，结果怎么读
- `references/faq.md`：排查：报错、任务卡住、推断条目太多怎么办
