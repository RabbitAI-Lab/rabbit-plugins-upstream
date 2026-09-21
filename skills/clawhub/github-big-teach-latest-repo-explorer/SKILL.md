---
name: "github-big-teach-latest-repo-explorer"
description: "国内外大厂最新开源仓库探索：优先选取 stars 最多仓库，支持自动扩窗。"
---

# 国内外大厂最新开源仓库探索

运行 `scripts/fetch_repo.py` 获取国内外大厂最新开源仓库，并基于仓库元数据与 README 解读项目定位、问题与解决方式。

## 筛选与扩窗逻辑

1. 默认扫描大厂组织列表最近 30 天（约 1 个月）创建的仓库。
2. 默认选择策略为 `stars`：从未输出候选中按 `stargazers_count` 降序选择，Stars 相同时按 `created_at` 降序。
3. 当当前窗口内的未输出仓库数为 0 时，自动按以下顺序扩大时间窗口：
   - 最近 30 天（默认，约 1 个月）
   - 最近 3 个月（按 90 天计算）
4. 每次扩大窗口后重新计算候选总数、已输出数和未输出数，排除 `references/history.json` 中已输出仓库。
5. 90 天窗口仍无未输出仓库时停止扩展并提示无可选结果。

## 常用命令

```bash
# 正常运行
python3 scripts/fetch_repo.py

# 试运行（测试环境，不写历史记录）
python3 scripts/fetch_repo.py --dry-run
```
