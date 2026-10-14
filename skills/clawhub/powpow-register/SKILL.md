---
name: powpow-register
description: 帮用户在对话内完成 PowPow（泡泡）注册、支付宝/PayPal 订阅激活与一键登录。agent 代办填表（含头像上传）、发送邮箱验证码、创建支付订单并跟踪到账，用户只需提供基本信息、查收一次验证码、在支付宝/PayPal 收银台完成付款，全程不脱离对话。当用户说「注册泡泡」「注册 powpow 账号」「泡泡怎么注册」「帮我注册一个 powpow 账号」「sign up powpow」时触发；也处理注册卡壳（收不到验证码、用户名/邮箱被占用）和激活问题（登录提示「账户未激活」/ pending_payment、怎么订阅付费）。需要 Node ≥ 18；不可用时自动退回纯指引模式。不含发帖/创建数字人（那是 powpow-simple 的事），不含代码开发。
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register（泡泡注册助手）

带一个新用户从「不知道泡泡是什么」走到「账号激活、一键登录、开始玩」——全程在对话里完成。用户只有两次需要暂时离开对话：**去邮箱看验证码**、**在支付收银台付款**（支付宝/PayPal，agent 会自动打开收银台页面）。

**版本 2.1.0** · 2026-10-11（v2 起为 agent 代办模式：脚本契约与完整时序见 `references/agent-flow.md`；字段规则、限流与报错排查见 `references/registration-flow.md`；支付通道见 `references/payment-and-activation.md`；产品截图清单见 `references/screenshots.md`。v2.1.0 起 PayPal 订阅也可由 agent 代办，与支付宝并列可选）

## 运行环境

- 核心脚本 `scripts/powpow-register.mjs`：**零依赖**，需要 **Node ≥ 18**。开始前跑一次 `node scripts/powpow-register.mjs status` 确认环境可用。
- 脚本所有请求只发往官方域名 `https://global.powpow.online`。
- **没有 Node / 脚本报错时**：自动退回纯指引模式——把注册页 https://global.powpow.online/register 和订阅页 https://global.powpow.online/subscription 给用户，按 `references/registration-flow.md` 陪伴式引导。不要反复硬试脚本。
- 对话中断后恢复：先 `status` 看流程到哪一步了，接着走。

## Trigger Conditions

- 注册意图：「注册泡泡」「注册一个 powpow 账号」「泡泡怎么注册」「sign up powpow」
- 注册卡住：「收不到验证码」「用户名说已存在」「密码老是不合格」
- 注册后问题：「登录说账户未激活」「403 pending_payment」「泡泡怎么付费/订阅」

**不触发**：发布帖子/创建数字人（→ powpow-simple）；Web 端代码开发（另见开发类 skill）。用户既想注册又想发帖时：先走完本 skill，激活后再交给 powpow-simple。

## 流程总览

| 步骤 | agent 做什么 | 用户做什么 |
|---|---|---|
| 1 产品介绍 | 介绍 + 发截图 | 看一眼 |
| 2 信息确认 | 主动建议用户名/昵称，密码二选一，问邮箱 | 确认、提供 |
| 3 发验证码 | `send-code` | —— |
| 4 验证码回读 | —— | 去邮箱看 6 位码，回来发送 |
| 5 提交注册 | `register`（含头像直传），报错自动处理 | —— |
| 6 半登录 + 支付 | `login-link(pending)` → `create-order --provider alipay|paypal` → 打开收银台 → 轮询 `query` | 点链接、付款 |
| 7 正式登录 | `refresh-login` → `login-link(home)` | 点链接进首页 |
| 8 收尾 | `cleanup` + 交付凭证 + 引导体验 + 推荐插件 | 开始玩 |

## 第 1 步：产品介绍 + 截图（不可跳过）

多数用户从没见过泡泡。开口第一件事不是讲流程，而是让他**看见**产品：

