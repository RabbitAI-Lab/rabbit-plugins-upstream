---
slug: cdp-browser-master
name: cdp-browser-master
version: "1.0.0"
displayName: CDP浏览器大师
summary: 解决反爬检测、选择器易变、SPA路由、等待不准四大痛点，附反检测与智能等待。
license: MIT
description: |-
  CDP浏览器大师是通过Chrome DevTools Protocol驱动已登录浏览器执行自动化任务的能力包。
  它不只给API列表，更解决四个高频痛点：反爬检测导致被封、网站改版选择器失效、
  Next.js等SPA内部路由难导航、固定sleep等待不准要么太快要么太慢。

  核心能力：
  - 反检测策略：UA伪装、WebGL指纹规避、行为拟人化、Cloudflare绕过思路
  - 选择器探测模式：先eval探索DOM结构再定位，多备选选择器降级
  - SPA导航模式：处理Next.js/React内部路由，先入可访问页再JS触发跳转
  - 智能等待：网络空闲检测替代固定sleep，既不快也不慢
  - Cookie获取：HttpOnly cookie的读取方案
  - 连接管理：端口复用、连接池、残留连接清理
  - 平台踩坑库：B站、小红书、Minimax等已验证路径

  适用场景：
  - JS渲染页面（B站、SPA应用）抓取
  - 需登录态的网站操作（已登录在你的浏览器里）
  - 需要交互（点击、填表、滚动）的自动化
  - 平台配额查询（如Minimax Token Plan）
  - 多标签页管理与数据提取

  差异化：
  - 原始版本只给基础API，本版补齐反检测与智能等待
  - 新增选择器探测模式（先探索再定位，多备选降级）
  - 新增SPA导航模式（解决Next.js内部路由404）
  - 新增连接管理器（端口复用、残留清理）
  - 新增HttpOnly Cookie获取方案
  - 增加FAQ与故障排查表

  触发关键词：CDP、浏览器自动化、Chrome、Edge、反爬、选择器、SPA、智能等待、Cookie
tags:
- 自动化
- 浏览器
- 数据抓取
tools:
- read
- exec
---

# CDP浏览器大师

通过用户已登录的浏览器（Edge/Chrome）执行自动化任务。核心技术：CDP（Chrome DevTools Protocol），通过WebSocket与浏览器通信。核心信条：**优先用web_fetch，CDP只用于JS渲染或需登录态的场景；先探测再定位，多备选降级。**

## 四大痛点与对策

| 痛点 | 典型表现 | 本skill对策 |
|:-----|:---------|:------------|
| 反爬检测 | 被Cloudflare拦、被识别为机器人 | 反检测策略 + 行为拟人化 |
| 选择器易变 | 网站改版选择器全失效 | 探测模式 + 多备选降级 |
| SPA路由难导航 | 直接navigate到子路由404 | 先入可访问页再JS触发跳转 |
| 等待不准 | sleep太短没渲染完，太长浪费时间 | 网络空闲检测替代固定sleep |

---

## 何时用CDP

优先用`web_fetch`。以下情况才用CDP：

| 场景 | 是否需要CDP |
|:-----|:------------|
| 静态HTML页面 | 不需要，web_fetch即可 |
| JS渲染页面（如B站） | 需要 |
| 需登录态的网站 | 需要 |
| 需要交互（点击、填表、滚动） | 需要 |
| 网站有反爬/风控 | 可能失败，需反检测策略 |

---

## 架构概览

```text
Agent
  ↓ require('./cdp-automation.js')
连接管理器（端口复用 + 残留清理）
  ↓ WebSocket (HTTP → CDP)
用户浏览器（Edge:9222 / Chrome:9223）
  ↓ 执行JS / 读DOM / 点击
目标网站
```

---

## 快速开始

### 1. 开启浏览器远程调试

**Edge（端口9222）：**
```powershell
taskkill /F /IM msedge.exe /T
Start-Sleep 3
Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222
```

**Chrome（端口9223）：**
```powershell
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9223
```

### 2. 调用

```javascript
const { edge, chrome } = require('./cdp-automation.js');

await edge.goto('https://目标网站.com');
const data = await edge.eval(`document.title`);
await edge.click('[class*="radio-filter__item"]');
await edge.waitNetworkIdle();  // 智能等待
const result = await edge.eval(`提取数据的JS`);
const png = await edge.screenshot();
```

---

## API参考

### `browser.goto(url)`

导航到指定URL，等待页面加载完成（Page.loadEventFired + 额外2s等待JS渲染）。

```javascript
await edge.goto('https://space.bilibili.com/151190274/video');
```

### `browser.eval(script)`

在页面上下文执行JavaScript，返回结果。

```javascript
// 读取DOM
const r = await edge.eval(`document.title`);
console.log(r.result.value);

// 提取结构化数据
const r = await edge.eval(`
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

