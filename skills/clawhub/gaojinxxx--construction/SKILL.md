---
name: construction-log
description: "Generate construction logs (施工日志) for 镇海区综合体育中心建设工程. Use when user sends daily site work summary via WeChat and needs a formatted .docx log. Covers: content expansion from shorthand, workflow continuity, weather lookup, page calculation, python-docx generation with 宋体11pt format."
version: 2.0.0
author: agent
tags: [construction, docx, word, chinese, template, 施工日志, 甬筑表C01-8]
---

# construction-log

Generate, update, and maintain construction logs (施工日志) for 镇海区综合体育中心建设工程 using 甬筑表C01-8 template.

## Trigger

User sends daily construction work summary (often via WeChat, oral/shorthand style) and needs a formatted .docx施工日志 file. Also triggers when user says "写施工日志", "昨天的施工日志", "补写施工日志", or references 施工部位/工序/班组.

---

## 1. Template Structure

**用户本次上传模板优先于旧默认。** 用户指定“第一个文件为模板、不能改变字体样式、每份一页”时，先检查该DOCX的真实字体、字号继承、rPr、pPr、表格行高及页边距；不能套过去华文行楷/宋体强制清理脚本。正文可直接深拷对应模板run的rPr，保留Normal样式和其余ZIP成员；`font.size is None`可能实际继承11pt，须用Word读取实际字号确认。有新模板时不强制旧六行高度/旧签名位置，更不能把内容截在exact行高里假称单页。先通过简洁、去重复、保留关键问题及处理状态来控制文字量，不为压页改小字体。每份实际Word只读导出PDF，检查pages==1且完整scene/quality/weather/末尾签名均存在，不能只看页数而遗漏被裁掉文字。

**监理质量栏授权范围按本次用户指令判断。** 虽然历史有“仅取施工情况”的限制，用户新明确要求“监理工作内容及问题处理大致改为施工单位日志样式”时可读取该栏并转换现场质量事实、问题和要求；不搬监理旁站、见证、签发通知等职责口吻，不以删主体方式冒写监理专属工作。源文已整改才写已整改；只要求整改则保持要求，不补完成结论。源册缺日期时先问只做有记录日期还是补全；用户选择仅有记录日则不得自作主张生成整月。源文标高/误差矛盾、‘有无沉陷’或未/为笔误不擅自变成确定合格结论，疑点外置。

Single 4-col × 6-row table in `.docx`, preceded by a title paragraph, then `<sectPr>`.

**Document body layout (top-level XML children):**
1. `<p>` — Title: "施工日志" (22pt, centered) — **MUST KEEP**
2. `<tbl>` — The 6-row table
3. `<sectPr>` — Section properties

No other paragraphs should exist outside the table (see §8 Post-generation cleanup).

| Row | Cell layout | Content |
|-----|-------------|---------|
| 0 | [0] 表格编号 \ [1] 甬筑表C01-8 \ [2] 页号 \ [3] page number | Page number = 43 + (target_date − 2026-05-20).days |
| 1 | [0] 工程名称 \ [1-3 merged] 镇海区综合体育中心建设工程 | Project name (fixed) |
| 2 | [0] 日期 \ [1] date string \ [2] 天气 \ [3] weather string | Date: `YYYY年 MM月 DD日 星期X`; Weather: `最高XX°C 最低XX°C 天气描述` |
| 3 | [0-3 merged] **TITLE ONLY:** `施工内容及情况：（施工部位、内容、机械、人员等）` | No detailed content here |
| 4 | [0-3 merged] 现场情况 | All site content: 现场情况/材料/机械/人员 — **single paragraph, `\n` line breaks** |
| 5 | [0-3 merged] 技术质量安全记录 + signature | Quality/safety items + `项目技术负责人：___` + `施工记录：YYYY年MM月DD日` — **single paragraph, `\n` line breaks** |

**Row 4 and Row 5 are visually merged across 4 columns.** Each must be exactly 1 Word paragraph with `\n` soft line breaks inside. Do NOT use `add_paragraph()` for routine logs — it changes spacing.

**Row height (A4 fill):**
```python
row_heights = [400, 360, 400, 400, 7000, 4500]  # R0-R5, twips, exact
```

---

## 2. Content Generation Rules

### 监理与旧施工日志逐日对照（来源优先模式）

**先以用户本轮明确授权的来源范围为准，不将旧回合限制硬套到新任务。** 用户新上传模板并明确要求将“监理工作内容及问题处理”转为施工日志质量安全内容时，应读取该栏，改写为施工方现场事实/问题/措施，不保留旁站、见证、督促施工单位等监理职务口吻；未完成整改不得写已完成。新模板字体、字号和页面规则优先，不能自动改成以前的手写体。监理月册同一张长表可能包含多天：扫描每一行的“日期+最高气温”识别日记录边界，再提取该日字段；不能假设一表一天。此次9月原文件17张顶层表实含30日，第二张含2/3日、第五张含7—10日、最后张含27—30日。提出缺日之前需用原XML日期全文扫描和Word页面交叉核对。

**旧回合恢复污染文件的范围纠正：监理日志仅使用“施工情况”栏。** 用此栏核对施工日志现场施工内容，补漏及纠正工序、部位、进度冲突。监理人员、材料设备/见证取样、机械、监理工作及问题处理、其他事项、天气等其他栏均不作为此次核对来源；不将监理旁站、检查、通知整改搬入施工记录。施工日志原有其他栏位保持，不因这次对照重写；此前已导入其他监理栏位的整包不能称为符合新范围。用户明确提供的后续实际浇筑日期、等级、方量优先保留。执行批量重新修订前从未受宽范围导入的有效原始/手写版本建立基线，而不是误将已导入监理内容当原施工事实。

**修复已污染整包时必须回退基线：** 先定位导入监理前的有效施工日志副本及哈希，不在污染后的技术质量安全栏上靠删“监理”二字修饰。原有质量记录能对应当天工序的，恢复原文本；确实不适用的改为施工方工序控制措辞，不编造整改、复查或验收完成。原材料/机械/人员/天气不从监理取值；无原记录的新增日期留空或采用有依据的中性控制事项，天气若需填写可独立查询。监理只隔离读取“施工情况”字段，严禁其余字段流入中间决策输入，构建和验证都检查该边界。施工栏保留原有独立非冲突事项，不以监理遗漏为由整段抹去施工方内容。完工交付要明确原质量恢复数量、必要调整数量及新增日期数量，并保留用户后续确认的浇筑节点。旧污染整包不作为新的底本。

