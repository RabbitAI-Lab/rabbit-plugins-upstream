---
name: loop-engineering
description: "基于 Loop Engineering 理念的元技能，为复杂多步骤任务构建可迭代、可验证、可安全停止的反馈闭环系统。适用于代码生成与调试、设计实现、内容创作、工具调用等任何需要多轮执行与自我修正的场景。"
version: 1.0.0
metadata:
  openclaw:
    emoji: "🔄"
    homepage: ""
---

# Loop Engineering — 构建可迭代执行的 Agent 闭环

将 AI Agent 从「一次性回答」升级为「可规划、可执行、可观察、可评估、可修正、可安全停止」的任务执行系统。

## 触发条件

当执行以下任何复杂多步骤任务时自动触发 Loop 流程：
- 代码生成、调试与重构
- 从设计稿到可运行应用的实现
- 多工具链调用与编排
- 内容生成与质量优化
- 数据分析与报告生成
- 任何涉及「执行 → 验证 → 修正」循环的任务

**单次问答类任务不触发**（如事实查询、简单翻译、概念解释）。

---

## 核心六步闭环

```
Goal → Plan → Act → Observe → Evaluate → Repair → Stop or Continue
```

### Step 1: 初始化 Loop State（Init）

每次进入 Loop 前，必须在对话上下文中显式建立并维护状态卡片：

```yaml
loop_state:
  goal: "任务目标，一句话描述最终交付物"
  plan:
    - "步骤1：..."
    - "步骤2：..."
    - "步骤N：..."
  current_step: "当前正在执行的步骤编号与名称"
  actions:
    - step: "步骤1"
      tool: "使用的工具/命令"
      result_summary: "结果一句话摘要"
      timestamp: "2026-07-07T10:00:00"
  errors:
    - error: "错误描述"
      type: "临时错误/参数错误/权限错误/证据不足/目标冲突"
      iteration: 1
      fix_strategy: "采用的修复策略"
  evidence:
    - "已确认的事实1"
    - "已找到的证据2"
  constraints:
    - "用户明确禁止的操作"
    - "安全边界（如不能删除数据）"
  iteration: 0
  max_iterations: 6
  max_tool_calls: 20
  status: running  # running / success / failed / need_human
```

**状态维护规则**：
- 每完成一轮 Act → Observe → Evaluate，必须更新 `iteration`、`actions`、`errors`、`current_step`
- 状态卡片必须在每轮循环开始时向用户简要汇报当前进展
- 禁止在状态未更新时直接开始下一轮执行

### Step 2: 计划拆解（Plan）

将 `goal` 拆分为 3–8 个可独立执行的步骤：

**拆解原则**：
- 每个步骤产出可验证（有明确的成功标准）
- 步骤之间有依赖顺序，但尽量降低耦合
- 包含至少一个「验证步骤」（如运行测试、截图对比、人工检查点）

**Plan 模板**：
```
① [准备] 环境检查与依赖安装 → 验证：npm install 成功无报错
② [实现] 核心组件/模块开发 → 验证：代码编译通过
③ [实现] 交互与状态逻辑 → 验证：功能流程可跑通
④ [验证] 运行测试或启动预览 → 验证：无运行时错误
⑤ [优化] 响应式适配与边界处理 → 验证：三端/多态正常
⑥ [交付] 最终检查与文档输出 → 验证：README 完整可运行
```

### Step 3: 执行（Act）

执行当前步骤，记录完整的工具调用与结果：

**必须记录**：
- 执行的命令/代码/工具名称
- 输入参数（关键参数必须显式写出）
- 原始输出（或输出的前 50 行摘要，若输出过长）

**执行原则**：
- 一次只执行一个步骤，禁止跳过验证直接执行下一步
- 涉及文件修改时，先读取原文件，再明确写出变更内容
- 高风险操作（删除、覆盖、发送请求）必须先确认状态卡片中的约束清单

### Step 4: 观察（Observe）

将原始输出解析为结构化观察对象，禁止直接把原始日志塞回模型：

