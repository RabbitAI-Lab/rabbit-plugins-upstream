---
name: skill-improver
display_name: Skill Improver
display_name_en: Skill Improver
description_zh: 当用户要求「改善我的技能包」「把评测整改项落地」「为什么我的技能被扣分、怎么修好」时使用。它把评测报告里的整改清单变成实际执行的改动，并在一处硬边界前停手：凡是靠伪造能力换分数的操作，一律不做。
description_en: Use when the user wants to act on a skill review — "fix my skill package", "apply the review findings", "why was my skill rejected and how do I fix it". It turns a review's remediation list into executed changes, and stops at one hard boundary: anything that would fake capability to raise a score is refused.
description: Use when the user wants to act on a skill review — "fix my skill package", "apply the review findings", "why was my skill rejected". It turns a remediation list into executed changes and refuses anything that would fake capability to raise a score. 当用户要求把评测整改项落地、修好被扣分的技能包时使用。The tool is faithful: it never fabricates tests, demos, or behavior claims.
category: developer-tools
version: 1.0.0
author: Zhao Xinghua
license: MIT
tags: skill-improvement, review-remediation, package-quality, ai-skills
---

# Skill Improver

诊断之后没人改，是技能生态里最常见的断点。这个包补的是那一环：**读一份评测报告，把能修的真修掉，修不动的明说到底。**

## 三条命令

```bash
# 1. 只诊断，不动任何文件（tools: scan）
python scripts/improve.py scan path/to/skill

# 2. 真改，改完自动复测（tools: apply）
python scripts/improve.py apply path/to/skill

# 3. 连带修文档漂移（改动既有内容，需显式开启）
python scripts/improve.py apply path/to/skill --fix-doc-drift

# 4. 指定评测器与同系列兄弟
python scripts/improve.py apply path/to/skill --reviewer path/to/review.py --siblings a,b
```

评测器默认按同系列约定去找兄弟包里的 `lgd-skill-review/scripts/review.py`；路径不同就用 `--reviewer` 指定。

## 一条硬边界

| 类型 | 处理 | 理由 |
|---|---|---|
| 元信息缺失（LICENSE、ai-index、tags、Triggers、互链） | 自动补 | 这些本来就该有，补上不改变能力 |
| 文档声明了没实现的参数 | 需 `--fix-doc-drift`，且保留说明行 | 改动既有内容，必须显式授权 |
| 无测试、无执行器、无 demo | **拒绝** | 自动生成空 runner 让它拿分，是教人作弊 |
| 无安全边界声明 | **拒绝** | 声明行为属于事实陈述，不能替作者编 |

判断标准只有一句：**改动之后，这个包真的变好了，还是只是分数变高了？**

后一种一律不做。

## 判定流程

按顺序问四句，任一步答案为否就停：

1. **这是可解析的技能包吗？** 有 `SKILL.md` 且 frontmatter 能读出 name——否则直接退出，不猜。
2. **这一项属于元信息缺失吗？** 是则进自动修复；不是则进第 3 步。
3. **补齐它会让包真的变好吗？** 否——只让分数变高——则拒绝，并入拒绝清单。
4. **改动会触及既有内容吗？** 是则需显式开关（`--fix-doc-drift`），否则直接做。

判定表：

| 情形 | 动作 |
|---|---|
| 若缺 LICENSE / ai-index / tags / Triggers / 互链 | 补 |
| 若声明了未实现的参数 | 仅 `--fix-doc-drift`，且留不含参数名的说明行 |
| 若无测试用例 / 无执行器 / 无 demo | 拒绝，逐条列明 |
| 若未声明安全边界 | 拒绝（代为声明行为等于代为保证） |

**不编造**：本工具从不凭空生成测试、demo 或行为声明。所有自动产出都标注来源，可追溯到具体字段。

**口径公开**：本工具的"分数"只有一个来源——同系列评测器 `lgd-skill-review` 的结构制（六维 100 分）。本工具不自造评分，只消费它的整改清单，改完再用同一把尺子复测。所以任何分数变化都可以由第三方用同一个评测器复现。

## 什么时候不用（Not for）

