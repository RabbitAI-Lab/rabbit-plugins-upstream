# Changelog

本 skill 的所有重要变更记录于此。格式遵循 [Keep a Changelog](https://keepachangelog.com/)。

**版本编号规则**：每一次 commit 递增一个末位号（`0.0.1 → 0.0.2 → …`），阶段性里程碑进位。全部历史提交已回溯打 tag，对照表见文末[「版本对照表」](#版本对照表)。

## [1.0.4] - 2026-08-09 - 建立版本管理

### Added
- **回溯打 tag**：为全部 17 次历史提交补打带注释的 `v0.0.1` → `v1.0.3` 标签（tag 时间对齐原提交时间），GitHub Releases 时间线可用，从此可按版本引用与回滚，不必再报 commit hash。
- **`SKILL.md` frontmatter 新增 `version` 字段**（当前 `1.0.4`），skill 自带版本声明。
- CHANGELOG 补充「版本编号规则」与「版本对照表」，历史条目由日期标题改为 `[版本号] - 日期` 标准形式。

## [1.0.3] - 2026-08-09 - README 架构重画 + 文档/代码对齐修复

### Changed
- **README 架构图重画为三层**（Agent 产品层 → skill 应用层 → 浏览器后端层 → zhipin.com）。此前移除 Codex 框时只删了框、留下悬空的分支连线，图形残缺；现每行等宽对齐，并显式区分「**Agent 产品**用什么随意（含 Codex）」与「**浏览器后端**只能是 `brs`」这两层——避免把 R12 误读成"禁止用 Codex 跑这个 skill"。
- **徽章**：`works with` 拆成 `agent`（WorkBuddy / OpenClaw / Claude Code / Codex）+ `browser backend: brs only (R12)` 两枚，语义不再混淆。
- **前置依赖**：Python 要求写明 3.10+，补充「自动探测 PATH / 受管解释器 / venv，勿自建外部垫片绕过预检层」，新增 `preflight_env.sh` 一键自检项。
- **安全段限速数值与代码对齐**：改为「5s±3s 抖动（书签 8s / 发送 20s）、`DAILY_CAP=100` 超限 `exit 5`、命中软限流指数退避 5→10→20→40 封顶 60s」（原「间隔≥5s」与抖动实现不符）。
- **快速开始**：第 2 步补上实际存在的 `scripts/search_jobs.sh`（原文仅写「Agent 执行」，与"禁现写等价物"的复用铁律冲突）；`candidates.csv` 路径统一到 `.work/`；`profile.yaml` 示例补 `goal` 字段。
- **目录结构树补全**：新增 `CHANGELOG.md` / `preflight_env.sh` / `run_py.sh` / `strip_title.py`（此前缺失）。
- **贡献指南**：新增后端须为受控运行时（R12）；新增 Python 脚本须经 `run_py.sh` 调用并登记 `script_catalog.md`。

### Fixed
- `process_job.sh`：临时文件 `.parse_job.tmp` 默认目录由 `.`（工作区根）改为 `.work/`，并为 `.parse_job.tmp` / `.verify_html3.tmp` 补 `mkdir -p` 兜底——修复根目录被临时文件污染的根因，以及纯 `--send`（不经 read-jd）路径下 `.work/` 不存在导致写入失败的隐患。

## [1.0.2] - 2026-08-05 - brs-only 安全收口 + R12 反作弊 + 便携运行器

> 含 `v1.0.1`（主体改动）与 `v1.0.2`（`.gitignore` 忽略本地 `.learnings/`）两次提交。

### Added
- **R12 反作弊红线**：BOSS 直聘禁止**任何 Agent** 的浏览器扩展直控（含 Codex `@Chrome` / CloakBrowser）。skill 统一 **brs 单后端**（agent-browser-runtime 受控运行时）；`BZC_BACKEND=codex|cloak` 被 `common.sh` 硬拒绝（`exit 1` + 安装链接），把"禁止扩展直控"从文档约束升级为可执行拦截。
- **`scripts/run_py.sh`**：便携 Python 运行器（`source common.sh` 取 `$PYTHON` + `to_win_path`），消除受管环境无 `python3` 直跑失败；SKILL/README/script_catalog 全部改 `bash scripts/run_py.sh`。
- **`bz_wait` / `rate_backoff` 接线**：读 JD 前 `bz_wait` 等渲染就绪（防空串）；发送后命中「操作频繁」触发指数退避。
- **错误处理补全 `exit 6`**：职位已关闭/下架（页面含「职位已关闭」但无 `.btn-startchat`）→ 跳过该岗，**非撞墙**，不冷却。
- **`references/safety_rules.md` 新增 R12 段**；SKILL/README/browser_backend 安全纪律统一升至 **R1–R12**。

### Changed
- `codex.sh` / `cloak.sh` 移入 `scripts/backends/_deprecated/` 并加 ⛔ 头（仅供其他站点参考 `bz_*` 抽象，绝不用于 BOSS）。
- `filter_library.py`：`REQUIRED_FIELDS` 去掉「薪资」（搜索候选池因反爬无薪资列，`salary_floor` 此前静默死）；薪资门槛仅 JD 富化后的库生效（已知限制，已注释说明）。
- `strip_title.py`：正则第二截 `{2,6}` → `{2,4}`，修复误剥「王芳 感谢您的回复」类正常消息首行。
- Axis B 预检层：`preflight_env.sh` 自举 `sleep`/`seq`、`resolve_python` 强制校验 PyYAML、`to_win_path` 替代裸 `cygpath`；删除 `.work/runtime_env.sh` 冗余绷带（绕过原生层会"测的不是 skill"）。
- 文档一致性：SKILL.md / README.md / browser_backend.md / safety_rules.md / script_catalog.md 清除过时的「hosted 短路 emit_plan」「R1–R9」「hosted codex 边界」等表述，与 brs-only + R1–R12 现状对齐。

### Removed
- 公开仓库不再收录任何浏览器扩展直控后端；`codex`/`cloak` 不再出现在"支持后端"清单。

---

## 版本对照表

`v1.0.2` 之前的版本为回溯补打的 tag，条目未逐个展开；完整信息见 `git show v<版本号>`。

| 版本 | 日期 | commit | 说明 |
|---|---|---|---|
| `v0.0.1` | 2026-07-20 | `e36378b` | 初版：通用 BOSS 直聘求职 copilot skill |
| `v0.0.2` | 2026-07-20 | `15c2cc6` | 文档层审查缺陷 P2/C11/C12 + 契约说明 |
| `v0.0.3` | 2026-07-20 | `79de80c` | 合并代码层 + 文档层审查修复 |
| `v0.0.4` | 2026-07-20 | `f281833` | V2 审查 N1–N7（面议误杀/分块碰撞/日限额持久化） |
| `v0.0.5` | 2026-07-20 | `36dd4bc` | LICENSE 版权署名修正 |
| `v0.0.6` | 2026-07-20 | `c7527f5` | 清理 SKILL/README 迭代噪音 |
| `v0.0.7` | 2026-07-20 | `0b4ba18` | README 加 GitHub 状态徽章 |
| `v0.0.8` | 2026-07-20 | `5d3a31a` | SKILL.md 二次压缩 + 美化 |
| `v0.0.9` | 2026-07-20 | `e8de0a0` | SKILL.md 删冗余 H1 |
| **`v0.1.0`** | 2026-07-20 | `11677ff` | **里程碑**：frontmatter 压缩，初版文档定型 |
| `v0.1.1` | 2026-07-21 | `a761e13` | 收编搜索脚本 + 复用铁律机制化 + V4 修复 |
| `v0.1.2` | 2026-07-23 | `faa40eb` | 复用原则泛化 + win-native 适配 + 禁无人值守后台 |
| `v0.1.3` | 2026-07-23 | `ee2fe49` | V5 审查逐条核实 + 迭代纪律固化 |
| **`v1.0.0`** | 2026-07-25 | `d338517` | **首个稳定版**：发送校验去空白匹配 + 防御性剥离标题行 |
| `v1.0.1` | 2026-08-05 | `a3c242a` | brs-only 安全收口 + R12 反作弊 + 便携运行器 |
| `v1.0.2` | 2026-08-05 | `22de1eb` | 忽略本地 `.learnings/` |
| `v1.0.3` | 2026-08-09 | `241f179` | README 架构图重画为三层 + 文档/代码对齐 |
| `v1.0.4` | 2026-08-09 | — | 建立版本管理（回溯打 tag + version 字段 + 本表） |
