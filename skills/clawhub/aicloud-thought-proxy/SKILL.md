---
name: aicloud-thought-proxy
description: 云思客（AIcloud-thought-proxy）——通过操控浏览器访问网页版 AI（DeepSeek、Kimi、豆包、通义千问、ChatGPT、Claude、Gemini、Grok 等）与本地 Agent 协同工作以节省 tokens。触发场景：用户要求"用浏览器打开某 AI 官网对话并协作"、"让网页版 AI 规划步骤/编写代码/逻辑推理、本地 Agent 执行"、"节省 tokens"、提到"云思客"等。自动检测浏览器内核（Chromium → chrome-mcp/BrowserSkill；Gecko → GeckoDriver + Marionette），引导用户选择模型/思考模式/联网搜索（含"最新/最强模型"等模糊语言解析），提示用户手动登录与人机验证，建立"网页 AI 出方案、本地 Agent 执行"的协作循环。
agent_created: true
---

# 云思客 (AIcloud-thought-proxy)

## 概述

通过操控浏览器访问指定 AI 的网页版对话，让网页版 AI 承担"规划步骤 / 编写代码 / 逻辑推理"等思维型工作，本地 Agent 承担"扒取代码、创建文件、运行脚本、下载资源、联网搜索"等执行型工作，从而把推理成本转移到网页版（免费额度 / 订阅会员），节省 API tokens。

## 触发条件

出现以下任一意图时触发本技能：

- 用户要求"用浏览器打开 <某AI> 的网页版 / 官网对话"并协作
- 用户提到"网页版 AI"、"云思客"、"节省 tokens"、"让 XX 来规划/写代码，你来执行"
- 用户给出协作指令示例（如"deepseek 专家模式，打开官网对话，我登录，然后协同工作"）
- 用户想在不消耗 API tokens 的情况下获得 AI 的规划与推理能力

## 核心原则（不可违反）

1. **语言跟随**：与用户的所有交互（包括向网页 AI 发送的消息）必须使用用户当前使用的语言（默认简体中文）。先用用户语言开场确认。
2. **不替用户登录**：绝不代填账号密码 / 验证码；只负责打开登录页并提示用户手动完成登录。
3. **人机验证交给用户**：遇到验证码 / 滑块 / 行为验证时，明确提示用户手动通过，Agent 等待并轮询页面状态。
4. **用户始终在场**：每个关键动作（发送协议消息、执行脚本、下载文件）前向用户确认；用户是"眼睛"，Agent 是"手"。
5. **先检测，后行动**：首次使用必须先检测浏览器内核，再选择对应的操控通道，除非用户手动指定了浏览器路径。

## 工作流决策树

```
触发
 └─ 阶段 0：确认语言（跟随用户语言）
 └─ 阶段 1：浏览器内核检测
     ├─ 用户指定路径 → 按路径判断内核
     └─ 否则 → 运行 scripts/detect_browser.py
         ├─ Chromium 内核 → 通道 A：chrome-mcp / BrowserSkill
         └─ Gecko 内核   → 通道 B：GeckoDriver + Marionette
 └─ 阶段 1.5：操控工具就绪检查
     ├─ 工具可用 → 继续
     └─ 工具缺失 → 询问用户是否自动安装
         ├─ 是 → Agent 侧自动安装 + 用小白语言指导浏览器侧操作
         └─ 否 → 中止，说明所需工具，留待用户自行安装
 └─ 阶段 2：选择 AI 品牌 / 具体型号 / 思考模式 / 联网搜索（支持模糊语言）
 └─ 阶段 3：打开网页版 AI → 提示用户手动登录 → 人机验证 → 确认进入纯文本对话模式
 └─ 阶段 4：发送第一条协作协议消息，建立分工
 └─ 阶段 5：协作循环：转达需求 → 网页 AI 给步骤 → 本地执行 → 反馈结果 → 循环
```

## 阶段 0：确认语言

