# Changelog

All notable changes to `pw-browser` are documented here. This project follows semver-ish versioning (`MAJOR.MINOR.PATCH`).

## [1.3.10] — 2026-07-30

### Security — download path traversal (proactive full-source audit)

Every prior hardening round was driven by external audit findings, all of which
concentrated on the credential primitives. A full sweep of `pw-browser.js` turned
up an unrelated and **more directly attacker-reachable** hole in `download`.

- **`download` no longer trusts the page-supplied filename.** `dl.suggestedFilename()`
  is chosen by the *web page being automated*, not by the operator. When the caller
  passed a destination **directory** (the normal case, e.g. `~/Downloads`), the old
  code did `path.join(dest, suggested)` — so a malicious page returning
  `../../.bashrc` wrote **outside** that directory. This is an arbitrary-file-write
  primitive triggered by merely visiting a hostile site, no operator mistake needed.
  New module-scoped `safeDownloadTarget()` reduces the name to a bare `path.basename`
  and then asserts the resolved target still sits inside the resolved destination,
  returning error kind `PathTraversal` otherwise. Passing an explicit **file** path
  as `dest` keeps its previous meaning (operator authority, used verbatim).
- **Constant-time daemon token comparison.** `provided !== daemonToken` short-circuits
  and leaks length/position through timing. Replaced with `timingSafeToken()` built on
  `crypto.timingSafeEqual` (length-checked first). Negligible risk against a 24-byte
  random token, but free to get right — defence in depth for the token that authorises
  `eval` / `run-code` / credential access.

### Internal

- CLI entry is now guarded by `require.main === module`, and `safeDownloadTarget` /
  `timingSafeToken` are exported when the file is `require`d — so pure logic can be
  unit-tested without launching a browser or a daemon.

### Tests

- New `tests/d-download.js` (15 assertions, browser-free — no daemon, no Chrome):
  traversal names (`../../.bashrc`, `../escape.png`, absolute paths, embedded
  separators) are all neutralised into `dest`; bare `..`, `a/..`, `../../` and empty
  names are rejected as `PathTraversal`; ordinary names pass through unchanged.
  `timingSafeToken` accepts the exact token and rejects wrong-value, shorter, longer,
  empty and `undefined` without throwing. Wired into `npm test` as the sixth group.

## [1.3.9] — 2026-07-30

### Security — session-persistence hardening (audit findings, 86–98% confidence)

Previous versions documented two credential-hygiene practices that were **advice only**, never enforced by code. This release turns both into real controls.

- **`PW_BROWSER_CRED_PERSIST=off` — credential-persistence kill switch.** Blocks
  `cookies export|import` and `storage export|import` (new error kind
  `CredentialPersistenceDisabled`) while leaving `list` / `get` / `set` / `clear`
  fully usable. This is deliberately **finer-grained than `PW_BROWSER_SAFE_MODE=1`**,
  which disables the credential primitives wholesale: the rogue-agent risk is
  dominated by session state *reaching the filesystem*, where it outlives the
  daemon and becomes a reusable identity. Removing only that primitive keeps
  normal automation working. Operator-controlled process env — a caller cannot
  lift it.
- **Secret files are now owner-only.** `~/.pw-browser/` is created `0700`; the
  daemon auth token (`daemon.json`) and every exported cookie/localStorage dump
  are written `0600`, with an explicit `chmod` so files left `0644` by older
  versions get tightened on rewrite. Previously `daemon.json` — which holds the
  token authorising `eval` / `run-code` / credential access — was written with
  default `0644`, letting **any other local user take over the browser session**.
  (POSIX only; on Windows mode bits are not OS-enforced and user-profile ACLs apply.)

### Docs

- Mitigation guidance rewritten across SKILL.md / README (zh+en) / QUICKSTART (zh+en):
  "remember to `chmod 600`" → "already enforced"; "don't persist credentials in
  automated flows" → "start the daemon with `PW_BROWSER_CRED_PERSIST=off`".
- Deployment matrix gains a **禁凭证落盘 / cred-persist-off** tier between "full" and
  "safe mode"; frontmatter `permissions.enforcement` gains `cred-persist-killswitch`
  and `secret-file-permissions`; execution-boundary list grows from 4 to 6 items.

### Tests

- `b-negative.js` phase 4: `CRED_PERSIST=off` blocks export/import yet in-memory
  `cookies list` / `storage set` still succeed.
- `b-negative.js` phase 5: exported credential file and `daemon.json` are `0600`,
  state dir is `0700` (assertions skipped with an existence check on win32).

## [1.3.8] — 2026-07-30

### Security — credential path confinement is no longer caller-waivable (privilege escalation, 97%)

- **Fixed a privilege-escalation path**: `--unsafe` alone used to lift the credential
  path confinement. Since the flag is supplied by the *caller* (possibly an untrusted or
  compromised agent), the guard could be disabled by the very actor it was meant to
  contain — a guard whose key is held by the constrained party is not a guard.
- **Privilege separation**: escaping confinement now requires **both**
  (1) the operator starting the daemon with `PW_BROWSER_ALLOW_UNSAFE_CRED_PATH=1`
  (a process env var a caller sending HTTP commands cannot set), and
  (2) the caller passing `--unsafe` (intent, not authority).
  Without (1), `--unsafe` is rejected with `UnsafeOverrideNotPermitted` and nothing is written.
- **Symlink escape closed**: paths are now resolved via `realpath` on the deepest existing
  ancestor, so a symlink planted inside `~/.pw-browser` can no longer redirect credential
  files outside the confinement.
- **Structured errors**: refusals now carry error kinds `CredentialPathConfined` /
  `UnsafeOverrideNotPermitted` instead of a bare 400 message.