**观察模板**：
```yaml
observation:
  tool: "使用的工具"
  passed: true/false
  summary: "一句话结果摘要"
  key_output: "关键输出内容"
  error_type: "none / timeout / bad_argument / permission_denied / assertion_error / compile_error / runtime_error"
  suspected_module: "可能出错的文件/模块"
  new_evidence: "本轮发现的新事实"
```

**常见观察转换**：

| 原始输出 | 结构化观察 |
|---------|-----------|
| 测试日志 200 行 | `passed: false, failed_cases: ["test_A"], error_type: "assertion_error", suspected_module: "auth.ts"` |
| API 响应 `{code: 500}` | `passed: false, error_type: "runtime_error", key_output: "Internal Server Error", suspected_module: "后端 /api/users"` |
| 构建输出 `Build completed` | `passed: true, summary: "构建成功，耗时 12s"` |
| 截图对比 | `passed: false, summary: "间距偏差 4px，颜色偏差 #F0F0F0 vs #FFF8F0"` |

### Step 5: 评估（Evaluate）

基于观察对象，使用外部评估信号判断当前状态：

**评估模板**：
```yaml
evaluation:
  passed: true/false
  score: 0.0-1.0
  failed_rules:
    - "未通过的规则1"
    - "未通过的规则2"
  risk: "none / low / medium / high"
  next_action: "continue / retry / fix_arguments / retrieve_more / ask_human / stop"
  reason: "评估结论的一句话解释"
```

**按任务类型的评估标准**：

| 任务类型 | 通过标准 | 评估信号 |
|---------|---------|---------|
| 代码生成 | 编译通过 + 测试通过 + lint 无报错 | `npm run build` 结果、`npm test` 结果 |
| 设计实现 | 还原度 ≥ 95% + 三端正常 + 无交互阻断 | 截图对比、DevTools 设备模拟 |
| 内容生成 | 结构完整 + 数据真实 + 无幻觉 | 字数统计、事实校验、原创度检查 |
| 工具调用 | 状态码 200 + 返回体符合 schema | HTTP 状态码、响应体字段校验 |
| 数据操作 | 写入成功 + 读取一致 + 无脏数据 | 数据库查询验证、前后端联调 |

**核心原则**：不要让模型自己宣布自己成功。必须通过可验证的外部信号（编译器、测试框架、截图对比、数据库查询）来评估。

### Step 6: 修复（Repair）

如果 `evaluation.passed == false`，根据 `error_type` 和 `risk` 选择修复策略：

**修复策略路由**：

| 错误类型 | 风险等级 | 修复策略 | 操作 |
|---------|---------|---------|------|
| 临时错误（超时/502/限流） | low | retry_with_backoff | 指数退避重试（1s → 2s → 4s），最多 3 次 |
| 参数错误（字段缺失/类型不匹配） | low | fix_arguments | 修正参数后重新调用，不重试原请求 |
| 编译错误（语法/类型） | low | fix_code | 定位报错文件 → 修复具体行 → 重新编译 |
| 测试失败（断言/逻辑） | medium | fix_logic | 分析失败 case → 修改代码 → 重新测试 |
| 证据不足（检索缺失） | medium | retrieve_more | 换查询词/扩展检索范围/追问用户 |
| 还原度不足（设计偏差） | medium | refine_style | 对比设计稿 → 修正样式参数 → 重新截图验证 |
| 权限错误（403/token 失效） | high | stop_and_request_auth | 立即停止，告知用户需要授权 |
| 目标冲突（用户需求矛盾） | high | ask_human | 停止并列出冲突点，请求用户决策 |
| 高风险动作（删除/支付/发布） | high | ask_human | 必须人工确认，禁止自动执行 |
| 超出能力范围 | high | stop_with_reason | 明确告知不可完成的原因 |

**修复后必须**：
1. 将本轮错误和修复策略记录到 `errors` 列表
2. 更新 `iteration`
3. 重新执行被失败的步骤（Act），而非直接进入下一步

---

## 停止条件（Stop Conditions）

Loop 必须在以下任一条件触发时停止：

