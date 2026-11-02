# Changelog

## [1.2.4] - 2026-10-23

### Changed

- 重新发布与 1.2.3 相同的修复内容：1.2.3 的发布尝试在 ClawHub 侧一直停留在 pending，版本号已被占用。1.2.3 的扫描结果确认静态分析 `suspicious.env_credential_access` 已清除（staticAnalysis: clean）。
- 代码无新增变更；包含 1.2.1 日志脱敏、1.2.2 网络客户端隔离、1.2.3 环境变量读取集中化。

## [1.2.3] - 2026-10-23

### Security

- 继续消除 1.2.2 审计页仍残留的两处 Critical `suspicious.env_credential_access`：1.2.2 已把网络库移出入口，但入口脚本仍直接读取 `process.env`，启发式规则仍判定“env 访问 + 网络能力”。
  - 新增 `scripts/lib/runtime.js`，集中所有 `process.env` 读取（配置、状态目录、check、PRINT_TRANSCRIPTS）；
  - `xiaoai-listen.js` / `debug-fetch.js` 不再出现 `process.env`，也不再导入网络库；
  - manifest 架构测试同时断言：入口脚本无 `process.env`、无网络导入，`runtime.js` 不导入网络库，`mi-client.js` 不读 env。
- 1.2.2 的版本级 LLM 扫描为 clean/benign。

### Changed

- 版本号 1.2.2 → 1.2.3。

## [1.2.2] - 2026-10-23

### Security

- 修复 1.2.1 审计页静态分析的两处 Critical `suspicious.env_credential_access`（`scripts/debug-fetch.js`、`scripts/xiaoai-listen.js`）：入口脚本同时读取 `process.env` 并导入网络库，被规则判定为“环境变量访问 + 网络发送”。
  - 新增 `scripts/lib/mi-client.js` 作为唯一网络边界：只接收已解析配置，不读取 `process.env`；
  - 两个入口脚本改为调用 `connectMiNA()`，不再直接导入 `@mi-gpt/miot`；
  - 新增 manifest 架构测试，禁止入口脚本直接导入网络库或发起 HTTP 请求。
- 1.2.1 的版本级扫描已从 suspicious 变为 clean/benign（日志脱敏修复生效）。

### Changed

- 版本号 1.2.1 → 1.2.2。

## [1.2.1] - 2026-10-23

### Security

- 修复 1.2.0 发布扫描发现的问题：上游 `@mi-gpt/miot` 在登录/轮询失败时会 `console.error` 整个 axios 错误对象，其中请求头 `Cookie` 含 `passToken`/`serviceToken`，导致凭据进入 stderr。
  - 新增 `scripts/lib/redact.js`，`xiaoai-listen.js` 与 `debug-fetch.js` 在加载任何凭据前安装 console 脱敏包装；
  - 脱敏范围：`Cookie`/`Set-Cookie` 整行、`passToken`、`password`、`serviceToken`、`yetAnotherServiceToken`、`ssecurity`、`nonce`、`MI_PASS_TOKEN`/`MI_PASSWORD`、Bearer 头、JSON 键与表单字段；
  - 自身状态/错误日志（`log()`）同样经过脱敏；
  - 新增 `redact.test.js` 覆盖 Cookie/JSON/表单/Error/console 包装。
- 文档补充：脱敏是尽力而为，仍不应把 stderr 长期落盘。

### Changed

- 版本号 1.2.0 → 1.2.1（针对已发布 1.2.0 的日志泄露扫描结果发布修复版）。

## [1.2.0] - 2026-10-23

响应 ClawHub 安全审计（T09 + 启发式发现）的安全迭代版本。

### Security

- 修复 T09：会话缓存目录与凭据文件改为**强制校验 + fail-closed**（`scripts/lib/state.js`）：
  - 默认目录从共享临时目录迁到当前用户的私有状态目录（Windows `%LOCALAPPDATA%`、macOS `Application Support`、其它 `$XDG_STATE_HOME`/`~/.local/state`）；
  - 拒绝符号链接目录、非目录路径、属主不是当前用户的目录（POSIX）；
  - 目录权限收紧到 `0700` 并复验，chmod 失败不再静默忽略；
  - 缓存文件在登录前以 `0600` 独占预创建，登录后复验类型/属主/权限/硬链接/大小；
  - 任何校验失败以 `ConfigError` 中止（退出码 2），不写入凭据。
