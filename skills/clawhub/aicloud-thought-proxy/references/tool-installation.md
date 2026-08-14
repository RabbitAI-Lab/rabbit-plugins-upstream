# 操控工具安装指南（tool-installation）

通道 A（Chromium）与通道 B（Gecko）的操控工具在缺失时的安装方法。
原则：**Agent 侧自动安装（经用户同意）** + **浏览器侧由用户手动完成（小白语言指引）**。

---

## 通道 A：Chromium 内核 → chrome-mcp（mcp-chrome）

chrome-mcp（又名 Chrome MCP Server）由两部分组成：
- **本地桥（Agent 侧）**：`mcp-chrome-bridge`，把 MCP 客户端与浏览器扩展连接起来，默认监听 `http://127.0.0.1:12306/mcp`。
- **浏览器扩展（浏览器侧）**：`chrome-mcp-server` 扩展，在用户自己的 Chrome/Edge 里执行导航、点击、读取等操作，天然保留登录态。

### Agent 侧（自动安装，需用户同意）

```bash
# 1. 全局安装本地桥（需 Node.js >= 18.19；WorkBuddy 自带 Node，可直接用其 npm）
npm install -g mcp-chrome-bridge
# 若用 pnpm 且版本 >= 7，先启用 postinstall 脚本再安装：
# pnpm config set enable-pre-post-scripts true && pnpm install -g mcp-chrome-bridge

# 2. 注册本地桥（若安装时未自动注册）
mcp-chrome-bridge register

# 3. 写入 MCP 配置 ~/.workbuddy/mcp.json 的 mcpServers：
#    {
#      "mcpServers": {
#        "chrome-mcp-server": {
#          "type": "streamableHttp",
#          "url": "http://127.0.0.1:12306/mcp"
#        }
#      }
#    }
#    若客户端只支持 stdio，改用 mcp-server-stdio.js（随桥安装）配置 command/args。
```

安装并写入配置后，告知用户：在 MCP/连接器管理页找到 `chrome-mcp-server`，点击"信任"启用（新配置不会自动激活）。

### 浏览器侧（用户手动，小白指引话术）

> 我需要你在浏览器里做 4 步：
> 1. 打开 GitHub 页面 https://github.com/hangwin/mcp-chrome/releases ，下载最新的 chrome-mcp-server-*.zip 压缩包；
> 2. 把压缩包解压到一个**固定位置**（比如桌面新建一个"chrome-mcp"文件夹），解压完**不要删除、不要移动**；
> 3. 在浏览器地址栏输入 chrome://extensions/ 回车，打开右上角"开发者模式"开关，然后点左上角"加载已解压的扩展程序"，选择刚才那个文件夹；
> 4. 点击浏览器右上角拼图图标，找到"Chrome MCP Server"，点图钉固定，然后点它的图标，在弹出的窗口里点"Connect"连接。
> 完成后告诉我一声，我这边就能操控你的浏览器了。

要点（Agent 自查）：
- 解压目录必须固定：Chrome 按引用加载，移动/删除目录会导致扩展失效。
- Edge 用户：地址栏用 `edge://extensions/`，其余步骤相同。
- 连接验证：扩展 popup 显示已连接、端口 12306；Agent 侧能加载 `mcp__chrome-mcp__chrome_navigate` 等工具。

### 常见问题

| 现象 | 处理 |
|---|---|
| `npm` 命令不存在 | 提示用户安装 Node.js（或使用 WorkBuddy 自带 Node 的 npm 路径） |
| 扩展装好但 popup 显示未连接 | 确认 `mcp-chrome-bridge` 已在运行、端口 12306 未被占用；点 popup 里的 Connect |
| 连接器显示 disconnected | 在连接器管理页对 `chrome-mcp-server` 点"信任/启用" |
| 扩展消失 / 报错 | 检查解压目录是否被移动或删除；重新"加载已解压的扩展程序" |
| 站点识别自动化 | 扩展运行在用户真实浏览器，登录态与指纹均正常，一般不会触发；若触发，请用户手动完成验证 |

### 备选：BrowserSkill / agent-browser

若 chrome-mcp 无法安装或用户不愿装扩展：
1. 用 find-skills / 技能市场搜索并安装 "agent-browser" 或 "BrowserSkill" 技能。
2. 按其 SKILL.md 驱动浏览器（通常基于 Playwright/Puppeteer）。
3. 注意保留登录态：优先连接用户现有浏览器实例（`--remote-debugging-port`）或复用 profile；否则需用户重新登录。
4. 若以上均不可用，可提示安装 Playwright 轻量方案（需下载浏览器驱动，先征得用户同意）。

---

## 通道 B：Gecko 内核 → GeckoDriver + Marionette

Firefox 内置 Marionette 自动化协议，只需一个 `geckodriver` 翻译层即可驱动，**浏览器侧无需安装任何插件**。

### Agent 侧（自动安装，需用户同意）

```bash
# 1. 下载 geckodriver（当前平台最新版）
#    https://github.com/mozilla/geckodriver/releases
#    Windows: geckodriver-v*.win64.zip；macOS: macos.tar.gz；Linux: linux64.tar.gz

# 2. 解压并将 geckodriver 放入 PATH
#    Windows 示例（放入用户目录并加入 PATH）：
#      mkdir -p ~/bin && unzip -o geckodriver-*.zip -d ~/bin
#      export PATH="$HOME/bin:$PATH"   # 写入 shell 配置永久生效
#    或使用 WorkBuddy 内置 Python 安装 selenium 托管驱动：
#      python -m pip install selenium   # selenium 4 的 Selenium Manager 可自动下载 geckodriver

# 3. 验证
geckodriver --version
```

### 浏览器侧（用户手动，小白指引话术）

> Firefox 这边不需要安装任何插件。你只需要保持 Firefox 正常打开、不要关闭即可。
> 如果稍后 Firefox 弹出"是否允许自动化控制"，点"允许"。
> 登录网页版 AI 时仍然由你手动完成（扫码/账号密码都可以）。

要点（Agent 自查）：
- Marionette 由 geckodriver 启动 Firefox 时自动启用，用户无需改 about:config。
- 保留登录态：优先用 `-profile <用户profile路径>` 复用用户配置（见 `references/gecko-automation.md`）。

### 常见问题

| 现象 | 处理 |
|---|---|
| `geckodriver` 无法启动 | 确认已解压到 PATH 并 `geckodriver --version` 通过 |
| Firefox 版本过旧 | geckodriver 与 Firefox 版本需大致匹配，升级 Firefox 或换对应版本驱动 |
| 登录态丢失 | 未复用 profile；按阶段 3 提示用户手动登录即可 |
| 防火墙/杀毒拦截 | 将 geckodriver 加入白名单，或改用 selenium 托管方式 |

---

## 安装完成后验证清单

- [ ] Agent 侧工具可用（chrome-mcp 工具可加载 / `geckodriver --version` 通过）
- [ ] 浏览器侧就绪（扩展已 Connect / Firefox 正常打开）
- [ ] 用最小操作验证：打开一个页面并读取标题成功
- [ ] 通过后进入阶段 2（选择 AI 品牌/模型/模式）
