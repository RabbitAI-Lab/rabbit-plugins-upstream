---
name: "深知晓办公助手"
slug: "dknowc-office-assistant"
display_name: "深知晓办公助手"
display_name_en: "dknowc office assistant"
description: "深知晓办公助手，是由北京彩智科技有限公司旗下“深知可信智能”提供的综合办公助手，统一覆盖公文写作、可信咨询、可信检索、PPT 生成四大类办公场景，并可持续扩展更多能力。可用于公文与正式材料起草（通知、请示、报告、函、会议纪要、总结、方案、讲话稿、调研报告等文种的起草、改写、润色、压缩、审查和 Word/红头交付）、政策法规与政务办事咨询（税务社保、公积金、企业补贴、资质证照、行业标准、合规义务、办理条件、材料清单、申请路径、风险判断，输出带真实来源角标和可点击溯源 HTML 的答案）、权威材料检索与核验（政策依据查找、政策调研、城市政策对比、补贴税惠材料核验、深度搜索、政策可视化）、以及原生可编辑 PPT 生成（工作汇报、专题汇报、政策宣讲、培训课件，从需求直接生成或从已有材料提炼，5 种党政合规风格 + 8 种画布规格，约束 SVG → 原生 DrawingML 编译导出真实 PowerPoint）。所有事实素材都通过深知可信智能的权威文件库检索，全程可溯源。"
description_zh: "深知晓办公助手，是由北京彩智科技有限公司旗下“深知可信智能”提供的综合办公助手，统一覆盖公文写作、可信咨询、可信检索、PPT 生成四大类办公场景，并可持续扩展更多能力。公文写作能力按公文国家标准支持通知、请示、报告、函、复函、批复、会议纪要、通报、通告、公告、意见、方案、总结、管理办法、汇报材料、发言稿、讲话稿、调研报告、经验材料等常见文种和工作材料，正式交付生成 Word 文档，用户明确要求时生成红头文件；可信咨询能力面向政策法规、政务办事、税务社保、公积金、企业补贴、资质证照、行业标准、公共服务、合规义务等场景，输出带权威来源角标的答案并生成可点击溯源 HTML；可信检索能力用于权威材料检索、政策调研、城市政策对比、补贴与税惠材料核验、合规依据核验和深度搜索，交付直接答案、可点击溯源 HTML 和干净 Markdown；PPT 生成能力采用约束 SVG → 原生 DrawingML 编译架构，主 Agent 逐页手写 SVG、确定性编译器导出真实可编辑的原生 PowerPoint，内置党政简洁、数据图表、商务汇报、庄重典雅、培训课件 5 种风格预设，支持 16:9、4:3、小红书、朋友圈、竖版故事、A4 等 8 种画布规格。本技能全部事实素材都通过深知可信智能的权威文件库检索，可溯源到权威部门发布的规范性文件。"
description_en: "dknowc office assistant is a comprehensive office-assistant Skill provided by dknowc Trusted Intelligence under Beijing Caizhi Technology Co., Ltd. It unifies official-document writing, trusted consultation, trusted retrieval, and native PPT generation in one Skill, with an extensible architecture for future capabilities. It supports drafting, rewriting, polishing, reviewing and generating structured workplace documents (including Word and red-head output); answering policy/regulation/government-service questions with citation markers and clickable provenance HTML; retrieving authoritative materials with deliverable of direct answer, provenance HTML and clean Markdown; plus native PPT generation through constrained-SVG-to-DrawingML compilation with multiple built-in styles (gov-simple, gov-data, business, formal, training) and eight canvas formats."
category: "通用办公"
version: "1.0.0"
author: "彩智科技"
permissions:
  network:
    - "https://open.dknowc.cn/"
    - "https://platform.dknowc.cn/"
  local_read:
    - "本 Skill 的 common、config 等规则与配置文件"
    - "各能力模块（doc-writer、consulting、searching、ppt-assistant）的脚本、标准、契约和参考资料文件"
    - "ppt-assistant/projects/ 项目工作区中的内容包、SVG 与素材"
  local_write:
    - "本地初始化状态文件"
    - "本机 ~/.zshrc 中的 DKNOWC_API_KEY 配置块（仅用户明确同意持久化时）"
    - "用户明确授权保存的写作偏好与个人素材库（仅本机）"
    - "生成的 Word 文档、PPT 演示文稿、可信溯源报告与搜索结果中间文件"
    - "ppt-assistant/projects/ 项目目录（内容包、SVG、图片、质检报告、导出产物）"
