---
name: cordis-plugin-builder
description: 从零构建 Cordis 插件（DSH 框架）的完整指南与参考体系，覆盖元框架核心概念、三种代码形态、运行时体系、能力挂载、六种部署形态与实测坑规避；当用户需要构建 Cordis 插件、进行插件开发教学答疑、或排查插件加载失败（PENDING/FAILED）时使用
---

# Cordis 插件构建指南：从元框架概念到部署

Cordis 是 DeepSeek Harness 底层的**元框架**（vendor 于 `vendor/cordis`，v4）——不是提供现成功能的框架，而是**组织能力的框架**：插件挂到共享 Context 上，Context 提供依赖注入、事件分发、生命周期管理。工具、LLM 适配器、文件访问、agent loop、skill 注册表都是插件。教程与 API 参考位于 DSH checkout 的 `docs/cordis-tutorial/` 与 `docs/cordis-primer.zh.md`。

> **平台全景**：DSH 是"一切皆插件"的开源 Coding Agent 运行框架，四种预设模式（标准/PTC/创造/极简）、
> 两条插件构建路径、社区生态与环境要求见 references/01-overview/dsh-platform.md——写插件前先读它建立大局观。

---

## 0. 元框架核心概念（先建立心智地图）

### 0.1 五要素关系脑图

```
                 ┌─────────────────────────────────────────┐
                 │              Context（服务容器）          │
                 │  Proxy 动态解析 · extend/isolate/intercept│
                 └───────┬──────────────────┬──────────────┘
                         │ 挂载              │ 依赖
                 ┌───────▼───────┐   ┌──────▼───────┐
                 │   Plugin 插件  │◄──┤  inject 声明  │
                 │ 函数/对象/Service│  │ 硬依赖自动等待 │
                 └───────┬───────┘   └──────────────┘
                         │ 执行 apply()
                 ┌───────▼───────┐
                 │  Fiber 生命周期 │  PENDING→ACTIVE→UNLOADING
                 └───────┬───────┘
                         │ 注册副作用（可逆）
                 ┌───────▼───────┐   ┌──────────────┐
                 │ effect/on 注册 │──►│  Event 分发    │
                 │ 返回 disposer  │   │ emit/waterfall│
                 └───────────────┘   │ /serial/...   │
                                     └──────────────┘
```

### 0.2 每个概念一句话 + 深挖入口

| 概念 | 一句话 | 深挖 |
|---|---|---|
| **Context** | 服务容器，Proxy 动态解析；插件的一切操作对象 | [philosophy.md](references/01-overview/philosophy.md) |
| **Plugin** | 能力单元，三种形态：函数 / 对象 / Service 子类 | [plugin-forms.md](references/02-workflow/plugin-forms.md) |
| **Service** | 注册到 `ctx.<name>` 的能力，构造即注册，按名引用 | [plugin-forms.md](references/02-workflow/plugin-forms.md) |
| **inject** | 硬依赖声明，自动等待就绪、消失自动卸载（持续跟踪） | [plugin-forms.md](references/02-workflow/plugin-forms.md) |
| **Config** | Standard Schema（schemastery）校验的插件配置，先于实现 | [plugin-forms.md](references/02-workflow/plugin-forms.md) |
| **Fiber** | 插件生命周期单元：PENDING→ACTIVE→FAILED→UNLOADING；存在父子层级，父卸载→子递归撤销（多 Agent 隔离的关键） | [lifecycle.md](references/03-runtime/lifecycle.md) |
| **effect/on** | 可逆副作用的唯一入口，返回 disposer，卸载自动回卷 | [lifecycle.md](references/03-runtime/lifecycle.md) |
| **Event** | 插件间通信，五种分发模式（emit/parallel/serial/bail/waterfall） | [events.md](references/03-runtime/events.md) |
| **Scope 派生** | extend（继承）/ isolate（隔离）/ intercept（拦截配置） | [philosophy.md](references/01-overview/philosophy.md) |
| **Loader** | 声明式装配：cordis.yml entry 树 + HMR 事务式重载，加载失败自动回滚至旧 Fiber 状态，杜绝半瘫痪 | [packaging.md](references/05-deployment/packaging.md) |

