---
name: oss-workflow
description: penguin-oss-suite 四层分型的路由层——套件唯一入口，唯一持有场景触发词。任何涉及 GitHub 协作的任务（提 PR、处理 issue、commit、push、建仓、改 README/CHANGELOG/docs、fork 同步）MUST 先加载本 skill；管线/规则/独立层 skill 不持有场景触发词，由本层调度。加载后从 references/checklists/s1–s5.md 实例化 CHECKLIST.md，每步内嵌要读的 skill 文件路径，agent 按清单逐步打勾执行。跳步 = 违规交付。触发词：任何包含 PR/issue/push/commit/建仓/README/CHANGELOG/docs/开源/fork 的指令。
metadata:
  openclaw:
    requires:
      bins: [git, gh, python, pwsh]
---

# oss-workflow：路由层（唯一入口）v3

## 0. 触发自检与四层分型

**你在处理任何涉及 GitHub 协作的任务之前，必须已完成本节自检。**

```
自检三问：
1. 这个任务会往 GitHub 推送任何东西吗？（PR/commit/push/issue 回复）
2. 这个任务会修改仓库的任何文档吗？（README/CHANGELOG/CONTRIBUTING/docs）
3. 这个任务涉及开源仓的任何协作动作吗？（fork/star/comment/review）

任何一个「是」→ 你现在正在读的应该是 oss-workflow，而不是自己动手。
如果你已经动手了 → 停下，从 §1 开始。
```

**为什么强制**：S2 实战教训（dsh-market#755, 2026-09-28）——agent 绕过 skill 直接干活，导致：AI 标识加错、正文语言错、markdown 被 PowerShell 反引号吃掉、未审直推。四错全部因为「会修 issue」的模式匹配优先了「该读 skill」的规则查找。**skill 躺在目录里不会自己跑**——本 skill 的职责就是把它们摊开在你面前。

**四层分型（v3 重组契约，诊断依据见套件 `corpus/org-sweep/drafts/ARCH-AUDIT.md`）**：

| 层 | 成员 | 职责 |
|---|---|---|
| 路由层 | oss-workflow（本 skill） | 唯一入口；唯一持有场景触发词；生成并追踪 CHECKLIST |
| 管线层 | oss-contribution（唯一管线 owner）+ oss-dev（P4–P6 实现段规则附件） | P0–P9 流程、门禁、证据 ID |
| 规则层 | oss-voice（文档风格，§7 多语言管理——原 oss-i18n）、oss-persona（声纹库；lyingbug 全卡为 references 参照数据） | 领域规则与声纹数据 |
| 独立层 | penguin-oss-ops、oss-security、oss-scaffold | 方法论/安全/建仓，各自独立触发、自带负向边界 |

场景触发词只在路由层；其余层被调度时才读。原 oss-i18n、lyingbug 两个独立 skill 已分别并入 oss-voice §7 与 oss-persona references（v0.2.1 重组）。

## 1. 场景识别与清单生成

识别任务属于哪个场景，然后**立即生成任务清单**：

| 场景 | 触发信号 | 清单模板 |
|---|---|---|
| S1 梳理 | 「帮我梳理这个仓库」「看看这个项目」 | references/checklists/s1.md |
| S2 提 PR / 修 bug | 「处理 issue」「提 PR」「修 bug」「fix」 | references/checklists/s2.md |
| S3 文档维护 | 「更新 README」「改 CHANGELOG」「文档整理」 | references/checklists/s3.md |
| S4 长期协作 | 「同步 fork」「跟进上游」「定期维护」 | references/checklists/s4.md |
| S5 建仓 | 「从 0 建仓」「新项目」「scaffold」「初始化」 | references/checklists/s5.md |

**清单生成动作**（确定性，非可选）：

```
1. 在工作区创建 .oss-task/<任务ID>/CHECKLIST.md（任务ID = issue 号或日期+关键词）
2. 从对应模板复制 + 填入任务特定信息（目标仓 URL、issue 号、分支名）
3. 清单文件创建后，本 skill 的工作就是追踪它——每完成一步打勾，每步的 gate 不过就停

**时序与证据约束（2026-09-29 #752 实战教训）**：
- 清单必须在**首个业务动作之前**实例化——先有清单再干活，不是干完活补清单
- 每步打勾必须带证据指针（命令输出摘要 / 文件路径 / PR 链接），无证据不打勾
- 一次落盘全部 [x] = 事后补勾 = 违规交付，等同跳步
- 勾了没做 = 比晚勾更重的违规（2026-09-29 三场实测：勾「读 oss-dev §4」但全程零读取）——真实性优先于时序
```

## 2. 执行规则

### 2.1 主 agent 执行（简单任务）

- 逐项执行 checklist，每步先读该步标注的 skill 文件路径的**相关章节**（不是全文，按需读）
- 打勾：把 `- [ ]` 改为 `- [x]`，同轮写入
- **Gate 步骤**（标有 🛑 的）必须停下来等作者确认，不能自行通过

### 2.2 子代理执行（复杂任务）

委派子代理时，prompt **只包含三样东西**：

```
1. 任务描述（一段话）
2. Checklist 路径（.oss-task/<ID>/CHECKLIST.md）
3. 指令：「按 checklist 逐步执行。每步标注的 skill 文件路径必须实际读取相关章节再行动。每步完成后打勾。Gate 步骤（🛑）停下来在返回中说明等待确认。」
```

**禁止**：主 agent 把 skill 规则摘要后塞进子代理 prompt——转述会丢细节（#755 的 AI 标识就是这么丢的）。子代理自己读一手规则。

### 2.3 完成判定

Checklist 全部打勾 → 交付报告（含 checklist 文件路径供审计）。
有任何未打勾项 → 列出哪步卡住 + 原因，**不算完成**。