1. 从用户消息判断语言（简体中文 / 繁体中文 / English / 日本語…），本会话全程固定使用该语言。
2. 用该语言向用户简述计划与角色分工：网页 AI 负责思考，本地 Agent 负责执行。

## 阶段 1：浏览器内核检测

1. 若用户手动指定了浏览器路径（如"用 C:\...\firefox.exe"），跳过检测，直接按可执行文件名判断内核。
2. 否则运行 `scripts/detect_browser.py` 检测系统默认浏览器：
   ```bash
   python scripts/detect_browser.py            # 自动检测
   python scripts/detect_browser.py --browser "<路径>"   # 手动指定
   ```
3. 依据脚本输出 `engine` 字段分派：
   - `chromium` → 通道 A（Google Chrome / Edge / Chromium / Brave / Opera / 360 / QQ 浏览器等）
   - `gecko` → 通道 B（Mozilla Firefox 等）
   - `unknown` → 提示用户手动指定浏览器路径后再继续
4. 检测方法与跨平台细节见 `references/browser-detection.md`。

### 通道 A：Chromium 内核

1. 优先连接 chrome-mcp 连接器（`mcp__chrome-mcp` 系列工具：`chrome_navigate` / `chrome_read_page` / `chrome_click_element` / `chrome_fill_or_select` / `chrome_screenshot` / `get_windows_and_tabs` 等）。若工具未加载，用 ToolSearch 按 `tool_names` 加载。
2. 若 chrome-mcp 不可用，通过 find-skills 搜索并加载 "agent-browser" 或 "BrowserSkill" 技能，按其说明驱动浏览器。
3. 若以上工具均不可用 → 进入**阶段 1.5**（询问自动安装，不擅自安装）。
4. 详细操作指南见 `references/chromium-automation.md`。

### 通道 B：Gecko 内核

1. 使用 GeckoDriver + Marionette 驱动 Firefox（Firefox 内置 Marionette 协议，geckodriver 是 WebDriver ↔ Marionette 的翻译层）。
2. 检查 geckodriver 是否可用（`geckodriver --version`）；不可用 → 进入**阶段 1.5**（询问自动安装，不擅自安装）。
3. 推荐用 Python（selenium 或纯 urllib 调用 WebDriver HTTP API）驱动，代码模板见 `references/gecko-automation.md`。
4. 重要：驱动 Firefox 时必须复用用户自己的 profile（`-profile <路径>` / `capabilities` 指定），否则登录态丢失；或提示用户重新登录。

## 阶段 1.5：操控工具就绪检查与自动安装

目标：确保所选通道的操控工具就绪；缺失时**先征求用户同意**，Agent 侧自动安装，同时**用小白能听懂的语言**指导用户完成浏览器侧操作。

### 就绪检查

- 通道 A（chromium）：
  - 检查 chrome-mcp 连接器是否已连接（能否成功加载 `mcp__chrome-mcp` 工具）；
  - 或检查 agent-browser / BrowserSkill 技能是否已安装可用。
- 通道 B（gecko）：运行 `geckodriver --version` 确认可用。

### 询问用户（原话模板，语言跟随用户）

> 检测到你的默认浏览器是 <浏览器名>（<内核> 内核）。操控它需要 <工具名>，但目前你的电脑上还没有安装。
> 我可以帮你自动安装，不过需要你配合做一步浏览器操作。要现在安装吗？（约 2-3 分钟）

- 用户同意 → 执行下方「自动安装」；用户拒绝 → 中止协作，说明缺少的工具与官方安装链接，待用户自行装好后再用云思客。

### 自动安装（Agent 侧）

- 通道 A（chromium）→ 安装 chrome-mcp（mcp-chrome），含三件事：
  1. `npm install -g mcp-chrome-bridge`（npm 不可用则提示用户先装 Node.js）；
  2. `mcp-chrome-bridge register` 注册本地桥（若未自动注册）；
  3. 在 `~/.workbuddy/mcp.json` 的 `mcpServers` 中加入 `chrome-mcp-server`（streamableHttp / stdio 配置），并提示用户在连接器管理页"信任"启用。