### 0.3 核心哲学（理解"为什么"）

- **时空可组合性**：插件副作用可完整撤销（时间）+ 依赖可响应出现/消失（空间）——HMR 的前提。
- **资源安全**：Context 是"插座"，插件是"插头"——卸载即拔掉，逆函数自动有序撤销所有资源占用，无需手动清理代码（类比 Rust 所有权：每个副作用有唯一"所有者"，生命周期结束即释放）。
- **服务 vs 事件分工**：服务解决"我要调用一种能力"；事件解决"我想介入一个过程"。
- **DSH 深度定制**：废弃闭包绑定改为 `Reflect.apply` 动态调用，降低高吞吐下 GC 压力；引入 `symbols.caller` 拦截器穿透 Shadow 上下文，精准定位真实调用方，确保遥测错误归属完全准确。

> 心智模型全景（三种加载机制 / 代码形态×部署形态正交 / 选型口诀 / 打包认知）见 references/01-overview/mental-models.md。

---

## 0.5 运行时全景：插件在请求链路中的位置

> 理解"插件怎么写"之前，先理解"插件运行时在什么位置、什么时候被触发"。
> 本节把 Cordis 概念挂到 DSH 的运行时时序上，帮你在写插件前建立"位置感"。

### 0.5.1 一次请求的完整生命周期

```
用户入口（CLI/Web/MCP）
     │
     ▼
① Session 注入：session.append('user/message', ...)
     │
     ▼
② PreStep 上下文装配  ←── 插件挂载点 A
   · systemPrompt.assemble() 收集所有提示词段
   · 工作区指令 + Skill 内容加载
   · agent/pre-step 瀑布（注入上下文 / 拦截）
     │
     ▼
③ LLM 推理 + 流式返回
   · llm.stream(request) → chunks
   · BlockAssembler 拼装（text / tool-call 块）
   · agent/request 瀑布（修改请求配置）
     │
     ▼
④ Assistant Message 提交 → session/event 触发
     │
     ├─ 无 tool-call → 本轮结束
     │
     └─ 有 tool-call → 进入工具管线
           │
           ▼
⑤ 工具执行管线  ←── 插件挂载点 B
   · prepare() → guards → approval → dispatch
   · Sandbox 隔离
   · execute() → 工具体执行
   · finalize() → 结果定型
     │
     ▼
⑥ Tool Result 回写 Session
   · session.append('tool/result', ...)
   · additionalContexts 注入 inbox
     │
     ▼
⑦ 循环决策
   · inbox.hasPending? → 回到 ② 下一 step
   · turnEnds? → 结束本轮
   · 无 pending → 等待用户输入
```

### 0.5.2 核心闭环

```
Session History → ② PreStep → ③ LLM → ④ Assistant Msg
                                            ↓ (有 tool-call)
                                      ⑤ Tool Runtime
                                            ↓
                                      ⑥ Tool Result → ② 下一轮
                                            ↓ (无 tool-call)
                                      ⑦ 本轮结束
```

一个 **step** = 一轮"模型生成 → 工具执行 → 结果回写"。
多个 step 组成一个 **turn**（一次用户请求的完整响应周期）。

### 0.5.3 三层循环理解法

| 轮次 | 范围 | 关键事件 | 插件在此 |
|------|------|---------|---------|
| 微循环 | 一个 step | preStep → LLM → assistant/message | 挂载点 A（pre-step） |
| 中循环 | 工具管线 | prepare → dispatch → finalize → result | 挂载点 B（tools/execute） |
| 宏循环 | 一个 turn | 多个 step 串联，直到用户消息结束 | 两端皆可 |

### 0.5.4 插件挂载点地图（按阶段索引）

