# 坑与规避（含实测案例）

> 以下坑均来自对 vendor/cordis v4.0.1 源码与教程的实测验证，非推测。

## 坑分类总览

```
┌─ 事件/分发 ────── waterfall 是分发非注册 · next(新值) 被忽略
├─ 依赖/生命周期 ── inject 缺失=静默 PENDING · 可选依赖误用 inject
├─ 装配/HMR ─────── 条目无 id=全量重挂 · HMR 三件套缺一静默
├─ 导出/Config ──── 默认导出丢 Config · Config 导普通对象无效
├─ 作用域/状态 ──── 服务命名冲突 · 全局变量绕过 Context
├─ 子进程/桥接 ──── 相对路径指向 CWD · 常驻进程僵尸 · stderr 吞掉
├─ 路径/构建 ────── Windows file:// 三斜杠 · paths 指向包目录 · .ts emit
└─ 装配/Windows ─── insert: 包裹 · 只改 patch 层 · junction 悬空
```

> 每个坑的完整症状/根因/规避见下文编号条目（31 个）。

## 1. waterfall：`next(新值)` 传参被静默忽略 ⚠️ 实测

- **现象**：监听器写 `next(text + suffix)`，下游收到的是**原始 args**，转换值丢失。
- **根因**：`next` 闭包捕获分发时的 args 数组；你传给 `next()` 的参数不参与 `cb(...args)`。
- **规避**：`const result = next()` 取下游返回值，包装后 `return`。
- **延伸**：`ctx.waterfall(name, fn)` 不是注册！`fn` 会被当成内层 next 立即执行（实测抛 `next is not a function`）。

## 2. 函数插件不能赋 `name` 属性 ⚠️ 实测

- **现象**：`Object.assign(fn, { name: 'x' })` 在 ES 严格模式抛 `TypeError: Cannot assign to read only property 'name'`。
- **规避**：模块级 `export const name = 'x'`；函数自身的 `name` 由声明自动获得。

## 3. `inject` 缺失 = 静默 PENDING，不是报错

- **现象**：插件不输出、进程状态码 0 静默退出，看似"没运行"。
- **根因**：PENDING 是合法状态——提供方可能稍后挂载；PENDING fiber 不保持事件循环活跃。
- **规避**：用 `FiberState.PENDING` 遍历 `ctx.registry` 诊断；确认 `cordis.yml` 里提供方条目存在。

## 4. cordis.yml 条目不带 `id` → HMR 全量重挂

- **现象**：编辑配置文件任意内容，所有插件都被重挂。
- **根因**：loader 按 `id` 对比条目；无 `id` 每次读文件生成新 id，视为删除+新增。
- **规避**：每个条目写稳定 `id`。

## 5. 默认导出插件丢失 Config schema

- **现象**：`export default { apply, Config }` 挂载后 config 校验不生效。
- **根因**：Loader 默认解包丢弃 `Config`（docs/postmortem/0001-acp-default-export-drops-inject.zh.md）。
- **规避**：只导出命名导出：`export const name` / `export function apply` / `export const Config`。

## 6. `Config` 导出普通对象无效

- **现象**：config 不校验，任何值都通过。
- **根因**：Cordis 接受 Standard Schema 验证器；普通对象不是 schema。
- **规避**：用 `@deepseek-ai/schemastery` 的 `Schema.object({...})`；类型与 schema 同名导出。

## 7. HMR 依赖三件套，缺一个就静默

- **现象**：改了文件不热重载。
- **根因**：HMR 插件 `inject` timer 服务（去抖）、经 logger 输出；两者缺失 → 永远 PENDING 且无提示。
- **规避**：同时挂 `cordis-plugin-logger-console` + `cordis-plugin-timer` + `cordis-plugin-hmr`。

## 8. 服务命名冲突

