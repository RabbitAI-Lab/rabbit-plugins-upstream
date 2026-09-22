# 设计切片：cloudbase-2.32.4 — 亮点清单

> **来源**：`<本地参考目录>/cloudbase-2.32.4`（腾讯云开发官方技能包，135 文件 / 30+ 子 skill）
> **架构类型**：Hub/套件型（顶层路由器 + 子 skill 套件）——本切片为 skill-designer 的**第七种结构框架**候选
> **一句话**：这个 skill 把"大领域多子域"拆成"一个路由器 + 一堆自治子 skill"，并用一张结构化路由契约（activation-map.yaml）把意图识别做成了机器可维护的工程。

---

## B01 条件积木

### A-011 · Hub/套件架构准入
- **落位**：B01 条件 / B07 计划
- **触发信号**：目标 skill 覆盖多个**正交子域**（auth / 数据库 / 云函数 / AI / ops…），单 SKILL.md 装不下、知识总量 > 50K
- **证据**：cloudbase 顶层 SKILL.md 仅 16KB 路由器，references/ 下 30+ 个子 skill 各自自治
- **要点**：当领域足够大且子域正交时，不做一个"巨型 skill"，而做**套件**：一个路由器 + N 个自治子 skill。路由器只留意图路由 + 全局护栏，领域细节全部下沉子 skill。

## B02 事实积木

### A-023 · 能力嗅探顺序 + 禁止中途横跳
- **落位**：B02 事实 / B07 计划
- **触发信号**：任务依赖多个外部能力且存在选型（DB 选型、SDK、工具链）
- **证据**：minimal-web-baas-demo 的 capability sniff order——`connector ready → template warmup → envQuery → 锁定一种 DB → MCP schema → CRUD → preview`，明文 "Do not reorder / no mid-flight thrash"
- **要点**：多依赖任务先写死**能力嗅探顺序**（先探什么、后探什么、何时锁定唯一方案），并禁止中途横跳——避免"选型摇摆"浪费整轮会话。

## B04 问题积木

### A-043 · EARS 验收标准句式
- **落位**：B04 问题 / B08 行动
- **触发信号**：spec/需求类工作流要写"可测试的验收标准"
- **证据**：spec-workflow 用 EARS——`While <前提>, when <触发>, the <系统> shall <响应>`
- **要点**：验收标准用 EARS 句式写（While/When/the system shall），从"模糊期望"变成"可机器判定的触发→响应"，直接喂给测试用例。

## B05 分析积木

### A-053 · BaaS-first 默认最小化
- **落位**：B05 分析 / B06 决策
- **触发信号**：同一目标有"简单路径 vs 复杂路径"（如直接 SDK CRUD vs 云函数中转）
- **证据**：minimal-web-baas-demo——"cloud functions forbidden by default / count = 0"，只有 (a) 规则表达不了 且 (b) 需要密钥或定时任务 才加
- **要点**：默认走最简能力路径，复杂组件**默认禁用**并写明"唯一允许升级的条件"（双条件都满足才升级）。反过度工程的设计决策。

## B06 决策积木

### A-063 · 工具选择决策表（多工具易混淆时）
- **落位**：B06 决策
- **触发信号**：多个工具/API 名字相近、职责易混（安全域名 vs 自定义域名 vs 复用域名）
- **证据**：cloudbase-platform 的 Domain Management 决策表（Requirement → Tool → Parameters → Purpose）+ "Key indicators" 判断线索
- **要点**：易混淆的多工具，用**决策表**固化"什么需求 → 用哪个工具 → 带什么参数 → 什么目的"，再补"关键判断线索"（看到什么词该选哪个），彻底消灭"猜工具"。

### A-064 · 权限模型选型表
- **落位**：B06 决策
- **触发信号**：涉及权限/安全规则设计，且有预定义权限档位
- **证据**：cloudbase-platform 的 READONLY / PRIVATE / ADMINWRITE / ADMINONLY / CUSTOM 五档 + "平台兼容性"（Web SDK 不能用 ADMINWRITE）+ 常见场景映射
- **要点**：权限档位用表格列出"每档含义 + 平台兼容约束 + 适用场景"，并标注**哪个组合会踩坑**（Web SDK 写 ADMINWRITE → 失败）——把权限设计从"自由发挥"变成"查表"。

## B07 计划积木

### A-074 · 结构化场景路由契约（activation-map）
- **落位**：B07 计划 / SKILL.md 意图路由
- **触发信号**：skill 有 5+ 个可区分场景需要路由
- **证据**：activation-map.yaml——每场景含 `priority / signals / firstRead / thenRead / beforeAction / doNotUse / commonMistakes / mustCheckBeforeAction`；SKILL.md 路由表由其自动生成
- **要点**：意图路由从"两列表"升级为**结构化契约**：触发信号（用户语言）+ 优先级 + 首读/再读/禁读 + 动作前检查 + 常见错误。单一数据源（yaml）→ 自动生成路由表，路由可维护、可机器校验。**本切片最核心的架构亮点。**

