# 🛒 全网比价 + 外卖比价 Skill

> 整合 12 个主流平台 API，一键查询全网最低价 + 外卖红包，为比价类小程序/插件提供核心能力。

---

## ✨ 功能亮点

| 功能 | 支持平台 | 说明 |
|------|----------|------|
| 🔍 全网商品比价 | 京东、淘宝、拼多多、抖音 | 输入商品名，返回各平台到手价 |
| 🍜 外卖比价 | 美团外卖、饿了么 | 同商家/菜品跨平台价格对比 |
| 🧧 红包聚合 | 美团、饿了么、京东、淘宝 | 展示当前可领红包 + 直达领券链接 |
| 📊 到手价计算 | 全平台 | 自动计算券后价、满减后价 |

---

## 🚀 快速开始

### 安装

```bash
clawhub install price-compare
```

或在 WorkBuddy 中搜索 `price-compare` 一键安装。

### 配置 API 密钥

在 WorkBuddy 工作区根目录创建 `.env` 文件：

```env
# 美团联盟（https://union.meituan.com）
MEITUAN_APPKEY=你的AppKey
MEITUAN_APPSECRET=你的AppSecret

# 京东联盟（https://union.jd.com）
JD_APPKEY=你的AppKey
JD_APPSECRET=你的AppSecret
JD_AUTH_KEY=你的授权Key

# 折淘客（https://www.zhetaoke.com）
ZHETAOKE_APPKEY=你的AppKey
ZHETAOKE_SID=你的sid

# 好单库（https://www.haodanku.com）
HAODANKU_APIKEY=你的apikey
```

> 📌 各平台注册地址详见 `SKILL.md` 中「API 凭证」章节。

---

## 💬 使用示例

**比价查询**
```
用户：帮我在全网找 iPhone 16 Pro 256G 最低价
```

**外卖比价**
```
用户：美团和饿了么买麦当劳哪个便宜？
```

**红包查询**
```
用户：美团外卖有什么红包可以领？
```

---

## 📦 支持平台一览

- ✅ 京东联盟（商品搜索 + 优惠券）
- ✅ 淘宝/天猫（通过好单库/折淘客）
- ✅ 美团联盟（外卖 + 到店 + 酒店）
- ✅ 饿了么（通过折淘客代理 + 直连 API）
- ✅ 拼多多（规划中）
- ✅ 抖音电商（规划中）

---

## 🔧 技术架构

```
price-compare/
├── SKILL.md            # Skill 主文件（触发词 + 执行流程）
├── README.md           # ClawHub 展示页（本文件）
├── scripts/
│   ├── query_jd.py          # 京东联盟查询
│   ├── query_taobao.py      # 好单库淘宝搜索
│   ├── query_meituan.py     # 美团联盟查询
│   ├── query_eleme.py       # 饿了么查询
│   └── compare_all.py       # 全平台并行比价
├── assets/
│   └── miniprogram_api.js   # 小程序集成 JS
└── references/
    └── api_docs.md          # 各平台 API 文档汇总
```

---

## 📱 小程序集成

本 Skill 可直接集成到微信小程序（如一券省），集成步骤：

1. 将 `assets/miniprogram_api.js` 导入小程序项目
2. 配置 `app.json` 添加比价页面路由
3. 在首页添加「比价」和「红包」入口按钮
4. 后端调用对应平台 API 完成查询展示

详细集成文档见 `assets/miniprogram_api.js` 注释。

---

## ⚠️ 注意事项

- 京东联盟授权 Key 有效期至 2027-03-04，到期需更新
- 淘宝联盟授权 30 天过期，需定期续期
- 好单库需联系客服开通 `supersearch` 权限
- 饿了么直连 AppSecret 需自行申请

---

## 📄 许可证

MIT-0

---

## 👨‍💻 作者

由 WorkBuddy AI 辅助开发，适用于一券省小程序及所有比价场景。

> 有问题或建议？欢迎在 ClawHub 留言！