| 停止类型 | 触发条件 | 结果 |
|---------|---------|------|
| **成功停止** | `evaluation.passed == true` 且所有计划步骤完成 | 输出最终交付物，附上执行摘要 |
| **失败停止** | 明确不可完成（依赖缺失、超出能力、环境不支持） | 给出失败原因 + 已尝试的方案 + 建议的人工接手路径 |
| **风险停止** | `evaluation.risk == "high"` 或涉及约束清单中的高风险动作 | 请求人工确认，说明风险点和建议操作 |
| **预算停止** | `iteration >= max_iterations` 或工具调用/时间超限 | 汇报当前进展、已完成部分、未完成部分、建议的下一步 |

**强制上限**：
- `max_iterations`: 6（默认）
- `max_tool_calls`: 20
- `max_minutes`: 15

---

## Loop 执行摘要输出

无论成功、失败还是人工接管，停止时必须输出结构化摘要：

```yaml
loop_summary:
  status: success/failed/need_human
  iterations: 3
  total_time: "8m 32s"
  completed_steps:
    - "① 环境准备 ✓"
    - "② 核心实现 ✓"
    - "③ 测试验证 ✓"
  failed_steps:
    - "④ 性能优化 ✗（超出迭代预算）"
  key_errors:
    - "TypeScript 类型不匹配（已修复）"
  final_deliverable: "交付物描述及路径"
  next_recommendation: "建议用户下一步操作"
```

---

## 自主蒸馏提纯（Self-Distillation & Refinement）

Loop Engineering 的第二层闭环：从执行轨迹中自动提炼可复用的经验知识，使 Agent 在同类任务中越用越强。

### 核心理念

```
执行闭环：Goal → Plan → Act → Observe → Evaluate → Repair → Stop
蒸馏闭环：Trace → Extract → Distill → Deposit → Retrieve → Apply → Validate
```

每一次任务执行都会产生一条完整的**执行轨迹（Trace）**。蒸馏提纯能力要求 Agent 在任务结束后，主动分析这条轨迹，提取成功模式与失败模式，沉淀为可复用的**经验原则（Principle）**，并在后续同类任务中自动检索和应用。

### 执行轨迹记录（Trace Logging）

轨迹是蒸馏的原材料。每次 Loop 必须生成完整的轨迹记录：

```yaml
loop_trace:
  trace_id: "trace-20260708-001"
  task_type: "代码生成 / 设计实现 / 内容创作 / 数据分析"
  goal: "任务目标"
  plan: ["步骤1", "步骤2", "步骤3"]
  execution_log:
    - iteration: 1
      step: "步骤1"
      act: "执行的命令或代码"
      observation:
        passed: true/false
        error_type: "..."
      evaluation:
        passed: true/false
        score: 0.0-1.0
      repair: "采用的修复策略（如有）"
    - iteration: 2
      step: "步骤2"
      ...
  final_result:
    status: "success / failed / need_human"
    deliverable: "最终交付物摘要"
    total_iterations: 5
    total_time: "12m 30s"
  context:
    tech_stack: ["React", "Next.js", "Prisma"]
    constraints: ["必须三端适配", "必须使用 SQLite"]
    environment: "Node.js 20 / macOS / ARM64"
```

**轨迹记录规则**：
- 每个 `loop_trace` 必须有唯一的 `trace_id`
- `task_type` 必须标准化分类，便于后续检索
- `execution_log` 必须按迭代顺序完整记录，禁止省略失败的迭代
- `context` 记录环境信息，因为同一方案在不同环境下可能失效

### 模式提取（Pattern Extraction）

从轨迹中识别可复用的成功模式和需规避的失败模式：

**成功模式提取**：
```yaml
success_pattern:
  pattern_id: "sp-001"
  task_type: "Next.js + Prisma 全栈项目"
  context_match:
    tech_stack: ["Next.js", "Prisma"]
    goal_keywords: ["用户系统", "认证"]
  successful_plan:
    - "先配置 prisma/schema.prisma 再执行 migrate"
    - "auth.ts 中使用 Credentials provider + bcrypt"
    - "seed.ts 中同时创建管理员账号和示例数据"
  key_successor: "prisma schema 定义完整后再迁移，避免后续反复修改"
  source_trace: "trace-20260708-001"
  occurrence_count: 3
  success_rate: 1.0
```

