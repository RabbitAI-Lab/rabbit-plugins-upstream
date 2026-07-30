# Changelog

All notable changes to `pw-browser` are documented here. This project follows semver-ish versioning (`MAJOR.MINOR.PATCH`).

## [1.3.2] — 2026-07-27

### Security
- **安全模式覆盖凭证原语（闭环 Rogue Agent / 会话持久化 97% 置信度发现）**：`PW_BROWSER_SAFE_MODE=1` 现在**整体禁用**全部 `cookies` / `storage` 子命令（`list/get/set/clear/export/import`），与 `eval` / `run-code` 同级返回 `Disabled`。此前安全模式只拦代码执行、拦不住凭证读写——不可信 agent 仍可无代码执行地导出/注入会话凭证做特权持久化；本版从代码层关闭该空档。
- **文档一致性**：SKILL.md（frontmatter description / capabilities / 核心能力声明 / Rogue Agent 缓解块）、README 中英文、QUICKSTART 中英文的"safe mode 拦不住 cookies/storage"表述全部改为新行为，消除描述-行为失配。

### Added
- `tests/b-negative.js` safe-mode 阶段新增 4 断言：`cookies list/export`、`storage get/import` 在安全模式下均返回 `Disabled`。

## [1.3.1] — 2026-07-27

### Security
- **会话凭证落盘路径限制（缓解 Rogue Agent / 令牌盗窃）**：`cookies` / `storage` 的 `export` / `import` 默认**限制在 `~/.pw-browser/` 目录内**，禁止静默把凭证写入 `/tmp` 或加载来自任意路径的攻击者构造文件；写到/读自该目录之外必须显式 `--unsafe`（不推荐，命令会拒绝否则）。新增 `CRED_WARNING` 常量，所有 `export`/`import` 的 JSON 响应均附带 `warning` 字段提示文件含实时会话凭证。
- **审计发现的文档闭环**：针对连续多条安全审计发现（导出未警告、导入+Agent 常态化、会话持久化 Rogue Agent、描述-行为失配、无警告/确认/路径限制），在 QUICKSTART（中英文）示例 4、SKILL.md 核心能力声明与「会话持久化风险」块、README（中英文）命令参考与「Cookie 与本地存储」节统一补齐能力声明、路径限制说明与缓解措施。

### Changed
- 版本号升至 `1.3.1`，并同步 `package-lock.json`。

## [1.3.0] — 2026-07-27

### Added
- **超大 DOM 快照保护**：`buildSnapshot` 新增 `SNAP_LIMIT`（默认 3000，环境变量 `PW_BROWSER_SNAP_LIMIT` 可配，设为 `0` 关闭上限）。遍历超上限即停止收集并标记 `truncated`；`snap` 的 JSON 返回 `truncated`、文本输出加截断提示，避免超大型页面拖慢/撑爆快照。
- **负向/错误路径测试 `tests/b-negative.js`**：点击/填充不存在 ref → `ElementNotFound`；`act` 未知 ref/未知动作 → 对应 `kind`；`storage`/`cookies set` 缺参 → `ok:false`；`open` 缺 url → `ok:false`；`wait-for` 超时 → `WaitTimeout`；安全模式 `eval`/`run-code` → `Disabled`。
- **快照上限测试 `tests/c-snapcap.js`**：验证 `PW_BROWSER_SNAP_LIMIT` 生效与早期元素仍被捕获。
- **端到端 Cookbook**：`QUICKSTART.md`（中文）/ `QUICKSTART.en.md`（英文），含表单提交、上传下载、shadow/iframe 穿透、cookie/storage 会话恢复、`act` 多步自纠错五个真实示例。
- **双语文档**：新增 `README.en.md`（英文 README），与 `README.md` 互相交叉链接；`SKILL.md` 顶部加英文文档指针。

### Changed
- `resolveRef` 返回结构统一带上 `ok: false`（此前缺省 `ok` 字段），使 `act` 结果条目契约一致。
- 快照 `refMap` 元素信息补充 `id` 字段（便于识别元素）。
- `sync.sh` 白名单新增 `README.en.md` / `QUICKSTART.md` / `QUICKSTART.en.md`。

### Security
- （沿用）全部命令除 `/health` 外均要求随机 token 认证；可经 `PW_BROWSER_SAFE_MODE=1` 彻底禁用代码执行。

## [1.2.0] — 2026-07-27

### Added
- **`download` 命令**：对称于 `upload`。可选 `<ref>` 触发下载，监听页面 `download` 事件并 `saveAs` 到 `--path`（默认当前目录）；亦可作为 `act` 动作 `{action:"download", ref:"eN", path:"/tmp/x.csv"}` 使用。
- **`cookies` 一等命令**：`cookies list` / `export [--path file]` / `import <file>` / `clear` / `set <name> <value> [--domain --path]`。不再需要靠 `eval` 曲线救国。
- **`storage` 一等命令**：`storage get [key]` / `set <key> <value>` / `clear` / `export [--path file]` / `import <file>`，基于 `localStorage`。
- **Daemon 端口可配 + 冲突避让**：
  - 环境变量 `PW_BROWSER_PORT` 覆盖默认 `19223`。
  - 启动时探测端口：若已有 daemon 存活则直接退出（避免双开），否则 `EADDRINUSE` 时自动递增端口直到可用，并把实际端口写回 `daemon.json`。客户端已读 `daemon.json` 端口，无需改动。

### Changed
- 成熟度工程化：上一轮已加入测试骨架（`tests/smoke.js`）、一键同步脚本（`sync.sh`）、git 初始化。

### Security
- （沿用 1.1.0）全部命令除 `/health` 外均要求随机 token 认证（优先 `Authorization: Bearer` 头，避免泄漏到 URL/日志）；`/health` 不回传 `pageUrl`；`run-code` 走 `Object.create(null)` VM 沙箱；可用 `PW_BROWSER_SAFE_MODE=1` 彻底禁用代码执行。

## [1.1.0] — 2026-07-27

### Added
- 借鉴 browser-use 的四项能力：A 稳定元素 ref（跨 snap 保持一致）、B `screenshot --annotate` 视觉标注、C `act` 动作序列 + 自纠错中断、D `history` 操作历史。
- iframe / open shadow DOM 穿透（`buildSnapshot` 递归 shadow root 与同源 iframe，`cssPath`/`frameChain` 定位）。
- `upload`、`drag` 命令；`resolveRef` 去重；daemon 空闲自动退出（`PW_BROWSER_IDLE_MS`）+ `shutdown` 加固（`safeCloseBrowser`/`gracefulExit`）。
- 测试骨架 + `sync.sh` + git 初始化。

### Security
- token 改为 header 传输；`/health` 去 `pageUrl` 泄漏。
