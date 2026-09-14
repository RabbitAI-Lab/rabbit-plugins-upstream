---
name: persistent-skill-memory
version: 2.0.0
description: Persist a deterministic skill index into the agent system prompt. One stdlib-only CLI (index/prompt/inject/verify/stats/hook), idempotent marker-block injection, no truncation, offline.
---

# persistent-skill-memory v2

把已安装技能集合变成**确定性、幂等、最小 token**的索引，注入 agent 系统提示，让任意模型零额外加载即可"看见"可用技能。

v1 的两个根本缺陷在 v2 被结构性消除：v1 的文档引用了两个**包内不存在的脚本**（幻影可执行，模型照着做必失败——幻觉源 #1）；v1 的"每域截断 10 条"与记忆目的相悖。v2 附带全部文档引用的脚本，且截断被"每域一行"的紧凑性取代（预算见 `stats`）。

## 命令契约（stdout 均为单行 JSON；错误 → stderr `{tool,error,hint}`）

| 命令 | 作用 | 退出码 |
| --- | --- | --- |
| `index --root DIR [--write PATH]` | 扫描+解析+去重+分类；可选写 SKILLS_INDEX.md（人读） | 0 / 2 |
| `prompt --root DIR` | 产出注入块（域头行 + 每名一行，域内升序，不截断） | 0 / 2 |
| `inject --root DIR --prompt-file F` | 标记块幂等注入（F 必须已存在，不创建） | 0 / 2 |
| `verify --root DIR --prompt-file F` | 提示块 ↔ 当前目录对账 | 0 / 2 / **3=漂移** |
| `stats --root DIR [--prompt-file F]` | token 预算统计（块字节/域计数/索引字节） | 0 / 2 |
| `hook --root DIR --prompt-file F --out PATH` | 生成 bash 包装：installer → index → inject → verify | 0 / 2 |

退出码纪律：**0** 成功；**2** 用法/IO/标记异常（含半开、多对、倒序标记）；**3** 仅 verify 漂移（missing/stale）。

## 标记块（inject / verify 的唯一约定）

```
<<<SKILL_INDEX_BEGIN>>>
[data-parsing]
alpha-tool
crlf-skill
[general]
beta-heading
<<<SKILL_INDEX_END>>>
```

- 格式 = **每域一个头行 `[domain]` + 域内名字各占一行**（名字升序）。无分隔符歧义：名字含逗号/引号/冒号也能原样往返（v1 逗号拼接会把 "a, b" 拆成两个名字——本格式修复）。
- 标记各独占一行。存在唯一正确一对 → **仅替换内部**（标记外字节不动）；不存在 → 追加到文件尾。
- 双注入 = 字节不变（幂等）；标记异常 = **rc2 不改文件**，不自动补全（自动修复会吞标记外内容）。
- 域顺序 = 固定优先级序（`references/categorization.md`）；块内无 description、无截断。
- verify 漂移字段：`missing` = 在磁盘但不在 prompt（新装未注入）；`stale` = 在 prompt 但不在磁盘（已删/假名）。两者皆空 → rc0。

## 设计决策（为什么这样做）

1. **不截断**：记忆工具截断 = 记忆失真。token 预算靠"每域一行 + 仅名字"控制（实测 8 技能块 ≈ 150 B）。
2. **确定性分类**：固定 10 域优先级表 + `general` 兜底，first-match-wins，全表见 `references/categorization.md`。跨域技能归先列域，可预期、可复现。
3. **去重键 `(owner, slug)`**：owner = 相对路径首个 `@` 段（无则空串）；同键保留字典序首路径，杜绝"同技能双路径"污染索引。
4. **frontmatter 确定性子集**：`---` 块内 `>`/`|` 块标量、引号标量、BOM/CRLF 归一；name 缺省=目录名，description 缺省=首个 `#` 标题。规则与未实现项全部文档化于 `references/frontmatter_parsing.md`（**内联注释不剥离**是有意简化）。
5. **离线 stdlib**：无网络、无第三方依赖；纯函数 + 单行 JSON，任何模型环境可复跑；自检全合成数据。

## 文件加载地图（token 经济）

| 文件 | 何时加载 |
| --- | --- |
| `scripts/skill_memory.py` | 执行任一命令时（自足，无需读文档） |
| `scripts/selftest.py` | 交付前 / 修改后（必须 100% PASS） |
| `references/frontmatter_parsing.md` | 排查解析差异时（供参考） |
| `references/categorization.md` | 分类新技能 / 调关键词时（供参考） |
| `references/injection_semantics.md` | 改 prompt 文件 / 排查注入失败时（供参考） |
| `SKILLS_INDEX.md`（`--write` 生成物） | 人类浏览；**勿**进 prompt |
