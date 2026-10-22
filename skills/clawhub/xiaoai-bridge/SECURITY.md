# 安全说明

## 支持的版本

| 版本 | 状态 |
|------|------|
| 1.1.x | 接收安全修复 |
| 1.0.x | 不再支持，且包含已泄露的会话文件，请勿使用 |

## 凭据模型

`MI_PASS_TOKEN`（或 `MI_PASSWORD`）等价于小米账号的登录能力，可读取设备列表与语音对话记录、控制音箱播放。

- 请使用专用账号，不要使用主账号。
- 优先使用 `passToken`，密码登录可能触发验证码与风控。
- 不要把 `.env`、`.mi.json` 提交到版本库或打包进发布物。

## 运行期会话缓存

上游依赖 `@mi-gpt/miot@1.2.2` 硬编码把会话写入 `process.cwd()/.mi.json`，内容包括 `passToken`、`serviceToken`、`ssecurity` 与设备信息。

本 Skill 的防护：

1. 登录前 `process.chdir()` 到 `XIAOAI_STATE_DIR`，默认 `os.tmpdir()/xiaoai-bridge`；
2. 目录权限收紧为 0700，缓存文件尽量收紧为 0600（Windows 上依赖用户目录 ACL）；
3. `node scripts/xiaoai-listen.js clean` 删除缓存；
4. `.gitignore` 忽略 `.mi.json`、`.env`、`.state/`；
5. 启动时若在技能目录发现遗留 `.mi.json`，只告警，不加载。

## 关于 v1.0.0 中泄露的会话数据

v1.0.0 的发布包包含 `scripts/.mi.json`，其中有一个真实的小米账号会话（账号 ID 与设备序列号不再在此重复）。该文件已在 1.1.0 中删除，但**删除文件不等于撤销会话**：

1. 如果你是该账号的所有者，请立即在小米账号中心退出所有设备的登录并修改密码；
2. 重新获取 passToken，旧 token 视为已泄露；
3. 检查账号下是否有异常的智能家居操作或设备绑定。

其他使用者请勿使用该文件中的任何凭据；它可能早已过期，但仍属于敏感数据。

## 依赖策略

- 依赖源固定为 `https://registry.npmjs.org/`（见 `scripts/.npmrc`），禁止明文 HTTP；
- `package-lock.json` 锁定完整依赖树并校验 integrity；
- 直接依赖使用精确版本；
- 发布前执行 `npm ci` 与 `npm audit --omit=dev`，要求 0 漏洞。

## 运行建议

- 使用专用、非特权系统账号运行；
- 只向该进程提供必要的环境变量；
- 不要把监听进程的 stdout 转写长期落盘；
- 定期执行 `clean`，并检查 `XIAOAI_STATE_DIR` 权限。

## 报告安全问题

请通过仓库 Issue 或发布者主页私下联系维护者，不要在公开 Issue 中粘贴 passToken、serviceToken、账号 ID 或语音转写内容。
