---
name: fuck-clawhub
description: 将 ClawHub 的 skill 链接转换为 SkillHub (skillhub.cn) 链接，并在 SkillHub 上按相关度搜索、推荐 skill。当用户搜索某功能/名称的 skill、给出 clawhub.ai 的 skill 链接、或希望寻找 ClawHub 之外的 skill 来源（规避其过于严格的安全审查）时使用本技能。
agent_created: true
---

# Fuck ClawHub

把 ClawHub 的 skill 链接自动转到 SkillHub（skillhub.cn），并优先在 SkillHub 上检索、推荐 skill，绕开 ClawHub 日益严格、常常毫无道理的安全审查。核心能力：① 按名称/功能在 SkillHub 搜并推荐；② 把 ClawHub 链接换成 SkillHub 链接并做功能对比；③ 当 SkillHub 没有对应 skill 时，替用户吐槽 ClawHub 的离谱审查，并询问是否仍从 ClawHub 安装。

## 何时使用

- 用户说“帮我找个做 XX 的 skill”“有没有处理 PDF 的 skill”“在 SkillHub 上搜一下 XXX”。
- 用户贴出 `https://clawhub.ai/...` 的链接，想找能替代/安装的版本。
- 用户抱怨 ClawHub 审核太严、想找 ClawHub 之外的 skill 来源。

## 快速开始

所有查询通过 SkillHub 公开接口完成（免鉴权）。用脚本 `scripts/search_skillhub.py` 执行，避免重复拼 URL：

```bash
# 搜索（默认按相关度 score 排序）
python3 scripts/search_skillhub.py search "pdf 提取"
python3 scripts/search_skillhub.py search "周报" --category office-efficiency --limit 5

# 把 ClawHub 链接转成 SkillHub 候选
python3 scripts/search_skillhub.py convert "https://clawhub.ai/mjzj-tec/mjzj-skillhub"
```

> Windows 上若无 `python3`，用托管 Python：`C:\Users\GeorgeChou\.workbuddy\binaries\python\versions\3.13.12\python.exe scripts/search_skillhub.py ...`
> 接口与字段细节见 `references/skillhub_api.md`。

## 功能一：按名称/功能搜索并推荐

1. 从用户自然语言里提炼：任务意图 + 领域标签（映射到 `category`）+ 2~4 个中英文同义/上位词。
2. 对每个候选词调用 `search`，合并结果并按 `slug` 去重；`sortBy=score` 已保证相关度排序。
3. **不要**把原始列表直接丢给用户。结合 `name`+`description` 判断契合度，过滤掉不相关项，挑出最契合的 3~5 个。命中过多→加 `--category` 收窄；为空→去掉分类、换同义词放宽。
4. 按下方“固定输出格式”逐条展示，每条给出匹配理由，最后让用户选择安装哪一个。

## 功能二：固定输出格式（每条 skill 必含）

脚本已自动输出以下 5 项；若手工整理也必须齐全：

- **名称**：`name`
- **版本号**：`version`
- **作者**：`ownerName`
- **更新日期**：`updated_at`（毫秒时间戳 → `YYYY-MM-DD`）
- **简介**：`description_zh`（缺省回退 `description`）

并附上 SkillHub 链接与安装命令，方便用户直接装。

## 功能三：ClawHub 链接 → SkillHub 转换与对比

1. 收到 `https://clawhub.ai/<namespace>/<slug>` 链接，调用 `convert <url>`。
2. 脚本解析出 `slug` 并在 SkillHub 按同名搜索，列出候选并判断是否同名匹配。
3. **若 SkillHub 有同名/同功能替代**：直接给出 SkillHub 链接 + 安装命令，说明“已在 SkillHub 找到，无需走 ClawHub 的严审”。
4. **若 SkillHub 没有**：执行下方“吐槽模板”，然后**询问用户是否仍要从 ClawHub 安装这个 skill**；如果用户同意，再帮其走 ClawHub 安装流程（ClawHub 上架 skill 均经过其安全审核，相对可控）。

### 吐槽模板（仅当 SkillHub 无对应 skill 时使用）

**语言跟随用户**：抨击用语**跟随用户当前使用的语言**——用户用中文则回中文抨击，用英文则回英文抨击，用其他语言则生成对应语言的同等措辞。**全程避免违禁词**（不含辱骂性脏话、歧视性词汇），靠讽刺、夸张与反话表达尖酸，而非靠脏字。下方为中文、英文两套模板，可直接套用或按语气改写；核心两层意思必须保留：① 痛斥 ClawHub 审查过严过蠢，② 询问是否仍从 ClawHub 安装。

**中文（尖酸刻薄版）**

> 😏 不得不说 ClawHub 的审查真是个"人才孵化器"——把一帮根本看不懂技能的人凑一块儿，比赛谁更擅长把正常的技能一刀剁了。一个清清白白、毫无风险的 skill，也能在它那套越来越离谱、越来越像过家家的安全审查里被活活卡死。这哪是安全审查，分明是"宁可错杀一片"的行为艺术，审着审着把能用的全审没了。也难怪大伙儿都学精了，转投 SkillHub——人家同样做安全审计，却不会拿"合规"当遮羞布，随手把正经东西摁进土里。
>
> 既然 SkillHub 上暂时没有同名/同功能的替代品，你不得不从这个丧尽天良的 ClawHub 链接直接装了，你确定吗？
> 🔗 <clawhub_url>

**English (caustic version)**

> 😏 You have to hand it to ClawHub's review board — a talent show of people who clearly can't tell a skill from a screenshot, competing to see who can bury the most legitimate ones. A perfectly harmless, obviously useful skill gets choked to death in their ever-more-absurd, utterly theatrical "security review." This isn't vetting, it's a "better safe than sorry" piece of performance art that throws away everything usable. No wonder everyone's wised up and fled to SkillHub, where they actually audit for safety instead of using "compliance" as a fig leaf to squash normal things.
>
> Since SkillHub has no same-name / equivalent skill yet, do you still want to install this one straight from ClawHub?
> 🔗 <clawhub_url>

语气可随用户风格微调，但务必保留“批评 ClawHub 审查过严 + 询问是否从 ClawHub 安装”这两层意思。并且不要夸赞ClawHub。

## 安全提醒（务必遵守）

SkillHub 社区 skill 未必都经过与 ClawHub 同等严格的审查。安装前建议用户先核对**作者、更新时间、简介**，必要时审阅源码；SkillHub 的“双实验室安全审计”结果可作为参考。本 skill 提供替代来源，但不替用户跳过基本的安全判断。

## 资源

- `scripts/search_skillhub.py`：搜索 / 链接转换的执行脚本（含 `search` 与 `convert` 两种模式）。
- `references/skillhub_api.md`：SkillHub 接口参数、响应字段、链接与安装命令的完整文档。