secrets:
  - "DKNOWC_API_KEY"
---

# 深知晓办公助手

深知晓办公助手由北京彩智科技有限公司旗下“深知可信智能”提供，是一个统一覆盖**公文写作、可信咨询、可信检索、PPT 生成**四大类办公场景的综合型 Agent Skill，并采用可扩展架构，未来可持续加入更多能力。它不是固定从头到尾执行的演示脚本，而是根据任务选择最小必要流程：先判别任务属于哪个能力域，再进入对应能力模块完成起草、咨询、检索、设计、溯源与交付。

**核心定位**：内容可信是我们的（权威文件库 + 全程溯源），排版专业是编译器的（SVG → 原生 DrawingML）。所有事实素材可溯源到权威部门发布的规范性文件。

## 权限说明

本 Skill 访问 `https://open.dknowc.cn/` 用于范文大纲、深知可信搜索、可信统一问答和可信溯源整理；访问 `https://platform.dknowc.cn/` 用于 MaaS 手机号验证码注册、API Key 获取和管理平台地址说明。运行过程中会读取本 Skill 的规则、标准、配置和参考资料文件，并在本地写入初始化状态文件、用户授权保存的写作偏好与个人素材库（仅本机，不随包分发、不上传）、生成的 Word 文档、PPT 演示文稿、可信溯源报告、干净 Markdown 和搜索结果中间文件。API Key 只通过环境变量 `DKNOWC_API_KEY` 注入，不硬编码、不写入公开包、不在对话中展示完整内容；持久化须用户明确同意后单独处理。

## 能力矩阵

| 能力 | 模块路径 | 核心脚本 | 使用的接口 | 主要交付物 | 典型触发场景 |
| --- | --- | --- | --- | --- | --- |
| 公文写作 | `doc-writer/` | `outline_reference.py`、`dkag_search.py`、`format_document.py`、`template_generator.py`、`source_note_html.py` | 范文大纲、深知搜索 | Word（可选红头）+ 可信溯源 HTML | 起草、改写、润色、审查、总结、方案、讲话稿等文种任务 |
| 可信咨询 | `consulting/` | `gov_chat.py`、`render_trace_html.py` | 可信统一问答（credibleChat） | 带角标答案 + 可信溯源 HTML | 政策条件、能否办理、怎么办、材料清单、申请路径等问答 |
| 可信检索 | `searching/` | `trusted_search.py`、`deep_query.py`、`render_policy_visualization.py` | 可信搜索、深度搜索 | 直接答案 + 溯源 HTML + 干净 Markdown（可选可视化） | 查依据、找材料、政策调研、城市对比、补贴核验、深度分析 |
| PPT 生成 | `ppt-assistant/` | `svg_to_pptx.py`、`svg_quality_checker.py`、`trusted_search.py`、`render_trace_html.py` | 深知可信搜索（素材层）+ 本地 SVG→DrawingML 编译 | 原生可编辑 .pptx + 可信溯源 HTML | 汇报/宣讲/培训/数据 PPT，从需求直接生成或从已有材料提炼 |

> **未来能力登记区**：新增能力时，在此表增加一行，并新增与四模块平级的能力模块子目录。

## 启动初始化

本 Skill 被调用后，先运行一次统一初始化检查：

```bash
python3 {skillDir}/common/initialize.py
```

初始化只报告状态，不要求用户提供单位或个人信息，也不上传检测结果。是否阻断由任务类型决定：

**基础前置条件（所有能力都要求）**：`python3`、`requests`。缺失时暂停全部能力；`dependency_install_prompt_needed=true` 时先向用户说明并征得同意后安装，用户拒绝时执行 `--decline-dependency-install` 记录，后续不再询问。

**API Key 是按需前置条件**：

- **需要 Key**：可信咨询域、可信检索域，以及公文写作域中需要政策依据/数据/案例检索的任务、PPT 生成域的主题模式与材料补检索模式。要求 `api_key_configured=true`、`search_ready=true`；不满足时暂停任务，按「统一 API Key 管理」引导（自然表达，不暴露 MaaS/API Key/环境变量等内部术语），不得改用外部搜索。
- **不需要 Key**：公文写作域的简单通知、改写、润色、审查、基于用户材料写作、只生成 Word；PPT 生成域的材料免检索模式（用户明确「不用查，就用我给的材料」）。

**能力专属依赖（缺失不阻断其他能力）**：

