---
name: content-visual-forge
archetype: general
description: 根据 PDF、网页、文章、截图、视频转写稿、单字或词表等多源内容，生成公众号封面、系列知识卡、单字卡等统一风格的视觉内容；当用户要求内容可视化、知识卡片、字卡、封面图、头图或批量卡片资产时使用。
---

# Content Visual Forge

版本：v2.3.7
定位：把多种内容源统一转化为多种视觉输出，包括公众号封面、公众号封面对、公众号文内配图、社交平台组图、系列知识卡、单字卡、词汇卡、语法卡与封面海报。

---

## 0. 核心判断

这个 Skill 的本质不是“做图”，而是：

> 先理解内容，再选择最合适的输出形式；先保证内容正确，再保证视觉统一；先判断宿主能力，再决定最终交付路径。

它融合了两条能力主线：

1. **内容卡片主线**：多源输入 → Source Lock → 输出模式路由 → 卡片脚本 / 数据填充 → 生图 / 渲染
2. **封面生成主线**：内容意图分析 → 风格路由 → 视觉概念 → 标题排版策略 → 预览 / 正式封面交付
3. **平台社交图主线**：平台规格 → 内容压缩阶梯 → 页面角色编排 → 多 frame 工程化渲染 / 质检

---

## 1. 能做什么

### A. 输出类型（Template Families）

1. `cover-card`：公众号封面 / 头图 / 首图 / 海报封面
2. `wechat-inline-image`：公众号文内配图 / 情绪过渡图 / 分节图 / 尾图
3. `social-card`：小红书 / Rednote / 社交平台 3:4 组图
4. `knowledge-carousel`：系列知识卡 / 方法论图解 / 长文拆页
5. `character-card`：单字学习卡
6. `vocabulary-card`：词汇卡
7. `grammar-card`：语法点卡
8. `phrase-card`：短语 / 句型卡

### B. 支持的输入源

- PDF
- 网页 URL / 网页正文
- 一段文字 / 长文 / Markdown
- 视频字幕 / 转写稿
- 音频转写稿
- 图片 / 截图 / 信息图
- PPT / Slides
- 单字 / 词表 / 结构化表格
- 多源混合材料

---

## 2. 非协商硬规则

1. **No Source Lock, No Generation**：没有完成 Source Lock，不允许直接生成图片。
2. **Current Source First**：当前输入源优先于历史示例。
3. **Output Mode Must Be Declared**：必须先确定输出模式。
4. **Execution Mode Must Be Declared**：必须先确定执行路径。
5. **Content Fidelity First**：内容忠实度优先。
6. **Anti-Plagiarism By Design**：参考图只能参考风格，不复制版式与装饰组合。
7. **Chinese Legibility First**：中文标题或关键文字可读性优先。
8. **Production Cover Defaults to Background + Typography Overlay**：正式封面默认优先采用“无文字背景图 + 后期标题排版”。
9. **Small Chinese Text Should Not Be Delegated to Image Models by Default**：小字号中文默认不交给图像模型。
10. **No Unrequested Exam Labels**：除非用户明确要求，具体卡片内容不自动加入考试名或等级标签。
11. **Engineering Rendering For Production**：批量、商用、文字必须准确时，优先切换工程化渲染。
12. **Painter Style Atlas Uses Local Snapshot**：画家风格图鉴默认读取本地 snapshot，只能转译为风格因子，不默认仿写具体艺术家。
13. **Editorial Systems Over Template Copying**：借鉴外部设计项目时只吸收网格、主题色、字号阶梯和质量门禁等方法，不复制模板、类名体系或素材。
14. **Platform Specs Before Social Cards**：社交平台组图和公众号封面对必须先声明平台尺寸、输出数量、安全区和命名规则。
15. **WeChat Cover Pair Is Not Cropping**：公众号 `21:9` 主封面和 `1:1` 方封面必须分别构图；方封面使用短标题，不把主封面硬裁或硬塞长标题。
16. **Design Enhancement Has Fallback**：设计增强必须先使用默认设计基线；额外设计能力只能补充视觉方向、token、模板和评审，不得成为阻断条件。
17. **Risk Action Blacklist Must Be Checked**：交付前必须检查 `references/config/risk-action-blacklist.md`；命中时回到对应路由、切换工程化渲染或停止交付。
18. **External Assets Need Source Records**：HTML / CSS 背景图、纹理、照片、logo 或产品图必须按 `references/config/asset-source-policy.md` 记录来源与授权；授权不明时改用 CSS 纹理、抽象视觉或请求用户补充素材。

