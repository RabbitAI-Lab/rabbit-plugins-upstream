---
name: idea-doctor
description: 规则计算＋Go/Pivot/Kill＋八维评分卡＋三情景经济账，输出12段体检报告，结果需人工复核。
version: 0.2.0
author: 貔貅OPC
---


# 点子体检官（貔貅OPC）

## 1. 功能
按固定八步框架（需求真伪→竞品替代→市场规模→付费意愿→渠道获客→合规门槛→算账→打分）对点子做规则计算，交付 12 段报告：八维评分卡（pain/moat/willingness/delivery/acquisition 等）＋三情景经济账（悲观/中性/乐观）＋判定（Go / Pivot / Kill）。判定在服务端跑，本地无模型、无本地依赖。本包为收口版，三源文件（main_v2.py、order_store.py、a2m_pay.py）以 2026-11-05 现场 md5 复认同步（见 55_146 / 57_150 / 58_152 收口口径）。

## 2. 用法（买家视角）
1. 向服务端点 https://linkkhub.top/api/v1/validate（版本现场读：服务端 提交请求。
2. 首次调用未支付时按 402 Payment-Needed 返回支付指引（含 amtPaymentLink/收银台链接），经 skillpay/402 协议完成支付或恢复会话后重试履约（条款核实无结论走 A，商业措辞照腾讯版原文保留）。
3. 兜底：402 流程不可达即停笔报错、不盲重试（单遍纪律）；重复调用按幂等路处理，already_fulfilled 取自落库值，同单不重复扣费。

## 3. 示例
请求（字段形状照包内 sample_validate_request.json / batch_validate_request.json）：

```json
{"idea": "<点子描述>", "scores": {"pain": 0, "moat": 0, "willingness": 0, "delivery": 0, "acquisition": 0}, "econ": {"price": 0, "pay_rate": 0, "reach": 0, "fixed_monthly": 0}}
```

响应形状照 2026-11-05 18:40 真单产物（形状引用，不造数、不含真实单号）：订单状态从 `PENDING_PAYMENT` →（402 支付完成）→ `PAID` / `FULFILLED`，交付 200；响应含 12 段报告（八维评分卡＋三情景经济账＋Go/Pivot/Kill 判定）与 `already_fulfilled` 字段（取自落库值）。错误响应形状照现文件：`{"code": "...", "message": "..."}`。

## 4. 异常处理
- 401：未授权/签名校验失败（验付路），返回 `{"code","message"}`；不扣费。
- 402：未支付，按 skillpay/402 协议流程处理（见 2）。
- 422：批量超过 10 条直接拒绝，不扣费。
- 500：履约落库校验失败返回 `FULFILLMENT_PERSIST_FAILED`（152 口径：mark_fulfilled 回读 bool 与落库值不一致时触发，显式 commit＋回读，149/150 收口）；其余 500 照现文件错误形状 `{"code","message"}`。落库校验失败时不交付、不重复交付（防重路：already 读落库值）。
- 网络不可达/密钥不可读：客户端最多重试一次，仍失败即停笔报错，不盲重试（单遍纪律）。

## 5. 限制与免责（照真产物免责段口径）
- 判定与评分为规则计算结果，需人工复核，不构成任何收益、投资或经营承诺。
- 三情景经济账基于提交的假设参数，参数错误则结论失真；免责段随 12 段报告一并交付。
- 本技能不接烂尾单：验收标准以本 SKILL.md 与包内 TESTS 口径为准。

## 6. 退款与售后边界（建议稿，待老板上传前过目）
- 未交付即退款（含 401/422 未扣费分支与 500 FULFILLMENT_PERSIST_FAILED 未交付分支）。
- 交付后按平台规则处理；"纳财不出 ≠ 不退款"：未交付的可退，已交付的按平台规则判定，不承诺无条件退款。
- 售后响应：反馈记 FEEDBACK.md，修复走版本号 `20261105-vN`；不承诺"永久免费更新"。

## 7. 来源与口径（照实带来源＋检索日期）
- SKILL.md frontmatter 规范：腾讯云开发者社区文章 cloud.tencent.com/developer/article/2697005 与 2696604（检索 2026-11-05）——frontmatter 必填 name≤20字/description≤50字/version 语义化/author/trigger 数组；选填 permission/dependency/pricing；正文含功能/用法/示例/异常处理＋明确限制禁过度承诺；上传需实名认证，审核三线（内容合规＋科恩漏洞扫描＋云鼎AI模型评估）3-7 工作日。
- 收口口径照实引：55_146（验付 signer 重绑收口）、57_150（显式 commit＋落库回读）、58_152（交付点落库校验补丁）。