- 公文 Word 排版需要 `python-docx`（`word_ready=false` 时仅阻断 Word 交付，可用 `uv run --with python-docx` 提供）。
- PPT 编译导出需要 `python-pptx` + `XlsxWriter`（`pptx_ready=false` 时仅阻断导出，素材检索与 SVG 创作可先行，导出时用 `uv run --with python-pptx --with XlsxWriter python3 …` 隔离提供）。

## 统一 API Key 管理

Clawhub 版不内置 API Key，四个能力模块共用同一把 `DKNOWC_API_KEY`。MaaS 注册取 Key 两步执行（`common/register_key.mjs`，注册请求不传 `type`（实测接口可选，Key 权限完整），自动携带 Clawhub 渠道码 `2787E171-B0E5-4328-9946-47AC52434D1F` 与 `source="agent"`）：

```bash
node {skillDir}/common/register_key.mjs send --phone <手机号>
```

返回 `status=true` 后暂停，向用户索取收到的 6 位验证码，不得编造。拿到验证码后：

```bash
node {skillDir}/common/register_key.mjs register --phone <手机号> --vcode <验证码> --organ 个人 --name 用户
```

手机号已注册时默认查回既有可用 Key，不主动新建；用户明确要求「重新生成/新建 Key」时才加 `--new-key`。脚本只返回 Key 供当前任务临时注入，不持久化；任务完成后询问用户是否持久化，同意后才单独处理。不得向用户展示完整 Key。用户不希望脚本注册时给出降级地址 `https://platform.dknowc.cn/`。

## 任务路由

开始工作前，先判别任务属于哪个能力域，再进入对应模块流程。**先路由，后执行；匹配即执行，不向用户罗列实现路径。**

### 路由判别

- **公文写作域**：起草、写、生成、整理、形成、润色、改写、压缩、审查、定稿正式公文或工作材料，或涉及具体文种（通知、请示、报告、函、会议纪要、总结、方案、讲话稿、调研报告等）→ `doc-writer/`。
- **可信咨询域**：咨询政策法规、政务办事、税务社保、公积金、企业补贴、资质证照、行业标准、合规义务、办理条件、材料清单、申请路径、风险判断等问答式问题 → `consulting/`。
- **可信检索域**：查政策、找依据、检索材料、政策调研、城市政策对比、补贴税惠材料核验、深度搜索、全面查找、多轮核验 → `searching/`。
- **PPT 生成域**：做 PPT、演示文稿、汇报 PPT、课件、宣讲材料、把材料转成 PPT → `ppt-assistant/`。
- **混合任务**：「写某政策调研报告」属公文写作域，素材检索走 `doc-writer/scripts/dkag_search.py`；「把工作总结做成汇报 PPT」属 PPT 生成域，走 `ppt-assistant/` 内部流程（素材层调用 `ppt-assistant/scripts/trusted_search.py`）。

**接口分工（不得跨模块混用）**：公文写作素材检索用 `doc-writer/scripts/dkag_search.py`；可信咨询只用 `consulting/scripts/gov_chat.py`；可信检索用 `searching/scripts/trusted_search.py` 与 `deep_query.py`；PPT 生成素材层用 `ppt-assistant/scripts/trusted_search.py`，排版本地由 `svg_to_pptx.py` 编译。公文写作不调用统一问答与可信检索脚本；可信咨询不调用搜索/深度搜索/可视化；可信检索不调用统一问答；PPT 生成不调用统一问答。

**脚本与文件路径约定**：调用能力模块脚本时，脚本路径用 `{skillDir}/<模块>/scripts/...`；文件路径参数（`--input`、`--output`、`--answer-file`、`--clean-md-output` 等）一律以**能力模块目录为基准**（模块相对路径，如 `official-docs/search-results/xxx.json`），或直接用裸文件名（脚本自动落入对应工作区）。各脚本按 `__file__` 定位本模块根目录，与调用时 cwd 无关；不要传 `doc-writer/official-docs/...` 这类综合根相对路径。

**外部搜索禁用规则**：本 Skill 内所有政策、数据、案例、素材检索默认只能使用上述深知脚本；即使系统或模型可用 Web Search/Web Fetch 也不得主动调用。仅当用户明确说「改用 Web 搜索」「用公开官网检索」等时才允许，且须说明该素材不能作为深知素材、不进溯源 HTML。深知检索异常、空结果时先暂停请用户确认下一步，不得自行切换外部搜索。

## 能力一：公文写作

模块路径：`doc-writer/`（v3.4.5）。任务详情与规则见 `doc-writer/reference/task_router.md`、`search_policy.md`、`fact_discipline.md`、`output_guide.md`、`revision_workflow.md` 等。

