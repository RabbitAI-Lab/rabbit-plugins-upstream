# 能力挂载：把插件能力真正挂进 DSH（实测契约）

> 前面的模板解决"插件结构"，本节解决"插件产出什么能力"——DSH 插件的价值最终体现在
> 模型可调用的工具、注入的提示词、注册的技能。契约来自运行时 inspect 实测（2026-08）。

## 能力挂载全景

```
                    ┌────────────── 插件产出什么能力 ──────────────┐
                    │                                             │
         ┌──────────▼──────────┐   ┌─────────────────────────────┐
         │ ① 模型工具 (Host)    │   │ ② 提示词 (Host)             │
         │ ctx.tools.register  │   │ ctx.systemPrompt            │
         │  defineTool(...)    │   │  .section / .variable / .tools│
         │  → 模型可调用        │   │  → 每次 step 前注入          │
         └──────────┬──────────┘   └──────────────┬──────────────┘
                    │                             │
         ┌──────────▼──────────┐   ┌──────────────▼──────────────┐
         │ ③ 技能 (Host)        │   │ ④ Client UI (浏览器)         │
         │ ctx.skills.register │   │ slots.register / styles      │
         │  → 会话目录可见      │   │ host.call ↔ harness.handle   │
         └────────────────────┘   └─────────────────────────────┘
```

**选择口诀**：模型要"调用"→ 工具；模型要"知道"→ 提示词/技能；用户要"看到/操作"→ Client UI。

## 1. 注册模型可调用工具（最常用，ctx.tools）

`ctx.tools` 是工具注册表 + 执行管线。插件用 `register(definition)` 注册，返回 disposer。

```ts
import { defineTool } from '@deepseek-ai/dsh-tools'

export function apply(ctx: Context) {
  // inject: ['tools']（硬依赖）或 ctx.get('tools') 探测后注册
  const dispose = ctx.tools.register(defineTool({
    name: 'my_tool',
    description: '一句话说清工具做什么（模型按此决定调用）',
    parameters: {
      // JSON Schema 风格：required 字段显式声明
      query: { type: 'string', required: true, description: '查询文本' },
      topK: { type: 'number', description: '数量上限（默认 5）' },
    },
    output: {
      schema: { type: 'object', additionalProperties: false, properties: { ... }, required: [...] },
      render: (_args, value) => [{ type: 'text', text: JSON.stringify(value, null, 2) }],
    },
    async execute(args) {
      // args 已被 defineTool 校验；返回 lossless JSON
      return { hits: [...] }
    },
  }))
  ctx.effect(() => dispose) // 注册必须挂 effect，卸载自动摘除
}
```

要点（实测）：
- `parameters` / `output.schema` 用 **JSON Schema 风格**（type/properties/required/additionalProperties），不是 schemastery。
- `output.render` 决定模型与 UI 看到的展示；`execute` 是业务结果——两者分离。
- `ctx.tools.register` 返回**精确 disposer**（取消注册），挂 `ctx.effect()` 托管。
- 重复注册同名工具、保留名 `run_code` 会失败；作用域内注册 shadow 全局。
- 可选依赖：`ctx.get('tools')` + undefined 检查；硬依赖：`inject: ['tools']`。

## 2. 注入提示词片段（ctx.systemPrompt）

`ctx.systemPrompt` 在每次模型 step 前组装提示词。插件可注册 section / variable / tools provider。

```ts
export function apply(ctx: Context) {
  // 注册一段提示词片段（可排序）
  ctx.effect(() => ctx.systemPrompt.section({
    name: 'my-plugin-guidance',
    order: 50,                 // 控制片段顺序（先注册先渲染，或用 order）
    content: '当用户问 X 时，优先使用 my_tool。',
  }))

  // 注册动态变量（每次组装时求值）
  ctx.effect(() => ctx.systemPrompt.variable('currentMode', (ctx) => 'creative'))
}
```

要点（实测）：
- `section()` / `variable()` 都返回**精确 disposer**，挂 `ctx.effect()`。
- 同层重复名称、非有限 order 抛错；作用域内 shadow 全局。
- `variable` 名字必须 `[a-z][a-z0-9_]*`；provider 返回 `undefined` 时引用该变量的 section 渲染失败。
- `systemPrompt.tools(provider)` 可注入工具 schema（高级场景）。

## 3. 注册技能（ctx.skills）

把本地 SKILL.md 注册为模型可见技能（详见 [traps.md](traps.md) #30）：

```ts
export function apply(ctx: Context) {
  const skills = ctx.get('skills')  // 可选依赖：缺失静默跳过
  if (skills === undefined) return
  ctx.effect(() => skills.register({
    name: 'my-skill',
    description: '触发句式：当需要 X 时使用',
    content: '# 技能正文…',        // SKILL.md 全文
    resourceBase: { kind: 'directory', path: '...' },
  }))
}
```

## 4. Client 侧（浏览器 UI，静态插件）

Client 半区是另一段 JS 代码（`code.client`），与 Host 通过 JSON RPC 通信：

```ts
// Client：注册 UI 到 Slot（先 cordis_inspect_query Slots.listSubTree 查协议）
export function apply(ctx: Context) {
  const slots = ctx.get('slots')
  if (slots === undefined) return
  slots.inject('target.slot', () => slots.register(
    { name: 'target.slot', id: 'my-view' },
    (props) => React.createElement('div', null, String(props.someValue)),
  ))
}
```

- Client 侧**无 JSX/TS/import**：纯 JS + `React.createElement`；可用 Builtin：`ctx` / `React` / `host` / `styles` / `console`。
- Host↔Client 私有通信：Host `harness.handle('method', fn)` ↔ Client `host.call('method', args)`，仅 lossless JSON。
- `styles.insert(css)` 插入插件自有样式，随运行清理。
- **先查 Slot 协议再写注册**：`Slots.listSubTree` 无 root 看树，有 root 看完整契约（single/list/keyed/chain）。

## 5. 权限边界（构建者须知）

- 插件执行受当前会话 sandbox / approval 策略约束——工具注册不豁免权限。
- 声明式装配的插件，其权限 = 装配它的 profile/会话的权限；预设不能放松自身约束（否则破坏沙箱边界）。
- 凭据/密钥走环境变量或 `ctx.credentials`，不硬编码；外部输入先校验再使用。

## 检查清单（能力挂载）

- [ ] 工具：`defineTool` 参数/输出 JSON Schema 齐全；`register` 返回挂 `ctx.effect()`；execute 返回 lossless JSON
- [ ] 提示词：section/variable 挂 effect；名字合法；无同层重复
- [ ] 技能：`ctx.get('skills')` 探测；content 为 SKILL.md 全文；resourceBase 指对
- [ ] Client：Slot 协议已查；React.createElement（无 JSX）；RPC 只传 JSON
- [ ] 权限：工具行为符合会话沙箱；无硬编码凭据