用户指定以监理日志为准时，采用逐日来源审核，不使用本技能的连续性推排、历史缺口分类或固定机械配置去补证。监理未提不等于冲突，但旧助手推排、轮换泛化质量整改、无独立当天证据的人员数量不能作为事实保留。历史“缺文件=假期/冬歇”的推定不是停工证据；实际逐日监理记录优先，不能据旧缺口清单排除有施工记录的日期。

若委派任务仅要求JSON决策，不生成Word、不修改原件。**先识别本次合同，不能套用其他任务的固定schema。** 原句审核合同可输出 `{date, keep_scene:[], keep_quality:[], alerts:[], omit_supervision_lines:[]}`；保留项采用旧日志完整原句/原条目，仅去编号，不改桩号、不拆拼成新事实。若合同要求omit_supervision_lines为空，不擅删监理重复或可疑行。

**原质量恢复合同：** 用户指定 `{date, scene:[], quality_mode:'restore'|'controls', controls:[], notes:[]}` 时，逐个输入日期输出，不把质量保留项默认置空而丢失恢复决策。以未污染旧施工日志为底，施工对照仅补缺纠冲突；独立消防水池、排水沟、坡面、破除等非冲突作业保留，不以监理未提及为删除理由。旧质量匹配合并后工序时选restore、controls为空，由父流程从原件逐字恢复；明显工种、部位或浇筑前后阶段冲突以及新增日期无旧质量时选controls，写2—4句当天施工方过程控制事项，不写监理、旁站、见证、监理通知，不虚构已验收、整改闭环等事实。缺少新增工序的质量条目本身不等于旧质量错误，不因此全日重写。用户允许简化时，可去冗长套话及已明确无据的助手估算百分比、人数，但保留非冲突的原材料等级、规格及部位；不能借简化增加事实。每个有内容来源均须有覆盖或有证据的冲突处置，施工正文不出现补录、待核对、AI等制作旁白，疑点只入notes。塔吊冲突按塔号＋构件＋阶段核对；未标塔号不能擅指认为已安装的同一塔吊。最终从磁盘重读，检查完整日期序列、数量、字段和模式计数；用户只要路径和数量时，交付仅给路径、总数及restore/controls计数。详见 `references/contractor-quality-restoration.md`。

**状态锚点与记录时点：** 旧助手逐日推排不能与监理实录无差别堆叠；对无独立当天证据的旧推排工序，采用授权施工栏作为状态锚点，并在notes说明未保留依据，但不能把监理未提直接说成明确冲突。用户明确提供的比例、剩余量及完成状态，非冲突时原样保留；“施工中”与同日“已完成”先区分构件、分区段和记录时点，时点未知不得虚构先后顺序，也不据缺失字段推定全区冲突。明确浇筑后，同一构件转为养护，不再保留旧钢筋/浇筑准备推排；后浇带、换撑带浇筑另行识别。旧整日停工不得覆盖施工栏已记的实际作业，但仅有台风后检查、维保、监测也不能自动证明全面复工。详细判例见 `references/contractor-quality-restoration.md`。

审核必须同时检查：日期/星期及重复日期、未来引用日期、每日和累计桩数衔接、试块“每桩1组”与成桩数、机械退场与台数连续性、停工次日“昨日成桩”等模板时序。**桩数一致不是桩号正确的充分条件：**还要按桩号（去掉机号前缀）跨日期和同日查重，确认工程/区域编号作用域；同一桩号被重复记为完成而无解释时，不保留相关整条旧条目，也不静默修正。累计衔接只在日期连续且统计口径一致时做等式校验，不把缺失日期视为零施工。

对疑似复制旧页、累计倒退或数据不一致，只列具体证据并保留源文；不能反推“应为”的数量、日期、规格或验收结论。**先完整扫描旧现场栏，再按章节抽取：**现场事项可能追加在材料、机械、人员之后的“其他现场作业”中，只截取“材料”之前会漏掉原句。对额外工序同时核对构件、部位和日期：消防水池、排水沟、破桩、构筑物破除等可与主工序并行，但已安装/检测的塔吊不能再保留同一基础的安装前开挖准备；不同部位或分段续作不能仅因日期不同判冲突。原句保留合同中，泛化百分比、估算方量或虚构验收结论混在一整条候选句时，不擅自拆改成新事实；用户明确允许简化的原质量恢复合同则可保留有来源的工序核心，剔除已明确无据的估算，处置依据记录在notes。只在本次授权的施工情况字段中核对轴线—区块对应、总数与分项、残缺单位；不为核对而扩读未授权的旁站或其他监理栏。没有记载不等于零施工，疑似漏记与明确矛盾须区分。输出后重读JSON，核验输入/输出日期序列及数量、精确字段、保留项原文子串、重复桩号、数组类型及原件未变。交付按用户要求只给绝对路径、日期数量及主要发现。详细案例见 `references/supervision-reconciliation.md`。

### 月度进度计划与横道图：用户的简洁呈现偏好

用户要求月度计划文字版时，按分区概括本期计划完成的施工内容，不默认逐日列日期；跨期未完事项与本期完成目标分开，按用户指定的切换日期合并旧总计划与新版分区计划。用户要求阶段总进度时，只列该阶段一项，不自动扩展为桩型、数量、分母和证据明细。若缺综合比例，先区分“按来源计算”与“用户给定计划控制值”；不能拿工程桩比例冒充整个桩基阶段，不能为了体现滞后虚构实际量。

用户明确提供每月“月初完成率→月底计划完成率”后，原样使用；下个月月初可能低于或高于上个月计划月底值，不强行改成连续曲线，也不解释成新的实测统计。当前偏好的简版PDF为：工程/月份标题、计划周期、一项阶段施工横道、两端百分比和一句本月目标。**不重复添加“序号/工作内容/月初完成率/月底计划完成率”汇总表**，用户已通过红圈明确删掉该块。截图局部修改只作用于圈定范围，保留其余文字与百分比，并合理上移填补空白。整批逐月核对日期、用户给定比例、被删表头不再存在、保留横道与目标，并实际渲染检查。压缩包只放用户要求的文件，不附使用说明。详见 `references/monthly-progress-plan-presentation.md`。

**后续地下室日志的计划来源：** 用户已提供地下室底板进度表，并约定普通工序可随实际偏差约1—2天、混凝土实际浇筑日期由其另行告知。编写后续日期前读取 `references/basement-schedule-baseline.md` 及其中的本地原表/规范化参照；实际反馈优先于计划，不能把计划浇筑写成已发生。