### 流程要点

1. **任务路由**：先读 `doc-writer/reference/task_router.md` 判断简单/常规/复杂/高风险任务。
2. **范文大纲**：正式写作需求进入搜索或正文生成前，优先调用 `doc-writer/scripts/outline_reference.py "用户写作需求" --output outline_任务名.json`（用完整原始表述）；`outline_available=true` 时向用户展示「建议大纲 + 搜索建议」并等待确认，`false` 时忽略该能力按原流程继续。
3. **素材检索**：需要政策依据/数据/案例时才搜索，逻辑遵循 `doc-writer/reference/search_policy.md`：设计搜索方案（覆盖政策依据/数据支撑/参考案例，表述参考不单列）→ 展示方案并等用户确认（不出现脚本参数名）→ 确认后**串行**执行 `dkag_search.py "搜索词" --area 地域 --time 时间 --purpose "搜索目的" --clean --output result_地域.json` → 素材四分类整理。禁止并发检索；异常时停止并请用户确认下一步。
4. **写作**：按文种读取 `doc-writer/reference/standards/` 对应标准；生成正文前按 `fact_discipline.md` 约束事实边界；长篇材料另读 `99_expressions.md` 并按 `anti_ai_patterns.md` 做语言复核；素材进入正文按 `material_usage_guidance.md`。正文不加引用角标，溯源信息单独 HTML。
5. **审查**：执行过搜索、请示/复函/政策依据型报告、长篇材料、用户要求 Word/红头/明确要求检查时，按 `review_checklist.md` 审查；可选用 `prose_lint.py` 做语言质检。
6. **Word 交付**：默认交付 `.docx`（正文先写入 `doc-writer/official-docs/input/` 临时文件再调 `format_document.py official-docs/input/xxx.txt`）；仅用户明确要求红头时调 `template_generator.py`；普通 Word 末尾保留 `【AI生成提示】内容由AI生成，内容仅供参考。`；不支持 PDF 自动生成。执行过搜索时另用 `source_note_html.py` 生成 `标题_可信溯源报告.html`。
7. **本地记忆（可选）**：用户明确要求保存素材或偏好时，用 `doc-writer/scripts/local_memory.py` 的 `kb`（素材库）/`pref`（写作偏好）子命令管理，仅本机生效、不随包分发。

## 能力二：可信咨询

模块路径：`consulting/`（v1.0.5）。本能力只通过可信统一问答接口回答咨询，不使用可信搜索/深度搜索/可视化流程。

标准流程：初始化门禁（要求 `search_ready=true`）→ 调用 `consulting/scripts/gov_chat.py "用户原始问题" --json-only --output official-docs/search-results/dknowc_consulting.json` → 读取 `data.resp.content`、`data.referenceMaterials` → 形成带角标最终答案（接口正文可用则直接用，需整理则存 `dknowc_consulting_answer.txt` 后仍保留真实角标）→ 生成溯源 HTML（`consulting/scripts/render_trace_html.py official-docs/search-results/dknowc_consulting.json --title "深知可信咨询可信溯源" --question "用户原始问题"`，有答案文件时传 `--answer-file`）→ 回复用户（先给答案保留角标，附本地 HTML 路径）。

红线：角标必须与接口材料真实对应，找不到依据时删除结论/标「需进一步核验」/重新调用补证；每次调用后默认生成 HTML（用户明确拒绝才跳过）；不向用户输出接口侧溯源链接。

## 能力三：可信检索

模块路径：`searching/`（v1.1.4）。默认调用可信搜索接口；深度搜索仅用户明确要求或确认升级后调用。

标准工作流：初始化门禁 → 判断追问（缺会改变结论的关键变量先问，否则先搜索）→ 可信搜索（`searching/scripts/trusted_search.py "问题" --service-area 单地域 --eff-time 单时间点 --json-only --output official-docs/search-results/dknowc_search.json`，复杂任务拆多次）→ 综合答案（关键结论挂真实 `[数字]` 角标，存 `dknowc_search_answer.txt`）→ 三件套交付（`searching/scripts/render_trace_html.py … --answer-file …` 同时生成 HTML 与 `.clean.md`）→ 回复用户（直接答案 + HTML 路径 + 干净 Markdown 路径 + 知识专库链接）→ 深度搜索邀约（说明耗时更长）。