点击匹配选择器的第一个元素。通过计算元素中心坐标后用`document.elementFromPoint`模拟点击。

```javascript
await edge.click('[class*="radio-filter__item"]');
```

### `browser.screenshot()`

截图当前页面，返回PNG base64字符串。

```javascript
const png = await edge.screenshot();
require('fs').writeFileSync('/tmp/screenshot.png', Buffer.from(png, 'base64'));
```

### `browser.wait(ms)`

显式等待，用于等待JS渲染或网络请求。

```javascript
await edge.wait(3000);
```

### `browser.waitNetworkIdle(timeout)`

**智能等待**：检测网络空闲（无请求持续500ms）后继续，替代固定sleep。既不会太快也不会太慢。

```javascript
await edge.click('.next-page');
await edge.waitNetworkIdle(10000);  // 最多等10秒，网络空闲即继续
```

### `browser.tabs()`

获取所有标签页列表（不含临时JS上下文）。

```javascript
const tabs = await edge.tabs();
const bTab = tabs.find(t => t.url.includes('bilibili.com'));
```

---

## 反检测策略

> 反爬检测是CDP自动化第一大拦路虎。

### 检测维度与规避

| 检测维度 | 网站怎么查 | 规避策略 |
|:---------|:-----------|:---------|
| User-Agent | 读取navigator.userAgent | 用真实浏览器（已登录的Edge/Chrome），UA天然真实 |
| WebDriver标记 | navigator.webdriver=true | 启动参数加`--disable-blink-features=AutomationControlled` |
| WebGL指纹 | 读取WebGL渲染器信息 | 用真实浏览器，指纹天然真实 |
| 鼠标行为 | 检测鼠标轨迹是否直线 | 用`elementFromPoint`模拟点击 + 加随机偏移 |
| 操作速度 | 检测操作间隔过短 | 操作间加`waitNetworkIdle` + 随机延迟 |
| Headless检测 | 检测是否无头模式 | 用有头模式（已登录浏览器） |

### 启动参数推荐

```powershell
# Edge反检测启动
Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" `
  --remote-debugging-port=9222 `
  --disable-blink-features=AutomationControlled `
  --disable-features=IsolateOrigins,site-per-process
```

### 行为拟人化

```javascript
// 不要瞬间连续操作
await edge.click('.btn');
await edge.wait(500 + Math.random() * 1000);  // 随机500-1500ms
await edge.click('.next');
await edge.waitNetworkIdle(10000);
```

### Cloudflare绕过思路

```text
1. 用真实已登录浏览器（非Headless）
2. 加--disable-blink-features=AutomationControlled
3. 操作间加随机延迟（拟人化）
4. 首次访问后等Cloudflare验证页通过（waitNetworkIdle）
5. 复用已通过验证的会话Cookie
```

> 注意：强反爬站点（如小红书）可能仍失败。建议先测试能否正常浏览，再尝试自动化。

---

## 选择器探测模式

> 网站改版选择器就失效。先探测再定位，多备选降级。

### 探测流程

```javascript
// 第一步：先eval探索DOM结构
const structure = await edge.eval(`
    JSON.stringify({
        title: document.title,
        samples: Array.from(document.querySelectorAll('[class*="note"]')).slice(0,3).map(x => ({
            text: x.innerText?.substring(0,100),
            class: x.className?.substring(0,60),
            tag: x.tagName
        }))
    })
`);
console.log(JSON.parse(structure.result.value));

// 第二步：根据探测结果写精确选择器
// 第三步：提供多备选，降级匹配
```

### 多备选选择器

```javascript
async function robustFind(browser, candidates) {
    for (const selector of candidates) {
        const found = await browser.eval(`
            document.querySelector('${selector}') ? true : false
        `);
        if (found.result.value) {
            return selector;  // 第一个命中的就用
        }
    }
    throw new Error(`所有备选选择器都未命中: ${candidates.join(', ')}`);
}

// 使用：从最精确到最宽松
const selector = await robustFind(edge, [
    '.bili-video-card__title',           // 精确class
    '[class*="video-card"] [class*="title"]',  // 模糊class
    'h3.title',                           // 语义tag
    'a[href*="/video/"]'                  // 属性选择器
]);
```

### 选择器韧性原则

- 优先用`[class*="xxx"]`模糊匹配（网站加哈希后缀也能命中）
- 避免用`nth-child`等位置选择器（布局一变就错）
- 用`data-*`属性（业务标识比class稳定）
- 提供语义备选（如`h3.title`、`a[href*="/video/"]`）

---

## SPA导航模式

> Next.js/React等SPA内部路由，直接`Page.navigate`到子路由会404。

### 正确做法

```javascript
// 错误：直接导航到子路由（404）
await edge.goto('https://app.com/user-center/token-plan');  // 404