**失败模式提取**：
```yaml
failure_pattern:
  pattern_id: "fp-001"
  task_type: "Next.js 项目构建"
  context_match:
    tech_stack: ["Next.js", "TypeScript"]
  failure_signature:
    error_type: "compile_error"
    symptom: "'session.user' is possibly 'undefined'"
    root_cause: "NextAuth 默认 Session 类型不包含自定义字段（id, role）"
  fix_strategy:
    - "创建 src/types/next-auth.d.ts 扩展 Session 和 JWT 类型"
    - "声明 module 'next-auth' 和 module 'next-auth/jwt'"
  prevention: "任何使用 NextAuth  credentials + role 的项目都必须先创建类型声明文件"
  source_trace: "trace-20260708-002"
  occurrence_count: 2
  fix_success_rate: 1.0
```

**提取规则**：
- 成功模式：连续 3 次以上在相似上下文中成功，且每次 Plan 的前 2 步一致
- 失败模式：同一错误在相似上下文中出现 2 次以上，且修复策略被验证有效
- 上下文匹配：通过 `task_type` + `tech_stack` + `goal_keywords` 三维匹配

### 原则蒸馏（Principle Distillation）

将提取的模式进一步提炼为简洁、可执行的原则：

**原则格式**：
```yaml
principle:
  principle_id: "p-001"
  category: "技术栈初始化 / 错误修复 / 架构设计 / 性能优化"
  condition: "当使用 NextAuth Credentials Provider 且需要自定义用户字段时"
  action: "必须首先创建 next-auth.d.ts 类型声明文件，扩展 Session 和 JWT 接口"
  rationale: "NextAuth v4 的默认 TypeScript 类型不包含自定义字段，不声明会导致编译错误"
  confidence: 0.95  # 基于成功次数 / (成功次数 + 失败次数)
  source_patterns: ["fp-001", "fp-003"]
  created_at: "2026-07-08"
  last_applied: "2026-07-08"
  application_count: 5
  application_success_rate: 1.0
```

**蒸馏标准**：
- 原则必须满足 `condition → action` 的触发式结构
- `rationale` 必须解释为什么这个原则有效（因果链）
- `confidence` 必须基于统计数据，低于 0.7 的原则标记为「实验性」
- 相似原则必须合并，避免经验库膨胀

### 经验库存储（Experience Bank）

经验库是 Agent 的「长期记忆」，按层级组织：

```yaml
experience_bank:
  version: "1.0.0"
  last_updated: "2026-07-08T14:00:00"
  principles:
    - principle_id: "p-001"
      ...
    - principle_id: "p-002"
      ...
  patterns:
    success_patterns: ["sp-001", "sp-002"]
    failure_patterns: ["fp-001", "fp-002"]
  task_type_index:
    "Next.js + Prisma 全栈项目": ["p-001", "p-003", "sp-001"]
    "React + Vite 纯前端项目": ["p-005", "sp-003"]
    "设计稿转代码": ["p-010", "fp-005"]
  anti_patterns:
    - "永远不要在前端硬编码 API 密钥"
    - "不要忽略 NextAuth 的 Session 类型扩展"
```

**存储规则**：
- 经验库以 YAML 格式存储在 `/workspace/.agent-experience/experience-bank.yaml`
- 每次任务结束后，如果提炼出新原则，追加到经验库
- 经验库版本号随重大结构变化递增

### 在线检索与应用（Online Retrieval & Application）

新任务开始时，根据当前任务特征从经验库检索相关原则：

**检索流程**：
1. **特征提取**：从当前任务的 `goal`、`task_type`、`tech_stack` 提取关键词
2. **索引匹配**：在 `task_type_index` 中查找匹配的任务类型
3. **相关性排序**：按 `confidence × application_success_rate` 排序
4. **条件过滤**：检查 `principle.condition` 是否匹配当前上下文
5. **应用注入**：将匹配的原则注入到 Plan 和 Repair 策略中

**应用方式**：

