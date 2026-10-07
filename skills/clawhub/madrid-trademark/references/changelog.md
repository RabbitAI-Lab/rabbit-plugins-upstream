# 马德里技能版本历史与开发规范

> **用途**：技能版本记录、技能规范与**最近 3 版**修订要点；控制面只保留版本指引。

> **权威范围**：本文件是技能**自身**版本与开发规范的唯一权威源，不承载业务规则（业务规则见控制面 §5 与各 references）。

> **归档策略（v3.7.2 确立）**：本文件**仅保留最近 3 个版本**的详细条目；更早版本已**移出技能包**归档至：

> `C:\Users\LENOVO\.workbuddy\skills-archive\madrid-trademark\changelog-archive-up-to-v3.7.1.md`

> 该路径为**包外留痕**、非技能资源，故以明文书写而**不写成 `@references/` 指针**（避免悬空引用）。

> **编码**：CRLF、UTF-8 无 BOM（与家族约定一致）。

---

> **当前版本**：v3.7.4（2026-10-04）

> **最近一次变更**：v3.7.4 — 补「行尾纯度」用例（Markdown 纯 CRLF / scripts LF / 无 BOM / 无 
 / 无孤立 CR）；v3.7.1 条目移入包外归档。

> **上一批变更**：v3.7.1 — 控制面预算基线确立（接受 SKILL.md 56,651 B / 624 行；§3.9 下沉章节索引表常驻控制面）。

## 一、版本历史（仅最近 3 版）

| 版本 | 日期 | 要点 |

| --- | --- | --- |
| **v3.7.4** | 2026-10-04 | **补「行尾纯度」断言**：`scripts/selftest.py` 新增用例「行尾纯度」（用例 15 → 16），按家族约定校验 Markdown（SKILL.md / references / templates）= **纯 CRLF**、`scripts/` 下 `.py` 与 `.json` = **LF**，且**均无 BOM、无 `\r\r\n`、无孤立 CR**；依归档策略将 v3.7.1 条目移入包外归档 |
| **v3.7.3** | 2026-10-04 | **补「平台结构合规」闸门 + 修一处文档偏差**：① `scripts/selftest.py` 新增用例「平台结构合规」（用例 14 → 15），按开放平台《技能》文档校验 **5 个必填字段 / 一级条目仅标准 4 项 / 子资源目录下无子目录（严格 2 级）/ scripts 各文件已在 SKILL.md 声明 / frontmatter 结构**；② **修正真实偏差**：`madrid_dateutil.py` 此前未在 SKILL.md 中声明（文档要求 scripts 须在 SKILL.md 声明），已在 §4.12 补入说明；③ 依归档策略将 v3.7.0 条目移入包外归档 |
| **v3.7.2** | 2026-10-04 | **文档体积治理（归档策略）**：本文件仅保留最近 3 版详细条目，v3.6.2 及以前整体移出技能包归档（`~/.workbuddy/skills-archive/madrid-trademark/`）；§三 新增第 9 条「文档体积治理」；SKILL.md 对 changelog 的引用措辞同步为「最近 3 版 + 归档」；changelog 19,512 → 约 9 KB |

> **更早版本（v3.7.1 及以前）已移出技能包归档** —— 含 v3.6.2 行尾归一至 v3.4.5 的全部条目，以及**原 `SKILL.md` 文末块**的修订要点；路径见本文件头。

---

## 二、技能规范（自原 SKILL.md 文末块保留）

> **结构规范**：对齐 WorkBuddy 官方技能开发文档（https://open.workbuddy.cn/docs/skill ）——必填字段 description / description_zh / description_en / version / author 齐备，另补 name / display_name / display_name_en / category；版本号改用语义化版本（SemVer）；参考资料统一以 @ 符号加相对路径的形式引用（@ 后接 references 目录内文件名，不加反引号）。**allowed-tools 按选填处理、不设白名单**——本技能需检索 references/ 下 15 份参考文件（13 份 Markdown + 2 份官方 PDF），白名单会屏蔽 Grep/Glob 等检索工具，且无法穷举 MCP 工具名，得不偿失。**数据单点维护**：规费数值唯一权威源为 `references/madrid-fees.md`（SKILL.md §4.8 仅保留构成规则与易错口径）；FAQ 与反例唯一权威源为 `references/madrid-faq.md`；声明唯一权威源为 `references/madrid-declarations.md`（17 类编号）。

> **目录深度**：本技能为严格 2 级结构（1 级 = SKILL.md / references/ / scripts/ / templates/；2 级 = 各目录内文件），符合开放平台「仅接受 2 级目录」要求，无 3 级及以上嵌套。新增子资源时不得在 references/、scripts/、templates/ 下再建子目录。

> **文件编码**：全部 **Markdown 文件（SKILL.md、references/、templates/）为纯 CRLF、无 BOM**（技能家族约定）；`scripts/` 下的 `.py` 与 `.json` 为 LF、UTF-8 无 BOM，与 Python 生态一致，不受该约定约束。

