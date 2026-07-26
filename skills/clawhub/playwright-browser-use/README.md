# pw-browser

> 基于 Playwright 的浏览器自动化 CLI — daemon + client 架构，直接使用系统 Chrome/Edge，无需下载额外浏览器。

## 特性

- **系统浏览器复用**：通过 Playwright `channel: 'chrome'` 连接系统已安装的 Chrome 或 Edge，不下载 Chromium
- **跨平台**：支持 Windows、macOS、Linux
- **持久化会话**：daemon 保持浏览器状态跨命令存活，无需每次重启
- **可访问性快照**：`snap` 命令生成页面元素树，带 ref 引用，无需写 CSS 选择器
- **非 headless**：浏览器窗口始终可见，用户可实时监控所有操作
- **人机协作**：遇到登录/验证码时自动交接给用户操作

## 安装

```bash
git clone <repo-url> pw-browser
cd pw-browser
npm install
```

> 前提：系统已安装 [Node.js](https://nodejs.org/) 18+ 和 Chrome 或 Edge 浏览器。

## 快速开始

```bash
# 1. 启动 daemon（后台运行）
node pw-browser.js daemon &

# 2. 等待 daemon 就绪
sleep 4

# 3. 打开页面
node pw-browser.js open https://www.baidu.com

# 4. 获取页面快照（必须！每次交互前都要 snap）
node pw-browser.js snap

# 5. 交互 — 基于快照中的 e0, e1, e2... ref
node pw-browser.js fill e12 "天气预报"
node pw-browser.js click e13

# 6. 查看结果
sleep 2
node pw-browser.js snap

# 7. 关闭
node pw-browser.js close --all
```

## 命令一览

| 类别 | 命令 | 说明 |
|------|------|------|
| 生命周期 | `init` / `open <url>` / `close` / `close --all` / `recover` | 启动、导航、关闭、恢复 |
| 状态感知 | `snap` / `wait-for <target>` | 快照、等待条件 |
| 交互 | `click <ref>` / `fill <ref> "text"` / `type "text"` / `press <key>` / `hover <ref>` / `select <ref> <opt>` / `check <ref>` / `uncheck <ref>` | 点击、填写、按键等 |
| 导航 | `goto <url>` / `go-back` / `go-forward` / `reload` | 页面导航控制 |
| Tab | `tab list` / `tab select <idx>` / `tab close <idx>` | 多标签页管理 |
| 高级 | `screenshot` / `mousewheel <dx> <dy>` / `eval "<expr>"` ⚠️ / `run-code "<code>"` ⚠️ | 截图、滚动、代码执行 |
| 延时 | `sleep <seconds>` | 等待 |

> ⚠️ `eval` 在**浏览器上下文**执行 JS（无 Node 权限）；`run-code` 在 daemon 的**受限沙箱（`vm`）**中执行 Playwright 代码（无直接 Node `fs`/`process`/`child_process` 权限，但可经浏览器下载/上传读写本地文件、发起任意网络请求）。二者均拥有完整浏览器控制权。仅在用户明确指定的任务中使用。

## 架构

```
┌──────────────┐     HTTP (localhost:19223)     ┌──────────────┐
│  pw-browser  │ ──────────────────────────────→│   Daemon     │
│  (CLI 客户端) │                                │  (浏览器进程)  │
└──────────────┘                                └──────┬───────┘
                                                       │
                                                       ├─ Playwright
                                                       ├─ Chrome / Edge
                                                       └─ 页面状态持久化
```

daemon 启动后持续运行，浏览器和页面状态跨命令保持。CLI 每次通过 HTTP 调用 daemon。

## 工作流核心规则

1. **先观察再操作**：每次交互前必须 `snap`，基于快照 ref 操作
2. **登录交接**：遇到登录/验证码页面时，告知用户手动操作，用户确认后继续
3. **翻页前先识别类型**：页码分页 / 无限滚动 / 加载更多，对应不同翻页方式
4. **daemon 故障恢复**：连接错误时杀端口 19223 进程 → 删 daemon.json → 重启

详细规则和示例见 `SKILL.md`。

## 安全说明

- daemon 监听 `127.0.0.1:19223`，仅本机可访问
- **命令认证**：除 `/health` 存活探针外，所有 daemon 命令都要求随机 `token`。token 在 daemon 启动时生成，写入 `~/.pw-browser/daemon.json`（默认仅当前用户可读），CLI 自动携带。未读取该文件的本地进程无法调用——这关闭了"无认证 HTTP 端点 = RCE 界面"的缺口
- **安全模式**：`PW_BROWSER_SAFE_MODE=1 node pw-browser.js daemon` 可彻底禁用 `run-code` / `eval`，仅保留 snap/click/fill 等白名单命令
- `eval` 运行在浏览器上下文；`run-code` 运行在 `vm` 受限沙箱（无直接 Node 系统 API，但可经浏览器下载/上传读写本地文件），仅限本地信任环境使用
- 浏览器以非 headless 模式运行，用户可实时监控
- 不推荐作为公开 API 服务暴露，如需请加认证和操作白名单

### 依赖安全说明（CVE-2025-59288）

本项目依赖 `playwright@1.61.1`（≥ 1.55.1，已修复 CVE-2025-59288）。该 CVE 影响的是 Playwright **下载并安装浏览器**的安装脚本（`curl -k` 未校验证书），而本工具通过 `channel: 'chrome'` 直接复用系统已安装的 Chrome/Edge，**从不调用 Playwright 的浏览器下载链路**，因此该漏洞在实际使用路径上不可触发。

## 作为 AI Skill 使用

本工具可作为 AI 助手的 skill 使用。将整个目录放入 skill 安装路径，AI 助手通过 `SKILL.md` 中的规则指导自动化操作。

## License

[MIT](LICENSE)
