# powpow-register

PowPow 泡泡注册助手（OpenClaw 版）：带一个新用户从「不知道泡泡是什么」走到
「账号激活、能正常使用」——产品介绍（含界面截图）、逐步注册引导、报错排查、
订阅激活说明。

纯指引型 skill，无脚本、无依赖；所有注册动作由用户在浏览器/App 内完成。

## 安装

```
openclaw skills install @durenzidu/powpow-register
```

## 功能

1. **产品介绍**：~120 字开场 + 托管在 GitHub 公开仓库的界面截图链接
   （地图页、帖子详情页等 6 张，按场景选发 1–3 张）。
2. **注册引导**：字段规则（用户名/密码/邮箱验证码/手机号/头像）、第三方登录
   （Google/Watcha/华为）、限流参数，全部来自平台源码并标注出处。
3. **报错排查**：收不到验证码、用户名/邮箱被占用、403 未激活、账户锁定等
   13 种常见问题。
4. **订阅激活**：PayPal（网页）/ 微信扫码（人工确认）/ 华为 IAP（鸿蒙）三条
   通道的说明与排查；现有支付链路可直接复用，skill 只负责引路。

## 文件结构

```
powpow-register/
├── SKILL.md                            # 主指引（触发条件、流程、语气规范）
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # 字段规则、限流、报错排查表（含源码出处）
    ├── payment-and-activation.md       # 订阅激活、支付通道、复用结论
    └── screenshots.md                  # 托管截图清单 + 场景速查
```

## 安全

- 不含任何密钥；无脚本，不接触用户凭据。
- **永远不索要**用户的密码、验证码或支付凭证；注册与支付全部在平台页面完成。

## 许可

MIT-0（ClawHub 统一许可）。

## 链接

- 官网：https://global.powpow.online
- 注册：https://global.powpow.online/register
- 了解泡泡（视频）：https://www.bilibili.com/video/BV1Wu826UEVz/