| 应用阶段 | 注入内容 | 示例 |
|---------|---------|------|
| **Plan 阶段** | 成功模式的 `successful_plan` 作为默认步骤模板 | "历史经验表明，此类项目应先配置 Prisma schema 再迁移" |
| **Repair 阶段** | 失败模式的 `fix_strategy` 作为首选修复方案 | "检测到 NextAuth 类型错误，历史最佳修复：创建 next-auth.d.ts" |
| **Evaluate 阶段** | 失败模式的 `prevention` 作为预检清单 | "检查清单：是否已创建类型声明文件？" |
| **约束阶段** | `anti_patterns` 作为禁止操作 | "约束：禁止在前端硬编码 API 密钥" |

**应用示例**：
```
[新任务] Goal: 创建一个使用 NextAuth 的 Todo 应用
  → Retrieve: 匹配到 task_type "Next.js + Prisma 全栈项目"
  → 检索到原则 p-001（confidence 0.95）
  → 注入 Plan: 步骤① 创建 next-auth.d.ts 类型声明
  → 注入约束: "禁止跳过类型声明直接写 auth.ts"
  → 开始执行...
  → 若编译错误 symptom 匹配 fp-001
  → 自动应用 fix_strategy: 创建 next-auth.d.ts
```

### 经验维护（Experience Maintenance）

经验库需要定期维护，防止膨胀和失效：

**维护规则**：

| 维护操作 | 触发条件 | 处理方式 |
|---------|---------|---------|
| **去重合并** | 两个原则的 `condition` 和 `action` 相似度 > 80% | 合并为一条原则，更新 `application_count` 和 `confidence` |
| **置信度衰减** | 原则超过 30 天未被应用 | `confidence` 每年衰减 10%，低于 0.5 标记为「待验证」 |
| **版本淘汰** | 技术栈版本升级导致原则失效 | 标记为 `deprecated`，保留但不再推荐，新增适用于新版本的原则 |
| **成功升级** | 原则连续 5 次应用成功 | `confidence` 提升至 0.95 以上，标记为「最佳实践」 |
| **失败降级** | 原则应用后失败次数 > 成功次数 | `confidence` 降低，若低于 0.3 移入 `discarded` 区 |

**维护周期**：
- 每完成 10 个任务执行一次批量维护
- 每次维护后更新 `experience_bank.version`
- 维护日志记录所有变更：`merged` / `deprecated` / `discarded` / `upgraded`

### 元策略进化（Meta-Policy Evolution）

随着经验库积累，Repair 策略路由和评估标准应自动进化：

**Repair 策略进化**：
- 当某类错误的 `fix_strategy` 在经验库中有高置信度原则时，该策略升级为「首选」
- 当某类错误的修复成功率长期低于 50%，标记为「需重新设计修复路径」

**评估标准进化**：
- 收集多次任务的 `evaluation.score` 分布
- 识别哪些评估规则经常不通过，分析是否需要调整阈值
- 新增从失败模式中提炼的预检规则

**Plan 模板进化**：
- 当某类任务的成功模式积累足够（≥5 条高置信度原则），生成该类任务的「黄金 Plan 模板」
- 后续同类任务直接以黄金模板作为默认 Plan，仅需微调

---

## 多代理模式（Multi-Agent）

当任务复杂度超出单 Agent 处理能力，或任务天然可拆分为多个专业领域时，启用多代理模式。

### 触发条件

以下情况自动从单代理升级为多代理：
- 任务涉及 ≥3 个不同技术栈（如前端 + 后端 + AI + 运维）
- 需要同时生成内容并由独立评审者验证质量
- 任务可拆分为无依赖或弱依赖的并行子任务
- 用户明确要求「多个专家协作」或「让不同角色分别负责」

### 多代理编排模式

根据任务特征选择以下三种编排模式之一：

#### 模式一：顺序管道（Sequential Pipeline）

多个 Agent 按固定顺序串行执行，前一个的输出作为后一个的输入。

```
用户输入 → Agent A（需求分析）→ Agent B（架构设计）→ Agent C（代码实现）→ Agent D（测试验证）→ 输出
```

**适用场景**：需求分析 → 设计 → 开发 → 测试等天然有依赖顺序的流程
**状态传递**：每个 Agent 完成后更新全局 Loop State，后续 Agent 读取状态中的 `evidence` 和 `actions`

