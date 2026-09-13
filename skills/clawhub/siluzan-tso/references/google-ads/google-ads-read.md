# Google 广告 · 查询与列表

> 流程见 `workflows.md` **W3**；诊断报告见 `playbooks.md` **P1**。金额/ID 口径见 [google-ads.md](google-ads.md)。
> **何时 Read**：查系列/组/创意/关键词、搜索词、地理（只读）。

## Contents

- ad campaigns
- ad groups
- ad list
- ad keywords
- keyword 推荐
- ad search-terms
- ad geo

---

## 金额单位（全局重要）

> **所有 CLI 金额参数均按「主币种金额」传入**（如 `1.5` = ¥1.50 / $1.50）；CLI 写入网关前对「分」字段 ×100（含 `ad keyword-edit --max-cpc` → `maxCPC`）。
> **禁止** 按 Google micros（×1,000,000）填写任何金额参数。

---

## ID 来源速查

| 需要的 ID           | 获取命令                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `accountId`（`-a`） | `siluzan-tso list-accounts -m Google --json-out ./snap` → `mediaCustomerId`（**纯数字**；UI 的 `123-456-7890` 可原样传入，CLI 去连字符） |
| 广告系列 `id`       | `siluzan-tso ad campaigns -a <accountId> --json-out ./snap` → `id`                                                                       |
| 广告组 `id`、`name` | `siluzan-tso ad groups -a <accountId> --json-out ./snap` → `id`、`name`                                                                  |
| 广告 `id`           | `siluzan-tso ad list -a <accountId> --json-out ./snap` → `id`                                                                            |
| 关键词 `id`         | `siluzan-tso ad keywords -a <accountId> --json-out ./snap` → `id`                                                                        |

> **Google CID**：带连字符进网关曾导致 `HTTP 403：123-456-7890`；现 CLI 已归一化。仍失败时用纯数字重试；**禁止臆测授权过期**，须 `account check-access -a <mediaCustomerId>`（详见 [google-ads.md](google-ads.md) Gotchas / `accounts-permissions.md`）。

---

## ad campaigns — 广告系列管理

### 查询列表

```bash
siluzan-tso ad campaigns -a <accountId> [--start <YYYY-MM-DD>] [--end <YYYY-MM-DD>] [--json-out ./snap]
```

落盘 JSON 中 **`budget` 为日预算**（主币种「元」，CLI 已 ÷100），另有 **`statusV2`**（`Enabled`/`Paused`/`Removed`）与 **`statusDisplay`**（`{statusV2}·日程文案`，如 `Enabled·有效`、`Enabled·投放期已结束`、`Removed·已删除`）。

> **消歧**：`statusDisplay` 含「投放期已结束」**不是**系列已删除——以 **`statusV2`** 为准；仅 `Removed` 才不可在其下新建组/广告。日程结束仍可 `ad-create`（是否投放另看预算与系列开关）。

命令名：列表是 **`ad campaigns`**（兼容别名 `campaign-list`），**没有** `google-ads` 命名空间。`--json-out` **必须带路径**（落盘，勿管道 stdout）。

带 `--start` / `--end` 时，同行的 **`spend` / `impressions` / `clicks` / `conversions` 为该闭区间合计**（**不是**日消耗）。
与日预算比较「是否超预算」时，**必须** `start=end=统计日`；多日窗口须先 ÷ 天数或改用 `balance-scan.dailySpend` / `overview.averageDailyCost` 再谈「日均」。

> **缓存**：网关侧此列表按 `账户 + 日期区间` 缓存 60 秒（Redis）。若刚 `campaign-create` / `campaign-edit` / `campaign-status` / `campaign-delete` 后立刻查询想看到最新结果，加 `--fresh` 跳过缓存（网关 `newest=true`）；日常巡检/报表不需要，留空更省配额。

### 启停

```bash
siluzan-tso ad campaign-status -a <accountId> --id <campaignId> --status <Enabled|Paused>
```

### 删除