// 正确：先入可访问页，再JS触发内部跳转
await edge.goto('https://app.com/user-center/basic-information');  // 可访问
await edge.waitNetworkIdle();

// 用JS点击侧边栏菜单（注意：可能是div不是a）
await edge.eval(`
    (function() {
        var allDivs = document.querySelectorAll('div');
        for (var d of allDivs) {
            if (d.innerText && d.innerText.trim() === 'Token Plan'
                && d.className.includes('cursor-pointer')) {
                d.click();
                return 'clicked';
            }
        }
        return 'not found';
    })()
`);
await edge.waitNetworkIdle();  // 等待SPA路由跳转完成
```

### SPA导航规律

- 侧边栏菜单多是`<div cursor-pointer>`而非`<a>`
- 不能用CDP `Input.dispatchMouseEvent`，必须用JS `element.click()`
- 跳转后URL会变但页面不刷新（纯前端路由）
- 跳转后用`waitNetworkIdle`等待数据加载

---

## Cookie获取方案

### 普通Cookie

```javascript
const cookies = await edge.eval(`document.cookie`);
// 只能拿到非HttpOnly的cookie
```

### HttpOnly Cookie

`document.cookie`拿不到HttpOnly cookie。方案：

```javascript
// 方案1：用CDP的Network.getCookies（推荐）
const cdpSession = await edge.getCDPSession();
const { cookies } = await cdpSession.send('Network.getCookies', {
    urls: ['https://目标网站.com']
});
// cookies包含HttpOnly的

// 方案2：从浏览器SQLite文件读（需解决锁文件问题）
// Edge: %LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cookies
// Chrome: %LOCALAPPDATA%\Google\Chrome\User Data\Default\Cookies
```

---

## 连接管理

### 端口复用

同一时间每个端口（9222/9223）只能有一个WebSocket连接。`ConnectionManager`管理复用：

```javascript
// 模块内部自动复用，无需手动管理
const { edge } = require('./cdp-automation.js');
// 多次调用共享同一连接
await edge.goto(url1);
await edge.goto(url2);  // 复用连接
```

### 残留连接清理

任务中途失败可能导致连接残留：

```javascript
// 清理残留连接
async function cleanupConnection(browser) {
    try {
        await browser.close();
    } catch (e) {
        // 连接已断，忽略
    }
}

// 重启浏览器远程调试（极端情况）
async function restartDebugging(port) {
    // 杀掉占用端口的进程
    const { exec } = require('child_process');
    exec(`taskkill /F /FI "PID eq ${getPidOnPort(port)}"`, () => {
        // 重新启动浏览器
    });
}
```

### 端口被占用排查

```powershell
# 查看端口占用
netstat -ano | findstr :9222

# 杀掉占用进程（如联想Vantage的msedgewebview2.exe）
taskkill /F /PID <pid>

