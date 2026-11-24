---
name: evidence-anchor
display_name: 证据挂锚
display_name_en: Evidence Anchor
description: Use when a report, review or audit makes conclusions and you must prove each one points at something real — "check my citations", "does this line number still exist", "verify every claim in this doc". It resolves `file:line` anchors against the tree and refuses to treat an unresolvable anchor as evidence.
description_zh: 当用户要求核对报告里的结论有没有落到真实位置（文件是否存在、行号是否越界）时使用。它逐个解析 `文件:行号` 锚点，解析不了的一律不算证据。
description_en: Use when a report, review or audit makes conclusions and you must prove each one points at something real — "check my citations", "does this line number still exist", "verify every claim in this doc". It resolves `file:line` anchors against the tree.
category: developer-tools
version: 1.0.0
license: MIT
author: Zhao Xinghua
tags:
  - evidence
  - citation-check
  - audit
  - anchor
---

# 证据挂锚

一条结论写成"这里有问题"，没人能核对；写成 `scripts/review.py:157`，任何人都能打开核对。差别不在措辞，在于**能不能被第三方验证**。

本技能做一件事：把报告里每一个 `文件:行号` 锚点，逐个回到真实文件里点一遍。

## 一条硬边界

| 类型 | 处理 | 理由 |
|---|---|---|
| 锚点能否解析（文件在不在、行号越不越界） | 逐条判定 | 这是事实，可机检 |
| 锚点指向的行是否"说得对" | **不做** | 判断内容对错需要读上下文，机器判定会制造假证据 |
| 无锚点的结论 | 只列出，不代写锚点 | 锚点是作者的断言，替写等于替它担保 |

判断标准只有一句：**这个锚点，别人打开文件能不能看到同一行？**

本工具是 faithful 的：它不编造锚点、不替作者补引用、不把"看起来像"当成"核对过"。

细节分层在 references 里，正文只留判定：

- 判定细则与退出码：`references/rules.md`
- 为什么有三件事坚决不做：`references/limits.md`
- 三种用法与真实输出：`references/usage.md`
- 9 条自检覆盖表：`references/selfcheck.md`
- 端到端演示：`demo/run_demo.py`（造一棵最小树 + 三类锚点，跑一遍看判定）

## 判定流程

按顺序问四句，任一步答案为否就停在该步：

1. **根目录是不是一棵真实目录树？** 不是就退出，不猜。
2. **这一行有没有锚点？** 没有就记入"无锚点"清单，不报错。
3. **锚点里的文件在根目录下存在吗？** 不存在记 `FILE_MISSING`。
4. **行号落在这个文件的行数范围内吗？** 越界记 `LINE_OOR`。

判定表：

| 情形 | 记什么 |
|---|---|
| 若文件存在且行号在范围内 | `OK` |
| 若文件不存在 | `FILE_MISSING`（这是最容易被忽略的一种假证据） |
| 若行号超出文件实际行数 | `LINE_OOR`（常见于文档改版后没更新） |
| 若无任何锚点 | `NO_ANCHOR`，只提示不判错 |
| 若不写 `--root` 且当前目录不是树根 | 报错退出，不猜根目录 |

## 三条命令

```bash
# 1. 查一份报告的锚点（tools: check）
python scripts/anchor.py check reports/review.md --root path/to/tree

# 2. 只列锚点与状态，不汇总
python scripts/anchor.py list reports/review.md --root path/to/tree

# 3. 一次查多份
python scripts/anchor.py check a.md b.md --root path/to/tree
```

没有子命令时默认 `check`，旧用法仍可用。

## 输出长什么样

```text
$ python scripts/anchor.py check reports/review.md --root .
OK           scripts/review.py:157      （文件 1097 行）
FILE_MISSING docs/CHANGELOG.md:12        （根目录下没有 docs/CHANGELOG.md）
LINE_OOR     SKILL.md:412                （文件只有 300 行）

锚点 3 个：OK 1 / FILE_MISSING 1 / LINE_OOR 1
结论不合格：有 2 个锚点解析不了，不能当作证据。
```

退出码：全 OK 为 0；出现 `FILE_MISSING` / `LINE_OOR` 为 1；参数或根目录错误为 2。

## 硬规则

1. **NEVER 把解析不了的锚点当证据。** 因为报告一旦带着失效锚点发出，读者按图索骥得不到东西，整篇的可信度会被连带否定。
2. **NEVER 替作者补锚点。** 因为锚点是"我说的这句在哪"，只有作者知道它在哪；机器补出来的位置看似合理，实则可能是另一行。
3. **NEVER 判定锚点那一行"说得对不对"。** 因为判对错要读上下文，机器判定只会制造"已验证"的假象。
4. **MUST 报告文件的总行数。** 因为读者要知道"1097 行里第 157 行"与"12 行里第 157 行"是完全不同的两件事。
5. **MUST 区分 NO_ANCHOR 与解析失败。** 因为没有锚点是作者的取舍，解析失败是错误，混在一起报会让人分不清哪些要改。
6. **NEVER 猜根目录。** 因为同一个相对路径在不同根下指向不同文件，猜错会给出看似确定的错误结论。
7. **MUST 路径支持正反斜杠。** 因为报告常在 Windows 上写、在 Linux 上读，`a\\b.md:3` 与 `a/b.md:3` 指的是同一个文件。
8. **NEVER 把 `行号:列号` 当成两个字段处理。** 因为 `file.py:12:5` 里的 5 是列，不是行——按行解析会误报越界。
9. **MUST 一次跑完再报告。** 因为多文件反复跑既慢又容易漏，一次结论才可复现。
10. **不得 在无锚点时返回非 0。** 因为纯叙述性文档本来就没有锚点，判错会让工具变成噪音。

## Triggers

- 核查引用：check citations, verify anchors
- 核对行号：line number still valid
- 发布前门禁：evidence gate, pre-publish check
- 审计报告：audit report anchors

## Related skills

- `lgd-skill-review`（同系列）：它的每条整改项都带 `文件:行号`，本技能负责验证这些位置真的存在。
- `skill-improver`（同系列）：改完之后用它复测，锚点不变才算真的没改坏。

## 安全边界

- 只读，不写任何文件。
- 只在 `--root` 指定的目录树内解析，不越界读取其他路径。
- **失败时的处理**：根目录不存在、文件读不出、参数缺失——打印明确错误并以 2 退出，不静默返回 0。因为静默成功会让失效锚点被当成已验证。

## Not for

- 判断论述是否正确（需要人读上下文）
- 生成引用或补写参考文献
- 检索外部网页、数据库