- 通道 B（gecko）→ 安装 GeckoDriver：
  1. 从 https://github.com/mozilla/geckodriver/releases 下载当前平台最新 zip；
  2. 解压并将 `geckodriver` 放入 PATH（Windows 建议放 `C:\Windows\System32` 或用户目录的 bin，并加入 PATH）；
  3. 验证：`geckodriver --version`。
- 若 Agent 环境无法自动安装（无权限 / 无网络）→ 如实告知用户，并提供官方链接让用户手动安装。

### 浏览器侧操作（小白语言，原话模板）

- 通道 A（chromium，chrome-mcp 扩展）：
  > 我需要你在浏览器里做 4 步：
  > 1. 打开 GitHub 页面 https://github.com/hangwin/mcp-chrome/releases ，下载最新的 chrome-mcp-server-*.zip 压缩包；
  > 2. 把压缩包解压到一个**固定位置**（比如桌面新建一个"chrome-mcp"文件夹），解压完**不要删除、不要移动**；
  > 3. 在浏览器地址栏输入 chrome://extensions/ 回车，打开右上角"开发者模式"开关，然后点左上角"加载已解压的扩展程序"，选择刚才那个文件夹；
  > 4. 点击浏览器右上角拼图图标，找到"Chrome MCP Server"，点图钉固定，然后点它的图标，在弹出的窗口里点"Connect"连接。
  > 完成后告诉我一声，我这边就能操控你的浏览器了。
- 通道 B（gecko）：
  > Firefox 这边不需要装插件，我（Agent）已经装好驱动了。你只需要保持 Firefox 正常打开、不要关闭即可；如果稍后它弹出"是否允许自动化控制"，点"允许"。登录网页版 AI 时还是由你手动完成。

### 安装后验证

- 通道 A：重新尝试加载 `mcp__chrome-mcp` 工具，确认扩展已连接（必要时请用户刷新扩展 popup 并重新 Connect）。
- 通道 B：`geckodriver --version` 通过后，用最小脚本（selenium 或纯 HTTP）打开 about:blank 验证驱动可用。
- 验证通过 → 继续阶段 2；失败 → 排查（参考 `references/tool-installation.md` 的常见问题）。

## 阶段 2：选择 AI 品牌 / 模型 / 模式

1. 用用户语言列出可选的 AI 品牌（目录见 `references/ai-models.md`）：DeepSeek、Kimi、豆包、通义千问、文心一言、ChatGPT、Claude、Gemini、Grok、智谱清言、腾讯元宝、讯飞星火等。
2. 依次向用户确认四要素（可用一次提问收集，也可逐项确认）：
   - **品牌**：选哪个 AI（如 deepseek）
   - **具体型号**：品牌下的具体模型（如 DeepSeek-R1）
   - **思考模式**：深度思考 / 标准 / 视觉等
   - **联网搜索**：开启或关闭
3. 模糊语言解析规则（用户说"最新/最强/专家/快速/识图"等时按下表解析）：
   - "最新模型" → 该品牌型号列表中版本号最高 / 官方标注为最新的
   - "最强模型" → 能力最强的旗舰型号（如 Qwen3.8-Max 优先于 Qwen3.7-Max；DeepSeek 专家模式优先于快速模式）
   - "专家模式" → 深度思考 / 推理模式（如 DeepSeek 的专家模式 / R1 深度思考）
   - "快速模式" → 标准即时回答模式
   - "识图模式" / "视觉" → 多模态模型
   - "默认 / 你决定" → 按该品牌最均衡的型号与模式
   - 无法唯一确定时向用户确认，不要擅自猜测。