| 阶段 | 挂载点 | 注册方式 | 用途 |
|------|--------|---------|------|
| ② PreStep | `agent/pre-step` 瀑布 | `ctx.waterfall` | 注入额外上下文、拦截请求 |
| ② PreStep | 提示词段 | `ctx.systemPrompt.section()` | 注册静态提示词 |
| ② PreStep | 动态变量 | `ctx.systemPrompt.variable()` | 注册运行时变量 |
| ② PreStep | 技能注册 | `ctx.skills.register()` | 注册按需加载的技能 |
| ③ LLM | `agent/request` 瀑布 | `ctx.waterfall` | 修改 LLM 请求配置 |
| ③ LLM | `agent/request-error` 瀑布 | `ctx.waterfall` | 错误处理/重试策略 |
| ④ Assistant | `session/event` | `ctx.on` | 监听 assistant/message 事件 |
| ⑤ Tool | 工具注册 | `ctx.tools.register()` | 注册模型可用工具 |
| ⑤ Tool | `tools/execute` 瀑布 | `ctx.waterfall` | 工具执行拦截 |
| ⑤ Tool | 守卫策略 | guards 配置 | 权限/频率检查 |
| ⑤ Tool | 执行前后策略 | pre/post-execute | 自定义处理 |
| ⑥ Tool Result | `session/event` | `ctx.on` | 监听 tool/result 事件 |
| ⑦ 循环 | inbox 注入 | `additionalContexts` | 工具返回附加上下文 |

### 0.5.5 关键时序细节

- **session/event 是 post-commit emit**：回调在日志 push 后运行，失败被包含（不使提交失败）。适合做链提取、日志、分析等附加处理。
- **assistant/message 先于工具执行**：模型在同一轮输出中可能同时包含 text 和 tool-call 块。`assistant/message` 先提交 → session/event 触发 → 工具管线再执行。
- **concludesTurn 声明**：工具可以标记"我的结果应该结束本轮"，用于需要等待用户输入的场景（如 ask_user）。
- **Session 是唯一事实来源**：所有输入、输出、工具调用、工具结果都作为事件追加到 session 日志。LLM 的上下文窗口由此派生。

### 0.5.6 与本技能其他章节的关系

```
0.5 运行时全景（当前节）→ 建立"插件运行时在哪"的位置感
         ↓
1. 构建流程        → 按 8 步流程构建插件
         ↓
3. 关键坑          → 避坑（含时序相关的坑）
         ↓
4. 检查清单        → 交付前验证
```

---

## 1. 从零构建：8 步流程（按序执行）

1. **定位与命名**：插件放 DSH checkout 的 `packages/<domain>/<name>/`；包名 kebab-case（`@deepseek-ai/dsh-<name>`）；依赖 `@deepseek-ai/cordis`。
2. **选形态**：默认纯函数插件；要公开 `ctx.<service>` 能力才用 `Service` 子类；对象插件仅特殊场景。
3. **契约先行**：先写 `Config` schema（`@deepseek-ai/schemastery` 的 `Schema.object`），类型与 schema 同名导出，再写实现。
4. **声明依赖**：`export const inject = ['serviceName']` 声明硬依赖（自动等待就绪、消失自动卸载）；可选依赖用 `ctx.get('name')` 探测。
5. **注册副作用**：所有注册走 `ctx.effect()` / `ctx.on()`，必须返回 disposer；Fiber dispose 时自动回卷。**能力挂载**（模型工具 `ctx.tools.register(defineTool(...))`、提示词 `ctx.systemPrompt.section/variable`、技能 `ctx.skills.register`、Client UI Slot）见 references/04-capability/harness-integration.md——这是插件产出"模型可见能力"的核心层。
6. **装配**：`cordis.yml` 加条目（带稳定 `id`），`config` 传参；`!!js` 表达式做运行时求值。
7. **验证**：先写失败测试再实现（红→绿）；运行确认，不凭声称完成。
8. **部署**：loader 启动（`node --import tsx vendor/cordis/bin.js`）；正式部署走 profile/bundle（`dsh plugin add` + `dsh.bundle` patch 层，见 [packaging.md](references/05-deployment/packaging.md)）；本地打包走 `npm pack`（tarball，见 packaging.md「npm pack 本地打包」）；HMR 热重载；模型场景用 `dsh-tool-cordis` 动态挂载。选部署形态先看 [deployment-overview.md](references/05-deployment/deployment-overview.md) 的六种形式全景与选择矩阵。

