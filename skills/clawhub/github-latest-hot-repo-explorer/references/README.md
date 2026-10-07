# GitHub Token 配置

脚本仅读取系统环境变量 `GITHUB_TOKEN`，不读取本目录的 `.env` 文件。

未配置 Token 时，脚本会使用 GitHub 匿名 API 请求；如果触发限流，请配置环境变量后重试：

```bash
export GITHUB_TOKEN="你的_GitHub_PAT"
python3 scripts/fetch_repo.py
```

Token 只需具备读取公开仓库所需的最小权限。不要把 Token 发到聊天、写入 `.env`、提交到 Git 仓库或共享给他人。

常见问题：

- `401 Unauthorized`：`GITHUB_TOKEN` 无效、已撤销或没有访问权限。
- `403` / `429`：GitHub API 限流；匿名请求请配置 `GITHUB_TOKEN` 后重试，已使用 Token 则稍后重试。
