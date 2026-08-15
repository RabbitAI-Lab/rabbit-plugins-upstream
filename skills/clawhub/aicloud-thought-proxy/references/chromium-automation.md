# Chromium 内核浏览器操控指南（通道 A）

适用于 Google Chrome / Edge / Chromium / Brave / Opera / 360 / QQ 浏览器等 Chromium 内核浏览器。

工具优先级：**chrome-mcp 连接器 > BrowserSkill / agent-browser 技能 > 其他浏览器自动化方案**。

## 1. chrome-mcp（首选）

chrome-mcp 是本环境的 MCP 连接器，提供"操控用户已打开的 Chrome"能力，天然保留用户的登录态与个人配置，最适合本技能（用户已登录网页版 AI）。

### 加载

chrome-mcp 工具属延迟加载工具，先用 ToolSearch 按工具名加载 schema：

```text
ToolSearch tool_names: [
  "mcp__chrome-mcp__chrome_navigate",
  "mcp__chrome-mcp__chrome_read_page",
  "mcp__chrome-mcp__chrome_click_element",
  "mcp__chrome-mcp__chrome_fill_or_select",
  "mcp__chrome-mcp__chrome_screenshot",
  "mcp__chrome-mcp__get_windows_and_tabs",
  "mcp__chrome-mcp__chrome_switch_tab"
]
```

若连接器显示 disconnected，提示用户在连接器管理页连接 chrome-mcp 后再继续（或降级到 BrowserSkill）。

### 常用操作序列

```text
1. 打开页面      chrome_navigate(url)
2. 查看标签页    get_windows_and_tabs / chrome_switch_tab
3. 读取内容      chrome_read_page / chrome_get_web_content（抓完整文本，含代码块）
4. 点击元素      chrome_click_element（优先用可见文本定位）
5. 输入文本      chrome_fill_or_select（输入框定位后填内容）
6. 截图检查      chrome_screenshot（确认页面状态 / 人机验证位置）
7. 页面脚本      chrome_javascript / chrome_console（高级操作）
```

### 发送消息到网页 AI 的标准流程

```text
1. chrome_navigate → 打开品牌对话 URL
2. 等待渲染（sleep 1-3s 或轮询读取）
3. chrome_read_page → 确认页面就绪（存在输入框 / 登录按钮 / 模式开关）
4. 若需登录 / 验证 → 告知用户手动完成，轮询页面状态
5. 设置模式：点击"深度思考 / 联网搜索"等开关（用文本定位）
6. chrome_fill_or_select → 在输入框填入消息文本
7. chrome_click_element → 点击发送按钮（或 chrome_javascript 模拟 Enter）
8. chrome_read_page → 读取 AI 回复（滚动到底部确保完整）
```

### 元素定位技巧

- 优先可见文本定位：按钮"发送"、"深度思考"、开关"联网搜索"。
- 输入框常用 `contenteditable` 或 `textarea[class*=textarea]`：可先用 chrome_javascript 检查 document 中的候选选择器。
- 回复区常是长滚动容器：用 chrome_javascript 执行 `document.querySelector(...).scrollTop = scrollHeight` 后重新读取。
- 避免硬编码 XPath；选择器变化时，用页面文本搜索（如"继续生成"按钮）兜底。

### 故障处理

- 页面未加载完 → 重新 chrome_read_page 并轮询。
- 登录态丢失 → 提示用户重新登录。
- 找不到发送按钮 → 尝试 Enter 键（chrome_keyboard 或 javascript 派发 KeyboardEvent）。
- 弹窗（dialog）→ chrome_handle_dialog 处理；广告遮罩 → chrome_click_element 关闭。

## 2. BrowserSkill / agent-browser（备选）

若 chrome-mcp 不可用：

1. 用 find-skills 搜索并安装 "agent-browser" 或 "BrowserSkill" 技能。
2. 按其 SKILL.md 的说明驱动浏览器（通常基于 Playwright / Puppeteer 或系统浏览器调试端口）。
3. 注意保留登录态：优先连接用户现有浏览器实例（如 `--remote-debugging-port` 启动并连接），或复用 profile 目录；否则需用户重新登录。
4. 若上述工具均缺失：**先征得用户同意**再安装，Agent 侧安装 + 浏览器侧小白指引见 `references/tool-installation.md`（chrome-mcp 扩展安装、npm 桥注册、常见问题排查）。
4. 其余操作序列与上文一致：打开 URL → 等渲染 → 读内容 → 设模式 → 输入 → 发送 → 读回复。

## 3. 通用兜底（无浏览器工具时）

若既无 chrome-mcp 也无浏览器技能：进入 SKILL.md 的**阶段 1.5**，先询问用户是否自动安装（不擅自安装）。可在用户同意后安装 chrome-mcp（`mcp-chrome-bridge` + 浏览器扩展）或轻量方案（如 Playwright，按 profile 复用方式连接用户浏览器）。安装细节与小白指引见 `references/tool-installation.md`。
