# 余额、消耗与多账户汇总

> 流程见 `playbooks.md` **P2** / **P3**；单户读数见 `workflows.md` **W1**。币种口径见 `currency.md`。

## Contents

- balance
- balance-scan（P2）
- accounts-digest（P3）
- stats

## balance-scan — 多账户余额续航扫描

一键扫描某媒体下**全部有效账户**的余额与日均消耗。`data.items` 返回**所有已检查账户**（不只预警行）；用 `hitReason` 标记续航/余额不足。**P2 必用**；**禁止**外层循环逐户 `balance`。

> **数据异常（exit 2）**：无账户 / 全部 OAuth 失效 / **余额全为 null** 时 CLI 退出码 **2**，`--json-out` 的 `ok=false` 且 `meta.dataIssue` 为 `no_accounts` | `all_oauth_invalid` | `all_balances_null`。须向用户说明原因，**禁止**当成「无预警命中」。可试 `--refresh-dp` / `login` / `--verbose`。

```bash
siluzan-tso balance-scan -m <媒体类型> [选项]
```

| 选项                                  | 说明                                                                           | 默认         |
| ------------------------------------- | ------------------------------------------------------------------------------ | ------------ |
| `-m, --media <type>`                  | 必填：`Google \| TikTok \| Yandex \| MetaAd \| BingV2 \| Kwai`                 | —            |
| `-a, --accounts <ids>`                | 指定 `mediaCustomerId`（逗号分隔）；**跳过清单翻页**，对这些 ID 拉数后全部输出 | —            |
| `--threshold-days <n>`                | 剩余续航天数阈值                                                               | `7`          |
| `--spend-days <n>`                    | 日均消耗回看自然日数（截至昨天不含今天，**北京时间**；日均 = 窗口合计 / N）    | `7`          |
| `--min-balance <n>`                   | 绝对余额阈值（与 threshold 取并集）                                            | —            |
| `--min-daily-spend <n>`               | 日均消耗低于此值视为僵尸账户，不做续航估算                                     | `0.01`       |
| `--target-days <n>`                   | 建议充值目标续航天数                                                           | `30`         |
| `--page-size <n>` / `--max-pages <n>` | 全量扫描分页（上限 500 / 200）                                                 | `200` / `20` |
| `--json-out`                          | Agent 推荐落盘                                                                 | —            |

**示例：**

```bash
# 全量巡检（Playbook P2）
siluzan-tso balance-scan -m Google --threshold-days 7 --json-out ./snap-p2

# 近 3 日日均 + 续航阈值 7 天
siluzan-tso balance-scan -m Google --threshold-days 7 --spend-days 3 --json-out ./snap-p2

# 已知子集
siluzan-tso balance-scan -m BingV2 -a id1,id2,id3 --json-out ./snap-p2-subset

# Meta 余额续航
siluzan-tso balance-scan -m MetaAd --json-out ./snap-p2-meta
```

**读盘要点**：先看 `meta.dataIssue`（非空则失败）。`data.items` = **全部已检查账户**（OAuth 失效户不在 items，见 `meta.skippedInvalidOAuth`）；`meta.hitCount` = 触阈值条数。预警筛 `hitReason !== "none"`；`hitReason="none"` 表示已检查但未触阈值。按 `remainingDays` 升序交付。用 **`dailySpend`** 做日均（口径见 `meta.spendDays` / `meta.spendWindow`），勿把 `stats` 区间合计 `spend` 当「每天消耗」。Google 消耗走 `account-spend-overview`，`startDate`/`endDate` 带东八区墙钟（`…T00:00:00+08:00` / `…T23:59:59+08:00`），与 `stats` 同口径。与 `balance` / `accounts-digest` 分工见 `references/core/agent-conventions.md` §八。

---

## balance — 查询实时余额

```bash
siluzan-tso balance -m <媒体类型> -a <账户ID列表>
```

| 选项                   | 说明                                                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-m, --media <type>`   | 媒体类型（必填）：`Google \| TikTok \| Yandex \| MetaAd \| BingV2 \| Kwai`（MetaAd 走 `GetMediaAccountInfo`，余额字段为 `spend_cap`）                       |
| `-a, --accounts <ids>` | 账户 `mediaCustomerId`（来自 `list-accounts` 的 `ma.mediaCustomerId`），逗号分隔（必填）。**禁止**传 `entityId` / tokenId / 其它 UUID；Yandex 须传 `porg-…` |
| `--json-out`           | 输出原始 JSON；不支持或查询失败时 stdout 为 `{"ok":false,"error":"..."}`                                                                                    |

**示例：**

```bash
# 查询单个 Google 账户余额（传 mediaCustomerId）
siluzan-tso balance -m Google -a 6326027735

# Yandex：传 porg-…（mediaCustomerId），禁止 entityId/UUID
siluzan-tso balance -m Yandex -a porg-kqquuxx6

# 查询多个 TikTok 账户余额
siluzan-tso balance -m TikTok -a 1234567890,9876543210

# 查询 Meta 广告账户余额
siluzan-tso balance -m MetaAd -a <mediaCustomerId>

