# 订阅激活与支付 — powpow-register

## 结论（先说答案）

**现有支付方式可以直接复用，注册助手 skill 零支付开发。**

原因：

1. 注册接口（`src/app/api/auth/register/route.ts`）在创建 pending 账号时已经签发
   JWT cookie + pendingUserToken HttpOnly cookie，用户落地 `/subscription` 时就是
   已登录态——三条支付通道都挂在这个订阅页上，激活的都是同一个 pending 账号。
2. 登录接口对 pending 账号返回 403 + `redirectTo: '/subscription'`，同样种好
   cookie——用户任何时候补缴都会被引导回同一页面。
3. 因此注册引导类 skill 的职责边界就是「把用户引到 /subscription」；不需要新的
   支付接口、不需要新的订单模型、不需要任何后端改动。

同时要注意：支付环节（PayPal JS SDK 按钮、微信扫码人工确认、华为原生 IAP）
**决定了它无法也不应该由命令行/聊天 skill 代付**。不要尝试用脚本调用支付接口
替用户付款，也不要索要用户的支付凭证。

## 订阅页三条通道

订阅页 `src/app/(public)/subscription/page.tsx` 按运行环境自动展示：

| 通道 | 环境 | 机制 | 激活方式 |
|---|---|---|---|
| PayPal 订阅 | 网页端（非鸿蒙） | `/api/subscription/create` 创建 PayPal 订阅 → 跳 PayPal 授权；按月自动续费，可随时取消（`/api/subscription/manage`） | PayPal Webhook（`BILLING.SUBSCRIPTION.*`）自动把 `accountStatus` 置 active |
| 微信扫码订阅 | 网页端（非鸿蒙） | 页面底部「微信扫码订阅」区块：扫码转账，**人工确认后开通**（`WechatQrPaymentSection`） | 人工确认，到账可能有延迟；用户付完别急着判定失败 |
| 华为应用内购买（IAP） | 鸿蒙 App 内 | 鸿蒙 WebView 中 PayPal/微信支付不可用，页面改走原生 `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` 验证华为订单后激活 |

计划与价格从 `/api/subscription/plans` 动态读取（PayPal 计划）；页面固定文案：
Auto-renews. Cancel anytime.

## 状态与跳转

- 支付成功 → `/subscription/success`（PayPal 回调带 `subscriptionId`）→ 账号
  active → 自动跳回 `next` 参数指定的原始页面（无则首页）。
- 已订阅用户再访问订阅页 → 显示 "You're All Set!"，3 秒后自动回首页。
- 支付失败/取消 → `/subscription/cancel`，可重新发起。

## 排查

| 现象 | 处理 |
|---|---|
| 付完还是 403 | PayPal：Webhook 偶有延迟，重新登录刷新状态（登录时会回查 DB 最新状态）；微信：人工确认未完成，稍等；华为：确认 App 内支付成功页是否出现 |
| 订阅页提示 "No subscription plans available" | `/api/subscription/plans` 无可用 PayPal 计划，属于平台侧配置问题，让用户稍后再试 |
| 微信付了没开通 | 人工确认是异步的，几小时内未开通再联系平台支持（dongtao@outlook.com） |

## 备注：支付宝（Alipay）

代码里存在一套支付宝网页支付（`src/lib/alipay.ts`、`/api/payment/create-order`，
普通会员 ¥9.90 / 高级会员 ¥99 的一次性买断模型，沙箱未配钥时自动降级为模拟支付），
**但未接入订阅页 UI**，属于闲置/预留代码。如果将来要在订阅页启用支付宝，
走这套现成代码接线即可——这与本 skill 无关，仅供平台侧决策参考。
