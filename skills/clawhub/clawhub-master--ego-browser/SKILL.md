---
name: ego-browser
description: ego-lite Windows 版浏览器自动化 Skill——让 AI Agent 通过自然语言控制浏览器，完成登录、抓取、表单填写、多 Space 并行任务。
tags: ["browser", "automation", "agent", "windows", "playwright"]
---

# ego-browser（Windows 版）

> ego-lite Windows 版的核心 Skill，让任何 AI Agent 通过自然语言驱动浏览器。
> 基于 Playwright + CDP Accessibility 构建，跨 Space 隔离，不抢占你的标签页。

## 核心能力

- **语义快照**：`snapshotText()` 从 accessibility tree 生成紧凑语义树，几十个 token vs 原始 DOM 上万 token
- **Space 隔离**：每个任务在独立 Space 中运行，Cookie/登录态持久化，不干扰你正常浏览
- **JavaScript 执行**：`js()` 在页面上下文直接执行，支持复杂 DOM 操作
- **多 Space 并行**：同一浏览器进程内多个 Space 并行，内存占用极低
- **Chrome 登录态继承**：复用 `storageState` 文件，无需重新登录

## 适用场景

- 已登录后台（SaaS、CRM、内部系统）
- 需要点击/填表/翻页的重复性任务
- 多站点并行抓取
- 需要验证码/支付确认时 Agent 会暂停等你

## 使用方式

### 方式一：运行脚本文件（Windows 推荐）

```bash
node D:\openclaw-data\workspace\ego-lite-windows\src\cli.js run task.js
```

### 方式二：管道输入

```powershell
Get-Content task.js | node D:\openclaw-data\workspace\ego-lite-windows\src\cli.js run -
```

### 方式三：直接调用（供其他 Skill/Agent 调用）

```javascript
import { runtime } from './core/runtime.js';
import { buildHelpers } from './run.js';
// 在 VM 中运行 agent 脚本
```

## 全局 Helper API

所有函数直接在脚本作用域调用，无需 import。

### Space 管理

```javascript
// 创建或进入一个 Space（每个任务对应一个 Space）
const task = await useOrCreateTaskSpace('搜索 GitHub Issues')

// 列出所有活跃 Space
const spaces = await listTaskSpaces()

// 关闭 Space（登录态自动持久化）
await closeTaskSpace('搜索 GitHub Issues')

// 任务完成，关闭并清理
await completeTaskSpace('搜索 GitHub Issues')
```

### 页面导航

```javascript
// 打开或复用当前 Space 的标签页
await openOrReuseTab('https://github.com', { wait: true, timeout: 20 })

// 导航并等待 load
await gotoAndWait('https://github.com/issues', { timeout: 20 })

// 强制新建标签页
await newTab('https://google.com')

// 获取当前标签页信息
const tab = await currentTab()
// tab = { tabId: '...', url: '...' }
```

### 语义快照（核心）

```javascript
// 获取当前页面的语义快照
const snap = await snapshotText()
// 返回格式化的文本，每行：@N [role] "name"

await cliLog(snap)

// 示例输出：
// Page: https://github.com
// Title: GitHub
// @0 [button] "Sign in"
// @1 [link] "Issues"
// @2 [textbox] "Search or jump to..."
```

### 元素操作

```javascript
// 点击引用元素
await click('@1')

// 双击
await doubleClick('@2')

// 悬停
await hover('@3')

// 向输入框填充文本（自动处理 focus/clear）
await fillInput('@4', '张三')

// 按键
await pressKey('Enter')
await pressKey('Escape')
await pressKey('Tab')
```

### JavaScript 执行

```javascript
// 在页面上下文执行 JS（推荐 String.raw 语法）
const title = await js(`document.title`)

// 复杂操作用 IIFE
const links = await js(String.raw`
  [...document.querySelectorAll('a')]
    .map(a => ({ text: a.innerText, href: a.href }))
`)
```

### 输出

```javascript
// 标准输出（Agent 脚本的唯一输出通道）
await cliLog('任务完成')
await cliLog(JSON.stringify(result))
```

### 帮助

```javascript
// 查看某个 helper 的用法
await cliLog(await help('click'))
```

## 典型任务示例

### 搜索 GitHub Issues

```javascript
const task = await useOrCreateTaskSpace('github-issue-search')

await openOrReuseTab('https://github.com', { wait: true, timeout: 20 })
cliLog(await snapshotText())

// 点击 Sign in 链接
await click('@0')  // Sign in button
cliLog(await snapshotText())

// 关闭
await closeTaskSpace('github-issue-search')
```

### 并行多站点抓取

```javascript
// 任务1：GitHub
const t1 = await useOrCreateTaskSpace('scrape-github')
await openOrReuseTab('https://github.com/trending')
cliLog(await snapshotText())
await completeTaskSpace('scrape-github')

// 任务2：Hacker News（在同一脚本顺序执行，或另起脚本并行）
const t2 = await useOrCreateTaskSpace('scrape-hn')
await openOrReuseTab('https://news.ycombinator.com')
cliLog(await snapshotText())
await completeTaskSpace('scrape-hn')
```

## 规则

1. **先 `snapshotText()` 再操作**——每次页面变化后重新快照
2. **`@N` 只对最近一次快照有效**——导航/刷新/表单提交后必须重新快照
3. **不要直接操作原始 DOM**——除非 `js()` 是唯一方案
4. **每个任务创建独立 Space**——不要跨 Space 共享 ref
5. **遇到高危操作（支付/删除/发布）暂停等确认**
6. **新站点操作后把经验写入 learnings/**

## 文件结构

```
D:\openclaw-data\workspace\ego-lite-windows\
├── src/
│   ├── cli.js              # CLI 入口
│   ├── run.js              # 脚本执行器（VM 注入 helpers）
│   ├── helpers.js          # helper 函数（已注入到 VM）
│   └── core/
│       ├── runtime.js      # 浏览器生命周期管理
│       ├── context-manager.js  # Space ↔ BrowserContext 映射
│       ├── page-manager.js     # 标签页管理
│       ├── snapshot.js         # CDP Accessibility 快照
│       ├── ref-table.js        # @N → backendDOMNodeId 映射
│       ├── actions.js          # click/fillInput/hover
│       └── eval.js             # js() 页面上下文执行
├── skill/ego-browser/
│   ├── SKILL.md            # 本文件
│   └── learnings/          # 站点经验积累
└── test/
```

## 健康评分

- Snapshot 生成正确性：✅
- click/fillInput 稳定性：✅
- Space 隔离：✅
- storageState 持久化：✅
- Windows IME 兼容：✅

**当前状态：SSS 级（Step 3/8 完成）**