#### 模式二：监督者-工作者（Orchestrator-Worker）

一个编排器 Agent（Orchestrator）负责任务拆解、分配、聚合；多个工作者 Agent（Worker）并行执行子任务。

```
用户输入 → Orchestrator（拆解任务）→ [Worker A ∥ Worker B ∥ Worker C] → Orchestrator（聚合结果）→ 验证 → 输出
```

**适用场景**：
- 设计稿转代码：Worker A 负责页面结构、Worker B 负责样式还原、Worker C 负责交互逻辑
- 多模块重构：每个 Worker 负责一个独立模块
- 内容生成：Worker A 生成初稿、Worker B 生成配图描述、Worker C 生成 SEO 元数据

**工作者定义模板**：
```yaml
worker:
  id: "worker-a"
  name: "前端结构专家"
  role: "负责将设计稿拆解为 HTML/JSX 骨架，输出组件树和布局代码"
  input: "设计稿解析规范 + 当前步骤的 Loop State"
  output: "结构化代码 + 观察报告"
  constraints:
    - "不处理样式细节"
    - "不处理交互逻辑"
  max_iterations: 3
```

#### 模式三：评审循环（Review Loop）

一个实现 Agent 与一个评审 Agent 成对协作，实现 → 评审 → 修正 → 再评审，直到达标。

```
用户输入 → Implementer（实现）→ Reviewer（评审）→ [passed?] → 是：输出 / 否：修正 → 循环
```

**适用场景**：
- 代码审查与重构
- 设计还原度检查
- 内容质量把关
- 安全漏洞扫描

**评审标准模板**：
```yaml
review_criteria:
  - rule: "还原度 ≥ 95%"
    check_method: "截图对比 + 像素偏差检测"
  - rule: "无 TypeScript 类型错误"
    check_method: "tsc --noEmit"
  - rule: "所有交互状态已覆盖"
    check_method: "人工检查清单"
reviewer:
  id: "reviewer-alpha"
  role: "严格的质量评审者，只指出问题不修改代码"
  output_format: "结构化评审报告：{passed, score, issues: [{severity, location, description, suggestion}]}"
```

### 多代理状态设计

多代理模式下，Loop State 扩展为支持多 Agent 读写：

```yaml
loop_state:
  goal: "任务目标"
  orchestrator: "编排器 Agent 的 ID"
  workers:
    - id: "worker-a"
      status: "running / done / failed / need_human"
      current_task: "当前子任务描述"
      deliverable: "已交付内容摘要"
      errors: []
    - id: "worker-b"
      status: "done"
      current_task: "样式还原"
      deliverable: "Tailwind 样式代码 + 颜色 token"
      errors: []
  shared_evidence:
    - "Worker A 已确认：组件树包含 12 个节点"
    - "Worker B 已确认：颜色系统提取完成"
  messages:
    - from: "worker-a"
      to: "worker-b"
      type: "dependency_ready"
      content: "组件树已稳定，可开始样式绑定"
    - from: "reviewer-alpha"
      to: "worker-c"
      type: "critique"
      content: "交互逻辑缺少 loading 状态，需补充"
  global_iteration: 2
  max_global_iterations: 6
  status: running
```

**状态同步规则**：
- 每个 Worker 完成子任务后，必须更新自己的 `status` 和 `deliverable`
- Orchestrator 在分配新任务前，必须检查所有依赖 Worker 的 `status == "done"`
- 全局 `messages` 作为 Agent 间通信的唯一通道，禁止绕过消息总线直接修改其他 Agent 的状态

### Agent 间通信协议

所有 Agent 间通信必须通过结构化消息：

```yaml
message:
  id: "msg-001"
  from: "agent-id"
  to: "agent-id / broadcast"
  type: "task_assign / result / critique / dependency_ready / escalation / heartbeat"
  payload:
    # 根据 type 变化
  timestamp: "2026-07-07T10:00:00"
  priority: "low / normal / high / critical"
```

**消息类型说明**：

