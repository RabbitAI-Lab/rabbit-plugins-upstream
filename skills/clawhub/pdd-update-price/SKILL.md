---
name: pdd-update-price
description: Changes Pinduoduo SKU prices with a dry-run-by-default workflow, change-ratio guardrails, audit log and one-command revert. Use only when the user explicitly asks to change prices on their PDD shop. 拼多多改价：默认只出计划不执行，显式确认才改价，带涨跌幅护栏、本机审计日志与一键回滚；仅在用户明确要求调价时使用。
homepage: https://claw-school.com
metadata: {"openclaw":{"emoji":"💱","homepage":"https://claw-school.com","requires":{"anyBins":["python3","python","py"]},"envVars":[{"name":"PDD_AUDIT_PATH","required":false,"description":"可选：审计日志路径，默认 ~/.pdd-data/price_audit.jsonl"}]}}
---
# pdd-update-price

对拼多多店铺商品做 SKU 级改价。走已登录 Chrome 的页面客户端（自动带风控签名），改价经平台 commit 流，**生效有 3~15 秒延迟**，脚本会自动轮询验证。

## ⚠️ 写操作纪律（必须遵守）
0. **默认即 dry-run**：不带 `--execute` 只输出计划，绝不改价。真实执行必须用户确认后显式加 `--execute`（`--revert` 同样）
1. **先跑一次无 `--execute`** 给用户看改价计划（before→target），用户确认后再加 `--execute` 真改
2. 涨跌幅超 30% 会被护栏拒绝——**不要擅自 `--force`**，让用户人工复核
3. 每次改价自动写审计日志（`price_audit.jsonl`），出错用 `--revert` 回滚
4. 用户只说"改价"没给幅度/目标价时，**先问清楚**，不要猜

## 用法
```bash
# 1. 预览（默认行为，不执行）：全部SKU 拼/单价 +0.5 元
python3 {baseDir}/scripts/update_price.py --goods <id> --delta +0.5
# 2. 执行（需用户确认后显式加 --execute）
python3 {baseDir}/scripts/update_price.py --goods <id> --delta +0.5 --execute
# 设定价（全部SKU 拼:单，元）
python3 {baseDir}/scripts/update_price.py --goods <id> --set 499:500 --execute
# 指定SKU
python3 {baseDir}/scripts/update_price.py --goods <id> --sku <skuId>:499.5:500.5 --execute
# 回滚最近一次改价
python3 {baseDir}/scripts/update_price.py --goods <id> --revert --execute
```
选项：`--port 9222`（CDP端口）· `--max-change-pct 30` · `--force`（跳过护栏，需用户明确授权）

## 返回
单行 JSON：`{"ok":true,"commit_id":...,"verified":true,"after":{...}}`
- `verified:false` + note = 提交成功但生效延迟，稍后不带 `--execute` 复读确认
- 失败含 `action` 字段（notify_user/retry），按它处理，不把技术报错丢给用户

## 前置
- 已登录 mms.pinduoduo.com 的 Chrome（CDP 开启，默认 9222）
- 依赖 `python3` + `requests` + `websocket-client`

## 技术契约（已实测验证 2026-10-09）
`POST /glide/v2/mms/price/adjust/adjust_in_list`：goods_id + market_price(分+元) + sku_prices[{sku_id, multi_price(拼单价,分+元), single_price(单买价,分+元)}] + need_delete_goods_commit:true → `{goods_commit_id}`。
注意：短时间内重复提交"与当前价相同"的目标会被平台幂等去重（返回旧 commit_id 不生效）——所以改价后必须轮询验证而非盲信提交成功。
