# 订阅激活与支付 — powpow-register

## 结论（先说答案）

**支付宝通道已上线（2026-10-07 起），是本 skill 的主推支付方式，agent 可以代办下单与到账跟踪。**
海外/无支付宝用户回退 PayPal；微信扫码（人工确认）与华为 IAP 仍在，但不由 skill 代办。

支付环节的职责边界：agent 可以**创建订单、打开收银台、查询到账**；**绝不**接触用户的支付宝
账号/支付凭证，绝不承诺"代付"。付款动作永远由用户本人在支付宝官方收银台完成。

## 支付宝通道（vibepay，主推）

一次性买断制：付一次开通对应时长，**不自动续费**。套餐写死在
`src/lib/alipay-vibepay.ts`（`ALIPAY_PACKAGES`）：

| key | planId | 名称 | 价格 | 时长 |
|---|---|---|---|---|
| `monthly` | alipay-monthly | 月度会员 | ¥6.99 | 30 天 |
| `quarterly` | alipay-quarterly | 季度会员 | ¥19.99 | 90 天 |
| `yearly` | alipay-yearly | 年度会员 | ¥69.99 | 365 天 |

### 接口契约（skill 脚本已封装，agent 不直接拼请求）

| 接口 | 方法 | 说明 |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | 需 `Authorization: Bearer <JWT>`（pending 用户即可）。body `{package}` → 返回 `{paymentHtml, outTradeNo, amount, planName}`；`paymentHtml` 是自动提交到支付宝网关的表单页 |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | 同样 Bearer 鉴权。返回 `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST（支付宝服务器回调） | 验签五要素（签名、app_id、金额一致、TRADE_SUCCESS/TRADE_FINISHED、商户唯一性）→ **幂等**更新订单 + 建订阅 + 激活账号。skill 永远不碰这个接口 |
| `/payment/alipay/return` | 浏览器回跳页 | 公开路径，支付后显示「支付成功」确认，页内轮询后端真实状态 |

- 未支付订单 **2 小时自动关闭**；用户中途放弃 → 直接重新 `create-order`，旧单不用管。
- 脚本把 `paymentHtml` 写进临时 HTML 文件，agent 用系统命令打开即可进入支付宝收银台
  （扫码或在支付宝里登录付款）。

### 激活链路（自动，无需人工）

notify 验签通过 → `paymentOrders` 标记已支付 → `user_subscriptions` 建立/顺延
（`planId`、`currentPeriodEnd` 按 durationDays 计算，续费在原到期日上顺延）→
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → 回跳页轮询到 paid 显示成功。

### 付款后必须换新登录态（重要）

JWT 里带着订阅声明（pending 账号是 `NONE`）。**支付到账只更新数据库，不会改已签发的
JWT**——旧 token 的声明仍是 NONE，直接用它生成登录链接会表现成"没会员"。
所以 skill 在确认 `paid` 后先跑 `refresh-login`（重新登录换新 JWT，声明变 ACTIVE），
再生成链接 2。这是设计行为，不是漏洞修复。

## 订阅页四条通道

订阅页 `src/app/(public)/subscription/page.tsx` 按运行环境展示：

| 通道 | 环境 | 机制 | 激活方式 |
|---|---|---|---|
| **支付宝（主推）** | 网页端 | `AlipayPaymentSection` 走 vibepay 接口（上表） | notify 服务端自动激活，秒级 |
| PayPal 订阅 | 网页端（非鸿蒙） | `/api/subscription/create` → 跳 PayPal 授权；按月自动续费可随时取消（`/api/subscription/manage`） | PayPal Webhook（`BILLING.SUBSCRIPTION.*`）自动置 active |
| 微信扫码订阅 | 网页端（非鸿蒙） | 页面底部「微信扫码订阅」：扫码转账 | **人工确认**，到账可能延迟；付完别急着判定失败 |
| 华为应用内购买 | 鸿蒙 App 内 | 原生 `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` 验证华为订单后激活 |

PayPal 计划与价格从 `/api/subscription/plans` 动态读取；页面固定文案：Auto-renews. Cancel anytime.

## 状态与跳转

- 支付宝付完 → 回跳页显示成功；PayPal 成功 → `/subscription/success` → 账号 active →
  自动跳回 `next` 参数指定的原始页面（无则首页）。
- 已订阅用户再访问订阅页 → 显示 "You're All Set!"，3 秒后自动回首页。
- 支付失败/取消（PayPal）→ `/subscription/cancel`，可重新发起。

## 排查

| 现象 | 处理 |
|---|---|
| 支付宝付完 `query` 还是 pending | notify 极少延迟；等 30 秒再查一次。仍不行让用户回浏览器看回跳页状态，再不行联系平台支持（dongtao@outlook.com），报 `outTradeNo` |
| 支付宝付完、链接 2 进去还是被挡 | 少跑了 `refresh-login`（旧 JWT 声明未更新）——先 `refresh-login` 再 `login-link` |
| 付完还是 403（PayPal） | Webhook 偶有延迟，重新登录刷新状态 |
| 微信付了没开通 | 人工确认是异步的，几小时内未开通再联系平台支持 |
| 订阅页提示 "No subscription plans available" | `/api/subscription/plans` 无可用 PayPal 计划，平台侧配置问题；国内用户改走支付宝即可 |

## 历史备注

代码里另有一套**旧的**支付宝网页支付（`src/lib/alipay.ts`、`/api/payment/create-order`，
¥9.90/¥99 一次性买断，沙箱未配钥时降级模拟支付），始终未接入订阅页 UI，与 vibepay
无关。skill 一律不碰它；`alipay-vibepay.ts` 才是现行通道。
