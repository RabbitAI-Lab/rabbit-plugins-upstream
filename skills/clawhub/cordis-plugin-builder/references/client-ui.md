# Client UI 深度：Slot 协议 / 主题 / 样式（实测 2026-08）

> Slot 树来自运行时 `Slots.listSubTree` 实测。Client 侧**先查树、再选位、后注册**——协议
> （single/list/keyed/chain）决定怎么写注册，选错位会 shadow 出厂 UI。

## 1. Slot 选择脑图（实测树）

```
要放什么 UI？
│
├─ 完整设置页          → settings.section (list, id+order+label)  ← 首选整页
│   └─ 单条偏好(轻)    → settings.general.item (list)
├─ 侧栏脚部小动作      → sidebar.footer.action (list)   ← 不要替换整个 sidebar
├─ 全屏浮层(提示/Toast)→ shell.overlay (list)
├─ 会话头部按钮        → conversation.session.header.actions (list)
├─ 轮次尾部补充内容    → conversation.chat.turnTail (chain, select 选择器)
├─ 输入区小控件        → conversation.input.left / .right (list)
├─ 输入区独立一行      → conversation.input.dock (list)
├─ 工具调用卡片定制    → tool.call.toolview (keyed, key=工具名)  ← 会替换默认卡
├─ 动态插件 Run 卡内   → tool.view.cordis (keyed, key='self' 唯一)
└─ 整列/整会话替换     → sidebar / conversation / conversation.session (single) ⚠️高风险
```

**红线**：
- `single` 位是"一个座位"——占据即**替换出厂 UI**（replaceRisk: shadows-shipped-ui）。默认不碰 root/sidebar/conversation/details。
- `keyed` 位按 key 分发；`tool.call.toolview` 的 key 是工具名，注册已有工具名会替换默认卡片。
- `chain` 位用 `select(owner)` 选择器路由；`conversation.composer` 是 composer 接管链。

## 2. 注册协议速查

```ts
// list 位：id + 可选 order/label（最常用）
slots.inject('settings.section', () => slots.register(
  { name: 'settings.section', id: 'my-page', order: 10, label: '我的页' },
  (props) => React.createElement('div', null, 'page body'),
))

// keyed 位：key 决定显示在哪
slots.inject('tool.call.toolview', () => slots.register(
  { name: 'tool.call.toolview', key: 'my_tool' },
  (props) => React.createElement('div', null, 'my tool card'),
))

// chain 位：select 返回匹配值或 null（null = 不接管）
slots.inject('conversation.chat.turnTail', () => slots.register(
  { name: 'conversation.chat.turnTail', select: (owner) => owner.kind === 'user' ? {} : null },
  (props) => React.createElement('div', null, 'tail'),
))
```

## 3. 从 Host 取数据（host.call）

Client 不能直接碰 Host 服务，走 Package 私有 JSON RPC：

```ts
// Host 半区
harness.handle('get-stats', async (args) => ({ count: 42 }))

// Client 半区
const result = await host.call('get-stats', { scope: 'all' })
```

- 只传 lossless JSON；不传函数/类实例/Context。
- `host.call` 失败先查：Host 方法名、当前 pluginRunId、JSON 参数、handler 内真实服务依赖。

## 4. 主题与样式

```ts
// 插件自有样式：styles.insert 返回 disposer，随运行清理
const dispose = styles.insert(`.my-card { color: var(--dsh-text-primary); }`)
ctx.effect(() => dispose)

// 全局主题覆盖（谨慎）：先查 Theme.listTokens，再按 light/dark 提供值
const theme = ctx.get('theme')
if (theme) {
  ctx.effect(() => theme.override('--dsh-brand', { light: '#000', dark: '#fff' }))
}
```

- **不要**操作 `document.body` / `window` / 硬编码产品 DOM 选择器。
- 颜色优先用主题 CSS 变量，而非硬编码色值。

## 5. Client Builtin 清单（实测）

`ctx` / `React`（仅 createElement，无 JSX）/ `host` / `styles` / `console`。
无 `window`/`document`/`fetch`/`process`——需要浏览器能力先查 Client Builtin Provider。

## 6. 常见失败排查

| 症状 | 先查 |
|---|---|
| UI 不出现 | Slot 名/协议查过没？id/key 正确？slots 服务存在（ctx.get）？ |
| 出厂 UI 不见了 | 占了 single 位或 keyed 已占用 key——换 additive 位 |
| 页面报错 | `client-render` 诊断 + stack；错误属于某次 Run，定义新 Package 修复 |
| host.call 失败 | 方法名 / pluginRunId / JSON 参数 / handler 依赖 |