# 再启动你的Edge
```

---

## 平台踩坑库

### B站

**选择器（已验证）：**
- 视频卡片：`.upload-video-card`
- 标题：`.bili-video-card__title`
- 播放量：`.bili-cover-card__stat span`（第一个span）
- "最多播放"tab：`[class*="radio-filter__item"]`

**要点：**
- B站页面完全JS渲染，`web_fetch`拿到的是空壳
- 播放量字段在DOM里是文本（如"1890"），需`parseInt(play.replace(/\D/g,''))`
- API有wbi签名保护，直接调API不可行，必须走DOM

### 小红书

**注意：**
- 有强反自动化检测（UA检测、行为检测）
- 建议先测试是否能正常浏览，再尝试自动化
- 选择器可能随时变，用探测模式先探索

```javascript
// 先探索页面结构
const r = await edge.eval(`
    JSON.stringify({
        title: document.title,
        samples: Array.from(document.querySelectorAll('[class*="note"]')).slice(0,3).map(x => ({
            text: x.innerText?.substring(0,100),
            class: x.className?.substring(0,60)
        }))
    })
`);
```

### Minimax（platform.minimaxi.com）

**查询目标：** Token Plan配额（每5小时重置）

**已验证路径：**
1. 先导航到任意minimaxi页面（需是`type=page`的标签页）
2. 再导航到`/user-center/basic-information`（可正常访问）
3. 用JS点击侧边栏的`div`（注意：不是`<a>`标签）触发SPA路由
4. 等待跳转后提取配额数据

**实际路径规律（Next.js SPA）：**
- 账户管理侧边栏是SPA内部路由，URL最终为`/user-center/payment/token-plan`
- 直接`Page.navigate`到`/user-center/token-plan`会404
- 正确做法：先进`/user-center/basic-information`，再JS点击触发路由跳转

**配额数据位置：**
- 套餐名：`Token Plan` / `Starter年度套餐`
- 剩余量：`可用额度：XXX次模型调用 / 5小时`
- 已用量：`XXX/600`

**提取脚本：**
```javascript
const r = await edge.eval(`(function(){
  var t = document.body.innerText;
  var plan = t.match(/(Starter|Pro|Enterprise)[^\\n]*/)?.[0];
  var quota = t.match(/可用额度[：:][^\\n]*/)?.[0];
  var used = t.match(/(\\d+)\\/600/)?.[0];
  return JSON.stringify({plan, quota, used});
})()`);
```

---

## 边界情况与陷阱

- **CDP连接复用**：每端口同时只能一个WebSocket，模块内ConnectionManager管理，失败需重启浏览器
- **等待时间不够**：JS密集页面5s可能不够，用`waitNetworkIdle`智能等待或手动加到8-10s
- **Edge被联想Vantage占用端口**：杀掉`msedgewebview2.exe`实例再启动你的Edge
- **HttpOnly Cookie**：`document.cookie`拿不到，用CDP `Network.getCookies`
- **Next.js SPA内部导航**：直接navigate到子路由404，需先入可访问页再JS点击
- **div菜单点击**：侧边栏菜单多是`<div cursor-pointer>`，不能用CDP鼠标事件，必须JS `element.click()`
- **反爬升级**：网站可能随时加强检测，定期验证自动化是否仍有效

---

## FAQ

**Q：什么时候该用CDP而不是web_fetch？**
A：JS渲染页面、需登录态、需交互（点击/填表）时用CDP。静态HTML用web_fetch即可。

**Q：被Cloudflare拦了怎么办？**
A：用真实已登录浏览器（非Headless），加`--disable-blink-features=AutomationControlled`，操作间加随机延迟，首次访问等验证页通过后复用Cookie。

**Q：选择器经常失效怎么办？**
A：用探测模式——先eval探索DOM结构再定位。提供多备选选择器（从精确class到模糊`[class*="xxx"]`到语义tag到属性选择器）降级匹配。

**Q：Next.js SPA子路由404怎么解决？**
A：直接navigate会404。先进入可访问的父页面（如`/user-center/basic-information`），再用JS点击侧边栏div触发内部路由跳转。

**Q：固定sleep该等多久？**
A：别用固定sleep。用`waitNetworkIdle`智能等待——检测无请求持续500ms即继续，既不快也不慢。

**Q：怎么拿HttpOnly Cookie？**
A：`document.cookie`拿不到。用CDP的`Network.getCookies`命令，或从浏览器SQLite文件读（需解决锁文件）。

**Q：CDP连接断了怎么办？**
A：模块内ConnectionManager会清理。极端情况重启浏览器远程调试——杀掉占用端口的进程再重新启动。

---

## 故障排查

| 症状 | 可能原因 | 解决 |
|:-----|:---------|:-----|
| 连接9222失败 | 端口被占/浏览器未起 | netstat查端口，taskkill清残留，重启浏览器 |
| eval返回空 | 页面未渲染完 | 用waitNetworkIdle替代固定sleep |
| click无反应 | 选择器未命中/元素不可点 | 探测模式验证选择器，用elementFromPoint |
| 被反爬拦截 | 检测到自动化 | 加反检测启动参数，行为拟人化，复用已验证会话 |
| SPA子路由404 | 直接navigate SPA路由 | 先入可访问页再JS触发跳转 |
| Cookie缺失 | HttpOnly拿不到 | 用CDP Network.getCookies |
| 连接残留 | 任务中途失败 | 重启浏览器远程调试 |
| 截图空白 | 页面未加载完 | 先waitNetworkIdle再screenshot |

---

## 模块文件位置

```text
~/.skill-platform/browser-automation/
├── cdp-automation.js   ← 核心模块（不用动）
└── SKILL.md            ← 本文件
```

调用时：
```javascript
const { edge, chrome } = require('~/.skill-platform/browser-automation/cdp-automation.js');
```

---

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows（Edge/Chrome路径示例为Windows，macOS/Linux类似）
- **浏览器**：Microsoft Edge 或 Google Chrome（已安装并可启动远程调试）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需（运行cdp-automation.js） | nodejs.org |
| Edge/Chrome | 浏览器 | 必需 | 系统自带或官网下载 |
| cdp-automation.js | 模块 | 必需 | 随skill提供 |

### API Key 配置
- 本skill基于本地浏览器自动化，无需额外API Key
- 涉及需登录的网站时，使用用户已登录的浏览器会话（无需配置凭证）

### 可用性分类
- **分类**：MD+EXEC（Markdown指令 + Node.js脚本执行）
- **说明**：通过自然语言指令驱动Agent调用cdp-automation.js控制浏览器执行自动化