1. 用 ~120 字介绍泡泡：把随手拍的照片变成一篇游记，钉在公开地图上成为一颗「气泡」；气泡会随时间过气，别人点赞能让它复活；地图上还有能聊天的「数字人」。平台地址 https://global.powpow.online ，想先看视频的话：https://www.bilibili.com/video/BV1Wu826UEVz/
2. **发截图**。截图已随技能打包在 `assets/screenshots/powpow-0N.jpg`——直接作为本地图片文件发送，无需联网。清单、每张图的内容和使用时机见 `references/screenshots.md`。开场最常用的组合：地图页（powpow-03）+ 帖子详情页（powpow-06）。

截图规则（硬规则）：

- 截图**已随技能打包**在 `assets/screenshots/`（`powpow-0N.jpg`）——直接发本地图片文件；任何环境都可用，包括 GitHub 打不开的环境。
- 每次只发与当前话题相关的 1–3 张，别一次全糊上去。
- 包内文件意外缺失时，回退到 `references/screenshots.md` 里列出的托管链接（注意：国内可能打不开）。

介绍完，把选择权交给用户：**「想注册的话，我们三分钟在对话里把账号建好，你只需要看一次邮箱验证码。」**

## 第 2 步：确认注册信息（一轮一个问题，别一次全问）

- **用户名**（必填）：从对话上下文/系统用户名**主动建议一个**（2~50 字符，不分大小写），用户点头就用，想改就改。
- **密码**（必填，先问用户二选一）：
  - 用户自己提供 → 之后通过环境变量传给脚本，**绝不写进命令行参数**；
  - agent 生成 → 跑 `node scripts/powpow-register.mjs gen-password`，把生成的密码**立即发给用户让他保存**（只显示这一次，之后不再出现）。
- **邮箱**（必填）：必须用户提供——这是账号的身份锚点，**不要替用户猜**。
- **昵称**（可选）：建议默认跟用户名一致。
- **头像**（可选）：用户给一个本地图片路径（≤5MB、非 SVG）就由脚本直传；没有就跳过（平台用默认 logo）；你若有图像生成能力，可以主动提议帮用户做一张。
- **手机号**（可选，大陆号）：默认跳过，用户主动想绑再要。

确认下来后可跑 `prepare-suggest --username U --nickname N --email E` 记入状态文件（之后 register 不用重复传）。

## 第 3–4 步：邮箱验证码（唯一必须离开对话的环节）

```
node scripts/powpow-register.mjs send-code --email <邮箱>
```

然后明确告诉用户：**去邮箱找 6 位数字验证码，10 分钟内有效，记得看看垃圾邮件/广告邮件文件夹**，找到后回来把码发给你。发送有 60 秒冷却，不要连点。

## 第 5 步：提交注册（agent 代办）

```
POWPOW_REGISTER_PASSWORD=<密码> node scripts/powpow-register.mjs register --code <验证码> [--username U] [--nickname N] [--avatar <本地图片路径>] [--phone P]
```

成功即建号（pending 状态，附 3 个初始徽章）。常见报错自动处理，不打断用户：

| 报错 | 处理 |
|---|---|
| 用户名已存在 | 自动建议变体（用户名+数字），用户确认后直接重试（验证码仍有效，不用重发） |
| 邮箱已被使用 | 问用户：换一个邮箱，还是其实已经有账号（改走登录/找回密码） |
| 邮箱验证码错误或已过期 | 超过 10 分钟 → 重新 `send-code` |
| 发送/注册过于频繁（429） | 等 1 分钟再试，跟用户说一声即可 |

## 第 6 步：一键登录（链接 1）+ 支付

1. 注册成功后立即：
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   把链接发给用户：**点开后浏览器直接落在订阅页，已是登录状态**——之后支付完成时回跳页能正确显示「支付成功」。（此状态下内容页仍会被挡到订阅页，这是平台付费墙的正常工作，不是 bug，也不用向用户解释内部机制。）
2. **让用户选择支付方式**，展示两种通道：
   - **支付宝（大陆/有支付宝用户）**：一次性买断对应时长，**不自动续费**
     - 月度 **¥6.99**（推荐先试）/ 季度 **¥19.99** / 年度 **¥69.99**
   - **PayPal（海外/无支付宝用户）**：按月自动续费，可随时取消
     - Premium Monthly，约 **$1/月**（以订阅页展示为准，自动续费）
