# 平台发布手册

各分发平台的命令、认证与注意事项。供 distribute.py 执行时参考或排障。

## GitHub（单一事实源，必配）

- 密钥: `GITHUB_TOKEN`（Personal Access Token，需 `repo` 权限）。
- 仓库不存在时 distribute.py 自动创建（默认 private，可在 config.json `github.private` 修改）。
- 命名空间即 GitHub 身份：`github.com/<owner>/<repo>`。
- 推送后 remote URL 会移除 token，避免凭证残留 `.git/config`。

## ClawHub（OpenClaw 技能注册中心）

- 安装: `npm install -g clawhub`
- 登录（一次性，OAuth 需 GitHub 账号）: `clawhub login`
- 发布: `clawhub skill publish <path> --slug <slug> --name <名称> --version <版本> --changelog <说明>`
- 更新版本: 修改 SKILL.md 版本后重新 publish；`--version` 不变化时命令会跳过未变更内容。
- 注意: 新账号要求 GitHub 账号注册满一周；发布前先 `clawhub validate` 校验技能包。（本工具已关闭 GitHub Actions 自动同步，发布一律由 distribute.py 显式触发）

## 官方 MCP Registry

- 安装: 从 modelcontextprotocol 官方 release 下载 `mcp-publisher` 二进制。
- 登录: `mcp-publisher login github`（交互式 OAuth，命名空间 `io.github.<用户名>/<server>`）；或 `mcp-publisher login dns --domain <域名>`（自定义域名，需配置 DNS TXT 记录与 Ed25519 密钥）。
- 发布: `mcp-publisher publish`，需仓库含 `server.json`。
- CI 模式: 部分认证方式支持 token 环境变量；交互式 OAuth 无法在 CI 完成时，改为本地一键命令发布（distribute.py 的 `mcp` 步骤）。

## 腾讯 SkillHub

- 官方站点: skillhub.cloud.tencent.com，支持 网页 / CLI / Agent 自动化部署 三种发布方式。
- 前置: 腾讯云实名认证（人脸核身，一次性）。
- SKILL.md frontmatter 需含: `slug`、`displayName`、`version`、`summary`、`license`。
- 发布: 网页上传 SKILL.md 文件，或 CLI/Agent 推送（CLI 名称以官方文档为准，可在 config.json `platforms.skillhub.command` 自定义）。
- 付费变现: 发布设置中勾选接入 SkillPay，企业认证并绑定支付账户后按调用量结算。
- 注意: 上架需平台安全审核；已发布到 Hub 后可在腾讯云智能网关侧管理上线/下线。

## 镜像站（Gitee / GitCode / GitLab）

- 方式一（平台内置）: Gitee / GitCode 提供"从 GitHub 导入并自动同步"功能，开启一次即可。
- 方式二（脚本）: 在 `config.json` 的 `mirrors.repos` 或 `MIRROR_URLS` 中列出含令牌的 git URL，由 distribute.py 显式执行 `git push --mirror`（仅发布时触发，无 CI 自动同步）。
- 注意: 镜像仓库是备份通道，不承担发布审核。

## 聚合目录（自动收录，无需主动上架）

- Glama / PulseMCP / Smithery / MCP Toplist / mcp.so: 自动抓取官方 MCP Registry 与 GitHub，发布到 Registry 后即会被收录。
- awesome-* 列表: 向对应仓库提交 Pull Request 将自己的仓库加入清单（一次性）。

## 通用排障

- `check_env.py` 未列出某 CLI → 该平台自动跳过，不影响其他平台。
- tag 已存在 → 用 `--tag` 指定新版本，或 `--force` 覆盖。
- 平台发布失败但返回非零 → 检查该平台登录态（clawhub login / mcp-publisher login / SkillHub 实名）。
