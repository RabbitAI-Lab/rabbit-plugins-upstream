---
name: cordis-plugin-builder
description: 当需要构建 Cordis 可用插件（DeepSeek Harness 插件框架，从 0 到部署）或进行插件开发指导（教学、答疑、讲解构建流程）时使用；讲解 DSH 平台全景（一切皆插件/四种预设模式/构建路径）与 Cordis 元框架核心概念（Context/Service/Event/Fiber/inject/effect/Config/Scope）、三种代码形态、能力挂载（模型工具/提示词/技能/Client UI）、动态插件、多语言内核桥接、六种部署形态、cordis.yml 组合、HMR/bundle 部署、npm pack 打包与卸载流程。
whenToUse: 构建、编写、修改或部署 Cordis 插件（含把工具、服务、事件或提示词片段挂进 harness 运行时）；插件开发指导、教学或答疑；讲解 Cordis 元框架概念；排查插件加载失败（PENDING/FAILED）
---

# Cordis 插件构建指南：从元框架概念到部署

Cordis 是 DeepSeek Harness 底层的**元框架**（vendor 于 `vendor/cordis`，v4）——不是提供现成功能的框架，而是**组织能力的框架**：插件挂到共享 Context 上，Context 提供依赖注入、事件分发、生命周期管理。工具、LLM 适配器、文件访问、agent loop、skill 注册表都是插件。教程与 API 参考位于 DSH checkout 的 `docs/cordis-tutorial/` 与 `docs/cordis-primer.zh.md`。

> **平台全景**：DSH 是"一切皆插件"的开源 Coding Agent 运行框架，四种预设模式（标准/PTC/创造/极简）、
> 两条插件构建路径、社区生态与环境要求见 references/dsh-platform.md——写插件前先读它建立大局观。

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
| **Context** | 服务容器，Proxy 动态解析；插件的一切操作对象 | [philosophy.md](references/philosophy.md) |
| **Plugin** | 能力单元，三种形态：函数 / 对象 / Service 子类 | [plugin-forms.md](references/plugin-forms.md) |
| **Service** | 注册到 `ctx.<name>` 的能力，构造即注册，按名引用 | [plugin-forms.md](references/plugin-forms.md) |
| **inject** | 硬依赖声明，自动等待就绪、消失自动卸载（持续跟踪） | [plugin-forms.md](references/plugin-forms.md) |
| **Config** | Standard Schema（schemastery）校验的插件配置，先于实现 | [plugin-forms.md](references/plugin-forms.md) |
| **Fiber** | 插件生命周期单元：PENDING→ACTIVE→FAILED→UNLOADING | [lifecycle.md](references/lifecycle.md) |
| **effect/on** | 可逆副作用的唯一入口，返回 disposer，卸载自动回卷 | [lifecycle.md](references/lifecycle.md) |
| **Event** | 插件间通信，五种分发模式（emit/parallel/serial/bail/waterfall） | [events.md](references/events.md) |
| **Scope 派生** | extend（继承）/ isolate（隔离）/ intercept（拦截配置） | [philosophy.md](references/philosophy.md) |
| **Loader** | 声明式装配：cordis.yml entry 树 + HMR 事务重载 | [packaging.md](references/packaging.md) |

### 0.3 核心哲学（理解"为什么"）

- **时空可组合性**：插件副作用可完整撤销（时间）+ 依赖可响应出现/消失（空间）——HMR 的前提。
- **资源安全**：Context 是"插座"，插件是"插头"，卸载即拔掉，逆函数自动有序撤销（类比 Rust 所有权）。
- **服务 vs 事件分工**：服务解决"我要调用一种能力"；事件解决"我想介入一个过程"。

> 心智模型全景（三种加载机制 / 代码形态×部署形态正交 / 选型口诀 / 打包认知）见 references/mental-models.md。

---

## 1. 从零构建：8 步流程（按序执行）