### 2.1 Role & Principle

Act as a construction technical lead with 15+ years experience. Transform the user's oral, shorthand, out-of-order site reports into professional, structured, traceable log content.

**Core principle: 真实记录施工过程，不为了"写得丰富"去虚构施工过程。**

**长日期段、仅有首尾节点时的用户版式偏好：** 用户明确表示文件只作工作使用、不要在每份 Word 里反复写“补录/待核实/拟核对”时，区分“正常施工日志版式”与“现场事实已核验”。可以让文档保留正常 C01-8 的简洁现场情况表达，把推排依据与不确定性集中写在交付说明中；但不能把由前推/后推得到的具体作业日期说成已核实的历史事实，更不能声称这种推排版可替代真实现场记录。先从最后一份现存日志**前推**已知进展、从用户提供的后续浇筑节点**逆推**前置工序，并逐日检查防水→保护层→钢筋→模板/预埋→浇筑的顺序。用户只说“目前完成50%”而未指明日期时，绝不把这一比例倒填到较早日期。下雨天避免默认露天防水铺贴；停工日不能仅凭缺文件猜测。若用户要实际用于正式工程原始资料，须先取得逐日现场证据，而不是靠排程冒充现场记录。交付时明确说明哪些是已提供的节点，哪些是推排，并只把版式检查称为版式检查。

**Never fabricate:** 日期、天气、人数、工程量、混凝土方量、钢筋吨位、桩号、标高、尺寸、强度等级、材料数量、机械数量、检测数据、试块数量、验收结果。If user didn't provide it, don't make it up.

**Preserve explicit progress exactly:** When the user states a completion ratio or stage (for example, “垫层完成80%” or “已完成约80%”), carry that status into Row 4 as `完成约80%，剩余部位持续施工` (or equivalent) rather than rounding it up to complete, replacing it with a vague “施工中”, or adding an unsupported quantity. Treat an explicitly stated completion percentage as a user-confirmed fact, not a value to infer.

### 2.2 Shorthand Expansion

User gives shorthand → expand into ONE concise flowing sentence per item.

Pattern: `N、[工序]施工，[作业内容描述]，[质量控制/验收]。`

Examples:
- "西南角水沟粉刷" → `西南角排水沟进行内壁及侧壁粉刷施工。`
- "西北角修坡，一级坡完成" → `西北角基坑边坡进行人工配合机械修坡施工，一级边坡修整完成。`

**Be concise.** User has explicitly rejected long repetitive content. One sentence per item.

### 2.3 Homophone/Dictation Correction

Correct obvious dictation errors silently based on construction context:
- "湖泊修坡" → "护坡修坡" or "基坑边坡修坡"
- "塔吊基础节买预埋" → "塔吊基础节埋件预埋"
- "水沟气体" → "水沟砌体"
- "出出口平台" → "出土口平台"
- "维护支撑梁" → "围护支撑梁"

If ambiguous and affects engineering facts, preserve original and remind user to confirm.

### 2.3.1 Voice-transcript correction for construction terms

When a user reports that a voice transcription is wrong, **do not treat the displayed transcript as site fact and do not infer a plausible technical term from it**. In particular, do not turn phonetic fragments into pile, column, reinforcement, concrete, or other engineering work without the user's confirmation. Preserve the exact specificity of confirmed facts: `2区钢筋绑扎完成` does **not** establish `2区底板钢筋绑扎完成`, even if bottom-slab concrete was poured the next day. Ask which component was tied, or keep it as `2区钢筋绑扎完成，具体部位待核对` in a clearly marked draft.

1. Pause document generation or revision.
2. State only the portion that is certain, if any.
3. Ask for a compact correction of the ambiguous items.
4. Treat the user's corrected wording as the authoritative record.
5. If a same-date log was already generated from the bad transcript, overwrite that file rather than create a duplicate; explicitly say that it was corrected.

A local re-transcription may diagnose quality, but it never overrides the user's correction. Do not describe a transcript as a gateway failure unless logs prove that transcription actually failed.

### 2.4 Row 4 Structure (现场情况)

```
一、现场情况：
1、[工序]施工，[作业内容]，[质量控制]。
2、...

二、材料：
[材料进场情况，or "混凝土、钢筋、模板等材料按需进场，满足当日施工需求。"]

三、机械：
[机械列表，e.g. "汽车泵1台、混凝土运输车4辆、振捣设备2套、小型挖掘机1台。"]

四、人员：
管理人员6人，资料员1人，工人N人。
```

### 2.5 Row 5 Structure (技术质量安全记录)

```
技术质量安全工作记录存在问题及处理情况：
1、[质量/安全控制措施，corresponding to Row 4 items]。
2、[安全巡查/整改情况]。
...
项目技术负责人：________________________
施工记录：YYYY年MM月DD日
```

Each Row 5 item should correspond to a Row 4 construction activity — quality control measures for that activity.

### 2.6 Language Standard

**用户明确纠正：日志正文采用现场记录人的简洁口吻，不插入制作过程说明。** 不得在施工内容或质量安全记录中写“依据前后日志连续性补录，现场具体情况需核对”“根据表格补充核对”“AI生成”“倒推/拟核对”等编写旁白。交付前扫描正文，保留已提供的现场工序和事实；仅删除编写说明时不要新增虚假的检查、整改或验收结果去填位置。疑点、计划依据及推排边界在聊天或独立说明里如实沟通，不能为了看起来像本人书写而把未证实事实写成已完成或已验收。用户反馈曾打印出8/12等历史日志中遗留说明，因此全量字体转换不能代替正文质量检查，交付整包前需检查所有月份。

**Formal written construction language only.**

Forbidden: 今天搞了、做了一点、差不多完成、搞好了、弄好了、应该没问题、估计完成

Use: 进行…、完成…、持续施工…、按计划推进…、施工完成…、检查完成…、整改完成…、经复查…

### 2.7 Preserve User's Site Terminology

Valid user-provided site terms must be preserved verbatim:
- `支撑梁包模加固` — do NOT normalize to `封模加固`; use `包模加固` in both Row 4 and Row 5
- `垫层栏方木` — accepted site term, preserve verbatim

---

## 3. Workflow Continuity (MANDATORY)

**Before writing each day's log, ALWAYS read the 2-3 most recent prior logs** to understand the project's workflow sequence.

### 3.0 Backfilling a date range

Full procedure, gap-audit script, and the bracket-interpolation rules live in
`references/backfill-and-gap-audit.md`. Read it whenever the request is "补齐/补写之前的施工日志".

