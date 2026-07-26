# 账户管理（导航）

> `SKILL.md` 已指向子文件时，**直接 Read 子文件**，不必先读本文件。

## 何时 Read

| 任务 | Read |
| ---- | ---- |
| 列表 / 有哪些 / 有多少 / OAuth 失效筛查 / 激活账单 / 开户申请历史 | [`accounts-list.md`](accounts-list.md) |
| 单户余额、多户余额续航（**P2 `balance-scan`**）、单户消耗 `stats`、多户画像（**P3 `accounts-digest`**） | [`accounts-balance-stats.md`](accounts-balance-stats.md) |
| 分享 / 解绑 / 重授权 / MCC / BC / BM / 关闭 / 提现 / 邮箱授权 | [`accounts-permissions.md`](accounts-permissions.md) |
| 六大媒体开户参数与首次必填 | [`open-account-by-media.md`](open-account-by-media.md)（Google UI：[`open-account-google-ui.md`](open-account-google-ui.md)） |
| 充值 / 转账 / 发票 | [`finance.md`](finance.md) |
| 币种与跨币种禁止求和 | [`currency.md`](currency.md) |
| 写审计 / `--commit` / restore | [`write-audit-restore.md`](write-audit-restore.md) |

## Gotchas（账户域）

- `list-accounts` **不含**余额/消耗；列全部账户用 `--page-size 999`，禁止默认 20 再翻页。
- `entityId`（UUID，分享/delink/账单/`reauth`）≠ `mediaCustomerId`（`balance`/`stats`/`accounts-digest`/`ad` 的 `-a`）。**Yandex 的 mediaCustomerId 形如 `porg-…`，不是 UUID。**
- MetaAd OAuth 户的 `mediaCustomerId` **须带 `act_` 前缀**。
- `stats`/`balance` 空结果 + verbose `HTTP 403`：先确认 `-a` 是否为 `ma.mediaCustomerId`；**禁止**把 `entityId` / tokenId 当 `-a`，也**禁止**未确认 `invalidOAuthToken=true` 就 `reauth`。
- 多账户余额预警用 `balance-scan`（P2），多账户消耗汇总用 `accounts-digest`（P3）；**禁止**外层 for-loop 逐户 `balance`/`stats`。
- `stats` 默认 `spend` = **区间合计**，不是日消耗；日均看 `balance-scan.dailySpend` 或合计÷天数。
