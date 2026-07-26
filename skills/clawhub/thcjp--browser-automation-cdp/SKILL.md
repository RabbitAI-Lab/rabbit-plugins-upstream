---
slug: browser-automation-cdp
name: browser-automation-cdp
version: "1.0.0"
displayName: Browser Automation (CDP)
summary: 通过已登录的Edge或Chrome浏览器，利用Chrome DevTools Protocol执行JS渲染页面的导航、点击、截图及数据提取等自动化操作。
license: MIT-0
description: |-
  通过已登录的Edge或Chrome浏览器，利用Chrome DevTools Protocol执行JS渲染页面的导航、点击、截图及数据提取等自动化操作。

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: (cdp), chrome, 通过已登录的, devtools, 执行, automation, browser, 渲染页面的导
tags:
- Automation
- Research
tools:
- read
- exec
---

# Browser Automation (CDP)

> 通过用户已登录的浏览器（Edge/Chrome）执行自动化任务。
> 核心技术：CDP（Chrome DevTools Protocol），通过 WebSocket 与浏览器通信。

---

## 何时使用

优先用 `web_fetch`。以下情况才需要 CDP 自动化：

| 场景 | 是否需要 CDP |
| --- | --- |
| 静态 HTML 页面 | ❌ `web_fetch` 即可 |
| JS 渲染的页面（如 B站） | ✅ 需要 |
| 需要登录态的网站（已登录在你的浏览器里） | ✅ 需要 |
| 需要交互（点击、填表、滚动） | ✅ 需要 |
| 网站有反爬/风控 | ⚠️ 可能失败 |

---

## 架构概览

```text
Agent（我）
    ↓ require('./cdp-automation.js')
cdp-automation.js（连接管理器 + 浏览器抽象类）
    ↓ WebSocket (HTTP → CDP)
用户 Windows 浏览器（Edge:9222 / Chrome:9223）
    ↓ 执行 JS / 读 DOM / 点击
目标网站（bilibili / 小红书 / Minimax 等）
```

---

## 快速开始

### 1. 确保浏览器 remote debugging 已开启

**Edge（端口 9222）：**

```powershell
taskkill /F /IM msedge.exe /T
Start-Sleep 3
Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222

Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\Skill平台Browser\Edge"
```

**Chrome（端口 9223）：**

```powershell
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9223
```

### 2. 在任务中调用

```javascript
const { edge, chrome } = require('./browser-automation/cdp-automation.js');

// 基础用法
await edge.goto('https://目标网站.com');
const data = await edge./* REMOVED: eval */ (`document.title`);

// 点击 + 等待 + 提取
await edge.click('[class*="radio-filter__item"]');  // CSS 选择器
await edge.wait(5000);  // 等待 JS 渲染
const result = await edge./* REMOVED: eval */ (`提取数据的 JS `);

// 截图
const png = await edge.screenshot();  // 返回 base64
```

---

## API 参考

### `browser.goto(url)`

导航到指定 URL，等待页面加载完成（Page.loadEventFired + 额外 2s 等待 JS 渲染）。

```javascript
await edge.goto('https://space.bilibili.com/151190274/video');
```

### `browser./* REMOVED: eval */ (script)`

在页面上下文执行 JavaScript，返回结果。

```javascript
// 读取 DOM
const r = await edge./* REMOVED: eval */ (`document.title`);
console.log(r.result.value);

// 提取结构化数据
const r = await edge./* REMOVED: eval */ (`
    JSON.stringify(
        Array.from(document.querySelectorAll('.upload-video-card')).slice(0,5).map(c => ({
            title: c.querySelector('.bili-video-card__title')?.innerText,
            play: c.querySelector('.bili-cover-card__stat span')?.innerText
        }))
    )
`);
const videos = JSON.parse(r.result.value);
```

### `browser.click(selector)`

点击匹配选择器的第一个元素。通过计算元素中心坐标后用 `document.elementFromPoint` 模拟点击，支持任何可点击元素。

```javascript
await edge.click('[class*="radio-filter__item"]');  // 点击"最多播放"tab
```

### `browser.screenshot()`

截图当前页面，返回 PNG base64 字符串。可选保存到文件：

```javascript
const png = await edge.screenshot();
require('fs').writeFileSync('/tmp/screenshot.png', Buffer.from(png, 'base64'));
```

### `browser.wait(ms)`

显式等待，用于等待 JS 渲染或网络请求。

```javascript
await edge.click('.next-page');
await edge.wait(3000);  // 等待翻页后内容加载
```

### `browser.tabs()`

获取所有标签页列表（不含临时 JS 上下文）。

```javascript
const tabs = await edge.tabs();
const bTab = tabs.find(t => t.url.includes('bilibili.com'));
```

---

## 平台踩坑经验

### B站

**选择器（2025年有效）：**

* 视频卡片：`.upload-video-card`
* 标题：`.bili-video-card__title`
* 播放量：`.bili-cover-card__stat span`（第一个 span）
* "最多播放" tab：`[class*="radio-filter__item"]`，文字为"最多播放"