| 类型 | 用途 | 发送者 | 接收者 |
|------|------|--------|--------|
| `task_assign` | 分配子任务 | Orchestrator | Worker |
| `result` | 交付子任务结果 | Worker | Orchestrator |
| `critique` | 指出问题并要求修正 | Reviewer | Implementer |
| `dependency_ready` | 通知依赖方前置条件已满足 | Worker | Worker |
| `escalation` | 遇到无法解决的问题，升级给人工 | Worker | Human |
| `heartbeat` | 定期汇报存活状态和当前进展 | Worker | Orchestrator |

### 结果聚合与冲突解决

当多个 Worker 的结果需要合并时，Orchestrator 执行以下流程：

**聚合步骤**：
1. **收集**：等待所有 Worker 返回 `result` 消息
2. **校验**：检查各结果之间是否存在接口/数据结构冲突
3. **合并**：按预定规则合并（如代码按文件路径拼接、数据按主键去重合并）
4. **验证**：运行集成测试或构建，确认合并后的整体可用

**冲突处理策略**：

| 冲突类型 | 检测方式 | 解决策略 |
|---------|---------|---------|
| 接口不一致 | Worker A 输出接口字段与 Worker B 期望不匹配 | Orchestrator 介入定义统一接口，要求双方对齐 |
| 文件覆盖 | 两个 Worker 修改同一文件 | 禁止并行修改同一文件，Orchestrator 在分配任务时隔离文件边界 |
| 数据矛盾 | Worker A 结论与 Worker B 结论相反 | 触发 Review Loop，由评审 Agent 判断哪方证据更充分 |
| 时序依赖 | Worker B 在 Worker A 完成前就开始执行 | Orchestrator 必须显式声明依赖关系，未满足前不分配下游任务 |

### 多代理停止条件

多代理模式下，停止条件增加全局维度：

| 停止类型 | 触发条件 |
|---------|---------|
| **全局成功** | 所有 Worker `status == "done"` + 集成验证通过 |
| **局部失败** | 单个 Worker 失败且无法通过 Repair 恢复，Orchestrator 判断整体不可完成 |
| **全局预算** | `global_iteration >= max_global_iterations`（默认 6） |
| **死锁** | 多个 Worker 互相等待依赖，且心跳超时（默认 5 分钟无响应） |
| **人工升级** | 任一 Worker 发送 `escalation` 消息，或冲突无法自动解决 |

### 与单代理模式的切换

**何时用单代理**：
- 任务步骤 ≤ 3 且技术栈单一
- 子任务间强耦合，无法解耦
- 需要深度上下文理解，拆分后信息丢失

**何时用多代理**：
- 任务步骤 ≥ 4 且可拆解为独立模块
- 涉及多个专业领域（设计/前端/后端/测试）
- 需要独立的质量评审角色
- 子任务间依赖关系清晰（DAG 结构）

---

## 与现有 Skill 的集成

### 与单 Skill 集成

当 Loop Engineering 与 `design-to-code` 等其他 skill 配合使用时：

- **design-to-code 的 Step 5（代码实现）** → 每一层（骨架/组件/交互/逻辑/后端）都作为一个 Loop 子任务执行
- **design-to-code 的 Step 6（多端验证）** → 作为 Loop 的 Evaluate 步骤，使用截图对比和 DevTools 作为外部评估信号
- **design-to-code 的构建错误** → 触发 Loop 的 Repair，按 `compile_error` 策略修复代码后重试构建

### 与多 Skill 协作

当多个 Skill 需要协作时，使用多代理模式：

```
用户: "设计并实现一个古诗词学习小程序"

Orchestrator:
  → 分配 Worker A 调用 design-spec-optimizer → 输出完整设计描述
  → 收集设计描述后
  → 分配 Worker B 调用 design-to-code → 输出前端代码
  → 分配 Worker C 调用 design-to-code（后端部分）→ 输出 API + 数据库
  → 分配 Worker D（Reviewer）评审还原度和代码质量
  → 聚合所有结果 → 集成验证 → 输出完整项目
```