```bash
siluzan-tso ad campaign-delete -a <accountId> --id <campaignId>
```

> 删除不可逆，建议先 `campaigns` 确认名称。

---

## ad groups — 广告组管理

### 查询列表

```bash
siluzan-tso ad groups -a <accountId> [--start/--end <date>] [--json-out ./snap]
```

> **缓存**：同 `ad campaigns`，网关按 `账户 + 日期区间` 缓存 60 秒；刚 `adgroup-create` / `adgroup-edit` 等写操作后要立刻看到最新结果时加 `--fresh`（网关 `newest=true`）。

### 创建

```bash
siluzan-tso ad adgroup-create \
  -a <accountId> \
  --campaign-id <campaignId> --campaign-name <campaignName> \
  --name <adGroupName> --max-cpc <主币种金额> \
  [--status ENABLED|PAUSED] [--json-out <path>]
```

| 选项                     | 说明                                                               | 必填 |
| ------------------------ | ------------------------------------------------------------------ | ---- |
| `-a, --account <id>`     | Google mediaCustomerId                                             | ✅   |
| `--campaign-id <id>`     | 所属广告系列 ID                                                    | ✅   |
| `--campaign-name <name>` | 所属广告系列名称                                                   | ✅   |
| `--name <name>`          | 广告组名称                                                         | ✅   |
| `--max-cpc <amount>`     | 最高 CPC（主币种金额）                                             | ✅   |
| `--status`               | `ENABLED`（默认）/ `PAUSED`                                        |      |
| `--json-out`             | 输出网关返回的完整 adgroup 对象（含 `id` / `maxCPCAmountYuan` 等） |      |

**返回字段（--json-out）**：网关同步返回完整 adgroup，含 **`id`**（adgroupId）、`name`、`campaignId`、`statusV2`、`maxCPCAmountYuan`（元，CLI 已 ÷100）、`typeV2: "SEARCH_STANDARD"` 等 75+ 字段。批量创建脚本应直接读 `id`，**不需要**再次 `ad groups --json-out ./snap` 反查。

### 启停

```bash
siluzan-tso ad adgroup-status -a <accountId> --id <adGroupId> --status <Enabled|Paused>
```

### 编辑

先用 `ad groups --json-out ./snap` 查看当前值，再只改传入字段。

```bash
siluzan-tso ad adgroup-edit \
  -a <accountId> --id <adGroupId> \
  [--name <新名称>] [--max-cpc <主币种金额>] [--target-cpa <主币种金额>] \
  [--start/--end <YYYY-MM-DD>]
```

`--max-cpc` / `--target-cpa` 与 `ad groups --json-out ./snap` 中 `maxCPCAmountYuan` / `targetCpaAmountYuan` 对齐（**元**，CLI 出口已统一）。

### 删除

```bash
siluzan-tso ad adgroup-delete -a <accountId> --id <adGroupId>
```

---

## ad list — 广告创意管理

### 查询列表

```bash
siluzan-tso ad list -a <accountId> [--start/--end <date>] [--include-deleted] [--json-out ./snap]
```

`--include-deleted` 用于审计/排障，会多传 `readDeleted=true`。

### 拒审巡检（`--json-out`）

关注 `policyApprovalStatusV2`（`2`=不通过、`3`=受限）、`approvalStatusDetails`（`;` 分隔摘要）、`statusV2`（过滤 `Removed`）。同源也可用 `google-analysis --sections ads --json-out <dir>`。

### 创建（RSA）

写操作细节与 `--commit` 见 `google-ads-write.md`（**ad ad-create**）。CLI **提交前本地校验**字数/条数，超限直接失败、不打 API。

```bash
siluzan-tso ad ad-create \
  -a <accountId> \
  --adgroup-id <adGroupId> --adgroup-name <adGroupName> \
  --final-url <url> \
  --headlines "标题1,标题2,标题3" \
  --descriptions "描述1,描述2" \
  [--path1 <≤15字符>] [--path2 <≤15字符>] \
  --commit "创建 RSA …" \
  [--json-out <path>]
```