---

## 2. 格式与规格（硬约束）

- 导出项：`name`（显示名）、`apply(ctx, config)`、`Config`（schema）、`inject`（依赖数组，可选）。
- 服务名共用扁平命名空间：加辨识前缀（`tools`/`llm`/`agents`/`sessions` 等已被 harness 占用）；消费方只按名引用，不 import 提供方。
- `apply` 永远收到**完整且校验过**的 config；无效配置 → `ValidationError`，fiber 进 FAILED，插件绝不在配置不完整时启动。
- `Config` 必须用 Standard Schema（仓库用 schemastery）；导出普通对象作为 `Config` 无效。
- TS 声明合并：`declare module '@deepseek-ai/cordis' { interface Context { ... } }` 只提供类型，不产生运行时接线。**注意**：如果依赖的包通过 `declare module` 在 Cordis 的 Events 上注册了事件类型（如 `agent/pre-step`），你需要**副作用导入**（`import '@pkg'`）来触发声明合并，`import type` 不够——类型传递不触发模块副作用（见 references/06-experience/traps.md #35）。
- 事件监听：用 `ctx.on` 注册（`ctx.waterfall(name, fn)` 是分发不是注册！）；waterfall 监听器必须 `next()` 并 return。`decision.messages` 必须扁平——agent-loop 逐条 `session.append` 不展平，嵌套数组会被整体写入 session 导致 LLM 请求畸形（见 references/06-experience/traps.md #34）。

---

## 3. 关键坑（实测）

| 坑 | 正确做法 |
|---|---|
| 不查 Inspect，凭技能文档印象写 API | 文档是地图、Inspect 是真相源：写代码前 `cordis_inspect_list`→`query` 确认精确契约（流程见 [inspect-workflow.md](references/02-workflow/inspect-workflow.md)） |
| 把工具 `execute()` 当全部（忽略管线前后阶段） | 工具走九阶段管线：守卫/审批/规范化不归你管；策略挂 pre/post-execute（见 [tool-pipeline.md](references/04-capability/tool-pipeline.md)） |
| `ctx.waterfall(name, fn)` 是分发不是注册 | 分发方法，最后一个参数是内层 `next`；监听器用 `ctx.on` 注册 |
| `next(新值)` 传参被忽略（args 被闭包捕获） | `const r = next()` 取下游返回值，包装后 `return` |
| `inject` 服务缺失 = 静默 PENDING（不崩溃不报错） | 用 `FiberState.PENDING` 诊断（见 references/05-deployment/packaging.md） |
| cordis.yml 条目不带 `id` | 每次读文件都视为删除+新增，HMR 全量重挂；务必给稳定 `id` |
| 给函数赋 `name` 属性 | ES 严格模式只读；用 `export const name = 'x'` 模块级导出 |
| `inject` 服务名写成 cordis.yml 条目 id | 服务名是 `super(ctx, 'serviceName')` 的 camelCase，条目 id 只是 loader 寻址用（见 references/06-experience/traps.md #33） |
| tsconfig `paths` 指向 `.d.ts` 文件 | tsx 运行时加载 d.ts 内部相对 `.ts` 导入失败；**paths 指向包目录**（tsc 读 types / tsx 读 main） |
| 未 start 的 Context 上 `await ctx.service` | 永久 pending；验证/装配必须 **`ctx.plugin(plugin, config)`**（fiber 启动） |
| Windows 绝对路径插件 `name` | 写 `file:///E:/...`（三斜杠），裸 `E:/...` 报 `ERR_UNSUPPORTED_ESM_URL_SCHEME` |
| DSH profile patch 插入新条目 | 裸 `- id:` 是覆盖语义；插入必须用 `- insert:` 包裹 |
| `systemPrompt.section()` 传 `content` 而非 `text` | `PromptSection` 接口字段是 `text`；传 `content` 使 `section.text=undefined` → 每轮 assemble 崩溃（见 references/06-experience/traps.md #32） |
| pre-step 返回嵌套 messages | `decision.messages` 必须扁平，agent-loop 不展平（见 references/06-experience/traps.md #34） |
| `import type` 不触发 Events 声明合并 | 加副作用 `import '@deepseek-ai/dsh-agent'` 触发 declare module（见 references/06-experience/traps.md #35） |
| `MessageId` 是 branded type 不能直接赋 string | `id as unknown as MessageId` 或 `MessageId(id)` 构造（见 references/06-experience/traps.md #36） |
| schemastery 没有 `z.literal` | 用 `Schema.const('value')` 或 `Schema.union([...])`（见 references/06-experience/traps.md #37） |
| `ctx.effect()` 不能直接传 disposer 函数 | 回调包装：`ctx.effect(() => dispose)`（见 references/06-experience/traps.md #38） |