1. **定位与命名**：插件放 DSH checkout 的 `packages/<domain>/<name>/`；包名 kebab-case（`@deepseek-ai/dsh-<name>`）；依赖 `@deepseek-ai/cordis`。
2. **选形态**：默认纯函数插件；要公开 `ctx.<service>` 能力才用 `Service` 子类；对象插件仅特殊场景。
3. **契约先行**：先写 `Config` schema（`@deepseek-ai/schemastery` 的 `Schema.object`），类型与 schema 同名导出，再写实现。
4. **声明依赖**：`export const inject = ['serviceName']` 声明硬依赖（自动等待就绪、消失自动卸载）；可选依赖用 `ctx.get('name')` 探测。
5. **注册副作用**：所有注册走 `ctx.effect()` / `ctx.on()`，必须返回 disposer；Fiber dispose 时自动回卷。**能力挂载**（模型工具 `ctx.tools.register(defineTool(...))`、提示词 `ctx.systemPrompt.section/variable`、技能 `ctx.skills.register`、Client UI Slot）见 references/harness-integration.md——这是插件产出"模型可见能力"的核心层。
6. **装配**：`cordis.yml` 加条目（带稳定 `id`），`config` 传参；`!!js` 表达式做运行时求值。
7. **验证**：先写失败测试再实现（红→绿）；运行确认，不凭声称完成。
8. **部署**：loader 启动（`node --import tsx vendor/cordis/bin.js`）；正式部署走 profile/bundle（`dsh plugin add` + `dsh.bundle` patch 层，见 [packaging.md](references/packaging.md)）；本地打包走 `npm pack`（tarball，见 packaging.md「npm pack 本地打包」）；HMR 热重载；模型场景用 `dsh-tool-cordis` 动态挂载。选部署形态先看 [deployment-overview.md](references/deployment-overview.md) 的六种形式全景与选择矩阵。

---

## 2. 格式与规格（硬约束）

- 导出项：`name`（显示名）、`apply(ctx, config)`、`Config`（schema）、`inject`（依赖数组，可选）。
- 服务名共用扁平命名空间：加辨识前缀（`tools`/`llm`/`agents`/`sessions` 等已被 harness 占用）；消费方只按名引用，不 import 提供方。
- `apply` 永远收到**完整且校验过**的 config；无效配置 → `ValidationError`，fiber 进 FAILED，插件绝不在配置不完整时启动。
- `Config` 必须用 Standard Schema（仓库用 schemastery）；导出普通对象作为 `Config` 无效。
- TS 声明合并：`declare module '@deepseek-ai/cordis' { interface Context { ... } }` 只提供类型，不产生运行时接线。
- 事件监听：用 `ctx.on` 注册（`ctx.waterfall(name, fn)` 是分发不是注册！）；waterfall 监听器必须 `next()` 并 return。

---

## 3. 关键坑（实测）

| 坑 | 正确做法 |
|---|---|
| 不查 Inspect，凭技能文档印象写 API | 文档是地图、Inspect 是真相源：写代码前 `cordis_inspect_list`→`query` 确认精确契约（流程见 [inspect-workflow.md](references/inspect-workflow.md)） |
| 把工具 `execute()` 当全部（忽略管线前后阶段） | 工具走九阶段管线：守卫/审批/规范化不归你管；策略挂 pre/post-execute（见 [tool-pipeline.md](references/tool-pipeline.md)） |
| `ctx.waterfall(name, fn)` 是分发不是注册 | 分发方法，最后一个参数是内层 `next`；监听器用 `ctx.on` 注册 |
| `next(新值)` 传参被忽略（args 被闭包捕获） | `const r = next()` 取下游返回值，包装后 `return` |
| `inject` 服务缺失 = 静默 PENDING（不崩溃不报错） | 用 `FiberState.PENDING` 诊断（见 references/packaging.md） |
| cordis.yml 条目不带 `id` | 每次读文件都视为删除+新增，HMR 全量重挂；务必给稳定 `id` |
| 给函数赋 `name` 属性 | ES 严格模式只读；用 `export const name = 'x'` 模块级导出 |
| tsconfig `paths` 指向 `.d.ts` 文件 | tsx 运行时加载 d.ts 内部相对 `.ts` 导入失败；**paths 指向包目录**（tsc 读 types / tsx 读 main） |
| 未 start 的 Context 上 `await ctx.service` | 永久 pending；验证/装配必须 **`ctx.plugin(plugin, config)`**（fiber 启动） |
| Windows 绝对路径插件 `name` | 写 `file:///E:/...`（三斜杠），裸 `E:/...` 报 `ERR_UNSUPPORTED_ESM_URL_SCHEME` |
| DSH profile patch 插入新条目 | 裸 `- id:` 是覆盖语义；插入必须用 `- insert:` 包裹 |

> 更多实测坑（tsx -e cjs 限制 / junction SymbolicLink 悬空 / 常驻进程句柄 / `.ts` emit / snake-camel 桥接等）见 [references/traps.md](references/traps.md) 第二部分。

---