**Audit before writing (do this first).** Walk *every* month folder and compute the full
missing-date list before generating anything. The gap list is routinely far larger and more
mixed than the user remembers — a 2026-09-11 audit found 240 logs with **51 missing days**,
of which ~46 were holiday/seasonal stoppage (元旦, 春节+冬歇, 劳动节) that must **not** be
backfilled at all. Present the classified gap table and let the user choose; never silently
mass-generate dozens of documents.

**Never invent a missing day's content.** If the user asks to backfill and has not supplied
that day's site facts, say so and ask. The one exception is bracket interpolation (below).

When the user says "补全最近几天/补齐施工日志/补齐之前没有完成的" and does not specify exact dates:
1. Inspect **all month folders** and identify the first/last missing dates vs. the current date. Scan both the last existing file date and the first gap.
2. Search recent session history for date-specific site facts before drafting; do not assume that a missing file means work occurred.
3. Use explicit user-confirmed events as hard facts. For example, if the user confirms a typhoon shutdown from 8/9 through 8/11, all three dates must be recorded as suspension/protection/inspection entries rather than normal construction.
4. Generate the missing range in chronological order and preserve page continuity. If an existing file in the range conflicts with a later user correction, replace it and state the correction.
5. When daily source facts are absent, mark the output as an inferred/draft record in the delivery message and avoid inventing headcounts, equipment counts, quantities, inspection results, or completion percentages. Use neutral wording such as "按当日安排到岗" and "按需使用" unless actual figures are supplied.
6. Save to the user's established desktop archive path (`桌面/自动日志/<月份>/`), not a new folder or the knowledge base.
7. **Cross-month handling**: When the gap spans a month boundary (e.g. 8/31 to 9/8), place each file in the correct month folder — August dates go into `8月份/`, September into `9月份/`. Create the new month folder with `mkdir -p` / `Path.mkdir(exist_ok=True)`.
8. **Interpolated days carry no percentages.** A day reconstructed from its neighbours may state that a 工序 was `施工开始` / `持续推进` / `剩余部位持续施工`, because the bracket proves the activity existed. It must **not** state a completion ratio — the bracket does not prove how much was done. `完成约15%` invented to sit between 0% and 30% is a fabricated 工程量.
9. **Show the derivation and flag the draft.** Deliver an interpolated log with a table mapping each Row 4 item to the neighbouring-log evidence that justifies it, label it a draft, and list the specific things the user should confirm (did this 工序 really start that day, is an adjacent log also missing the item, was there other work).

**Multi-day progression planning (working scenario, not factual interpolation):** When the user provides only the current day's status (e.g. "现在挖土到2区，二区承台ALC完成，垫层80%"), work backwards from that endpoint and forwards from the last existing log to build a plausible daily progression. Unlike the single-day bracket interpolation in §3.5, a missing span longer than one day cannot prove that a given trade worked on a specific date. Such a span may be delivered only as an explicitly described *working-use reconstruction* (if the user requests one), never as verified historical field evidence. A normal-layout Word file does not change that provenance. See `references/multi-day-progression-reconstruction.md` for the two-ended schedule check and delivery/verification boundary. Use the pattern:
- **Phase transition days** (e.g. 1-1区收尾 → 2区准备): include "基本完成 / 测量放线 / 技术交底" bridging entries.
- **New workface ramp-up** (e.g. 2区开始开挖): first day is "开始", subsequent days "持续推进".
- **Parallel activities**: as one zone finishes (养护/模板), a new zone starts (开挖/破桩). Overlap is normal.
- Each day's Row 5 must correspond to that day's Row 4 — don't copy-paste identical safety records across all days.
- Fetch weather for the entire date range in a single API call rather than day-by-day.

A range-backfill delivery must list the dates created/modified in a summary table (date, page number, weather, key content), identify which dates rely on inferred workflow continuity, and call out any values the user should verify.

### 3.1 Carry-Forward Rules

1. Read prior 2-3 `.docx` logs (Row 4 content)
2. Items mid-progress (e.g. "钢筋绑扎80%") → next log: completion or continuation
3. Items just completed (e.g. "混凝土浇筑完成") → next log: "养护中"
4. Items just started (e.g. "模板开始封模") → next log: "模板加固" or "浇筑"
5. Add carried-forward items alongside user's stated items

**Example (7/29 → 7/31):**
- 7/29: 6区支撑梁混凝土浇筑完成 / 8区支撑梁钢筋绑扎完成+模板开始封模 / 东北角二级坡调土整平
- User's 7/31 input: "东侧二级坡回填土小挖机整平，九区支撑梁模板加固并浇筑混凝土"
- Expanded 7/31: + 8区支撑梁模板加固及封模施工（from 7/29 模板开始封模）+ 6区支撑梁混凝土养护中（from 7/29 浇筑完成）

### 3.2 Worker Headcount

**2026-10-26起班组规模参考：** 用户口述钢筋工约30、泥工约8、防水工约6、木工约10，“根据每日施工量做变化”。这是写作参考，不是每一天四个班组全部到岗的考勤证据。某日只明确钢筋绑扎时，可写“钢筋工约30人进行钢筋绑扎；其他工种按当日作业面需要配合”；泥工、防水工、木工人数只在对应当天作业/考勤有依据时写入，不凭施工量自动换算精确人数。

Only write worker counts supplied for the relevant date or backed by actual attendance records. Workface count, historical staffing and a previous correction do not establish another day's headcount. When the user gives no count, use neutral wording such as `管理及作业人员按当日各作业面施工安排配合` rather than inventing a plausible number. If explicitly asked to estimate manpower for planning, label that as a separate staffing estimate, not a fact in the daily log.

### 3.3 Machinery Count

**复工日后续区块土方尚未启动时的写法（2026-10-26用户纠正）：** “后续区块土方开挖尚未启动”只限定后续区块，不能写成“土方开挖尚未开始”或“当日未开展土方开挖”来否定已开挖区块/其他土方作业。固定挖机配置可写“现场维持200型挖掘机7台、30型小型挖掘机1台配置”，不据此断言当天全部挖机停用或全部投入土方作业。钢筋加工机具可随已确认下料/绑扎写入，不臆造机具台数。

**Standing fleet (user-confirmed 2026-09-11):** 200型挖掘机 7台 + 30型小型挖掘机 1台. The user
describes this as fixed for the current earthwork phase. Write it explicitly rather than falling
back to the vague `土方开挖、运输及垫层施工设备按现场施工需要配置使用`:

