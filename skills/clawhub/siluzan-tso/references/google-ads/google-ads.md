# Google 广告（导航）

> `SKILL.md` / 工作流已指向子文件时，**直接 Read 子文件**。本文件含共享 Gotchas。

## 何时 Read

| 任务 | Read |
| ---- | ---- |
| 查系列/组/创意/关键词/搜索词/地理 | [`google-ads-read.md`](google-ads-read.md) |
| 创建/编辑/启停/否词/附加信息/PMax/设备出价 | [`google-ads-write.md`](google-ads-write.md) |
| batch 流水线、`ad batch`、AI 智投草稿（W4） | [`google-ads-batch.md`](google-ads-batch.md) |
| 搜索系列 7 步方案与门禁 | [`google-ads-campaign-plan.md`](google-ads-campaign-plan.md) |
| PMax 网关路径 | [`pmax-api.md`](pmax-api.md) |
| 优化/合规 SOP | [`rules/README.md`](rules/README.md)（只读索引 → 再读一个 rules 文件） |

## Gotchas

## 金额单位（全局重要）

> **所有 CLI 金额参数均按「主币种金额」传入**（如 `1.5` = ¥1.50 / $1.50）；CLI 写入网关前对「分」字段 ×100（含 `ad keyword-edit --max-cpc` → `maxCPC`）。
> **禁止** 按 Google micros（×1,000,000）填写任何金额参数。

---

## ID 来源速查

| 需要的 ID           | 获取命令                                                                |
| ------------------- | ----------------------------------------------------------------------- |
| `accountId`（`-a`） | `siluzan-tso list-accounts --json-out ./snap` → `mediaCustomerId`       |
| 广告系列 `id`       | `siluzan-tso ad campaigns -a <accountId> --json-out ./snap` → `id`      |
| 广告组 `id`、`name` | `siluzan-tso ad groups -a <accountId> --json-out ./snap` → `id`、`name` |
| 广告 `id`           | `siluzan-tso ad list -a <accountId> --json-out ./snap` → `id`           |
| 关键词 `id`         | `siluzan-tso ad keywords -a <accountId> --json-out ./snap` → `id`       |

---