> **脚本维护**：改动规费数值时须同步 `references/madrid-fees.md` 与 `scripts/madrid_fee_data.json`，并运行 `py scripts/selftest.py` 通过全部用例后再提交。

> **维护建议**：定期依据 WIPO 官方更新和 CNIPA 实务指引进行修订；建议按 §3.0 的复核周期触发核验。

---

## 三、版本治理与元数据约定（v3.6.1 确立）

> 本节是技能版本治理的**唯一权威约定**，用以替代此前的「三件套」口头表述。

**1｜单一真源**：`SKILL.md` frontmatter 的 `version:` 字段。版本变更**只改这一处**，其余皆为派生。

**2｜派生同步点（三处，必须与单一真源一致）**：

| # | 位置 | 形态 | 校验方式 |

|---|------|------|----------|
| 1 | `SKILL.md` frontmatter | `version: x.y.z` | 单一真源 |
| 2 | `SKILL.md` 文末 | `> **版本**：vx.y.z` | `scripts/selftest.py`「版本一致性」用例 |
| 3 | `references/changelog.md` | `> **当前版本**：vx.y.z` 与版本历史表首行 | 同上 |

**3｜不设 `meta.yaml`（明确约定）**：

· 本技能族 51 个技能**无任何 yaml 元数据文件先例**（全库仅 5 个 yaml，均为功能配置：risk_rules / score_rules / time_rules / linkage-rules / openai）；

· 本技能自述「**严格 2 级结构**——1 级仅 `SKILL.md` / `references/` / `scripts/` / `templates/`」，根目录新增 `meta.yaml` 会违反该自述规范；

· 本技能不设 `metadata.openclaw.version` 字段，**「第三副本」本就不存在**；为建 `meta.yaml` 而先引入该字段，等于为治理而制造一个待治理的副本。

**4｜不设独立 `scripts/versions.py`（明确约定）**：

· 家族现有 4 份 `versions.py`（patent-infringement-guide / ip-management-compliance / patent-examination-guide / legal-doc-converter）大小与 md5 互异，但同源一模板（`SELF_NAME` 各自硬编码），**属「同构副本」**，与「IP 家族脚本通过 delegation 共享、禁止子技能副本拷贝」的原则存在张力；新增第 5 份会扩大该问题；

· 其校验锚点为 `<!-- VERSION_TABLE_START/END -->` 标记块，本技能不采用该形态；

· **功能已由 `scripts/selftest.py` 的「版本一致性」用例等效实现**——校验上述三个同步点，纳入既有回归流程，退出码可阻断。

**5｜版本号规范**：语义化版本（SemVer）。控制面结构变更（内容外置 / 章节增删）→ minor；仅修订措辞、脚本或用例 → patch。

**6｜文件编码**：Markdown（`SKILL.md`、`references/`、`templates/`）= CRLF、UTF-8 无 BOM；`scripts/` 下 `.py` 与 `.json` = LF、UTF-8 无 BOM。**v3.6.1 已修正 `scripts/selftest.py` 误用 CRLF 的历史遗留**。

**7｜家族级版本治理（如后续推进）**：正确方向是**上收为共享层**——将 `versions.py` 参数化（技能名作入参，替代硬编码 `SELF_NAME`），由 delegation 统一调用，一次性消解现有 4 份副本。属家族级项目，不在本技能范围内实施。

**8｜控制面预算基线（v3.7.1 确立）**：控制面（`SKILL.md`）**接受的基线为 56,651 B / 624 行**（相对 v3.4.5 的 84,061 B 为 −32.6%）。该基线含三项**有意常驻**的导航与裁决资产：① §3.9 下沉章节索引（15 行，常驻以保障下沉内容可反查）；② §5.3 分层优先级裁决与唯一权威源清单；③ §4.0 任务路由表（含「控制面外权威源」列）。

已评估把 §3.9 映射表迁入 `references/madrid-file-index.md`（可回收约 2,300 B），**经权衡决定不迁**：该表属**导航层**，非常驻即失去反查价值，与 TAA 类技能把「下沉章节索引」置于 SKILL.md 的做法一致。

**续用判据（后续新增控制面内容一律适用）**：拟新增的内容须能回答"**常驻能否换来可反查 / 可裁决能力**"——能者留控制面，不能者一律下沉至 `references/` 并登记于 §3.9 索引。

**9｜文档体积治理（归档策略，v3.7.2 确立）**：本文件**仅保留最近 3 个版本**的详细条目，更早版本移出技能包归档至 `~/.workbuddy/skills-archive/<技能名>/`。**理由**：changelog 属「导航」类文件，体积随版本线性增长而单条价值递减；冷热分离可在不丢失历史的前提下控制常读文件体积。**执行规则**：① 升版后若详细条目超过 3 条，将最早条目整段移入归档；② 归档文件顶部须声明覆盖范围与恢复方式；③ 归档路径以**明文**书写，**不得**写成 `@references/` 指针（包外文件不在技能资源内，写成指针会造成悬空引用）；④ 归档**不改变**「版本历史表首行 = 当前版本」的既有闸门要求（`selftest.py`「版本一致性」用例仍校验首行）。