```
三、机械：
200型挖掘机7台、30型小型挖掘机1台，配合土方运输车辆投入现场施工作业。
```

Keep using this until the user says the fleet changed. When a phase shifts (e.g. earthwork →
主体结构) the fleet will change — ask rather than carrying the excavator count forward blindly.

Outside a user-confirmed standing fleet, do not invent machinery counts for a first draft. Use a non-quantified description of the relevant equipment, and request actual counts only if needed. Clearly separate a planned equipment allocation from actual daily equipment attendance. Later user corrections override prior estimates but must not be applied to unrelated dates automatically.

**Editing the 机械 block in an existing file:** when splicing a new `三、机械：` section into
Row 4 by line-scanning, the loop that skips old lines until `四、` also eats the blank separator
line. Re-insert it — Row 4 sections are separated by one empty line, and losing it visibly
changes the layout. Verify by printing the full Row 4 text after the edit, not just the
paragraph count.

### 3.4 Actual-milestone corrections and revision scope

用户补充实际浇筑日期、区块、强度/抗渗等级及方量，并要求“钢筋绑扎日期也改掉”时，不能只新增浇筑当日：先读取最新有效修订套件及前后现场、材料、质量栏，按**区块＋构件＋工序**检查绑扎→浇筑准备→浇筑→养护。保留监理已记载的真实绑扎日期；后续浇筑节点只能限定前序必须发生在此前，不能证明此前每条绑扎记录都错，也不能推出准确开工/收尾日。若用户未给准确绑扎日期，优先保留有来源日期；必要的工作用衔接安排须在聊天说明，不补造隐蔽验收合格。

按字段记录用户新事实，区分“预计”“当日完成”“已完成状态”；强度/抗渗等级与方量同时核对现场栏及材料栏，不把同一方量因两栏重复展示而加总。真实后浇带、换撑带浇筑不能误当同一区底板整体浇筑，也不能误删墙柱、承台等不同构件的钢筋施工。用户新确认的实际节点优先于旧计划及先前助手推排；若与监理原文存在明确冲突，保留来源并单独说明，不能暗中改监理文件。

另存最新完整版本并可附仅含改动日期的增量包，原文件不变；未改日期逐字节比对，输出数量、增量数量和页号方案均由代码验证。**页号方案继承当前套件**：历史日期公式与后来整套连续重编是两种方案，不可混用。详见 `references/actual-milestone-revisions.md`。

### 3.4.1 Same-day correction: a “停工” log was actually a复工 day

When the user supplies dated first-hand progress contradicting an existing all-day stoppage record, inspect that exact `.docx` before editing. The user's correction is authoritative for **that date only**: do not keep `全天停工`, stopped machinery/personnel assertions, or stoppage-specific safety text alongside the new work. Audit the weather cell separately: `台风影响` used as a stoppage reason is not a measured weather observation; if weather is required, replace it with a sourced actual-weather lookup. Do not infer adjacent missing days were stopped or resumed.

Preserve component and progress precisely: `底板上排筋绑扎` does not mean all slab reinforcement is complete; `承台钢筋约30%` stays at 30%. **Earthwork statements must be scoped to the named zones:** if the user says later zones have not started excavation, write only `后续区块土方开挖尚未启动`. Do not generalize to `土方开挖尚未开始`, `土方尚未开挖`, or `当日未开展土方开挖` for the whole site. The standing excavator fleet is a configuration, not proof of use or non-use that day. “其他零碎工作” without specifics does not authorize inventing trades, materials, staffing, machinery, inspections, or completed整改. Leave unsupported subsections neutral (`—`) and describe relevant quality/safety controls without claiming completion of checks or acceptance.

Back up the original outside the active month-level date scan, then revise the canonical `施工日志_YYYYMMDD.docx` rather than leaving two active same-date versions. Inherit the **current file's** page numbering; do not recalculate using an older formula. Preserve scoped fonts (Row 4 and Row 5 body 华文行楷11pt; fixed labels/signature/date in their original font). Re-open the final file, checking exact work/progress, unchanged page, Row 4/5 single-paragraph structure, ZIP integrity, and absence of contradicted stoppage text. State briefly what was excluded for lack of detail.

### 3.5 Continuous Days Logic

- Don't repeat same problem items day after day
- Don't write completed work as "正在施工"
- Ensure construction progress is logically continuous
- Previous day's unfinished work → "继续施工"

---

## 4. Daily Workflow (Step by Step)

### Step 1: Read prior logs
Read 2-3 most recent `.docx` files from the current month folder.

### Step 2: Get weather
```bash
# Open-Meteo (structured, recommended)
curl -s "https://api.open-meteo.com/v1/forecast?latitude=29.87&longitude=121.55&daily=temperature_2m_max,temperature_2m_min,weathercode&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&timezone=Asia/Shanghai"
```
Round temps to whole degrees. Map WMO code via `references/wmo-weather-codes.md`.
Format: `最高XX°C 最低XX°C 天气描述`

**Weather cell length pitfall:** Keep weather value short enough for one line. For typhoon days use compact `最高33°C 最低26°C 台风`; put full reason in Row 4/5.

### Step 3: Calculate page number
```python
from datetime import date
base = date(2026, 5, 20)
target = date(2026, 8, 11)  # example
page = 43 + (target - base).days
```

### Step 4: Copy template and generate
**Style base:** Always use the most recent correct-format log as template. Authoritative style base: `6月份/施工日志_20260628.docx` or earlier. **Do NOT use files dated 6/29 or later as style template** (they incorrectly force 18pt body text).

For new month: create `X月份/` folder, use last log of previous month as style base.

### Step 5: Write content via python-docx

**Approach A (recommended — `cell.text` with `\n`):**
```python
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
import shutil

shutil.copy2(src_path, out_path)
doc = Document(out_path)
table = doc.tables[0]

# Row 0: page number
table.rows[0].cells[3].text = str(page_num)

# Row 2: date + weather
table.rows[2].cells[1].text = f'{year}年 {month:02d}月 {day:02d}日 星期{weekday}'
table.rows[2].cells[3].text = weather_str

# Row 4: site content (single paragraph, \n breaks)
content_r4 = (
    '一、现场情况：\n'
    '1、[工序]施工，[作业内容]，[质量控制]。\n'
    '2、...\n'
    '\n'
    '二、材料：\n'
    '...\n'
    '\n'
    '三、机械：\n'
    '...\n'
    '\n'
    '四、人员：\n'
    '管理人员6人，资料员1人，工人N人。'
)
for ci in range(4):
    table.rows[4].cells[ci].text = content_r4

# Row 5: safety + signature
content_r5 = (
    '技术质量安全工作记录存在问题及处理情况：\n'
    '1、[质量/安全控制措施]。\n'
    '2、...\n'
    '项目技术负责人：________________________\n'
    '施工记录：YYYY年MM月DD日'
)
for ci in range(4):
    table.rows[5].cells[ci].text = content_r5

doc.save(out_path)
```

