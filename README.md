# rabbit-plugins-upstream

上游 Agent Skills 的全量镜像仓库。内容由 GitHub Actions 定时同步，变更以 Pull Request 形式进入，请通过 PR 审查后再合并。

> ⚠️ 本仓库内容均为上游公开内容的**镜像**，版权归原作者/发布者所有，各 skill 目录内保留其原始 LICENSE。skill 内容本质上是 prompt 与可执行脚本，**合并 PR 前请人工审查上游变更**。

## 上游来源

| 来源 | 说明 | 镜像方式 |
|---|---|---|
| [ClawHub](https://clawhub.ai) | OpenClaw 官方 skill 注册表（约 69k skills） | `/api/v1/skills` 全量枚举 + `/api/v1/download` 下载完整内容 |
| [skills.sh](https://www.skills.sh) | Vercel 的 agent skills 目录（约 20k skills） | sitemap 枚举 + 从对应 GitHub 仓库拉取 skill 目录内容 |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/skills) | Nous Research 的聚合索引（约 90k skills，含上述两者） | 镜像其 unified index（元数据，按来源拆分）；其中 official / github 等带仓库路径的条目额外镜像完整内容 |

## 目录结构

```
skills/
  clawhub/<slug>/ 或 <owner>--<slug>/    # ClawHub skill 完整内容（slug 撞名时带 owner 前缀）
  skills-sh/<owner>--<repo>--<skillId>/  # skills.sh skill 完整内容
  hermes/_index/<source>.json            # Hermes 聚合索引（仅元数据）
  hermes/<identifier>/                   # Hermes 索引中 official / github 等来源的 skill 完整内容
index/<source>.json                      # 各来源索引（由 build-index 生成）
sync-state/<source>.json                 # 各来源增量同步状态（按源隔离，支持并行同步）
scripts/                                 # 同步脚本（Node.js，零第三方依赖）
.github/workflows/sync.yml               # 定时同步 workflow（matrix 三 job 并行）
```

每个 skill 目录内含 `.upstream.json`，记录来源 URL、版本、内容哈希与同步时间。

## 同步机制

- **定时**：每天通过 `.github/workflows/sync.yml` 运行，三个来源 **matrix 并行**，也可手动 `workflow_dispatch` 触发（可选单一来源）。
- **首次全量**：ClawHub 全量（约 70k）在本地跑 `npm run sync:clawhub` 后直接提交 main；Actions 不承担首轮全量。
- **增量**：以 `sync-state/<source>.json` 对比上游版本/哈希，只拉新增与变更。ClawHub 枚举按最近活跃排序：**每日只枚举最新 40 页**（约 4000 条，覆盖 3000 条更新额度），**每周一全量枚举**（约 700+ 页，覆盖下架删除与深层变更）；上游下架的 skill 在全量轮删除（在 PR diff 中可见）。
- **分批**：单次运行处理量受 `SYNC_MAX_ITEMS`（默认 3000/来源）限制，状态随每次提交持久化。
- **落地**：每个来源独立建分支 `sync/<source>/<date>` 并开独立 PR（文件路径互不重叠，可分别审查合并）；无变更则不开。

## 本地运行

```bash
# 小批量试跑
SYNC_MAX_ITEMS=20 npm run sync:clawhub

# skills.sh 源需要 GitHub token（仓库 API 限流），Actions 中自动注入
GITHUB_TOKEN=$(gh auth token) SYNC_MAX_ITEMS=20 npm run sync:skills-sh

npm run sync:hermes   # 只拉一个约 35MB 的索引 JSON
node scripts/build-index.mjs clawhub   # 重新生成 index/<source>.json 与下方对应统计区
```

环境变量：`SYNC_MAX_ITEMS`（每轮处理上限）、`SYNC_CONCURRENCY`（并发数，默认 6）、`GITHUB_TOKEN`。

## 索引统计

### ClawHub

<!-- INDEX:clawhub:START -->
最后同步：2026-07-26T20:32:47.298Z

已镜像完整内容：**71024** 个 skill，明细见 `index/clawhub.json` 与 `skills/clawhub/`。
<!-- INDEX:clawhub:END -->

### skills.sh

<!-- INDEX:skills-sh:START -->
最后同步：2026-08-23T07:53:29.850Z

已镜像完整内容：**4880** 个 skill，明细见 `index/skills-sh.json` 与 `skills/skills-sh/`。
<!-- INDEX:skills-sh:END -->

### Hermes 聚合索引

<!-- INDEX:hermes:START -->
最后同步：2026-07-27T10:53:35.712Z（上游索引生成于 2026-07-20T18:55:15.264264+00:00）

| 上游来源 | skill 数（元数据） |
|---|---|
| browse-sh | 440 |
| claude-marketplace | 1 |
| clawhub | 69150 |
| github | 438 |
| lobehub | 505 |
| official | 104 |
| skills.sh | 19967 |

其中已镜像完整内容：**542** 个（official / github 等来源，见 `skills/hermes/`）；元数据明细见 `skills/hermes/_index/`。
<!-- INDEX:hermes:END -->