**集成示例（单代理模式）**：
```
[Loop Start] Goal: 实现古诗词学习应用的游戏页
  Plan: [①组件开发 ②游戏逻辑 ③测试运行]
  → Act: 编写游戏组件
  → Observe: 构建成功
  → Evaluate: passed=true
  → Act: 实现拼图游戏逻辑
  → Observe: 构建成功，但运行时数组越界
  → Evaluate: passed=false, error_type=runtime_error
  → Repair: fix_logic → 修正数组边界检查
  → Act: 重新测试
  → Observe: 游戏正常运行，得分逻辑正确
  → Evaluate: passed=true
  → Stop: 成功停止，输出游戏页代码
```

**集成示例（多代理模式）**：
```
[Multi-Agent Loop Start] Goal: 从设计稿实现完整应用
  Orchestrator Plan: [Worker A:页面结构 ∥ Worker B:样式还原] → [Worker C:交互逻辑] → [Reviewer:质量评审]

  → Worker A Act: 输出 JSX 骨架
  → Worker A Observe: 组件树完整
  → Worker A → msg(dependency_ready) → Worker B

  → Worker B Act: 输出 Tailwind 样式
  → Worker B Observe: 还原度 96%
  → Worker B → msg(result) → Orchestrator

  → Orchestrator: 分配 Worker C（依赖 A+B 均完成）
  → Worker C Act: 输出交互逻辑
  → Worker C Observe: 构建通过
  → Worker C → msg(result) → Orchestrator

  → Orchestrator: 分配 Reviewer
  → Reviewer Evaluate: passed=false, issues=["缺少 loading 状态"]
  → Reviewer → msg(critique) → Worker C

  → Worker C Repair: 补充 loading 状态
  → Worker C → msg(result) → Orchestrator
  → Reviewer Evaluate: passed=true

  → Orchestrator: 全局成功停止，聚合输出完整项目
```

---

## 输出原则

- **状态必显式**：每轮循环必须向用户展示当前状态卡片（至少包含 current_step、iteration、status）
- **观察必结构化**：禁止把原始日志/报错直接作为下一步的输入，必须先提炼为 observation 对象
- **评估必外部**：必须通过编译器、测试框架、截图对比等外部信号评估，禁止模型自评
- **修复必分类**：失败时必须按错误类型选择修复策略，禁止无脑重试
- **停止必清晰**：达到停止条件时，必须说明停止类型、原因和当前交付状态
- **摘要必输出**：Loop 结束时必须输出结构化执行摘要
- **轨迹必记录**：每次 Loop 结束后必须生成完整的 `loop_trace`，作为蒸馏的原材料，禁止省略失败迭代
- **经验必蒸馏**：每完成 3–5 个同类任务，必须执行一次离线蒸馏，提取成功/失败模式并沉淀为 `principle`
- **原则必应用**：新任务开始时必须从经验库检索相关原则，注入到 Plan 和 Repair 策略中，避免重复踩坑
- **经验库必维护**：每 10 个任务执行一次批量维护（去重、衰减、淘汰），防止经验库膨胀和失效

---

## 常见陷阱规避

- ❌ 不要把 Loop 写成「失败就再来一次」的无限 while，必须有状态、有分类、有上限
- ❌ 不要让模型自己判断成功，必须通过外部可验证信号评估
- ❌ 不要在状态未记录时开始下一轮执行，否则 Agent 会忘记之前的错误
- ❌ 不要把高风险操作（删除数据库、发送邮件、调用支付）放入自动 Repair 流程
- ❌ 不要忽略「预算停止」，即使没有成功也要汇报进展而不是静默失败
- ❌ 不要把多个步骤合并为一轮执行，每个步骤必须有独立的 Act → Observe → Evaluate
- ❌ 不要忽略轨迹记录，没有轨迹就无法蒸馏，Agent 永远学不会
- ❌ 不要把失败的迭代从轨迹中删除，失败模式比成功模式更有蒸馏价值
- ❌ 不要让经验库无限膨胀而不维护，低置信度/过期的原则会污染后续决策
- ❌ 不要把特定环境（如 macOS ARM64）下的经验无条件应用到其他环境（如 Windows x64）
- ❌ 不要忽略原则的 `rationale`，没有因果解释的原则是不可信的迷信