# JSON 输出，供脚本使用
siluzan-tso balance -m Google -a 6326027735 --json-out ./snap
```

**单户余额与续航**：`balance` 只反映当前余额；判断「还能跑几天 / 是否够花」需结合 `stats`（或业务侧日均消耗）。多账户续航预警用 `balance-scan`（P2）、多账户投放画像用下文 `accounts-digest`（P3）。

---

## accounts-digest — 多账户投放画像汇总

一条命令替代 AI 对每个账户循环 `list-accounts -k` + `stats`。**多账户汇总表、对比消耗、跨账户巡检、账户级 CPA / 零转化巡检** 应优先本命令，禁止外层 for-loop 逐户 `stats`。

> **数据时效性**：与 `stats` / `balance-scan` 相同（Google `account-spend-overview` 分流；TikTok/Yandex/BingV2/Kwai/**MetaAd** 为截至昨天的 `accountsoverview`）。完整表见 `references/analytics/account-analytics.md` 顶部。

> **反模式**：
>
> - **无** `--period` / `--date-start`；区间只用 `--start`/`--end`（别名 `--start-date`/`--end-date`）。
> - 口语「零询盘 / 转化成本」且**无 CRM 询盘附件** → 本命令（P3），**不是** P7。
> - `conversions` / `cpa` 可能为 **null**（overview 未返回转化）→ 交付写「转化未返回」；脚本勿对 null 做数值比较。过滤用 `--max-cpa` / `--zero-conversions`，勿手写脆弱 Python。

```bash
siluzan-tso accounts-digest -m <媒体类型> [选项]
```

| 选项                          | 说明                                                                                                          | 默认    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- | ------- |
| `-m, --media <type>`          | 媒体类型（必填）：`Google \| TikTok \| Yandex \| MetaAd \| BingV2 \| Kwai`                                    | —       |
| `-a, --accounts <ids>`        | 指定 `mediaCustomerId`，逗号分隔；**留空**则翻页拉该媒体全部账户                                              | —       |
| `--start <YYYY-MM-DD>`        | 统计开始日期（SKILL 要求 AI 先与用户确认区间）                                                                | 近 7 天 |
| `--end <YYYY-MM-DD>`          | 统计结束日期                                                                                                  | 昨天    |
| `--start-date` / `--end-date` | 同 `--start` / `--end`（兼容别名）                                                                            | —       |
| `--min-spend <n>`             | 过滤：区间内消耗 ≤ 此值的账户不返回                                                                           | `0`     |
| `--max-cpa <n>`               | 过滤：保留 CPA > n 的账户；有消耗且转化为 0 视为命中（CPA 无穷）                                              | —       |
| `--zero-conversions`          | 过滤：保留区间消耗 > 0 且转化 = 0 或转化未返回的账户                                                          | off     |
| `--page-size <n>`             | 全量扫描时清单分页大小（上限 500）                                                                            | `200`   |
| `--max-pages <n>`             | 全量扫描时最多页数（上限 200）                                                                                | `20`    |
| `--json-out <path>`           | **Agent 推荐**：落盘目录或 `*.json` 文件；stdout 一行摘要（含 `outlineFile`、`writtenFiles`、`manifestFile`） | —       |

**`--json-out` 落盘**：

- 目录模式典型文件：`accounts-digest-<媒体小写>.json`、同 stem 的 `*.outline.txt`、`cli-manifest-<媒体小写>.json`（读盘协议见 `references/core/agent-conventions.md` §三）。
- 响应结构：`{ ok, data: { items: [...] }, meta: { media, window, scanned, returned, source, totals, nullConversionCount, currencyNote, generatedAt } }`。
- `meta.source`：`list` = 全量翻清单后拉数；`subset` = 传了 `-a`，跳过清单翻页（**`advertiserName` 会缺失**，公司名列显示 `-`）。
- `meta.nullConversionCount`：`conversions == null` 的行数；交付时勿把 null 当 0 硬比。

**与 `stats` / `balance-scan` 的分工**见 `references/core/agent-conventions.md` §八 批量任务硬约束。

**示例：**

```bash
# 指定账户子集（跳过清单翻页，Playbook P3）
siluzan-tso accounts-digest -m Google -a 6326027735,4256317784 \
  --start 2026-04-01 --end 2026-04-15 \
  --json-out ./snap-p3

# 扫描某媒体全部账户（内部翻页，勿先 list-accounts 再拼 -a）
siluzan-tso accounts-digest -m BingV2 --start 2026-05-01 --end 2026-05-24 \
  --json-out ./snap-digest-bing

# 过滤低消耗账户
siluzan-tso accounts-digest -m Google -a id1,id2 --min-spend 10 \
  --start 2026-04-01 --end 2026-04-15 --json-out ./snap-p3

# 转化成本巡检：CPA > 500（含有消耗零转化）
siluzan-tso accounts-digest -m Google --start 2026-07-14 --end 2026-07-20 \
  --max-cpa 500 --json-out ./snap-cpa

