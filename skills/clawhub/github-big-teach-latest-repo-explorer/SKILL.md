---
name: "github-big-teach-latest-repo-explorer"
description: "默认90天窗口，star必须>1000；无满足条件仓库时依次扩大到180/360/540天。"
---

# 自动扩展时间窗口

## 默认行为

- 默认扫描最近 90 天（约 3 个月）。
- 硬性过滤条件：`stargazers_count` **必须大于 1000**，不满足直接排除，不计入候选。
- 默认选择策略为 `stars`：从满足 stars>1000 且未输出过的候选中按 `stargazers_count` 降序选择，Stars 相同时按 `created_at` 降序。
- 使用 GitHub Core API 获取组织公开仓库，并在本地按 `created_at` 与 `stargazers_count > 1000` 双重筛选。

## 扩窗规则

当当前窗口内满足 `stars > 1000` 的未输出仓库数为 0 时，按以下顺序自动扩大：

1. 最近 90 天（默认，约 3 个月）
2. 最近 180 天（约 6 个月）
3. 最近 360 天（约 12 个月）
4. 最近 540 天（约 18 个月）

每次扩大窗口后重新计算候选总数、已输出数和未输出数（均基于 stars>1000 过滤后的集合），排除 `references/history.json` 中已经输出的 `full_name`，并按当前选择策略重新选择。540 天窗口仍无满足条件（stars>1000 且未输出）的仓库时停止扩展并输出无可选结果。

## 参数和输出

- `--days N`：用户显式指定时作为初始窗口；扩窗候选为 `N`、180、360、540 天，并去除重复或不大于当前窗口的窗口。
- `--pick stars`：默认，选择 Stars 最多（仍需先满足 stars>1000）。
- `--pick oldest`：在满足 stars>1000 的候选中选择创建时间最早。
- `--pick random`：在满足 stars>1000 的候选中随机选择。
- `--count`、`--org-config`、`--reset-history`、`--dry-run`、`--workers` 保持现有行为。
- 严格遵守 `references/output_template.md`，标题、筛选条件和统计使用最终实际窗口，并明确标注 `stars > 1000` 这一硬性条件；README 信息不足时明确标注“信息有限，基于元数据推断”，禁止编造。

## 历史和验收

- 正式运行成功选择后才写入 `references/history.json`；dry-run 不修改历史。
- 组织请求失败继续处理其它组织，并列出失败组织。
- 验收命令：

```bash
python3 scripts/fetch_repo.py --days 90 --count 1 --dry-run
```