> 更多实测坑（tsx -e cjs 限制 / junction SymbolicLink 悬空 / 常驻进程句柄 / `.ts` emit / snake-camel 桥接 / systemPrompt 字段名 / pre-step 扁平 / Events 声明合并 / MessageId branded type / schemastery API 差异等）见 [references/06-experience/traps.md](references/06-experience/traps.md) 第二至第六部分。

---

## 4. 检查清单（交付前）

- [ ] Config schema 先于实现，字段类型齐全（required 无缺省）
- [ ] 写代码前已 `cordis_inspect_list`→`query` 确认每个用到的 Service/Event/Slot 契约（不猜 API、不凭文档印象；流程见 [inspect-workflow.md](references/02-workflow/inspect-workflow.md)）
- [ ] 每个 effect/on 都有 disposer；teardown 顺序敏感的放在同一 effect
- [ ] 服务名带前缀；`declare module` 声明合并已加
- [ ] 能力挂载：工具 `defineTool` JSON Schema 齐全且 register 挂 effect；提示词 section/variable 挂 effect（注意 `PromptSection` 字段名是 `text` 非 `content`）；技能注册八字段齐全（name/description/whenToUse/content/source/provider/resourceBase/invocation）+ 动态读文件 + 降级；Client UI 按 [harness-integration.md](references/04-capability/harness-integration.md) 检查单
- [ ] 事件监听：先查 [events-catalog.md](references/03-runtime/events-catalog.md) 选事件与模式；waterfall 监听器记得 `next()` 并 return；精确契约来自 Event Provider 查询；Events 声明合并需副作用导入（`import '@pkg'` 而非 `import type`）
- [ ] pre-step / waterfall 返回格式：`decision.messages` 必须扁平，agent-loop 不展平——返回数组前确保无嵌套（见 references/06-experience/traps.md #34）
- [ ] Client UI：Slot 协议已查（single/list/keyed/chain）；additive 位优先（settings.section/sidebar.footer.action 等）；不占 single 高危位；React.createElement 无 JSX
- [ ] 多语言内核：路径绝对化；子进程错误包装 + logger；常驻进程放 ctx.effect 释放；Windows 强制 UTF-8；snake/camel 显式转换
- [ ] cordis.yml 条目带 `id`；config 通过 schema 验证
- [ ] 测试覆盖正常路径 + 边界/失败用例（先红后绿）
- [ ] 运行验证输出可复现（demo 或测试全绿）
- [ ] 副作用可逆性测试：卸载后无幽灵状态（`ctx.effect` 全托管）
- [ ] 装配 DSH profile 检查单：`insert:` 包裹新条目、Windows 路径 `file:///` 三斜杠、装配后验证两信号（常驻子进程 + 工具列表）、只改 patch 层
- [ ] 卸载走配置移除（删 patch 行 → HMR 重装配），不是 `cordis_undefine`；先备份、后验证两信号、可回滚
- [ ] npm pack 打包：`workspace:^` 已替换真实版本；cordis/dsh-tools 在 peerDependencies；registry 版本已对齐；tarball 解包 + loader 验证 PASS

> **自演化愿景**：时空可组合性最终指向自演化能力——智能体可检查当前运行时插件树，编写并挂载新临时插件扩展能力，任务完成后"干净"卸载，系统不会越运行越混乱。

