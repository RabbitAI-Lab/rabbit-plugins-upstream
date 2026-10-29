---
name: "github-big-teach-latest-repo-explorer"
description: "默认3个月窗口，star必须>1000；无满足条件仓库时依次扩大到6/12/24/36/48/60个月，最晚回溯到GPT-4发布时间（2023-03-14）。"
---

# 自动扩展时间窗口

## 默认行为

- 默认扫描最近 3 个自然月。
- 硬性过滤条件：`stargazers_count` **必须大于 1000**，不满足直接排除，不计入候选。
- 默认选择策略为 `stars`：从满足 stars>1000 且未输出过的候选中按 `stargazers_count` 降序选择，Stars 相同时按 `created_at` 降序。
- 使用 GitHub Core API 获取组织公开仓库，并在本地按 `created_at` 与 `stargazers_count > 1000` 双重筛选。

## 数据来源

- 组织名单：本地文件 `references/organizations.json`，格式为 `{公司: [组织主页链接, ...]}`，目前 9 家公司、158 个 GitHub 组织。脚本把链接解析成组织名；名单手工维护，不自动发现。`scripts/probe_orgs.py` 仅用于检查名单中的链接是否有效，不参与正常运行。
- 仓库列表：GitHub Core API，逐个组织请求 `GET https://api.github.com/orgs/{org}/repos?type=public&sort=created&direction=desc&per_page=100`，按创建时间倒序分页，翻到早于窗口起点的仓库即停止；不使用 Search API。
- 本地筛选：用 `created_at` 过滤时间窗口，再用 `stargazers_count > 1000` 过滤。
- README：单独请求 `GET /repos/{owner}/{repo}/readme`。
- 认证与额度：使用 `GITHUB_TOKEN`，Core API 额度为每小时 5000 次；每个窗口档位都会重新请求全部组织，额度耗尽时请求返回 403，该组织记为查询失败。
- 只覆盖名单内的组织，名单外的仓库不会被搜到。

## 扩窗规则

当当前窗口内满足 `stars > 1000` 的未输出仓库数为 0 时，按以下顺序自动扩大（单位：自然月）：

1. 最近 3 个月（默认）
2. 最近 6 个月
3. 最近 12 个月
4. 最近 24 个月
5. 最近 36 个月
6. 最近 48 个月
7. 最近 60 个月

任一档的起始日期不晚于 GPT-4 发布日期（2023-03-14）时，起始日期按 2023-03-14 截断，并作为最后一个窗口，不再继续扩大。

每次扩大窗口后重新计算候选总数、已输出数和未输出数（均基于 stars>1000 过滤后的集合），排除 `references/history.json` 中已经输出的 `full_name`，并按当前选择策略重新选择。最终窗口（GPT-4 发布时间）仍无满足条件（stars>1000 且未输出）的仓库时停止扩展并输出无可选结果。

## 参数和输出

- `--months N`：用户显式指定时作为初始窗口（自然月）；扩窗候选为 `N`、3、6、12、24、36、48、60 个月，去除重复或不大于当前窗口的档位，起始日期不早于 2023-03-14。
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
python3 scripts/fetch_repo.py --months 3 --count 1 --dry-run
```