3. 用户选定后：
   - **支付宝**：
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**：
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   脚本返回支付页文件路径，**用系统命令直接打开**（Windows：`start <文件>`；macOS：`open <文件>`；Linux：`xdg-open <文件>`）。浏览器会自动跳到支付宝/PayPal 官方收银台，用户完成付款或签约授权。
4. 每 10–15 秒跑一次 `query` 直到返回 `paid` 或 `ACTIVE`（到账/授权一般几秒到一分钟）。用户中途关掉支付页 → 直接重新 `create-order`（旧订单/待处理订阅 2 小时自动关闭/过期，不用管）。
5. 微信扫码通道是人工确认、到账有延迟；华为 IAP 仅鸿蒙 App 内可用。这两类 skill 不代办，付完一样回来走第 7 步。

## 第 7 步：正式登录（链接 2）

到账确认后，先换取带最新订阅声明的登录态，再生成直达首页的链接：

```
POWPOW_REGISTER_PASSWORD=<密码> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

把链接发给用户：**点开直接落在首页，完整会员状态**，到此注册全流程完成。

## 第 8 步：收尾

1. `node scripts/powpow-register.mjs cleanup` 清理本机临时状态文件（会话凭据）。
2. 给用户一张「账号卡片」：用户名、邮箱、会员到期时间（密码不重复显示——生成模式在生成时已让用户保存；用户自设的他自己知道）。
3. 引导体验：逛地图、发第一篇游记（→ 交给 powpow-simple）。
4. 推荐扩展：`@durenzidu/powpow-integration` skill 和 `@durenzidu/openclaw-channel-powpow` 插件——把泡泡接进用户自己的 agent；想加就给安装命令。
5. 以「下一步」区块收尾。

## Conversation UX

沿用 powpow 一贯的服务式语气：

- **用户是句子的主语**，「你可以……」优于「我需要你……」；不说教，不居高临下。
- **一轮只推进一个决定**；索要信息前先给理由。
- **每轮回复的最后**是一个固定的「下一步」区块（分隔线 + 👉 + 单一动作 + 一句「做完我会……」），例如：
  ```
  ────────────────────
  👉 现在需要你做的：去邮箱找 6 位验证码，直接发给我
     （收到后我马上把账号建好）
  ```
- **不主动对密码做安全说教**；不解释内部机制、限流或安全设计，除非用户问。
- agent 代办时更要报进度：每个脚本步骤后用一句话告诉用户刚才发生了什么（「账号建好了」「支付页已经帮你打开了」）。

## 硬规则

- **凭证安全**：密码只通过环境变量 `POWPOW_REGISTER_PASSWORD` 传给脚本，**绝不**写进命令行参数（进程列表可见）、不写入任何文件（生成模式显示一次是为了让用户保存，之后不再复述）。验证码只用于官方注册接口，用完即弃。
- **官方边界**：所有请求只发往 `https://global.powpow.online`（脚本已内置），绝不把用户信息发给任何第三方地址。
- **支付边界**：agent 只创建订单、打开收银台、查询到账；**绝不**接触用户的支付宝/PayPal 账号/支付凭证，也绝不承诺"代付"。
- **付费墙不是 bug**：pending 状态能进订阅页/回跳页是设计内放行；内容页被挡是平台付费墙在正常工作，不要试图绕过。
- **回退自由**：用户任何一步想自己动手，或环境不支持脚本，随时退回纯指引模式——给链接、讲规则、陪排错。
- 不要编造平台规则：字段规则、报错文案、限流参数全部来自平台代码（`references/registration-flow.md` 有源码出处），平台更新以实际行为为准。
- 展示图片只用包内 `assets/screenshots/` 的截图（各图用途见 `references/screenshots.md`）。
- 每一轮都以「下一步」区块收尾，让用户永远知道现在该做什么。