---

## 5. 详细参考（按分类索引）

### 全景认知
| 主题 | 文件 |
|------|------|
| DSH 平台全景（预设模式/构建路径/生态/环境要求） | [references/01-overview/dsh-platform.md](references/01-overview/dsh-platform.md) |
| 核心理念 / Context 作用域 / DSH 魔改 | [references/01-overview/philosophy.md](references/01-overview/philosophy.md) |
| 插件系统认知模型（加载机制/形态正交/选型口诀/打包认知） | [references/01-overview/mental-models.md](references/01-overview/mental-models.md) |
| CLAUDE.md API/胶水公约 → 插件语境映射（直接用/转译/不适用） | [references/01-overview/api-contract.md](references/01-overview/api-contract.md) |

### 开发流程
| 主题 | 文件 |
|------|------|
| cordis_inspect_* 实时查询方法论（文档是地图/Inspect 是真相源） | [references/02-workflow/inspect-workflow.md](references/02-workflow/inspect-workflow.md) |
| 三种形态 / Service / Config / inject 完整模板 | [references/02-workflow/plugin-forms.md](references/02-workflow/plugin-forms.md) |
| 测试方法论（真实 Context 单测范式） | [references/02-workflow/testing.md](references/02-workflow/testing.md) |

### 运行时体系
| 主题 | 文件 |
|------|------|
| Fiber / effect / 生命周期 / HMR 行为 | [references/03-runtime/lifecycle.md](references/03-runtime/lifecycle.md) |
| 五种事件分发模式与 waterfall 语义 | [references/03-runtime/events.md](references/03-runtime/events.md) |
| DSH 事件目录（选择脑图 + 高频事件 + 精确契约获取） | [references/03-runtime/events-catalog.md](references/03-runtime/events-catalog.md) |
| Agent 循环生命周期（turn/step 事件流 + 生产者消费者矩阵） | [references/03-runtime/agent-lifecycle.md](references/03-runtime/agent-lifecycle.md) |
| 能力接缝 Seam（三角色模式：Definition/Provider/Consumer） | [references/03-runtime/seams.md](references/03-runtime/seams.md) |
| 身份接缝（Hook ↔ Tool 身份等式与运行时防御） | [references/03-runtime/identity-seam.md](references/03-runtime/identity-seam.md) |
| Hook ↔ Tool 数据传递六条通路（stdin/stdout/context/decision/事件/steer） | [references/03-runtime/hook-tool-data-flow.md](references/03-runtime/hook-tool-data-flow.md) |

### 能力挂载
| 主题 | 文件 |
|------|------|
| 能力挂载：模型工具 / 提示词 / 技能注册 / Client UI / 权限 | [references/04-capability/harness-integration.md](references/04-capability/harness-integration.md) |
| 工具执行管线（pre-execute→guards→execute→post→result 九阶段） | [references/04-capability/tool-pipeline.md](references/04-capability/tool-pipeline.md) |
| Client UI：Slot 选择脑图 / 注册协议 / 主题 / host.call | [references/04-capability/client-ui.md](references/04-capability/client-ui.md) |
| 动态插件：生命周期 / 双平台 Builtin / 版本授权 / 修复 | [references/04-capability/dynamic-plugins.md](references/04-capability/dynamic-plugins.md) |

### 交付运维
| 主题 | 文件 |
|------|------|
| 六种部署形态全景 / 七种部署流程 / 卸载 / 选择矩阵 | [references/05-deployment/deployment-overview.md](references/05-deployment/deployment-overview.md) |
| 打包 / cordis.yml / 部署 / npm pack / 发布 / 安装 / 诊断 PENDING | [references/05-deployment/packaging.md](references/05-deployment/packaging.md) |

### 实战经验
| 主题 | 文件 |
|------|------|
| 坑与规避（含实测案例，5 部分 42 个坑：工程/运行时/装配/部署 + 类型系统/DSH 补充/e2e 假阳性） | [references/06-experience/traps.md](references/06-experience/traps.md) |