- 从零写一个新技能包 —— 这是造，不是改；用 skill-forge 那类工具
- 只想要一个分数、不打算改 —— 直接用 `lgd-skill-review`
- 包本身结构崩坏（没有 SKILL.md）—— 先修结构，本工具依赖可解析的 frontmatter
- 想通过改分数通过审核 —— 本工具的设计目标正相反

## 硬规则

1. **NEVER 复用旧快照写文件。** 每个写操作前必须重读——因为串联修复器共享一次读入的内容时，后一个会把前一个的成果覆盖回旧值，实测分数从 54 反降到 50。
2. **MUST 复测之后再报告。** 因为"我改完了"和"分数真的变了"是两件事，只有复测能区分。
3. **NEVER 生成空测试或空 demo 充数。** 因为那会让评测器变成自欺工具，也会让后来者以为这个包验过。
4. **MUST 拒绝项逐条列出并给原因。** 因为只说"有 3 项没修"等于没说，使用者会以为工具漏了。
5. **NEVER 静默删除既有内容。** 因为原声明可能是作者的规划，删了等于替人做决定；改文档必须留说明行。
6. **MUST 自动产物标注来源。** 因为 `ai-index.json` 的 intents 是机器推的，不标注待校订就会被人当成人工确认过的。
7. **MUST 判定变化说清。** 因为 BLOCK→WARN 和 46→67 是两件事，前者才是真正解除风险。
8. **NEVER 猜评测器路径。** 找不到就报错退出——因为不同机器目录布局不同，猜错会静默跑错包。
9. **NEVER 反复轮询评测。** 因为评测要执行测试，反复跑既浪费也可能触发限流；一次跑完再决定。
10. **NEVER 把本工具当作提分器。** 因为它的价值恰恰在于敢拒绝：能修的修完，剩下的才暴露真问题。
11. **不得 修改包外文件。** 因为作用域一旦越界，工具就从"助手"变成"风险"。
12. **不得 假设 frontmatter 可解析成功。** 读不出 name 就退出——因为对破损包做猜测性修补，会把问题藏得更深。
13. **NEVER 在 scan 模式下写文件。** 因为只读诊断是他人敢于先跑一遍的前提；一旦 scan 也写，就没人敢拿它试。

## 一次真实运行的输出

```text
$ python scripts/improve.py apply ./my-skill --siblings lgd-skill-review
基线：结构制 46/100 BLOCK
执行改造：
  ✓ 写入 LICENSE（MIT，作者取自 frontmatter 的 author）
  ✓ 补 tags（my-skill, review, remediation）
  ✓ 追加 Triggers 段（5 条，取自 description）
复测：结构制 46/100 BLOCK  →  67/100 WARN   (+21)
仍必须人工的 4 项未动——自动改造只补元信息，不伪造能力。
```

## Triggers

- 把评测整改项落地
- 修复技能包被扣分的项
- 为什么我的技能被拒 / 被判 BLOCK
- 技能包体检后怎么改
- apply review findings to my skill

## Related skills

本技能属于**同系列技能**，与下列包构成闭环：

- `lgd-skill-review` — 同系列技能，负责诊断与打分；本包消费它的整改清单
- `summarize-pro` — 同系列技能，会议纪要与摘要
- `debug-pro` — 同系列技能，排障与复现

完整闭环：诊断（lgd-skill-review）→ 改造（本包）→ 复测（回到 lgd-skill-review）。

## 安全边界

- 只读写用户指定的包目录，不触碰包外文件（除了评测器脚本的只读调用）。
- 不联网、不执行被改包里的任何脚本；`--run` 只在与评测器约定时下放，由评测器负责。
- 不加 `--apply` 时不写任何文件，纯只读诊断。
- **失败时的处理**：读不到 `SKILL.md`、找不到评测器、评测器报错——一律打印明确的错误信息并以非 0 退出，不静默继续、不猜测。因为静默失败会让人以为改成功了。
- 遇到无法解析的 frontmatter 直接退出，不做猜测性修补。

细节见 `references/fixers.md`（每个修复器的判定条件与产出）与 `references/limits.md`（拒绝清单与理由）。