---

## 3. 两层路由

### 第一层：输出模式路由（Output Mode Router）

根据用户目标与内容结构，选择：
- `cover-card`
- `wechat-inline-image`
- `social-card`
- `knowledge-carousel`
- `character-card`
- `vocabulary-card`
- `grammar-card`
- `phrase-card`

### 第二层：执行路径路由（Execution Mode Router）

根据宿主能力和交付要求，选择：
- `preview_image`：快速预览图
- `production_cover`：正式封面
- `background_then_layout`：先背景图，后排版
- `direct_image_preview`：直接生图预览
- `prompt_package`：仅输出提示词包
- `engineering_rendering`：模板渲染 / 程序排版

---

## 4. 固定执行流程

### 阶段 0：Input Type Router
识别输入源。

### 阶段 1：Source Lock
锁定内容源，生成 `Content Source Brief`。

### 阶段 2：Output Mode Router
判断应该做封面、系列知识卡还是单字卡等。

### 阶段 3：Execution Mode Router
判断是快速预览、正式封面、提示词包还是工程化渲染。

### 阶段 4：Content Analysis
提炼内容骨架、传播角度和可视化机会点。

### 阶段 4A：Content Compression Ladder（社交卡 / 长文拆页时必选）
将来源压缩为 `core_claim`、`viewer_promise`、`section_map`、`page_hooks`、`body_fragments` 与 `visual_evidence`，避免把全文塞进图片。

### 阶段 4B：Style Atlas Routing（可选）
当用户要求画家 / 流派 / 图鉴风格，或当前输出需要更精确的视觉风格锚点时，读取本地 `assets/style-atlas/qiaomu-style-atlas.snapshot.json`，选择风格家族或条目，并转译为 `style_factors`、`prompt_style_phrase` 与 `blocked_mimicry`。

### 阶段 4C：Design Enhancement Routing（可选）
当用户要求美化、设计方向探索、模板升级或设计评审时，先使用 `design-principles` 与 `design-enhancement-routing` 生成受控的 `design_intent`、`visual_tokens`、`layout_variants`、`css_update_notes` 与 `design_qa`。额外设计能力只做增强，不得替代内容路由和事实门禁。

### 阶段 5A：Card Script / Data Fill
- `knowledge-carousel` 进入分页脚本
- `social-card` 进入平台规格、页面角色和社交组图脚本
- `character-card` 等进入结构化字段填充

### 阶段 5B：Cover Concept
- `cover-card` 进入内容意图分析、风格路由、视觉概念、版式策略
- 如使用画家 / 流派 / 风格图鉴，先转译为风格因子与版权边界

### 阶段 6：Prompt / Render Package
生成每页 / 每卡 / 封面的提示词或渲染包。

### 阶段 7：Batch Generation / Rendering
批量生成或模板渲染。

### 阶段 8：Quality Gate
执行内容忠实度检查、风险动作黑名单扫描与视觉质量门禁。

### 阶段 9：Retry / Production Upgrade
不合格内容单独重试；商用需求升级到工程化渲染。

---

## 5. 视觉系统

### A. 知识卡系统
- 画幅：3:4
- 奶油白 / 米白背景
- 深墨绿、鼠尾草绿、珊瑚橙
- 书卷感、编辑感、信息层级清晰