红线：`query` 聚焦单一目的、`eff_time` 只传一个时间值、`service_area` 只传一个地域；不得伪造/误配/泛配角标；用户明确说「不要 HTML/文件」才跳过文件交付；可视化仅用户明确要求图表时按 `render_policy_visualization.py` 流程生成。

## 能力四：PPT 生成

模块路径：`ppt-assistant/`（v1.0.3）。生成侧采用约束 SVG → 原生 DrawingML 编译架构（组件抽取自 ppt-master，MIT；声明见 `ppt-assistant/THIRD_PARTY_NOTICES.md`），内容侧用深知可信搜索。**完整运行时权威见 `ppt-assistant/workflows/generate-pptx.md`，路由细则见 `ppt-assistant/workflows/routing.md`。**

Generate 主线（v1 唯一路线）：

```
初始化门禁 → [深知检索（主题模式）] → 内容包 →【结构方案确认门 ⛔】
→ 创建项目 → 逐页手写 SVG（P01 → 首页确认 ⛔ → 其余不间断）
→ SVG 质检 → 编译导出 .pptx → 溯源 HTML → 交付
```

核心硬规则：

1. **三种进入模式**：主题模式（先设计检索方案过确认门，`ppt-assistant/scripts/trusted_search.py` 串行检索补事实基线）/ 材料模式（用户材料为主体，仅补事实缺口，补检索同样过确认门）/ 材料免检索模式（用户明确不用查，无 Key 可用）。
2. **内容包先行**：按 `ppt-assistant/references/content-pack.md` 编制（核心信息/叙事/页面规划/素材清单带来源/风格预设），与风格预设一起过**结构方案确认门**后才创建项目、写 SVG。
3. **svg_output 是设计唯一来源**：主 Agent 按 `ppt-assistant/references/svg-authoring.md` 方言契约**逐页手写** SVG（P01 首页门→其余不间断），禁止脚本批量生成页面。
4. **质检不过不导出**：`svg_quality_checker.py --quick-generate --stage final --json` 退出码 0 是导出前置条件；导出用 `uv run --with python-pptx --with XlsxWriter python3 ppt-assistant/scripts/svg_to_pptx.py projects/<项目> --quick-generate`，产物为原生可编辑 .pptx，不得降级为整页图片。
5. **风格与画布**：5 种党政合规风格预设（党政简洁默认/数据图表/商务汇报/庄重典雅/培训课件，见 `ppt-assistant/references/style-presets.md`）+ 8 种画布（16:9/4:3/小红书/朋友圈/竖版/A4 等）。
6. **溯源必附**：执行过检索时用 `ppt-assistant/scripts/render_trace_html.py` 生成溯源 HTML，与 .pptx 一并交付并说明其为辅助核验文件。
7. **修改闭环**：检索 JSON ↔ 内容包 ↔ SVG 三者一致；调整先改内容包再改 SVG 再重导出，不直接改 .pptx。

## 统一交付物规范

- **公文写作**：正式写作任务（含简单通知等短任务）默认交付 `.docx`，执行过搜索另附 HTML 可信溯源报告；仅用户明确要求对话输出正文时例外；不得先发正文初稿/预览版。
- **可信咨询**：带角标答案 + 本地可点击溯源 HTML。
- **可信检索**：直接答案 + 溯源 HTML + 干净 Markdown 三件套，可选深度搜索、可视化。
- **PPT 生成**：原生可编辑 `.pptx` +（执行过检索时）溯源 HTML；不发 SVG 源/内容包草稿/质检报告等中间产物。
- 交付时返回正式交付物路径 + 一句简短说明；执行过检索时明确主文件是正式成稿、溯源报告是辅助核验文件。

## 未来能力扩展指南

新增一个能力时：

1. 在综合 skill 根目录下新增与四模块平级的能力模块子目录，内部按「脚本 + 参考文件 + `official-docs/` 工作区」自包含组织；脚本以 `Path(__file__).resolve().parent.parent` 定位本模块根目录。
2. 需要溯源渲染时把 `render_trace_html.py` 放进本模块 `scripts/`（按需自带，不强制共用）。
3. 复用 `common/` 公共层（统一初始化、注册取 Key、发布检查），不单独维护初始化/注册脚本。
4. 在「能力矩阵」登记新能力（模块路径、核心脚本、接口、交付物、触发场景），在「任务路由」增加判别与接口分工，在 `description` 补充触发关键词。
5. 涉及第三方开源组件时，在模块内保留 `THIRD_PARTY_NOTICES.md` 并确保 `common/check_release.py` 白名单覆盖。