# 零转化 / 口语「零询盘」巡检（无 CRM 附件时用本命令，不是 P7）
siluzan-tso accounts-digest -m Google --start 2026-07-20 --end 2026-07-20 \
  --zero-conversions --json-out ./snap-zero-conv
```

**`data.items[]` 主要字段**：`mediaCustomerId`、`name`、`advertiserName`、`currencyCode`、`balance`、`spend`（**区间合计**，同 `stats`）、`impressions`、`clicks`、`conversions`（可为 null）、`ctr`（%）、`cpc`、`cpa`（可为 null）。跨币种汇总见 `references/accounts/currency.md`（**禁止**对 `meta.totals` 跨币种直接当最终结论）。

---

## stats — 查询投放消耗数据

> **数据时效性**：
>
> - **Google**：走 `account-spend-overview`；`--start` / `--end` 日历日按 **UTC+8** 转为 `YYYY-MM-DDTHH:mm:ss+08:00` 再请求（起 00:00:00、止 23:59:59，含今天时 end 截到当前时刻）。与 `google-analysis`（只传年月日）口径不同。
>   - 窗口完全在历史 → `database` 模式；窗口含今天 → `googleCombined` 模式（仅实时消耗，无余额/状态/币种/账户名）。
> - **TikTok / Yandex / BingV2 / Kwai**：走旧版 `accountsoverview`，每日凌晨同步昨天数据，**不能查今天**。Bing 看昨天/今天消耗用 `bing-analysis`（数据可能不完整）；TikTok 用 `tiktok-analysis official-report`。Google「今天」仍走 `google-analysis(-batch) --sections overview`。
> - 完整时效性表见 `references/analytics/account-analytics.md` 顶部。

```bash
siluzan-tso stats -m <媒体类型> [选项]
```

| 选项                          | 说明                                                                                                                           | 默认   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------ |
| `-m, --media <type>`          | 媒体类型（必填）                                                                                                               | —      |
| `-a, --accounts <ids>`        | 账户 `mediaCustomerId`（**必填**；与 `list-accounts` 的 `ma.mediaCustomerId` 一致；Yandex=`porg-…`；**禁止** UUID/`entityId`） | —      |
| `--start <YYYY-MM-DD>`        | 开始日期                                                                                                                       | 7 天前 |
| `--end <YYYY-MM-DD>`          | 结束日期                                                                                                                       | 昨天   |
| `--start-date` / `--end-date` | 与 `--start` / `--end` 同义（CLI 别名，与 SKILL Playbook 一致）                                                                | —      |
| `--by-day`                    | 按日明细（`items[]` 带 `date`）；按日 Excel 见 `stats-daily-excel.md`                                                          | 关     |
| `--json-out`                  | 输出原始 JSON；**失败时 stdout 仍为 JSON**（`{"ok":false,"error":"..."}`）                                                     | —      |

**口径（易错）**：默认 **`spend` = 区间合计**（非日消耗）。按日加 `--by-day`；单日可用 `start=end`；日均用 `spend/天数` 或 `balance-scan` 的 `dailySpend`。

**空结果 / verbose `HTTP 403` 排查（必做，再谈 OAuth）**：

1. 用户若已给出账户号（如 Yandex `porg-kqquuxx6`），`-a` **必须原样用该 mediaCustomerId**；先 `list-accounts -m <媒体> -k <mediaCustomerId>` 核验存在即可。
2. **禁止**把 `ma.entityId`、`externalMediaAccountTokenId` 或会话里其它 UUID 传给 `-a`（会空结果，verbose 常打出被吞的 `HTTP 403`，**不等于** OAuth 过期）。
3. Google：仅当 `list-accounts` **输出中出现** `scopeActivatedSources` 且可判定未激活时，才可向用户说明需先激活套餐；**若无该字段，禁止谈套餐激活**。空结果时按 CLI 报错/字段说明，**禁止**用非 CLI / 自拼请求等方式绕过。
4. 仅当 `list-accounts` 显示 `invalidOAuthToken=true`（或授权状态列为失效），且用户确认后，才走 `account reauth --id <entityId> --i-confirm --commit "…"`（见 `accounts-permissions.md`）。
5. `list-accounts` 显示 `Linked` + `hasToken:1` + `invalidOAuthToken=false`（若有激活字段则须已激活）时，**禁止**因 stats/balance 空结果自行 `reauth`/解绑。

**示例：**

```bash
siluzan-tso stats -m Google -a <mediaCustomerId>
siluzan-tso stats -m Google -a <mediaCustomerId> --start 2026-03-01 --end 2026-03-31
# Yandex：-a 必须是 porg-…（mediaCustomerId），不是 entityId
siluzan-tso list-accounts -m Yandex -k porg-kqquuxx6 --json-out ./snap
siluzan-tso stats -m Yandex -a porg-kqquuxx6 --start 2026-07-21 --end 2026-07-21 --json-out ./snap
siluzan-tso stats -m Yandex -a porg-xxx --start <S> --end <E> --by-day --json-out ./snap/daily.json
siluzan-tso stats -m BingV2 -a <id1>,<id2> --start 2026-03-01
siluzan-tso stats -m Google -a <mediaCustomerId> --json-out ./snap
```

---