**重要：**

* B站页面完全 JS 渲染，`web_fetch` 拿到的是空壳
* 播放量字段在 DOM 里是文本（如"1890"），不是数字
* 排序需要 JS 端做：`parseInt(play.replace(/\D/g,''))`
* API 有 wbi 签名保护，直接调 API 不可行，必须走 DOM

### 小红书（Xiaohongshu）

**注意：**

* 有强反自动化检测（UA 检测、行为检测）
* 建议先测试是否能正常浏览，再尝试自动化
* 选择器可能随时变，建议先 `eval` 探索DOM结构

**处理方式：**

```javascript
// 先探索页面结构
const r = await xhs./* REMOVED: eval */ (`
    JSON.stringify({
        title: document.title,
        samples: Array.from(document.querySelectorAll('[class*="note"]')).slice(0,3).map(x => ({
            text: x.innerText?.substring(0,100),
            class: x.className?.substring(0,60)
        }))
    })
`);
console.log(JSON.parse(r.result.value));
```

### Minimax（平台：platform.minimaxi.com）

**查询目标：** Token Plan 配额（每 5 小时重置）

**关键路径（已验证）：**

1. 先导航到任意 minimaxi 页面（需是 `type=page` 的标签页）
2. 再导航到 `/user-center/basic-information`（可正常访问）
3. 用 JS 点击侧边栏的 `div`（注意：不是 `<a>` 标签）：

   javascript

   ```
   // 找到并点击"Token Plan"菜单项
   const r = await edge./* REMOVED: eval */ (`
     (function() {
       var allDivs = document.querySelectorAll('div');
       for (var d of allDivs) {
         if (d.innerText && d.innerText.trim() === 'Token Plan' && d.className.includes('cursor-pointer')) {
           d.click();
           return 'clicked';
         }
       }
       return 'not found';
     })()
   `);
   ```
4. 等待页面跳转后，提取配额数据

**实际路径规律（Next.js SPA）：**

* 账户管理侧边栏是 SPA 内部路由，URL 最终为 `/user-center/payment/token-plan`
* 直接 `Page.navigate` 到 `/user-center/token-plan` 会 404
* 正确做法：先进 `/user-center/basic-information`，再 JS 点击触发路由跳转

**配额数据所在位置（2026-03 验证）：**

* 套餐名：`Token Plan` / `Starter年度套餐`
* 剩余量：`可用额度：XXX次模型调用 / 5小时`
* 已用量：`XXX/600`
* 重置倒计时：页面显示

**示例提取脚本：**

```javascript
// 已在 basic-information 页面，点击 Token Plan 后执行：
const r = await edge./* REMOVED: eval */ (`(function(){
  var t = document.body.innerText;
  // 提取套餐信息
  var plan = t.match(/(Starter|Pro|Enterprise)[^\\n]*/)?.[0];
  var quota = t.match(/可用额度[：:][^\\n]*/)?.[0];
  var used = t.match(/(\\d+)\\/600/)?.[0];
  return JSON.stringify({plan, quota, used});
})()`);
```

---

## 已知限制

### CDP 连接复用问题

同一时间每个端口（9222/9223）只能有一个 WebSocket 连接。模块内部通过 `ConnectionManager` 管理，如果任务中途失败导致连接残留，需要重启浏览器 remote debugging。

### 等待时间不够

B站等 JS 密集型页面有时 5s 不够，可以手动加到 8-10s：

```javascript
await edge.wait(8000);
```

### Edge 被联想 Vantage 占用端口

如果 Edge 调试端口被联想预装软件（`msedgewebview2.exe`）的实例占用：

1. 杀掉 Vantage 服务：`taskkill /F /PID <pid>`
2. 再启动你的日常 Edge

### HTTP-only Cookie

`document.cookie` 拿不到 `HttpOnly` cookie。如果需要完整 cookie，考虑从浏览器文件直接读取 SQLite（需解决锁文件问题）。

### Next.js SPA 内部导航

有些页面（如 Minimax）使用 Next.js SPA 路由：

* 直接 `Page.navigate` 到 `/user-center/token-plan` 返回 404
* 需要先进一个已知可用的子页面（如 `/user-center/basic-information`），再用 JS 触发 div 点击来执行内部路由跳转
* 侧边栏菜单项大多是 `<div cursor-pointer>` 而非 `<a>`，不能用 CDP `Input.dispatchMouseEvent`，必须用 JS `element.click()`

---

## 模块文件位置

```text
~/.skill-platform/browser-automation/
├── cdp-automation.js   ← 核心模块（不用动）
└── SKILL.md           ← 本文件
```

调用时：

```javascript
const { edge, chrome } = require('~/.skill-platform/browser-automation/cdp-automation.js');
```

---

*最后更新：2026-03-24*
*踩坑：B站选择器 / Edge 端口占用 / CDP 连接复用 / Minimax SPA 导航 / div 菜单点击*

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