## 3. 依赖（分级账本：核心缺失硬停，推荐缺失警告继续）

### 3.1 分级原则

- **核心必装**：缺失 → 硬停，先安装再启动任务，不降级。
- **流程必装**：对应场景缺失 → 该场景硬停；其他场景不受影响。
- **推荐**：缺失 → 警告并继续，交付物标注降级（如「未过 humanizer 润色」），与 oss-contribution「降级不是惩罚，是准确交付」的口径对齐。oss-contribution 侧红线（R13/R15/R16）与其 §8.2 强制降级表仍按其管线裁决。
- **可选**：缺失正常继续，用到对应场景时再提示。

### 3.2 依赖账本

| 依赖 | 级别 | 用途 | 需要 API Key | 检查方式 |
|---|---|---|---|---|
| superpowers（systematic-debugging 等） | 核心必装 | P4–P6 代码侧工程门禁 | 不需要 | skill 目录存在 |
| ocr CLI | 核心必装 | P7 确定性缺陷检测 | 需要：OPENAI_API_KEY 或 ANTHROPIC_API_KEY | `ocr --version` + 环境变量在位 |
| github-contributor | 流程必装（S2 非中文/非自有仓） | 英文仓 PR 交付接管 | 不需要 | skill 目录存在 |
| khazix-writer | 流程必装（S2 提 PR） | R15：PR 正文必须过其复审（必选 ≠ 必须采用其文风） | 不需要 | skill 目录存在 |
| humanizer + zh-tech-writing | 文档推荐（S3/S5；对应 R13/R16） | 润色链：去 AI 腔 + 中文句式定稿 | 不需要 | skill 目录存在 |
| vitepress | 建仓推荐（S5 重档文档站） | 文档站生成 | 不需要 | skill 目录存在 |
| firecrawl 系列 | 可选（调研/抓取场景） | 联网调研、语料抓取 | 可选：FIRECRAWL_API_KEY（无 key 走免费额度） | skill 目录存在 |

### 3.3 搜索引擎能力矩阵（本机实测 2026-09-28，13 引擎全通）

| 引擎 | 本机状态 | 适用场景 | 需要环境变量 |
|---|---|---|---|
| bing（默认） | ✅ 免费 | 通用搜索、快速事实核查 | 不需要 |
| exa | ✅ 付费 | 语义搜索（找相似内容/代码） | EXA_API_KEY |
| tavily | ✅ 付费 | AI 优化搜索（综述/调研） | TAVILY_API_KEY |
| keenable | ✅ 付费 | 精准网页检索 | KEENABLE_API_KEY |
| firecrawl | ✅ 付费 | 网页正文提取/站点抓取 | FIRECRAWL_API_KEY |
| deepseek-official | ✅ 付费 | 中文技术搜索 | DEEPSEEK_API_KEY |
| baidu | ✅ 付费 | 中文搜索（国内生态覆盖强） | BAIDU_API_KEY |
| kimi | ✅ 付费 | 长上下文搜索 | MOONSHOT_API_KEY |
| aliyun | ✅ 付费 | 通义生态搜索 | DASHSCOPE_API_KEY |
| ddg / ddg-lite | ✅ 免费 | 隐私搜索、国际内容 | 不需要 |
| anysearch / parallel | ✅ 免费 | 聚合搜索 | 不需要 |

**场景 → 引擎选型**：

| 场景 | 首选引擎 | 理由 |
|---|---|---|
| S1 梳理（仓库调研） | multi_search（exa + tavily + bing） | 跨源验证仓库信息 |
| S2 修 bug（上游复现搜索） | deepseek-official + bing | 中文技术报错搜索最强 |
| S3 文档（API/规范查证） | keenable + exa | 精准技术文档检索 |
| 生态对标（oz-skills 类） | multi_search（tavily + baidu + bing） | 国内外开源生态双覆盖 |
| 语料补抓（readme-real 类） | firecrawl | 网页正文提取+批量 |
| GitHub 代码/仓库搜索 | platform_search(github) | 专用通道非通用搜索 |

引擎不可用时自动降级到免费引擎（bing/ddg），搜索层**永不硬停**。

## 4. 各场景调度关系

| 场景 | 调用的实质 skill | 各管什么 |
|---|---|---|
| S1 | oss-contribution §P0 探针 + oss-voice §1 语言分布 + archify（代码地图） | 仓库解剖五件套（功能价值/archify 代码地图/请求生命周期/核心抽象/真实执行跟踪，2026-09-29 用户定标） |
| S2 | oss-contribution 全管线 P0–P9（P4–P6 实现段用 oss-dev）+ oss-dev §3-4 + oss-security §2 + khazix-writer（R15） | PR 交付（本 skill 只管调度和清单） |
| S3 | oss-voice 全部（§7 多语言同步）+ humanizer/zh-tech-writing | 文档产出 |
| S4 | oss-contribution §P9 + oss-persona 声纹（WeKnora 侧加 references/lyingbug-voiceprint.md） | 维护者侧回应 |
| S5 | oss-scaffold 全部 + oss-voice（含 §7 多语言命名）+ oss-persona | 建仓全组件 |

**调度 ≠ 摘要**：本 skill 只告诉每步去读哪个文件的哪一节，不复制其内容；checklist 条目同样只留步骤 + 指针，规则语义一律活在规则源（单一真相，防双源冲突）。子代理/主 agent 到那步就去读。

## 5. 审计

每个任务的 CHECKLIST.md 留在 .oss-task/ 目录，事后可审计：
- 哪些步骤被跳过（未打勾）
- Gate 步骤的确认记录
- 交付与清单的对照

这是套件从「知识文档」变成「执行系统」的证据链。