- **现象**：`ctx.myService` 类型/行为异常或覆盖现有服务。
- **根因**：服务名是扁平命名空间，`tools`/`llm`/`agents`/`sessions`/`skills` 等已被 harness 占用。
- **规避**：加辨识前缀；查询 `docs/subsystems/core.md` 的 `cordis-surface` 区块确认未占用。

## 9. 可选依赖误用 `inject`

- **现象**：某个可选能力缺失时插件永远不启动。
- **根因**：`inject` 是硬依赖，缺失即 PENDING。
- **规避**：可选依赖不 inject，用 `ctx.get('name')` 运行时探测（undefined 即无提供方）。

## 10. 忘记 disposer → 卸载泄漏

- **现象**：HMR 重载后旧资源（定时器/监听器/服务）仍在运行，行为叠加。
- **根因**：副作用未走 `ctx.effect()`/`ctx.on()`，fiber 卸载无法回卷。
- **规避**：一切注册走 effect/on 并返回 disposer；teardown 顺序敏感工作放同一 effect。

## 11. 子进程相对路径指向 CWD 而非插件目录

- **现象**：`child_process` 调用 `./script.py`，换个启动目录就 `ENOENT` 找不到文件。
- **根因**：相对路径相对 Node **当前工作目录**解析，不是插件源码目录。
- **规避**：`path.join(__dirname, './script.py')` 转绝对路径。

## 12. 常驻子进程未释放 → 僵尸进程

- **现象**：HMR 重载后旧 WebSocket/常驻进程仍存活，端口占用或行为叠加。
- **根因**：`new` 出来的常驻进程只启动、没在 `ctx.effect()` 里注册释放逻辑。
- **规避**：把底层进程的 kill/close 放进 `ctx.effect()` 的 disposer。

## 13. 子进程 stderr 未包装 → 静默失败

- **现象**：底层 Python 崩了，Harness 表现怪异但看不到原因。
- **根因**：Python 报错不会自动转为 Node 异常，stderr 被吞。
- **规避**：try-catch 包裹调用，stderr 经 `ctx.logger` 格式化输出（最好转 Cordis `Error`）。

---

# 第二部分：Windows 本地开发与装配（⚠️ 实测 2026-08，dsh-memory 构建）

## 14. `tsx -e` 不支持顶层 await

- **现象**：`npx tsx -e "await import(...)"` 报 `Top-level await is currently not supported with the "cjs" output format`，无任何输出。
- **根因**：`-e` 内联脚本按 cjs 处理。
- **规避**：验证脚本写成 `.ts` 文件再 `tsx scripts/xxx.ts`（文件按 package.json `type: module` 走 ESM）。

## 15. tsconfig `paths` 指向 `.d.ts` 文件 → tsx 运行时加载失败

- **现象**：tsc 通过（类型 OK），但 tsx 运行报 `ERR_MODULE_NOT_FOUND .../lib/types/context.ts`（.d.ts 内部相对 `.ts` 导入指向不存在的源码路径）。
- **根因**：paths 指到 `lib/types/index.d.ts`，tsx 按 paths 解析运行时入口，加载了 d.ts 而非可执行模块。
- **规避**：**paths 指向包目录**（`vendor/cordis` 而非 `lib/types/index.d.ts`）——tsc 读其 `types` 字段，tsx 读其 `main` 字段，两者自洽。

## 16. Windows junction 到 pnpm node_modules → SymbolicLink 悬空

- **现象**：`New-Item -ItemType Junction node_modules → <pnpm包>/node_modules` 后，部分 `@deepseek-ai/*` 目录 `Test-Path` 为 True 但内部文件缺失。
- **根因**：pnpm 的包链接是**相对 SymbolicLink**（`..\..\vendor\xxx`），从 junction 新基位置解析错位。
- **规避**：**逐包绝对 junction**：`node_modules/@deepseek-ai/<pkg>` → `D:/.../vendor/<pkg>`（Junction 类型目标绝对，可穿透）。

## 17. 未 start 的 Context 上 `await ctx.service` 永久 pending

