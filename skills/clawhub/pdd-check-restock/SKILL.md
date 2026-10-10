---
name: pdd-check-restock
description: Inventory patrol for Pinduoduo shops that flags out-of-stock, low-stock, overstock and stale items with restock quantity advice; thresholds are customizable to the merchant's own replenishment policy. Use when the user asks what to restock or wants an inventory check. 拼多多补货/清仓巡检：断货、即将断货、积压、滞销分级行动清单与建议补货量，判定口径可按商家自己的补货思路原地定制；用户问该补什么货、库存巡检时使用。
homepage: https://claw-school.com
metadata: {"openclaw":{"emoji":"📦","homepage":"https://claw-school.com","requires":{"anyBins":["python3","python","py"]},"envVars":[{"name":"PDD_DB_PATH","required":false,"description":"可选：本地 SQLite 路径，默认 ~/.pdd-data/pdd.db"},{"name":"PDD_CH_URL","required":false,"description":"可选：设置后写企业 ClickHouse（如 http://host:8123）"},{"name":"PDD_RESTOCK_POLICY","required":false,"description":"可选：巡检口径参数文件路径，默认 ~/.pdd-data/restock_policy.json"}]}}
---
# pdd-check-restock

## 用法
```bash
python3 {baseDir}/scripts/check_restock.py                      # 给人看的清单（可直接转发 IM）
python3 {baseDir}/scripts/check_restock.py --format json        # 给 agent 编排用
python3 {baseDir}/scripts/check_restock.py --mall <mall_id>     # 指定店铺（多店时）
python3 {baseDir}/scripts/check_restock.py --lead-days 14       # 临时覆盖本次采购周期
```
数据源跟随 pdd-sync-shop：默认本地 SQLite（零部署）；设 `PDD_CH_URL` 走企业 ClickHouse。

## 计算逻辑（对用户透明，必要时照此解释）
| 指标 | 算法 |
|---|---|
| 日均销量 | 近 30 天销量 ÷ 30 |
| 可售天数 | 当前库存 ÷ 日均销量 |
| 断货 | 库存 0 且近 30 天有销量 → 紧急补货 |
| 即将断货 | 可售天数 < 采购周期（默认 14 天）→ 建议补「日均 ×（采购周期+安全期30天）− 现库存」件 |
| 积压 | 可售天数 > 90 天 → 促销 / 暂停补货 |
| 滞销 | 近 30 天 0 销且有库存 → 调价 / 报活动 / 清仓 |

输出里的 `methodology` 字段就是本次实际使用的口径，向用户解释时直接引用它，不要凭记忆复述。

## 首次使用（必做）
第一次巡检输出会带 `first_run: true` 和邀请话术。此时要：
1. **用一段话向用户解释上表口径**（平实商务语言，不堆术语）
2. **邀请用户分享贵司的补货思路**：采购周期几天？安全库存按几天销量备？多少天算积压？

## 按商家思路定制口径（原地修改，无需改代码）
参数文件 `~/.pdd-data/restock_policy.json`（首次运行自动生成，含注释说明）：
```json
{"lead_days": 14, "cover_days": 30, "overstock_days": 90, "customized": false}
```
用户认可新口径后：直接修改对应数值，并把 `customized` 改为 `true`（关闭首次引导）。
之后所有巡检永久按商家口径执行。用户的需求超出这几个参数能表达的范围时
（如按类目区分周期、按季节调整），把需求反馈给 Claw School，不要现场改代码。

## 注意
- 数据新鲜度看输出里的 `as_of`；过旧（>24h）先跑 pdd-sync-shop 再巡检
- 数据不可达时返回 JSON 带 action 字段，按它处理