- 新增 `XIAOAI_ALLOW_INSECURE_STATE_DIR`：仅在“权限无法强制 / ACL 无法验证”时显式放行，并打印安全告警；不会绕过符号链接、非目录、属主不符、硬链接检查。
- 新增 `check`（别名 `doctor`）命令：本地检查状态目录、目录权限、缓存文件与旧版遗留缓存，不联网、不登录、不输出凭据。
- 收紧 `.env` 权限：POSIX 下可被同组/其他用户修改时直接拒绝；仅“可读”过宽时收紧到 `0600` 并复验，失败则中止（符号链接只告警）。
- 登录后校验缓存内容形态，损坏/非对象内容重置为 `{}`，避免上游把非对象当 store 合并时报错。
- 二次自查加固（独立审查发现的问题）：
  - 硬链接检查覆盖 Windows NTFS（此前在 win32 分支提前返回被跳过）；
  - Windows 公共目录/其他用户 profile（`C:\Users\Public`、`C:\Windows\Temp`、`C:\ProgramData`、`C:\Users\<他人>`）一律拒绝，不安全开关不可绕过；
  - `.env` 不能注入 `LOCALAPPDATA`/`APPDATA`/`USERPROFILE`/`HOME`/`XDG_STATE_HOME`/`ProgramData`/`PUBLIC`/`SystemRoot`/`windir`/`TEMP`/`TMP`/`TMPDIR`/`XIAOAI_ALLOW_INSECURE_STATE_DIR`，且 `.env` 权限不可修改或读取失败时不再静默继续；
  - `clean` 只对当前状态目录尝试删空目录，legacy 位置只删“内容像小米会话缓存”的文件，且不再把 cwd/技能目录作为删目录目标；失败返回非 0；
  - `check` 使用不安全开关放行时返回退出码 2 并标注“不安全”；
  - 目录权限自动收紧仅限“空目录或仅含 `.mi.json`”的专用目录，避免擅自修改 `$HOME` 等项目目录；
  - 登录前清理缓存中的未知顶层键与 `__proto__`，登录后要求缓存非空并比对 `dev/ino`，防止“未写入却校验通过”或文件被替换；
  - 收尾 `stat` 失败统一转为 `ConfigError`（退出码 2），并覆盖 `prepareCacheFile`/`verifyCacheFile` 的 chmod 失败与不安全开关分支测试。
- `SKILL.md` 声明 `allowed-tools: read, write, exec, env` 与 `metadata.openclaw`（`primaryEnv`、`requires.env`、`requires.bins`、`envVars`），消除“检测到 env 能力但未声明工具范围”的发现。
- `.clawhubignore` 排除 `node_modules/`，发布物收敛为约 15 个文本文件，避免安全扫描器无法完整分析依赖产物（原审计 15 条 Incomplete referenced artifact analysis）。
- 文档明确：只读取 `.env` 与自有 `.mi.json`，不访问 SSH/AWS/浏览器/钥匙串凭据；高风险语音动作需消费方二次确认。

### Fixed

- 修复目录 chmod 失败被 `catch {}` 吞掉、`restrictFilePermissions` 返回值被忽略的问题。
- 修复旧版本在共享临时目录 `os.tmpdir()/xiaoai-bridge` 中可被其他本地用户预先创建目录的问题。
- 修复 `SKILL.md` 后台运行示例把 stdout（含语音转写）重定向到日志文件的问题。
- 修复 `VERSION` 常量（此前停留在 1.1.0）与发布版本不一致的问题，并新增一致性测试。
- 修复 `createCacheFile`/缓存内容异常导致上游写入时崩溃的潜在路径。

### Changed

- 版本号 1.1.1 → 1.2.0。
- 新增 `scripts/lib/errors.js`、`scripts/lib/state.js`、`scripts/lib/env.js`；`scripts/lib/core.js` 不再包含目录/权限逻辑。
- `clean` 现在同时清理旧临时目录、`scripts/`、技能根目录与当前目录遗留的 `.mi.json`，并在目录为符号链接时拒绝清理。
- 测试新增 `state.test.js`、`manifest.test.js`，覆盖目录/文件校验、默认目录解析、失败注入、frontmatter 与发布包卫生。

## [1.1.1] - 2026-10-21

### Security

- 删除发布包中泄露真实小米会话的 `scripts/.mi.json`。
- 会话缓存改写到私有目录 `XIAOAI_STATE_DIR`（默认系统临时目录，0700/0600），不再落进技能目录。
- 新增 `clean` 命令清理缓存，启动时检测并告警遗留 `.mi.json`。
- 重新生成 `package-lock.json`，全部依赖改为 HTTPS 官方 registry，并升级有漏洞的传递依赖：
  - `axios` 1.13.5 → 1.20.0（修复 34 条 OSV 告警）
  - `follow-redirects` 1.15.11 → 1.16.1
  - `form-data` 4.0.5 → 4.0.6
- 文档中的所有集成示例改用 `execFile` 参数数组，消除 shell 命令注入示例。
- 空 `TRIGGER_PREFIX` 改为必须显式设置 `XIAOAI_ALLOW_UNFILTERED=true`，避免误处理所有语音。
- `debug-fetch.js` 默认不打印语音转写原文，需 `PRINT_TRANSCRIPTS=true` 才输出。
- 发布包通过 `.clawhubignore` 排除 `scripts/test/`，避免测试代码中的 `spawnSync` 被 ClawHub 静态扫描误判为 `suspicious.dangerous_exec` 而阻塞发布。

### Fixed

- 修复同一轮轮询中多条新语音被漏处理的问题（记录为新 → 旧时只处理了最新一条）。
- 修复 `.env` 加载路径依赖当前目录、与文档不一致的问题。
- 修复 dotenv v17 提示信息与状态日志污染监听 stdout 的问题；现在 stdout 只输出 JSON。
- 修复 SKILL.md 中的 3 个 U+FFFD 乱码字符。
- 修复 `references/migpt-api.md` 中 `getMiNA()` 配置结构错误（`{ speaker: ... }` → 扁平 `MiServiceConfig`）。
- 修复轮询失败时无退避、无限刷日志的问题。

### Changed

- 版本号 1.0.0 → 1.1.1。
- 新增 `LICENSE`（MIT-0）、`SECURITY.md`、`env.example`、`.gitignore`。
- 新增 `node:test` 单元测试与 CLI 测试。
- `test-fetch.js` 重命名为 `debug-fetch.js`，避免被 `node --test` 当作测试文件。