4. 确定后，规划网页交互步骤：要点击哪些模式切换按钮、勾选哪些开关（如"深度思考"、"联网搜索"），记录为待执行清单。

## 阶段 3：打开网页版 AI + 登录 + 人机验证

1. 用所选浏览器通道打开 `references/ai-models.md` 中对应品牌的官网对话 URL。
2. 向用户播报："已打开 <品牌> 对话页面，请手动登录（扫码 / 账号密码均可），若出现人机验证（滑块 / 验证码 / 行为验证）请手动通过。完成后告诉我'登录好了'。"
3. 等待用户确认登录；期间可轮询页面状态（检测头像 / 用户名 / 侧边栏等登录特征元素），但**绝不代填凭证、绝不代过人机验证**。
4. 若页面有模式切换（思考 / 联网搜索），按阶段 2 的清单完成设置。
5. 将对话切换为**纯文本模式**（方便直接查看和复制代码），关闭无关侧栏组件。

## 阶段 4：建立协作协议

1. 确认登录且页面就绪后，向网页 AI 发送第一条协作协议消息（语言跟随用户；示例为简体中文）：

   > 我是来自用户电脑中的 AI agent，你负责规划步骤 / 编写代码 / 逻辑推理，我可以根据你的步骤完成扒取代码、创建文件、运行脚本、下载资源、联网搜索等等，而且完全在用户的电脑中，稍后我会给你用户的要求。

2. 读取网页 AI 的回复，确认它已理解分工（若回复为空或异常，重发一次并检查页面状态）。

## 阶段 5：协作循环

循环执行，直到用户终止：

1. **转达**：接收用户的新要求，用用户语言完整转达给网页 AI（保留原意与细节，不自行删减）。
2. **读取方案**：读取网页 AI 回复中的步骤 / 代码 / 推理结论（注意抓取完整内容，必要时滚动页面、展开代码块）。
3. **本地执行**：按步骤在用户电脑上执行——扒取代码、创建文件、运行脚本、下载资源、联网搜索、运行程序等；执行时使用用户语言汇报进度。
4. **反馈闭环**：将执行结果、报错信息、输出摘要反馈给网页 AI，请其修正或继续。
5. **暂停点**：任何需要用户决策、凭证、安装软件或涉及敏感操作的地方，停下向用户确认后再继续。

## 注意事项与陷阱

- 网页 AI 回复可能较长或被"继续生成"按钮截断：滚动到底、点"继续"后重新读取。
- 代码可能以 Markdown 代码块渲染：读取页面纯文本可保留内容；复制后核对关键行。
- 网页元素选择器不稳定：优先用可见文本 / role 定位元素，避免死板 XPath。
- 页面刷新 / 跳转会丢失登录态或模式设置：检测到后提示用户重新登录，并重新确认纯文本模式与联网搜索开关。
- 用户手动完成人机验证后，先重新读取页面状态再继续下一步，不要盲目点击。
- 若目标站点强要求移动端扫码或地区限制，告知用户并提供备选品牌。

## 资源

- `scripts/detect_browser.py`：默认浏览器内核检测脚本（Windows 注册表 + macOS/Linux 兜底 + 常见安装路径），输出 JSON。
- `references/ai-models.md`：AI 品牌 / 型号 / 思考模式 / 联网能力目录、官网对话 URL、模糊语言映射表。
- `references/browser-detection.md`：跨平台（Windows / macOS / Linux）默认浏览器与内核检测方法详解。
- `references/tool-installation.md`：操控工具（chrome-mcp / BrowserSkill / GeckoDriver）的安装指南——Agent 侧自动安装步骤 + 浏览器侧小白指引 + 常见问题排查。
- `references/chromium-automation.md`：chrome-mcp 与 BrowserSkill / agent-browser 的操作指南、元素定位技巧。
- `references/gecko-automation.md`：GeckoDriver + Marionette 驱动 Firefox 的完整指南（含 selenium 与纯 HTTP 两种代码模板）。
