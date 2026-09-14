# Runbook 步骤提取规则（供参考 · 定性）

> 依据：CommonMark §4.5 Fenced code blocks（spec.commonmark.org/0.22，2026-09-06 核对）：
> "content consists of all subsequent lines, until a **closing code fence of the same type
> (backticks or tildes) with at least as many** backticks/tildes **as the opening fence**；
> closing fence 可缩进 ≤3 空格且其后只能有空白；**若到文档末尾仍未找到闭合围栏，块延伸到文档末尾**。"
> 推论：` ```bash ` 块内再出现一行 3 反引号即为合法闭合围栏 → 朴素"按围栏切分"的提取器
> 会在内嵌围栏处**静默截断**载荷。

## 本工具 extract-steps 的判定

开栏：`^ {0,3}(`{3,}|~{3,})` + 可选 info string（首词=lang）。
闭栏：同字符、长度 ≥ 开栏、整行仅围栏字符（+ 缩进 ≤3 列 —— Tab 按 CommonMark
展开到下一个 4 列，故 1 个前导 Tab = 4 列 = **非法缩进，不视为闭栏**；行尾仅空白）。
**带 info string 的围栏行不是闭栏**（CommonMark：info string 只允许在开栏）。
未闭合 → `unterminated: true`，内容到文档末尾。

## 结构完整性（status）

| 情况 | status | 原因 |
|---|---|---|
| 块未闭合 | suspect | 载荷可能截断 |
| 块内 heredoc 无终止标签行 | suspect | 内嵌围栏提前闭合了块，heredoc 被切断（v1 观察到的字段陷阱同构） |
| 其余 | ok | — |

heredoc 识别：行首 `cat|tee`（允许 `> file` 重定向、`-flags`），到首个 `<<`（允许 `<<-`、
引号标签、连字符标签如 `MY-LABEL`）。
终止行：整行 == 标签（`<<-` 时允许前导 Tab）。
`|`/`&`/`;` 之后的 heredoc（管道链/命令链）不识别 —— 有意的保守降级，此类行应人工核对。

## --write-steps 字节约定

- 步骤内容按原文写出（行原样 + 末尾补 `\n`；空步骤写空文件），**不做任何归一化**。
- `steps.json`：每步 `{index, file, bytes, sha256, status}`；sha256 对写出文件复算必须一致（自检覆盖）。

## 与 v1 Rule 4 的关系

v1 说"按显式行范围切割并确认 EOF_* 标签存在"。本工具把该规则机械化：
extract-steps 给出 CommonMark 正确的块边界 + heredoc 终止核查；凡 `suspect` 步骤，
next_action 统一为"按显式行范围切割，勿直接执行"。