**Merged-cell pitfall:** When using `add_paragraph()` (Approach B, for fine control), do NOT loop over `row.cells` writing same content to every cell — python-docx merged-cell aliases cause duplicate blank paragraphs. Write only to `cells[0]`.

### Step 6: Force font on ALL runs (CRITICAL)

**Formatting inheritance pitfall (confirmed 2026-07-13):** Copying a correct-format file is NOT sufficient. Newly created runs may have `run.font.size is None` and silently inherit Word's Normal style (18pt). After replacing any content, explicitly set every non-empty run.

```python
doc2 = Document(out_path)
table2 = doc2.tables[0]
for row in table2.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                if not run.text:
                    continue
                run.font.name = '宋体'
                run.font.size = Pt(11)
                rfonts = run._element.get_or_add_rPr().get_or_add_rFonts()
                for attr in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
                    rfonts.set(qn('w:' + attr), '宋体')
doc2.save(out_path)
```

**Do NOT deduplicate with `id(cell._tc)`**: python-docx may create temporary wrappers whose Python ids can be reused, causing some merged-cell runs to be skipped.

### Step 7: Remove external signature paragraphs
```python
doc3 = Document(out_path)
body = doc3.element.body
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
to_remove = []
for child in body:
    tag = child.tag.split('}')[1] if '}' in child.tag else child.tag
    if tag == 'p':
        txt = ''.join(node.text or '' for node in child.iter(f'{NS}t'))
        if '项目技术负责人' in txt or ('施工记录' in txt and '2026' in txt):
            to_remove.append(child)
for child in to_remove:
    body.remove(child)
doc3.save(out_path)
```

### Step 8: Verify
```python
doc4 = Document(out_path)
t = doc4.tables[0]
# Check: 1 table, 6 rows
# Check: external paragraphs = 1 (only "施工日志" title)
# Check: Row 4 cells[0].paragraphs count = 1
# Check: Row 5 cells[0].paragraphs count = 1
# Check: all non-empty runs have size=11pt, eastAsia=宋体
# Check: Row 5 ends with 项目技术负责人 + 施工记录
```

**Font verification pitfall (confirmed 2026-09-09):** When checking `rFonts` attributes in the verification loop, do NOT use `run._element.rPr.rFonts` with a truth test — newer lxml emits `FutureWarning` on element truth-testing and may evaluate a valid element as falsy, causing ALL runs to be reported as "bad font" when they are actually correct. Use explicit `find()` instead:
```python
rpr = run._element.find(qn('w:rPr'))
if rpr is not None:
    rf = rpr.find(qn('w:rFonts'))
    ea = rf.get(qn('w:eastAsia')) if rf is not None else None
else:
    ea = None
```

---

## 5. File Locations

| Item | Path |
|------|------|
| Style base (approved) | `自动日志/6月份/施工日志_20260628.docx` |
| May logs | `自动日志/501-531/施工日志_YYYYMMDD.docx` |
| June logs | `自动日志/6月份/施工日志_YYYYMMDD.docx` |
| July logs | `自动日志/7月份/施工日志_YYYYMMDD.docx` |
| August logs | `自动日志/8月份/施工日志_YYYYMMDD.docx` |
| September logs | `自动日志/9月份/施工日志_YYYYMMDD.docx` |
| Python venv | `/home/hi/.hermes/venvs/docx/bin/python` |

