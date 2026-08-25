# guard —— Google 全户熔断扫描（只读）

> 流程见 `hosted-automation-user-catalog.md`（预算/空耗自控）。单户排障仍可用 `ad campaigns` / `ad groups`。
> **仅 Google**。本命令**只扫描列出命中，不会暂停任何账户/系列/组/创意**。
> 若要对某个命中对象停投，必须对该账户单独执行 `ad campaign-status` / `ad adgroup-status` / `ad ad-status`（带 `--commit`），以便写审计能记清「改了哪个账户的哪个对象」。

## 何时用

| 用户话术                                           | 命令                                   |
| -------------------------------------------------- | -------------------------------------- |
| 所有账户系列当日花费 ≥ 日预算 110% → **列出**      | `guard budget-circuit`                 |
| 空耗：花 ≥ 目标 CPA × N 且转化 0 → **列出**组/创意 | `guard zero-conv`                      |
| 确认后暂停某一户的某一条系列/组/创意               | `ad campaign-status` / `adgroup-status` / `ad-status` |
| 只查某一户 / 改预算后复核单系列                    | 仍用 `ad campaigns -a … --start=--end` |

**禁止**外层 for-loop：`list-accounts` × 多媒体再逐户 `ad campaigns` 做全户扫描。  
**禁止**指望 `guard` 一条命令批量暂停——没有 `--apply`，也不会改投放状态。

---

## budget-circuit（超预算）

```bash
siluzan-tso guard budget-circuit -m Google \
  [--date YYYY-MM-DD] [--ratio 1.1] [-a id1,id2] \
  --json-out ./snap-guard

# 确认某条命中后，对该账户单独暂停（须 --commit，写审计记这一次）
siluzan-tso ad campaign-status -a <mediaCustomerId> --id <campaignId> \
  --status Paused --commit "超预算熔断 2026-07-28"
```

| 选项         | 说明                                                             |
| ------------ | ---------------------------------------------------------------- |
| `-m Google`  | 必填；其它媒体 exit 1                                            |
| `-a`         | 子集 mediaCustomerId；省略则扫名下全部 Google 户                 |
| `--date`     | 统计日；默认 Asia/Shanghai 今天；**强制当日 spend**（start=end） |
| `--ratio`    | 默认 `1.1`（建议 1.10–1.20）                                     |
| `--status`   | 默认只查 `Enabled`；传 `*` 不过滤                                |
| `--json-out` | Agent 必带                                                       |

命中条件：`budget > 0` 且 `spend >= budget * ratio`（`budget`/`spend` 均为元；`spend` 为该日合计）。

---

## zero-conv（空耗）

```bash
siluzan-tso guard zero-conv -m Google \
  [--date YYYY-MM-DD] [--cpa-multiple 3] [--level adgroup|ad|both] \
  [--fallback-target-cpa <元>] \
  --json-out ./snap-guard

# 确认某条命中后，对该账户单独暂停
siluzan-tso ad adgroup-status -a <mediaCustomerId> --id <adGroupId> \
  --status Paused --commit "空耗熔断 2026-07-28"
```

| 选项                     | 说明                                                                          |
| ------------------------ | ----------------------------------------------------------------------------- |
| `--cpa-multiple`         | 默认 `3`                                                                      |
| `--level`                | 默认 `adgroup`；`ad`/`both` 需 `--fallback-target-cpa`（创意无组级 CPA 字段） |
| `--fallback-target-cpa`  | 组无 `targetCpaAmountYuan` 时回退；缺失则进 `skipped[]`                       |
| `--json-out`             | Agent 必带                                                                    |

命中：`conversions === 0` 且 `spend >= targetCpaYuan * N`。摘要文案为 **「空耗熔断」**（宿主发 P1 时用此文案；CLI 不代发通知）。

---

## 输出与交付

- `--json-out` 落盘命中表；无命中也必须收口（打印「无命中」）
- 命中后用 **逐账户** `ad *-status` 暂停，**没有** `--apply`

恢复：人工加预算 / 改出价后，用 `ad campaign-status|adgroup-status|ad-status … --status Enabled`（或网页），**禁止**无人值守自动恢复。

---

## 与旧编排对照

| 旧（易失败）                                             | 新                               |
| -------------------------------------------------------- | -------------------------------- |
| 6 媒体 list-accounts → 逐户 ad campaigns → 脚本比 budget | `guard budget-circuit -m Google` |
| 逐户 ad groups + 手写阈值                                | `guard zero-conv -m Google`      |
| `ad campaigns -m Google`（非法）                         | 单户用 `-a`；全户扫描用 `guard`  |