### B. 单字卡系统
- 画幅：3:4
- 童趣、贴纸感、启蒙友好
- 模块化信息区：主字 / 拼音 / 义项 / 常用词 / 例句 / 记忆提示
- 默认不写考试名或等级标签

### C. 公众号封面系统
- 场景优先、标题可读、留白克制
- 正式封面优先无文字背景图 + 后期标题排版
- 预览图可直接带标题，但不视为最终商用品质交付
- 要求封面对时，`21:9` 主封面与 `1:1` 方封面分别构图，方封面使用短标题

### D. 社交平台组图系统
- 默认 3:4，`1080 x 1440`
- 1 张封面 + 4-8 张内容页
- 每页一个观点，页面角色要有变化
- 截图 / 产品图 / 照片是证据层，不是装饰
- 信息过载时先压缩内容，不缩小到移动端不可读

---

## 6. V2.1 起新增闭环

### A. 公众号文内配图模式

`wechat-inline-image` 专门处理公众号正文中的图，不等同于小红书知识卡。

默认规则：

- 不使用右上角页码胶囊
- 不强制写大标题
- 不强制写要点列表
- 不默认生成 6 张
- 文字量极低，必要时只保留一句短句
- 重点服务阅读节奏、情绪过渡、段落分隔和结尾收束

### B. 配图数量判断

在生成公众号图片前，必须先判断文章类型：

- 教程 / 方法论：封面 + 3–6 张结构图
- 观点文章：封面 + 2–3 张文内重点图
- 影评 / 散文 / 情绪随笔：封面 + 1–2 张氛围图 + 1 张尾图
- 短文：只生成封面或封面 + 1 张尾图
- 产品文：封面 + 功能亮点图 + 使用场景图

详见：`references/config/wechat-image-count-rules.md`

### C. Run Log

每次正式执行都应生成运行记录，包含：

- 输入源
- Source Lock 摘要
- 输出模式
- 执行模式
- 生成物列表
- 质检结果
- 重试建议
- 是否建议工程化渲染

详见：`references/run-log/RUN_LOG_SPEC.md`

### D. 工程化渲染骨架

当前版本提供可落地的模板骨架：

- `assets/render-engine/html-templates/`
- `assets/render-engine/css/`
- `assets/render-engine/data/`
- `scripts/render-engine/`

用于后续把“策略闭环”升级到“生产闭环”。

---

## 7. 推荐使用方式

### 生成公众号封面
“使用多源内容视觉卡片 Skill，根据这篇文章生成公众号封面，先做 Source Lock，再走 cover-card + production_cover 路径。”

### 生成系列知识卡
“使用多源内容视觉卡片 Skill，根据这份 PDF 生成 8 页 3:4 系列知识卡，先做 Source Lock，再走 knowledge-carousel 路径。”

### 生成单字卡
"使用多源内容视觉卡片 Skill，为汉字'穿'生成一张单字学习卡，不要出现考试名称标签。"

### 生成小红书/Rednote 社交组图
"使用多源内容视觉卡片 Skill，根据这篇文章生成一组小红书 3:4 社交卡，先做 Source Lock，再走 social-card 路径，使用内容压缩阶梯处理长文。"

### 生成公众号封面对
"使用多源内容视觉卡片 Skill，为这篇文章生成公众号封面对（21:9 主封面 + 1:1 方封面），主封面使用完整标题，方封面使用短标题，分别构图。"

---

## 8. 主要目录

- `references/`：工作流、输出族、输入适配器、配置、Schema、运行记录规范与封面引擎规则
- `assets/`：提示词模板、分页模板、封面提示词、示例资产与工程化渲染静态模板
- `scripts/`：可执行辅助脚本
- `agents/`：OpenAI agent 元数据
- `evals/`：benchmark 与 eval 定义
- `tests/`：回归测试与内部测试报告

---

## 9. 版本历史

详见 `CHANGELOG.md`