## 4. 检查清单（交付前）

- [ ] Config schema 先于实现，字段类型齐全（required 无缺省）
- [ ] 写代码前已 `cordis_inspect_list`→`query` 确认每个用到的 Service/Event/Slot 契约（不猜 API、不凭文档印象；流程见 [inspect-workflow.md](references/inspect-workflow.md)）
- [ ] 每个 effect/on 都有 disposer；teardown 顺序敏感的放在同一 effect
- [ ] 服务名带前缀；`declare module` 声明合并已加
- [ ] 能力挂载：工具 `defineTool` JSON Schema 齐全且 register 挂 effect；提示词 section/variable 挂 effect；技能/Client UI 按 [harness-integration.md](references/harness-integration.md) 检查单
- [ ] 事件监听：先查 [events-catalog.md](references/events-catalog.md) 选事件与模式；waterfall 监听器记得 `next()` 并 return；精确契约来自 Event Provider 查询
- [ ] Client UI：Slot 协议已查（single/list/keyed/chain）；additive 位优先（settings.section/sidebar.footer.action 等）；不占 single 高危位；React.createElement 无 JSX
- [ ] 多语言内核：路径绝对化；子进程错误包装 + logger；常驻进程放 ctx.effect 释放；Windows 强制 UTF-8；snake/camel 显式转换
- [ ] cordis.yml 条目带 `id`；config 通过 schema 验证
- [ ] 测试覆盖正常路径 + 边界/失败用例（先红后绿）
- [ ] 运行验证输出可复现（demo 或测试全绿）
- [ ] 副作用可逆性测试：卸载后无幽灵状态（`ctx.effect` 全托管）
- [ ] 装配 DSH profile 检查单：`insert:` 包裹新条目、Windows 路径 `file:///` 三斜杠、装配后验证两信号（常驻子进程 + 工具列表）、只改 patch 层
- [ ] 卸载走配置移除（删 patch 行 → HMR 重装配），不是 `cordis_undefine`；先备份、后验证两信号、可回滚
- [ ] npm pack 打包：`workspace:^` 已替换真实版本；cordis/dsh-tools 在 peerDependencies；registry 版本已对齐；tarball 解包 + loader 验证 PASS

---

## 5. 详细参考（按学习路径排序）

| 主题 | 文件 |
|---|---|
| **概念层** | |
| DSH 平台全景（预设模式/构建路径/生态/环境要求） | `references/dsh-platform.md` |
| 核心理念 / Context 作用域 / DSH 魔改 | `references/philosophy.md` |
| cordis_inspect_* 实时查询方法论（文档是地图/Inspect 是真相源） | `references/inspect-workflow.md` |
| 插件系统认知模型（加载机制/形态正交/选型口诀/打包认知） | `references/mental-models.md` |
| CLAUDE.md API/胶水公约 → 插件语境映射（直接用/转译/不适用） | `references/api-contract.md` |
| **结构层** | |
| 三种形态 / Service / Config / inject 完整模板 | `references/plugin-forms.md` |
| 能力接缝 Seam（三角色模式：Definition/Provider/Consumer） | `references/seams.md` |
| Fiber / effect / 生命周期 / HMR 行为 | `references/lifecycle.md` |
| 五种事件分发模式与 waterfall 语义 | `references/events.md` |
| DSH 事件目录（选择脑图 + 高频事件 + 精确契约获取） | `references/events-catalog.md` |
| Agent 循环生命周期（turn/step 事件流 + 生产者消费者矩阵） | `references/agent-lifecycle.md` |
| **能力层** | |
| 能力挂载：模型工具 / 提示词 / 技能注册 / Client UI / 权限 | `references/harness-integration.md` |
| 工具执行管线（pre-execute→guards→execute→post→result 九阶段） | `references/tool-pipeline.md` |
| Client UI：Slot 选择脑图 / 注册协议 / 主题 / host.call | `references/client-ui.md` |
| 动态插件：生命周期 / 双平台 Builtin / 版本授权 / 修复 | `references/dynamic-plugins.md` |
| **交付层** | |
| 六种部署形态全景 / 七种部署流程 / 卸载 / 选择矩阵 | `references/deployment-overview.md` |
| 打包 / cordis.yml / 部署 / npm pack / 诊断 PENDING | `references/packaging.md` |
| 测试方法论（真实 Context 单测范式） | `references/testing.md` |
| **坑库** | |
| 坑与规避（含实测案例） | `references/traps.md` |