WSL paths: `C:\Users\hi\Desktop\自动日志\` → `/mnt/c/Users/hi/Desktop/自动日志/`

**Month transition:** For first log of a new month, create the folder (`8月份/`) and use the last log of the previous month as the style base. **Do NOT cross-copy** between month folders — user explicitly rejected mirroring.

---

## 6. Environment Setup

Resolve the interpreter **before** writing the generator script — the venv path differs by host, and the wrong one wastes a round trip.

**WSL / Linux:**
```bash
VENV=/home/hi/.hermes/venvs/docx
if [ ! -x "$VENV/bin/python" ]; then python3 -m venv "$VENV"; fi
"$VENV/bin/python" -m pip install -q python-docx
```

**Windows-native session (git-bash/MSYS, cwd `D:\AI\Hermes`):** the WSL venv above does not exist, `python3` is absent, and the Hermes bundled `python` has **no pip module** (`No module named pip`). Do not attempt `python -m pip install python-docx`. Use `uv`, which is present on this host:
```bash
cd /d/AI/Hermes
uv venv --python 3.11 .docxvenv                                      # reuse if it already exists
uv pip install --python .docxvenv/Scripts/python.exe python-docx
./.docxvenv/Scripts/python.exe gen_log_YYYYMMDD.py
```
Windows venv layout is `Scripts/python.exe`, not `bin/python`. Check for `.docxvenv` before recreating it. Docx paths may stay in `C:/Users/hi/Desktop/自动日志/...` forward-slash form — python-docx accepts them directly from git-bash, no `/mnt/c` translation needed.

**execute_code restriction workaround:** In non-interactive contexts (cron, background), use `write_file` to save script to `/tmp/gen_log_YYYYMMDD.py`, then run via `terminal`:
```bash
VENV=/home/hi/.hermes/venvs/docx && "$VENV/bin/python" /tmp/gen_log_YYYYMMDD.py
```

---

## 7. Common Pitfalls

### 7.1 Session timeout / missed response
User sends construction content via WeChat, but session times out before agent responds. Next session:
1. Use `session_search(query="施工日志 YYYY-MM-DD")` to find missed messages
2. Check for construction-related content with no assistant response
3. Confirm with user: "昨天X点你让我写施工日志，会话超时了，现在补上"
4. Generate the missed log + offer to generate today's if user is active

### 7.2 Date ambiguity: "今天" / "这两天" vs system date
When user says "今天的施工日志" or "这两天", do **not** trust stale session metadata or server default timezone. The user's working timezone is China time (`Asia/Shanghai`). The **message send timestamp converted to Asia/Shanghai** is authoritative, especially for late-night messages processed after midnight or when the host default timezone is EDT/UTC.

**Required check before assigning dates:**
```bash
TZ=Asia/Shanghai date '+%Y-%m-%d %A %H:%M %Z'
```

**Timezone trap (confirmed 2026-08-11):** The WSL system default timezone may be **EDT (America/New_York)** and session-start metadata can carry a stale date. When the user corrects the date (e.g. "今天怎么会是8月5号呢"), immediately verify China time and acknowledge the correction. Use China-local date for log date, weekday, weather lookup, and page number.

Interpretation examples:
- If China date is 2026-08-11 and user says "这两天没写", default to 2026-08-10 and 2026-08-11 unless user corrects.
- If a tool/session context says an older date but China time differs, use China time.

If ambiguity remains after checking China time, ask for exact dates rather than generating logs for the wrong days.

### 7.3 Power outage / connection drop
User may say "刚刚断电了" mid-conversation. Pick up from session history — do NOT ask user to repeat. Pending content is in recent messages.

### 7.4 Typhoon / weather cell length
Keep weather cell short (`最高33°C 最低26°C 台风`). Put full suspension reason in Row 4/5.

### 7.5 WeChat "正在输入" forever / voice recognized as English

**Symptom A:** User says WeChat shows "正在输入" (typing indicator) but no response ever arrives.

**Diagnosis:** Check gateway log:
```bash
grep 'inbound.*weixin' ~/.hermes/logs/gateway.log | tail -5
```
If log shows `msg=''` for the inbound message, the user sent a **voice or image message** whose text body did not reach the agent. The gateway receives the message event but the parsed text is empty, so the agent has nothing to process.

**Symptom B:** User sends Chinese voice but the transcript is weird English.

**Cause/fix (confirmed 2026-08-11):** STT language was set to English. For this user, Chinese voice dictation is expected. Verify and set:
```bash
hermes config get stt
hermes config set stt.language zh
hermes config set stt.local.language zh
```
Then restart the gateway for config changes to take effect.

**Also check media download:** If logs show `voice download failed` or `novac2c.cdn.weixin.qq.com ... SSL handshake failure`, the voice file itself failed to download from WeChat CDN (often proxy/duplicate-gateway related). See §7.7.

**Also check authorization:** If the log shows `WARNING: Unauthorized user`, pairing hasn't been approved yet. Run `hermes pairing list` and `hermes pairing approve weixin <request-id>`.

### 7.6 WeChat pairing (first-time setup)

When a new WeChat account sends the pairing code, approve it:
```bash
hermes pairing list                              # See pending requests
hermes pairing approve weixin <request-id>       # Approve
```
The pairing code the user relays (e.g. `QTEFSZMH`) is just for identification — the actual approval is done via `hermes pairing approve`. After approval, the user is recognized automatically on their next message.

**Gateway restart after pairing:** If the gateway was running before pairing was approved, the first message may have been flagged `Unauthorized user` and dropped. Restart the gateway to ensure clean state:
```bash
kill $(ps aux | grep 'hermes gateway run' | grep -v grep | awk '{print $2}') 2>/dev/null
sleep 2
hermes -p default gateway run --replace
```

### 7.7 WeChat MEDIA file delivery fails (SSL handshake via proxy)

**Symptom:** User receives `⚠️ Couldn't deliver the file attachment (施工日志_XXXX.docx)` even though the file exists and is valid (24KB, correct format).

**Diagnosis — gateway log shows the real error:**
```bash
grep -i "send_document\|Failed to send media" ~/.hermes/logs/gateway.log | tail -5
```
Signature: `Failed to send media (.docx): Cannot connect to host novac2c.cdn.weixin.qq.com:443 ... [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE]`

