# Changelog

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