### A-075 · Hub 套件目录架构（第七种 archetype）
- **落位**：B07 计划 / skill-archetypes
- **触发信号**：领域大到需要 10+ 个自治子 skill
- **证据**：cloudbase/ 结构——顶层 `SKILL.md`（路由器）+ `references/<skill-id>/SKILL.md`（每子 skill 自治，含自己的 references）
- **要点**：在 minimal/pipeline/tool/knowledge/template/full 之外增加 **suite（套件）**：顶层只做路由 + 全局护栏 + 工程宪法，子 skill 用稳定 id 引用（`references/<skill-id>/SKILL.md`），同域内用相对路径互引。

### A-076 · 显式负向路由 doNotUse
- **落位**：B07 计划 / 意图路由
- **触发信号**：不同场景容易误路由到"看起来相关实则错误"的 skill
- **证据**：activation-map 每场景带 `doNotUse`（如小程序场景禁 `auth-web-cloudbase`、PG 场景禁 NoSQL/MySQL）
- **要点**：路由表加 **"Do NOT route to" 列**——不只说"该读什么"，还说"**千万别路由到哪**"，把最常见的误路由直接堵死（正面路由 + 负向路由双向约束）。

### A-077 · commonMistakes 前置注入
- **落位**：B07 计划 / B10 复盘
- **触发信号**：领域有反复踩坑的已知错误
- **证据**：activation-map 每场景带 `commonMistakes`（"把 Web 登录实现成云函数认证逻辑""跳过资格检查直接写 SDK 调用"）
- **要点**：把"常见错误"**写进路由表**，agent 一进场景就先看到"别这么做"——比让 agent 自己摸索省 10× 试错成本（呼应负向约束优先，且前置到路由层）。

### A-078 · mustCheckBeforeAction 动作前检查
- **落位**：B07 计划 / B05 分析
- **触发信号**：动手前有必须完成的资格/前置检查（权限是否开启、资源包是否开通）
- **证据**：activation-map 每场景带 `mustCheckBeforeAction`（AI 模型调用前必查 Token Credits 资源包 + 成长计划报名）
- **要点**：路由到场景后、写代码前，**强制先跑资格检查清单**——把"运行时才发现缺资格"提前到"动手前"。

### A-079 · 三层横切协议层
- **落位**：B07 计划
- **触发信号**：skill 有**跨所有子场景**的强制红线（变更安全、部署门禁、敏感数据）
- **证据**：cloudbase-platform 的 `references/protocols/`——change-safety-protocol / deployment-gate / sensitive-runtime-data-protection，任何代码改动/部署前必读
- **要点**：跨场景的强制约束**独立成协议层**（`references/protocols/`），由路由器统一声明"任何改动前必读"——不散落在各子 skill，避免漏执行。

### A-07A · tooling-fallback 降级决策树
- **落位**：B07 计划 / Error Handling
- **触发信号**：主工具（MCP）可能未就绪，但任务不能阻塞
- **证据**：tooling-fallback.md 决策树——"MCP 可用？→ 是走 MCP；否则配置 MCP 给下个会话 + 用 CLI 现在干完"。硬规则："不循环 / 不假装 / 不空转"
- **要点**：工具不可用时的降级路径写成**决策树**：探测 → 降级 → 顺手为下次铺路。纪律：失败 1–2 次即降级不反复重试、不假装工具可用、等待期间并行预热。

## B08 行动积木

### A-083 · 双轨代码审查规则库
- **落位**：B08 行动 / B09 结果
- **触发信号**：需要"实现后自检"且审查项可分成确定性 + 语义两层
- **证据**：cloudbase-code-review——Lint（正则，秒级，查确定性错误）+ LLM 审查（语义，查路由守卫/RLS 完整性）；每条规则统一格式 `Module/Severity/Stage + 正则检查/LLM检查/修复指引`，RULES_INDEX 做模块×前端类型的规则矩阵
- **要点**：审查/自检规则**沉淀成规则库**，每条统一格式（确定性规则给正则、判断性规则给 LLM 提示、都带修复指引），配规则索引矩阵——把"实现后自检"从临场发挥变成可累积的资产。

## B10 复盘积木

### A-103 · 规则边界纪律（防经验库被特例污染）
- **落位**：B10 复盘 / 经验沉淀
- **触发信号**：把失败/成功经验沉淀为规则时
- **证据**：cloudbase-code-review Rule boundary——"单个失败或 case-specific workaround 不提升为硬规则；只有稳定文档/反复失败/确定性运行时行为才能进规则库"
- **要点**：经验晋升为规则要过**准入标准**（稳定来源 / 反复失败 / 确定性行为），case-specific 只留归因报告不入库——与 skill-designer lessons 的三问晋升检查同构，但更强调"防特例污染"。

---

## 沉淀对照

- 已写入 `references/design-blocks-library.md`：A-011 / A-023 / A-043 / A-053 / A-063 / A-064 / A-074 / A-075 / A-076 / A-077 / A-078 / A-079 / A-07A / A-083 / A-103
- 待用户拍板：是否把「Hub 套件架构 A-075」正式加入 skill-archetypes 第七种结构；是否把「结构化路由契约 A-074」升级 skill-designer 自身意图路由表。
