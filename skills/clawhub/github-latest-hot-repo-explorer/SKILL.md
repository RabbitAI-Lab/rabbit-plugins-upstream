---
name: "github-latest-hot-repo-explorer"
description: "GitHub 热门仓库探索：严格选取最高 star 仓库。"
---

# GitHub 最新热门仓库探索

运行 `scripts/fetch_repo.py` 获取符合条件的 GitHub 最新热门仓库，并基于仓库元数据与 README 解读项目定位、问题与解决方式。

## 筛选与获取逻辑

1. 默认筛选 stars > 5000 且最近 1 个自然月创建的仓库（可用 `--stars` 和 `--months` 调整）。
2. 在符合条件且未播报的仓库中，严格选取 star 最多的仓库（不再随机抽取）。
3. 当前窗口候选池全已播报时，按 `1 → 2 → 3 → 6 → 12 → 24 → 36 → 48 → 60` 个自然月自动扩窗，最早回溯到 2023-03-14（GPT-4 发布日），超出则以该日期为截止，不再继续扩大。
4. 排除已在 `references/history.json` 记录的历史仓库。

## Token 与限流

1. 优先读取系统环境变量 `GITHUB_TOKEN`，不读取或创建 `.env` 文件。
2. 未配置 Token 的匿名请求遇到限流时，提示配置系统环境变量 `GITHUB_TOKEN`（示例 `export GITHUB_TOKEN="***"`），不得索要或展示 Token。
3. 已配置 Token 仍遇限流时，提示等待配额恢复后重试。

## 常用命令

```bash
python3 scripts/fetch_repo.py
python3 scripts/fetch_repo.py --stars 5000 --months 2
python3 scripts/fetch_repo.py --reset-history
python3 scripts/fetch_repo.py --dry-run
```