- **现象**：`new Context()` + `new FakeTools(ctx)` 后 `await ctx.tools` 卡死无输出（超时）。
- **根因**：Service 需 fiber 启动才 resolve；裸 Context 上 await 服务永不返回。
- **规避**：验证/装配必须用 **`ctx.plugin(plugin, config)`**（cordis 启动 fibers）；`apply()` 直调只用于已就绪服务的单元场景。

## 18. Service 构造即注册（无需 ctx.provide）

- **现象**：按老习惯写 `ctx.provide(service)` 报类型错（provide 参数是 string）。
- **根因**：cordis v4 `Service` 子类 `constructor(ctx, name)` **构造即注册**（内部调 `ctx.reflect.provide`）。
- **规避**：`new XxxService(ctx, 'name')` 即完成注册，fiber 卸载自动反注册。

## 19. 常驻子进程句柄 → 验证脚本"超时"（跑完不退出）

- **现象**：验证脚本打印完所有结果但进程不退出（120s 超时 kill）。
- **根因**：child_process 的 stdin/stdout + readline 引用保持 event loop 存活。
- **规避**：验证脚本结尾显式 `process.exit(0)`（生产插件由 fiber disposer 管理，不受影响）。

## 20. `.ts` 扩展导入与 emit 冲突

- **现象**：源码用 DSH 风格 `import './x.ts'`（`allowImportingTsExtensions: true` 只能配 `noEmit`），构建 emit 报 TS5097。
- **规避**：构建配置开 **`rewriteRelativeImportExtensions: true`**（TS 5.7+），emit 时自动改写 `.ts` → `.js`。

## 21. DSH loader 原生加载 `.ts` 源码，无需构建 lib

- **现象**：tsdown 构建在独立目录失败（pnpm 嵌套链接缺失导致 CLI 依赖解析崩溃）。
- **根因**：独立目录的 node_modules 链接树不完整，构建工具无法解析传递依赖。
- **规避**：**cordis.yml 的 `name` 直接指向 `.ts` 源码文件**（loader 用 tsx 加载，DSH 原生支持）；lib 构建仅为正式 workspace 包选项。

## 22. `ctx.plugin` 不传 config → 默认空 → 运行参数缺失

- **现象**：插件加载成功但 Python 侧 `ModuleNotFoundError`（skillRoot 空）。
- **根因**：`ctx.plugin(plugin)` 未传 config，cordis 用 `{}` 默认 → 路径类配置全空。
- **规避**：`ctx.plugin(plugin, { skillRoot: '...', ... })` 显式传配置。

## 23. 跨语言桥接：snake_case ↔ camelCase 必须显式转换

- **现象**：TS 类型声明 `{ memoryId }` 但 Python 返回 `{ memory_id }`，运行时 `result.memoryId` 为 undefined（类型欺骗，tsc 不报错）。
- **根因**：桥接层直接透传未做字段名转换，类型标注与实际不符。
- **规避**：胶水层（Service 封装）显式做 snake→camel 转换 + 单独的类型转换函数，勿透传裸 RPC 结果。

## 24. DSH profile 装配：patch 插入语义 + file:// URL + HMR

- **现象**：cordis.patch.yml 裸写 `- id: memory` 被当「按 id 覆盖」而非「插入」，插件不加载；`name: 'E:/...'` 报 `ERR_UNSUPPORTED_ESM_URL_SCHEME`。
- **规避**：
  - 插入新条目用 **`- insert:`** 包裹（裸条目是覆盖语义）
  - Windows 绝对路径 name 写 **`file:///E:/...`**（三斜杠）
  - HMR：改 patch 无需重启 DSH，验证信号 = 常驻 python 进程 + 工具列表出现 `memory_*`

# 第三部分：001 笔记蒸馏补充（2026-08）

## 25. 配置补丁是整体替换，不是深度合并