| 字段                | 数量     | 每条上限（Google 字符宽，CJK×2） |
| ------------------- | -------- | -------------------------------- |
| `--headlines`       | **3–15** | **≤30**                          |
| `--descriptions`    | **2–4**  | **≤90**                          |
| `--path1`/`--path2` | 可选     | **≤15**                          |

提交前用脚本 `len`/CJK×2 自检；**禁止**一次塞入 >4 条描述。创建后暂停：`ad ad-status … --status Paused --commit "…"`。

### 启停 / 删除

```bash
siluzan-tso ad ad-status -a <accountId> --id <adId> --status <Enabled|Paused>
siluzan-tso ad ad-delete -a <accountId> --id <adId>
```

---

## ad keywords — 关键词管理

### 查询

```bash
siluzan-tso ad keywords -a <accountId> [--negative] [--start/--end <date>] [--json-out ./snap]
```

### 添加关键词

```bash
siluzan-tso ad keyword-create \
  -a <accountId> \
  --adgroup-id <adGroupId> --adgroup-name <adGroupName> \
  --campaign-id <campaignId> --campaign-name <campaignName> \
  --keywords "词1,词2,多词短语" [--final-url <url>] \
  [--match-type Broad|Phrase|Exact] [--keywords-file ./kws.json] \
  [--json-out <path>]
```

`--keywords` **支持空格多词**（逗号才是分隔符）。`--json-out` 落盘 `{ request: { adgroupId, count }, response: ... }`，批量脚本可直接据此核对成功量。

### 否定关键词

**支持空格多词短语**（如 `how to make`、`home cooking`）。匹配类型与 Web 一致：裸词=广泛，`"短语"`=词组，`[词]`=完全；也可用 `--match-type`。多词/带引号时推荐 `--keywords-file`，避免 shell 转义。

**三级层级：** Campaign（系列）/ AdGroup（组）/ **Account（账户级，Sammamish 2026-08 新增）**。不传 `--level` 时按是否传 `--adgroup-id` 自动判断 Campaign / AdGroup（兼容旧用法）；**账户级必须显式传 `--level Account`**，且不能传 `--campaign-id` / `--adgroup-id`。账户级否词一次生效于整个账户下所有系列（对应 Google Ads「Account Settings → Negative keywords」），**无需再去 Google 后台手工应用**——这是本次新增前的旧限制，现已由接口直接支持。

```bash
# 添加（默认系列层级；传 --adgroup-id 则为组层级）
# 多词短语直接写空格，逗号分隔多条——CLI 支持，无需改后台手工补
siluzan-tso ad keyword-negative-create \
  -a <accountId> \
  --campaign-id <campaignId> --campaign-name <campaignName> \
  --keywords "how to make,home cooking,second hand,near me"

# 统一词组匹配 + JSON 文件（推荐）
# negatives.json → ["how to make","home cooking","vegan recipe"]
siluzan-tso ad keyword-negative-create \
  -a <accountId> \
  --campaign-id <campaignId> --campaign-name <campaignName> \
  --keywords-file ./negatives.json --match-type Phrase

# 添加账户级否词（--level Account；无需 campaign-id/adgroup-id）
siluzan-tso ad keyword-negative-create \
  -a <accountId> --level Account \
  --keywords "free,jobs,DIY"

# 查询：--level Account|Campaign|AdGroup 按层级过滤；不传则三级都返回（用输出里的「级别」区分）
siluzan-tso ad keywords -a <accountId> --negative --level Account --json-out ./snap
siluzan-tso ad keywords -a <accountId> --negative --level AdGroup

# 删除/编辑对三级通用（先用 ad keywords --negative --json-out ./snap 获取 id，无需额外传层级）
# 编辑成功后 id 可能变（网关先建后删），以 CLI 提示的新 id 为准
siluzan-tso ad keyword-negative-delete -a <accountId> --id <negativeKeywordId>
```