**Root cause (confirmed 2026-08-11):** The gateway process inherits the system proxy env vars (`https_proxy=http://127.0.0.1:7897` — user's Windows global proxy). WeChat file uploads go through `novac2c.cdn.weixin.qq.com:443`; the proxy breaks the TLS handshake to this CDN. The user's own proxy software being off/restarted mid-session triggers this — it's transient, not a file problem.

**Fix order:**
1. Just retry delivering the same MEDIA: path — often succeeds once the proxy recovers.
2. Check proxy env on the gateway process: `env | grep -i proxy` (both the shell and the running gateway inherit it).
3. If persistent, restart the gateway with proxy bypassed so file uploads reach WeChat CDN directly:
```bash
kill $(ps aux | grep 'hermes gateway run' | grep -v grep | awk '{print $2}') 2>/dev/null
sleep 2
env -u http_proxy -u https_proxy -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY -u all_proxy \
  hermes -p default gateway run --replace
```
4. Re-send the MEDIA attachments after restart.

---

## 8. Verification Checklist

**Drafts in nested folders:** A month-level verifier may scan only `自动日志/<月份>/` and miss files stored under `待核实草稿/`. A `MISSING` row plus `all checked files pass` is **not** successful verification: it checked zero target files. For nested draft files, open each generated absolute path with `python-docx` and assert the date/page, body/table/row structure, Row 4/5 paragraph counts, font attributes, and signature. State which method actually checked the documents. Keep unverified process assumptions in a `待核实草稿` folder rather than silently treating plausible scheduling as historical fact.

Before delivering the file, verify:
- [ ] 1 table, 6 rows
- [ ] External paragraphs = 1 (only "施工日志" title)
- [ ] Row 4 = 1 paragraph with `\n` breaks
- [ ] Row 5 = 1 paragraph with `\n` breaks
- [ ] Row 5 ends with `项目技术负责人：________________________` and `施工记录：YYYY年MM月DD日`
- [ ] ALL non-empty runs: size=11pt, ascii/hAnsi/eastAsia/cs=宋体
- [ ] Page number correct: 43 + (date − 2026-05-20).days
- [ ] Date format: `YYYY年 MM月 DD日 星期X`
- [ ] Weather format: `最高XX°C 最低XX°C 天气描述`
- [ ] File saved to correct month folder
- [ ] Content expanded from prior days' workflow (carry-forward items)
- [ ] No fabricated data (工程量, 人数, 机械数量 not provided by user)

---

## 9. References

- `references/supervision-reconciliation.md` — 监理优先逐日审核、稀疏JSON、跨日期/同日桩号查重与源文不静默修正的验证流程

- `references/format-example.md` — Row 4/5 paragraph-by-paragraph layout example
- `references/content-generation-guidelines.md` — Content generation rules, language standards, structured output format, specialized modes (桩基/基坑/主体/装修/收尾养护)
- `references/wmo-weather-codes.md` — WMO weather code to Chinese description mapping
- `references/generator-script.md` — Legacy generator script reference (fallback only)
- `references/construction-log-context.md` — Project background details
- `references/file-locations.md` — File path reference
- `references/backfill-and-gap-audit.md` — Auditing date gaps across all month folders, classifying stoppage vs omission vs isolated miss, and bracket-interpolating a single unreported day without fabricating quantities

## 现场固定配置（2026-09 起）

### 机械（固定配置，除非用户另行说明）

```
三、机械：
200型挖掘机7台、30型小型挖掘机1台，配合土方运输车辆投入现场施工作业。
```

用户于 2026-09-11 确认该配置为现阶段固定值。在此之前的日志沿用中性表述（"土方开挖、运输及XX设备按现场施工需要配置使用"），**不要回溯修改历史日志**，除非用户明确要求。

### 工序进度基线（截至 2026-09-11）

| 区域 | 状态 |
|---|---|
| 1区 | 承台及底板防水施工开始，9/11 完成约10% |
| 1-1区 | 承台模板及钢筋施工（9/5 起） |
| 1-2区 | 承台土方开挖，9/11 完成约40% |
| 2区 | 土方开挖完成、桩头破除完成、ALC预制板安装完成（9/9）、承台垫层浇筑完成（9/11），剩余后浇带部位垫层待施工 |
| 3区 | 承台土方开挖，9/11 完成约30% |

## 缺口补写规则

补写历史日志前**必须**先扫描目录确认缺口性质，不要假设"缺失=漏记"：

```python
import os, re
from datetime import date, timedelta
base = 'C:/Users/hi/Desktop/自动日志'
found = {}
for root, dirs, files in os.walk(base):
    for f in files:
        m = re.match(r'^施工日志_(\d{8})\.docx$', f)
        if m and not f.startswith('~$'):
            found.setdefault(m.group(1), []).append(os.path.relpath(root, base))
```

**历史缺口初筛（2025-11-25 ~ 2026-09-11，旧盘点共240份）：以下为当时按缺文件推定的分类，不是停工事实。后续取得逐日监理后，已发现2026-01-21至2026-02-28中多日实际施工；不得再把这整段当冬歇排除。**

- 2025-12-31 ~ 2026-01-05（6天）—— 曾推定元旦假期；2026-01-05另有疑似复制旧页的监理记录，必须审核主源，不可直接认定停工。
- 2026-01-21 ~ 2026-02-28（39天）—— 曾推定春节+冬歇，现已被多日监理施工记录否定；本次主源仅明确2月16、17日春节放假未施工，其他日期逐日审核，不向未审核日期外推。
- 2026-05-01（1天）—— 曾按节假日推定停工，仍须取得当天证据后判定。
- 2026-07-17 / 07-25 / 07-28 / 07-30（4天）—— 孤立缺口，前后正常施工，**待用户提供内容后补**
- 2026-09-10 —— 已于 2026-09-11 补齐

**已证实停工期不得编造正常施工内容。** 但上列元旦、春节等历史缺口只是曾经的推定，不能当成事实锁定。用户提供监理日志、考勤或实际施工资料后，以当日来源修正：若监理明确有施工，允许新增该日施工记录；若明确停工，可形成停工/值班记录，绝不能因旧推定而忽略新证据。本项目新提供监理资料显示1月下旬、2月多数日期及5月1日有施工，2月16—17日明确春节停工，取用时须再读当日原文。

### 倒推补写方法（仅当用户未提供内容且明确要求补写时）

当缺口日前后两天都有日志，可用区间夹逼法倒推：

1. 读取前一天（T-1）和后一天（T+1）的 Row 4
2. 找出 T+1 出现而 T-1 没有的工序 → 该工序在 T 日"开始"
3. 找出 T-1 为"完成约N%"而 T+1 为"完成"的工序 → 该工序在 T 日"持续推进"
4. 找出 T+1 存在前置条件的工序（如防水前必有基层清理）→ T 日可写前置作业

**倒推硬约束：**

- **绝不写百分比**。没有用户提供的数据，只写"开始""持续推进""完成"等定性描述
- 生成后必须向用户说明这是倒推草稿，并列出每条的推导依据，请其核对
- 若前后日志间隔超过1天，不做倒推——不确定性太大

## Scoped font variants and visual previews

用户要求“施工内容改为手写字体，发给我看看”时，按**局部字体变体**处理，而不是重生成整份日志：默认只修改 Row 4（现场情况、材料、机械、人员所在合并单元格），保留11磅字号、行高、内容及其他栏位，另存带“施工内容手写体”后缀的文件，原文件不覆盖。先确认字体已安装；中文手写效果可优先试华文行楷，不得把一次预览请求扩展成以后所有日志默认手写体。仅改现有 run 的字体及 ascii/hAnsi/eastAsia/cs 属性，避免用 cell.text 重建导致格式变化。

“看看”应尽量交付**真实文档渲染预览 + Word文件**，不只返回字体名称。用实际渲染器导出PDF后截图，检查目标栏位清晰、未截断；结构验证不能替代渲染。若导出后两页或天气单元格裁切，应把原文件也用同一渲染器导出对比，区分原有版式问题与本次修改造成的回归；未获授权不顺便改字号、页边距或其他栏位。局部截图须说明其为局部预览，不能据此宣称整份文件分页正常。

详见 `references/scoped-font-variants-and-word-preview.md`，含Windows字体发现、Word只读导出及前后差异验证步骤。

## Formatting Summary

**本用户已明确将整套施工日志转为局部手写字体版：** 后续修改该套文件时，Row 4施工内容栏和Row 5质量安全标题下面、负责人及日期上面的正文沿用华文行楷11磅；固定表头、质量安全标题及签名/日期保留原字体。不要用“所有run强制宋体”的历史清理脚本覆盖此明确要求。首次单份试样不应自动变全局偏好，但本会话后续整套转换请求已确认该版本范围。转换必须另存，原文件保持不变；整包仅收有效日期版本，不能夹旧草稿或使用说明。正文交付前另做编写旁白扫描，单纯转换字体不会清掉历史“补录/需核对”等残留。

以下为未指定字体变体时的原始模板基线：
- A4 paper (210×297mm)
- Font: 宋体 (SimSun), 11pt (22 half-points) for ALL table text Row 0—Row 5
- Every non-empty run: `ascii`/`hAnsi`/`eastAsia`/`cs` all set to 宋体
- Row 4/5: single paragraph, `\n` soft line breaks
- Line spacing and paragraph spacing preserve 2026-06-28 template settings
- Style base: `6月份/施工日志_20260628.docx` and earlier; 6/29+ files must NOT be used as style template