- **现象**：patch 里只为插件写一个新字段，原有配置（如 API Key）直接消失。
- **根因**：Cordis patch 是**整体替换**该条目的配置，不合并已有字段。
- **规避**：patch 中必须带完整配置；或用 `!!js` 表达式从环境变量/上级配置读取缺失字段。

## 26. 全局变量绕过 Context → 幽灵状态 → HMR 失效

- **现象**：插件卸载/热重载后行为残留，系统越跑越乱，只能重启。
- **根因**：插件用了全局变量或未封装的外部 API，绕过 Context 的 Proxy 副作用追踪——卸载时框架无法撤销这些残留。
- **规避**：所有副作用（监听器/定时器/服务注册）一律走 `ctx.on()`/`ctx.effect()`；禁用模块级可变全局状态。

## 27. 异步初始化别写插件主体，放 `ready` 事件

- **现象**：插件加载时异步操作（文件/网络）竞态——依赖服务还没就绪就开始跑。
- **规避**：文件/网络等异步初始化放 **`ready` 事件**（应用完全启动 + 依赖插件加载完成后执行）。

# 第四部分：DSH profile 装配详细版蒸馏（2026-08，插件项目 docs/DSH-装配经验.md）

## 28. loader 验证必须 `ctx.plugin(Loader)`，不是 `new Loader(ctx)`

- **现象**：独立验证脚本 `new Loader(ctx)` 报 `Cyclic __proto__`（循环原型）。
- **根因**：loader 包的正确加载方式是作为插件 `ctx.plugin(Loader)`（cordis fiber 初始化），直接 new 破坏了原型链。
- **规避**：
  ```ts
  await ctx.plugin(Loader)                       // ✅
  await ctx.loader.create({ id, name, config })  // 然后 create + await
  ```
- **loader 包不在插件 node_modules 时的解析**：`createRequire('D:/.../apps/cli/package.json')`（harness 应用包）从依赖树解析。

## 29. profile 根 `cordis.yml` 启动时被重写为 `[]`

- **现象**：手动改了 `$DSH_HOME/profiles/<name>/cordis.yml`，重启后消失。
- **根因**：profile 根 cordis.yml 每次启动被程序重写为空列表，装配全靠 **patch 层**（`cordis.patch.yml`）。
- **规避**：**只改 patch 层**（`cordis.patch.yml`），不动 profile 根 cordis.yml。生效层序：bundle patch → profile patch → home patch → `--patch` 覆盖（后层优先）。

# 第五部分：技能注册与桥接扩展蒸馏（2026-08，E 系列）

## 30. 技能注册用 `ctx.skills.register()` 直注册，无需完整 provider

- **场景**：把本地 SKILL.md 注册为模型可见技能（非文件系统 provider 场景）。
- **做法**：`ctx.skills.register(SkillRegistration)`——`SkillRegistration = Omit<SkillDefinition, 'invocation'|'provider'> & { invocation?, provider? }`（含 name/description/content/source/resourceBase）。
- **要点**：
  - `ctx.skills` 是**可选依赖**：用 `ctx.get('skills')` 探测，缺失静默跳过（勿进 `inject`）
  - `content` = SKILL.md 全文；`resourceBase: { kind: 'directory', path }` 让模型可解析相对资源
  - 完整 `SkillProvider`（list/get）仅在需要动态目录/远程源时才实现；静态技能直注册更简单

## 31. DSH `Session` 公开面很薄，深度内容提取受限

- **现象**：想从 `agent.session` 读"最近用户消息"做自动存储，发现没有简单的 log/messages 读取方法。
- **根因**：`Session` 类 `private log` + `surface`（事件序号折叠视图），公开只有 `header`/`firstLiveSeq`/`surface`。
- **规避**：跨语言桥接的自动闭环用**可插拔提取回调**（默认占位 + 用户自定义）；深度解析需走 surface 事件模型（SessionEvent 折叠），标注为已知限制而非硬编码。
