---
name: pdd-shop-report
description: Generates business-grade HTML dashboards for Pinduoduo shops - single-shop report or multi-shop cockpit - from data synced by pdd-sync-shop. Use when the user asks for a PDD shop report or operations overview. 基于 pdd-sync-shop 同步的数据生成商务版经营报表（KPI、趋势、库存健康、待办清单）与店群驾驶舱；用户要看报表、经营情况时使用。
homepage: https://claw-school.com
metadata: {"openclaw":{"emoji":"📊","homepage":"https://claw-school.com","requires":{"anyBins":["python3","python","py"]},"envVars":[{"name":"PDD_DB_PATH","required":false,"description":"可选：本地 SQLite 路径，默认 ~/.pdd-data/pdd.db"},{"name":"PDD_CH_URL","required":false,"description":"可选：设置后写企业 ClickHouse（如 http://host:8123）"},{"name":"PDD_DATA_DIR","required":false,"description":"可选：数据目录（读店铺注册表取显示名），默认 ~/.pdd-data"}]}}
---
# pdd-shop-report

## 用法
```bash
python3 {baseDir}/scripts/report.py [--mall <id>] [--theme clawschool] [--out report.html]   # 单店报表
python3 {baseDir}/scripts/report.py --cockpit                                              # 店群驾驶舱（全部店铺合并）
```
返回 `{"ok":true,"report":"<路径>","actions_needed":N}`；无数据时按 action 提示先跑 pdd-sync-shop。

## 店群驾驶舱（多店合并）
`--cockpit` 一屏看全部店铺：各店 GMV/订单/在售/库存/需处理对比（按 GMV 排序）+
全店待办汇总（每店 Top 6）。数据来自本地库全部 mall（先跑 `pdd-sync-shop --all`），
店铺显示名取自 `~/.pdd-data/shops.yaml` 注册表。单店深挖 = 生成单店报表（`--mall`）。

## 风格纪律（必须遵守）
- 报表是**商务文档**：禁止 emoji、禁止 AI 腔的大段寒暄；数字优先、高信噪比
- 默认主题 `clawschool`（品牌色：纸白底/墨绿标题/赭金点缀/衬线标题）——**不要擅自改样式**
- 用户主动要求换风格时，只能从预设主题中选：
  - `clawschool`（默认，已核准）
  - `boardroom` 黑白灰极简 · `slate` 深色 ——（内部预览，呈现时注明"待创始人核准"）
- 用户要的其他定制：记录需求反馈给 Claw School，不现场发挥

## 图表与数据口径
- 近30天成交额/订单量 = 平台数据中心**真实日历史**（与后台交易概况同口径，sync 时自动拉取）
- 库存走势 = 同步快照序列（平台无库存历史）；单品价格走势 = 快照火花线
- 全部内嵌 SVG + hover 十字线/tooltip，指标均带 ⓘ 算法说明，不依赖 CDN
- 商品名/缩略图点击直达后台单品页；"需处理事项" KPI 直达后台商品列表

## 用户继续定制
报表底部给了示例 prompt。用户提出修改时：主题只能用预设；布局/内容的小改可直接改 report.py 并保存为用户副本；大改先记录需求。
