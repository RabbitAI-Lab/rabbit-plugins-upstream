# Changelog

## 0.1.2 — 2026-11-05

可移植性修复版。功能、安全边界和发布包内容规则不变，只修“ClawHub 安装副本跑不通随包测试”。

### 修复

- ClawHub 发布器会跳过任何含点号路径段的文件，`tests/fixtures/aging-agent` 里的 `.mcp.json`、`.app.json`、`.usage.json` 因此进不了安装副本，导致安装后 `python3 -m unittest discover -s tests` 出现 2 项失败。`tests/test_audit.py` 现在会在拷贝 fixture 后按内联内容补齐这三个隐藏文件。
- `tests/test_release.py` 的清单一致性检查允许“隐藏文件缺失”，但仍要求其余清单项与 GitHub 包完全一致，避免掩盖真实缺件。

### 验证

- 剥离全部点号路径文件模拟 ClawHub 安装副本后，`python3 -m unittest discover -s tests` 33 tests OK。
- 三个平台安装副本与源码 `scripts/agent_slim.py` 的 SHA-256 一致。

## 0.1.1 — 2026-11-05

发布后回查修复版。0.1.0 的功能与安全边界不变，仅修复“发布包内测试不能独立运行”和文档状态。

### 修复

- `tests/fixtures/aging-agent` 之前被 `.gitignore` 排除且未随包发布，导致干净安装后运行 `python3 -m unittest discover -s tests` 时 `test_audit` / `test_workflow` 共 13 项报 `FileNotFoundError`。fixture 现随仓库和 GitHub/ClawHub 包发布，SkillHub 轻量包仍不含 tests。
- `.gitignore` 不再忽略该合成 fixture；它只含生成数据，无用户、项目或公司内容。

### 文档

- README 增加 GitHub / SkillHub / ClawHub 三平台安装入口、版本和 SHA-256 核对方式。
- 更新“当前状态”：三平台已发布 v0.1.1，并保留真实宿主触发回归 `PARTIAL` 的说明。

### 验证

- 本机与公开包隔离目录均执行 `python3 -m unittest discover -s tests`：33 tests OK。
- 公开包 fixture 端到端：180 个文件 apply 后 `restore --apply` 全部复原（SHA-256、大小、mode、mtime 一致），二次恢复返回 `already-restored`。

## 0.1.0 — 2026-11-05

首次公开发布（release candidate）。

### 功能

- `host`：只读探测宿主能力，输出 `supported / unknown / unsupported` 三态；缺失 Home 时相关能力降级为 `unknown`，不猜。
- `audit`：Hot/Warm/Cold 三层盘点，Token 与磁盘分账，输出结构化证据、warning、unknown 和候选。
- `plan`：只把 allowlist 内动作放进 ready；无哈希或确认证据的项停在 pending。
- `apply`：默认 dry-run；`--apply` 事务化移动，写 manifest、`manifest.sha256`、`restore.py` 和 `restore.sh`。
- `verify`：保留文件、引用、frontmatter、可选 test-prompts 回归；缺 test-prompts 时为 `PARTIAL`。
- `restore`：幂等恢复，冲突返回 `SOURCE_CONFLICT` 并保留双方内容。
- 三种可执行动作：`quarantine-redundant-backup`、`archive-verified-old-session`、`quarantine-low-frequency-file`。

### 发布包

- GitHub 完整包：源码、测试、docs、references、schemas、agents 配置和图标。
- SkillHub 轻量文本包：运行脚本、SKILL/README、契约文档和图标，不含 tests 与构建脚本。
- ClawHub 合规包：与 GitHub 完整包功能一致，按仓库根目录布局。
- 三包共享文件逐字节一致，SHA-256 写入 `SHA256SUMS.txt`。

### 版本说明

开发期内部里程碑曾使用 0.1.0 → 0.2.x → 0.3.0 作为工作版本号。公开发布按计划统一重编号为首发版 0.1.0；此前版本从未对外发布，不存在外部用户升级问题。功能等价于内部 0.3.0（s4 完成态）。

### 已知缺口

- 真实宿主 test-prompts 未提供，触发/路由回归只能记 `PARTIAL`，不作为“能力未回退”的完整证据。
- 非 Codex 宿主只有适配器接口，未实测。
- 内容改写、插件关闭、数据库维护、系统配置修改仍属人工复核，不在自动执行范围。

### 兼容性

Python 3.9+，仅标准库；macOS、Windows、Linux。文件路径参数请加引号以避免空格问题；Windows 请使用 PowerShell 或 Git Bash 调用 `.sh` 之外的 `.py` 入口。
