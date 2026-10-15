# powpow-register

PowPow 泡泡注册助手（OpenClaw 版）：带一个新用户从「不知道泡泡是什么」走到
「账号激活、一键登录、开始玩」——产品介绍（含界面截图）、agent 代办注册
（含头像上传）、支付宝/PayPal 订阅下单与到账跟踪、双链接一键登录、报错排查。

**v2.0.0 起为 agent 代办模式，v2.1.0 起 PayPal 也可代办**：核心脚本 `scripts/powpow-register.mjs` 零依赖
（Node ≥ 18），用户全程不脱离对话，只有两次暂时离开：去邮箱看验证码、在支付宝/PayPal
收银台付款。没有 Node 或用户想自己动手时，自动回退纯指引模式。

## 安装

```
openclaw skills install @durenzidu/powpow-register
```

## 功能

1. **产品介绍**：~120 字开场 + 随包内置的界面截图（`assets/screenshots/` 下 6 张：
   地图页、帖子详情页等，按场景选发 1–3 张；无需外部图床、离线可用）。
2. **代办注册**：agent 主动建议用户名/昵称、密码二选一（用户提供或 agent 生成）、
   验证码发送与提交、头像直传（≤5MB 非 SVG）、常见报错自动处理（占用/过期/限流）。
3. **一键登录（双链接）**：注册成功即给「半登录」链接直达订阅页；付款到账后
   换新登录态再给完整会员链接直达首页（走平台官方 `me?token=` 桥，自动种
   HttpOnly cookie）。
4. **订阅支付**：支付宝（月 ¥6.99 / 季 ¥19.99 / 年 ¥69.99，一次性买断不自动续费）与
   PayPal（Premium Monthly 约 $1/月，自动续费可随时取消）均可 agent 代办下单 + 轮询到账；
   微信扫码/华为 IAP 指路。
5. **报错排查**：收不到验证码、用户名/邮箱被占用、403 未激活、账户锁定等
   常见问题，全部来自平台源码并标注出处。

## 文件结构

```
powpow-register/
├── SKILL.md                            # 主指引（触发条件、8 步流程、语气规范、硬规则）
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # 随包产品截图（powpow-01~06.jpg）
├── scripts/
│   └── powpow-register.mjs             # 核心脚本（零依赖 Node≥18，11 个子命令）
└── references/
    ├── agent-flow.md                   # 脚本契约、完整时序、双链接机制、安全设计
    ├── registration-flow.md            # 字段规则、限流、报错排查表（含源码出处）
    ├── payment-and-activation.md       # 支付宝 vibepay 契约、激活链路、通道排查
    └── screenshots.md                  # 随包截图清单 + 场景速查
```

## 安全

- **密码**只经环境变量传入脚本进程，绝不写命令行参数、不落盘、不进状态文件；
  agent 生成的密码只显示一次供用户保存。
- **验证码**只用于官方注册接口，用完即弃；状态文件（邮箱/用户名/token/订单号）
  存系统临时目录，流程结束 `cleanup` 一键清除。
- **支付**：agent 只创建订单、打开收银台、查询到账；绝不接触用户的支付宝/PayPal
  账号或支付凭证，绝不代付。付款永远在用户与官方收银台之间完成。
- 所有请求只发官方域名 `https://global.powpow.online`；不含任何密钥。

## 许可

MIT-0（ClawHub 统一许可）。

## 链接

- 官网：https://global.powpow.online
- 注册：https://global.powpow.online/register
- 了解泡泡（视频）：https://www.bilibili.com/video/BV1Wu826UEVz/
