# 宿主编排：Yandex 只读巡检

> **何时 Read**：用户要 Yandex / 直通广告自动化、巡检、熔断、余额或 CPA 预警。Google 熔断走 `references/operations/guard.md`；Bing 走 `hosted-automation-bing.md`。
> **能做什么**：拉余额、拉日报/周期报表、宿主按阈值告警。
> **不能做什么**：暂停、改价、改预算、封禁专用接口、拒审列表、落地页列表、小时花费。没有写命令，**禁止**假装已执行熔断。

**前置**：已 `siluzan-tso login`，并用 `list-accounts -m Yandex --json-out ./snap` 确认 `mediaCustomerId`（形如 `porg-…`，**不是**纯数字，也不是 `entityId`）。

**硬约束**：

- `guard` **只支持 Google**。禁止 `guard … -m Yandex`。
- 没有 `account-status` / `bulk-ads` / `campaign-entities` 这类实体子命令。
- `yandex-analysis` 日期不能晚于今天；省略则默认近 7 天**含今天**。`search-terms` 只支持近 180 天。
- `balance-scan` / `accounts-digest` 的消耗是每日同步**截至昨天**；查当天消耗用 `yandex-analysis`，不要用 `stats` 判断今天。

---

## 1. 余额续航

```bash
siluzan-tso balance-scan -m Yandex --threshold-days 7 --json-out ./snap-yandex
```

已知子集加 `-a porg-xxx,porg-yyy`。命中续航/余额不足 → 宿主通知充值。CLI **不能**自动充值。单户复核：

```bash
siluzan-tso balance -m Yandex -a <porg-xxx> --json-out ./snap-yandex
```

---

## 2. 多账户消耗 / CPA / 零转化（截至昨天）

一条命令扫该媒体全部户（或 `-a` 子集）。区间必须是已结束的日期，**不要把今天当完整日**：

```bash
siluzan-tso accounts-digest -m Yandex --start <S> --end <D> --json-out ./snap-yandex
siluzan-tso accounts-digest -m Yandex --start <S> --end <D> --zero-conversions --json-out ./snap-yandex
siluzan-tso accounts-digest -m Yandex --start <S> --end <D> --max-cpa <目标CPA> --json-out ./snap-yandex
```

命中 → 宿主告警账户、区间花费、转化、CPA。不能自动关停。

---

## 3. 单户当日 / 近日花费与 CPA（可含今天）

```bash
mkdir -p ./snap-yandex
siluzan-tso yandex-analysis -a <porg-xxx> --json-out ./snap-yandex \
  --start <当日或近几日> --end <当日> --sections overview,daily,campaigns
```

宿主侧：

- **日花费异动**：读 `daily` 按日对比前一日或近 7 日均值，超阈值告警。
- **系列花费 / 预算**：同一窗口读 `campaigns`，用落盘里的花费对照 `budget`；缺字段就不要猜，改用日环比。
- **CPA**：`花费 / 转化`（转化为 0 不算 CPA，改走空耗判断）。超过约定目标倍数 → 告警。
- **空耗**：当日（或约定日）花费已达「目标 CPA × N」且转化为 0 → 告警「空耗预警」，文案不要写成「已熔断」。目标 CPA 用落盘 `targetCpa` 或账户约定。

没有小时维度，做不了「近两小时 CPA」。

---

## 4. 周期报告（给人看，不代替巡检告警）

```bash
siluzan-tso yandex-analysis -a <porg-xxx> --start <S> --end <D> --json-out ./snap-yandex
```

出 HTML 按 `report-templates/yandex-period-report.md` 写 narrative 后再 `yandex-analysis render`。自动化任务里报告是可选交付物；阈值告警仍走上面 1–3 步。

---

## 做不到（勿编造命令）

| 场景           | 现状                                      |
| -------------- | ----------------------------------------- |
| 账户封禁专用   | 无；`list-accounts` 状态仅供人工看        |
| 素材拒审       | 无拒审列表                                |
| 落地页探活     | 无最终到达网址接口                        |
| 小时花费       | 无                                        |
| 自动暂停 / 改价 | 无写接口；告警后人工在 Yandex 后台处理 |
