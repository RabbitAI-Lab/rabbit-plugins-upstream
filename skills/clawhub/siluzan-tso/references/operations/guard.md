# guard —— Google 全户熔断扫描

> 流程见 `hosted-automation-user-catalog.md`（预算/空耗自控）。单户排障仍可用 `ad campaigns` / `ad groups`。
> **仅 Google**。非 Google 媒体本 CLI 无系列/组/创意暂停写能力。

## Contents

- 何时用
- budget-circuit（超预算）
- zero-conv（空耗）
- 输出与交付
- 与旧编排对照

---

## 何时用

| 用户话术 | 命令 |
| -------- | ---- |
| 所有账户系列当日花费 ≥ 日预算 110% → 暂停 | `guard budget-circuit` |
| 空耗熔断：花 ≥ 目标 CPA × N 且转化 0 → 暂停组/创意 | `guard zero-conv` |
| 只查某一户 / 改预算后复核单系列 | 仍用 `ad campaigns -a … --start=--end` |

**禁止**外层 for-loop：`list-accounts` × 多媒体再逐户 `ad campaigns` 做全户熔断。

---

## budget-circuit（超预算）

```bash
siluzan-tso guard budget-circuit -m Google \
  [--date YYYY-MM-DD] [--ratio 1.1] [-a id1,id2] \
  --json-out ./snap-guard

# 确认命中后暂停（须全局 --commit）
siluzan-tso guard budget-circuit -m Google --date 2026-07-28 --ratio 1.1 \
  --apply --json-out ./snap-guard --commit "budget-circuit 2026-07-28"
```

| 选项 | 说明 |
| ---- | ---- |
| `-m Google` | 必填；其它媒体 exit 1 |
| `-a` | 子集 mediaCustomerId；省略则扫名下全部 Google 户 |
| `--date` | 统计日；默认 Asia/Shanghai 今天；**强制当日 spend**（start=end） |
| `--ratio` | 默认 `1.1`（建议 1.10–1.20） |
| `--status` | 默认只查 `Enabled`；传 `*` 不过滤 |
| `--apply` | 默认 dry-run；加此旗才 `Paused` |
| `--json-out` | Agent 必带 |

命中条件：`budget > 0` 且 `spend >= budget * ratio`（`budget`/`spend` 均为元；`spend` 为该日合计）。

---

## zero-conv（空耗）

```bash
siluzan-tso guard zero-conv -m Google \
  [--date YYYY-MM-DD] [--cpa-multiple 3] [--level adgroup|ad|both] \
  [--fallback-target-cpa <元>] \
  --json-out ./snap-guard

siluzan-tso guard zero-conv -m Google --cpa-multiple 3 --apply \
  --json-out ./snap-guard --commit "zero-conv 空耗熔断"
```

| 选项 | 说明 |
| ---- | ---- |
| `--cpa-multiple` | 默认 `3` |
| `--level` | 默认 `adgroup`；`ad`/`both` 需 `--fallback-target-cpa`（创意无组级 CPA 字段） |
| `--fallback-target-cpa` | 组无 `targetCpaAmountYuan` 时回退；缺失则进 `skipped[]` |
| `--apply` / `--json-out` | 同 budget-circuit |

命中：`conversions === 0` 且 `spend >= targetCpaYuan * N`。`summary.label` 固定为 **「空耗熔断」**（宿主发 P1 时用此文案；CLI 不代发通知）。

---

## 输出与交付

- 落盘 section：`guard-budget-circuit` / `guard-zero-conv`
- 字段：`meta`、`summary`、`hits[]`、`paused[]`、`errors[]`（zero-conv 另有 `skipped[]`）
- stdout：一行摘要 JSON（若 `--json-out`）+ **人类可读命中表**（无命中也打印「无命中」——巡检必须收口）
- dry-run 命中后提示追加 `--apply --commit …`

恢复：人工加预算 / 改出价后，用 `ad campaign-status|adgroup-status|ad-status … --status Enabled`（或网页），**禁止**无人值守自动恢复。

---

## 与旧编排对照

| 旧（易失败） | 新 |
| ------------ | -- |
| 6 媒体 list-accounts → 逐户 ad campaigns → 脚本比 budget | `guard budget-circuit -m Google` |
| 逐户 ad groups + 手写阈值 | `guard zero-conv -m Google` |
| `ad campaigns -m Google`（非法） | 单户用 `-a`；全户熔断用 `guard` |