- **Audit trail**: every credential-path access (allowed, denied, or operator-escaped) is
  logged to the daemon's stderr; the daemon also prints a startup warning when the
  override env is enabled. Responses gain a `confined` boolean.
- Docs aligned across SKILL.md (frontmatter `permissions.enforcement` +
  `operator-gated-override`, enforcement-boundary section, Rogue Agent mitigation ⑤),
  README zh/en, QUICKSTART zh/en, and the `--help` banner (now lists daemon env vars).
- Tests: `b-negative.js` gains a phase 3 daemon with the operator opt-in; asserts
  `--unsafe` alone is refused and writes nothing, that the env alone does not weaken the
  default, and that env + flag yields `confined:false` + warning. `a-group.js` exports now
  stay inside `STATE_DIR`.

## [1.3.7] — 2026-07-30

### Fixed

- **`eval "<expr>" <ref>` (element-scoped) was broken** — the expression was closed over from Node scope
  (`el.evaluate(el => eval(expr))`). Playwright serializes the callback to a string and runs it in the
  browser, so `expr` was never defined there and the call failed with a `ReferenceError`. The expression
  is now passed explicitly as an evaluate argument. This path had **no test coverage**, which is why the
  defect went unnoticed.

### Changed

- `eval` responses now carry an explicit `scope` field (`"page"` | `"element"`) so callers can verify
  which semantics were applied instead of guessing.
- Result serialization hardened: `JSON.stringify` failures (circular structures, `undefined`) no longer
  produce a broken payload; they fall back to `String(v)`.
- Rewrote the `eval` code comment to state the real execution semantics (Playwright does **not** capture
  Node closures; `el` is the documented binding for the element-scoped form) alongside the security
  boundary, removing an ambiguity that invited unsafe assumptions about where code actually runs.

### Documentation

- `SKILL.md` / `README.md` / `README.en.md` now document the scope semantics of `eval`: without `ref` the
  expression evaluates against the page global; with `ref` the identifier `el` is bound to the DOM node.
  Return values must be JSON-serializable (DOM nodes and circular structures cannot cross the bridge).

### Tests

- `tests/features.js`: +5 assertions covering the previously untested element-scoped `eval` path
  (`el.textContent`, `el.id.toUpperCase()`, `el.getAttribute(...)`, `scope` field for both forms).

## [1.3.6] — 2026-07-30

### Docs / Security (intent-code divergence, 93% confidence)
- **修正 `run-code` 沙箱注释夸大安全边界**：原注释称"user code can drive the browser but cannot reach the host"，暗示已被锁死，但忽略注入的 `page` 对象本身就是完整浏览器权威（可访问任意站点、读认证会话、触发下载/上传、以用户身份发带凭证请求）。新注释明确：VM 隔离的是**宿主机**（OS/文件系统/进程），**不是浏览器会话/网络**；`page` 等同把用户的浏览器交给代码；必须仅在可信、用户可见的本地环境启用，不可信输入绝不能到达；并澄清 token 认证只限网络可达性、非能力沙箱。SKILL.md/README 既有 `run-code` 描述本已准确，无需改动。

## [1.3.5] — 2026-07-30

### Docs / Security (description-behavior mismatch, 95% confidence)
- **包描述不再轻描淡写**：`package.json` 的 `description` 原为"普通浏览器自动化 CLI"，漏掉了实质高危能力。现改为如实声明 `INCLUDES HIGH-RISK PRIMITIVES`：cookie/localStorage 凭证提取/注入（会话令牌）、页面任意 JS（`eval`）、守护进程代码执行（`run-code`）及持久化凭证会话，并标注 daemon token 认证与 `PW_BROWSER_SAFE_MODE=1` 可禁用全部代码执行与凭证原语。
- README 中英文开头同步新增 ⚠️ 醒目警示，明确"本工具不只是点开网页"，列出代码执行与凭证操控能力，并指向「🔐 权限模型与最低特权」「⚠️ 安全边界」两节，消除与 SKILL.md 已有准确描述的失配。三处（package.json / README.zh / README.en）现已一致。

## [1.3.4] — 2026-07-30

### Docs / Security (LP3 — MCP least-privilege, 90% confidence)
- **形式化权限模型**：此前 SKILL.md 仅有自由文本 `capabilities` / `allowed-tools`，缺乏可被编排者/审核者解析的权限模型，容易把"能力清单"误读成"授权边界"从而低估攻击面。本版在 SKILL.md frontmatter 新增**机器可读的 `permissions` 块**（`model: none-formal`、`enforcement`、`least-privilege`、`metadata-is`），并新增章节「🔐 权限模型与最低特权」：
  - 明确 `capabilities` 是**攻击面描述，不是权限授予、也不是沙箱边界**；
  - 给出**三级部署矩阵**（全能力 / 安全模式 / 沙箱+安全模式）及每级残余风险；
  - 列出**实际执行边界**（token 仅限网络可达性、安全模式是唯一内建能力开关、路径限制、宿主工具策略局限）；
  - 声明本技能**没有**独立于上述四点的形式化权限系统，最低特权须在编排层落实。
- README 中英文「安全说明」同步补充权限模型提示，与 SKILL.md 三处一致。

## [1.3.3] — 2026-07-30

### Fixed
- **技能名不合规导致安装失败**：SKILL.md frontmatter 的 `name` 由 `Playwright-browser-use` 改为全小写 `playwright-browser-use`。宿主平台校验规则要求技能名只能包含小写字母、数字与连字符，原大写首字母会在添加技能时报 `Invalid skill name`。
- 同步将发布镜像目录改名为 `playwright-browser-use`，并更新 `sync.sh` / `make-release.sh` 的默认路径，保证目录名与技能名一致。

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