> **禁止**因「多词」就让用户去 Google Ads 后台手工补否词——那是 Agent 误判；用上面命令即可。
> 账户级否词账户上限约 1000 词；权限不足返回 `403`，Google 侧错误返回 `400`。
> 查询 `--level AdGroup` 时 CLI 会映射为网关历史值 `appliedlevel=Ad group`（有空格），调用方无需关心。

---

## keyword — 关键字推荐

多场景编排（竞品 URL + 种子、账户词叠市场指标、否词与建户表等）见 **`references/analytics/keyword-planner-workflows.md`**。

```bash
siluzan-tso keyword -k <搜索词> [-a <mediaCustomerId>] [--geo <geoTargetConstantIds>] [--url <url>] [--google-only] [--include <words>] [--exclude <words>] [--json-out <dir>]
siluzan-tso keyword geo-list [--country-code <US,CN,...>] [--name-contains <text>] [--json-out ./snap]
```

`--geo` 传多个 ID（如 `2840,2826`）时，返回的搜索量/CPC/竞争度为**跨所传地区的汇总数据**，响应中**无**按地区拆分的字段。若要分别查看各市场指标，须**多次调用**且每次 `--geo` **只传一个** ID（详见 **`references/analytics/keyword-planner-workflows.md`**「多地区 `--geo`」）。

`--url` 触发网址拓词（`websitereco`）并合并进结果；与 `--google-only` 互斥（仅 Google Keyword Planner 时用后者）。`--include`/`--exclude` 为本地过滤。仅 Google、不联网搜索的 Agent 编排见 **`references/analytics/keyword-planner-workflows.md`**「分支 B」。

---

## ad search-terms — 搜索字词报告

只读报告。屏蔽搜索词：先查到词，再用 `keyword-negative-create` 加否词。

```bash
siluzan-tso ad search-terms -a <accountId> [--start/--end YYYY-MM-DD] [--json-out ./snap]
```

---

## ad geo — 地理位置定向管理

```bash
# 搜索 locationId（单国）
# 单国搜索（--json-out 含 picked / targetedLocations / nameToId，与 resolve 同构字段）
siluzan-tso ad geo search -a <accountId> -q <地名> --json-out ./snap-geo

# 批量解析地名→id（投放方案多国；落盘含 locations / targetedLocations / nameToId）
siluzan-tso ad geo resolve -a <accountId> --from-file ./locations.json --json-out ./snap-geo
siluzan-tso ad geo resolve -a <accountId> -q "Peru,Chile,Kenya" --json-out ./snap-geo

# 查询已定向
siluzan-tso ad geo list -a <accountId> --mode targeted|excluded|report [--start/--end <date>]

# 添加定向
siluzan-tso ad geo add -a <accountId> --campaign-id <id> --location-id <id> [--bid-modifier 1.2] [--exclude]

# 修改已定向地区的出价调整（系列级 campaign_criterion）
siluzan-tso ad geo set-bid -a <accountId> --campaign-id <id> --location-id <id> --bid-modifier 1.2
# 或使用 list 返回的 criterion id
siluzan-tso ad geo set-bid -a <accountId> --campaign-id <id> --criterion-id <id> --bid-modifier 0.8

# 删除
siluzan-tso ad geo remove -a <accountId> --campaign-id <id> --location-id <id>
```

**`--bid-modifier` 口径（`add` / `set-bid` 均为 Google 倍率）**

| 倍率  | 含义     |
| ----- | -------- |
| `1.0` | 不调整   |
| `1.2` | 提高 20% |
| `0.8` | 降低 20% |

- `add`：写入 `PUT …/criterion/{account}` 时 CLI 会换算为后端百分比。
- `set-bid`：直接设置出价系数；与 `ad device-bid set`（系列级）同口径。
- `list` 返回的 `bidModifier` 为 Google **倍率**（如 `1.2` = +20%），不是百分比整数。未设置的 `0` 展示为 `—`（与 Google 后台一致），不要写成 `-100%`。

---
