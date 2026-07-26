---
name: "price-compare"
description: "全网比价与外卖比价技能。支持美团、京东、淘宝(折淘客/好单库)、饿了么等平台商品价格查询与对比，以及各平台红包/优惠券查询。当用户说比价、查价格、哪个平台便宜、外卖比价、查红包、领券等关键词时触发。"
agent_created: true
version: "1.0.0"
---

# 一券省 · 全网比价 & 外卖比价 Skill

本技能为一券省小程序提供全平台价格对比与红包入口能力，整合12个平台API。

## 触发词

- 比价 / 价格对比 / 哪个便宜
- 查价格 / 找优惠
- 外卖比价 / 美团饿了么对比
- 红包 / 领券 / 优惠券
- 全网比价

---

## API 凭证（来自用户密钥清单）

### 1. 微信小程序
- AppID: `请在下方配置你的 AppID`
- AppSecret: `请在下方配置你的 AppSecret`
- JWT Secret: `请在下方配置你的 JWT Secret`
> 📝 配置方式：在 `skills/price-compare/` 目录下创建 `.env` 文件，填入你的密钥

### 2. 美团联盟
- 注册地址: <ADDRESS_REMOVED>
- 需要配置: `MEITUAN_APPKEY`, `MEITUAN_APPSECRET`, `MEITUAN_CALLBACK_SECRET`
- 媒体名称: 你的媒体名称
- 回调地址: 你的回调地址

### 3. 京东联盟
- 注册地址: <ADDRESS_REMOVED>
- 需要配置: `JD_APPKEY`, `JD_APPSECRET`, `JD_AUTH_KEY`

### 4. 折淘客（淘宝/饿了么代理）
- 注册地址: <ADDRESS_REMOVED>
- 需要配置: `ZHETAOKE_APPKEY`, `ZHETAOKE_SID`

### 5. 好单库（淘宝搜索API）
- 注册地址: <ADDRESS_REMOVED>
- 需要配置: `HAODANKU_APIKEY`
- 注意: 需联系好单库开通 supersearch 权限

### 6. 饿了么联盟（直连）
- 注册地址: <ADDRESS_REMOVED>
- 需要配置: `ELEME_APPKEY`, `ELEME_APPSECRET`

### AI 模型 API（可选，用于结果润色）
- 智谱 AI: `ZHIPU_ACCESS_KEY`
- 阿里云百炼: `DASHSCOPE_API_KEY`
- 百度千帆: `QIANFAN_API_KEY`

---
## 配置说明

在项目根目录创建 `.env` 文件，填入你的 API 密钥：

```
# 美团联盟
MEITUAN_APPKEY=你的AppKey
MEITUAN_APPSECRET=你的AppSecret
MEITUAN_CALLBACK_SECRET=你的回调密钥

# 京东联盟
JD_APPKEY=你的AppKey
JD_APPSECRET=你的AppSecret
JD_AUTH_KEY=你的授权Key

# 折淘客
ZHETAOKE_APPKEY=你的AppKey
ZHETAOKE_SID=你的sid

# 好单库
HAODANKU_APIKEY=你的apikey

# 饿了么直连（可选）
ELEME_APPKEY=你的AppKey
ELEME_APPSECRET=你的AppSecret
```

> ⚠️ 注意：`.env` 文件包含敏感信息，请勿提交到 Git 仓库！

---

## 执行流程

### 比价查询流程

1. 解析用户输入的商品名称
2. 并行调用以下平台API：
   - 京东联盟 (`scripts/query_jd.py`)
   - 好单库淘宝 (`scripts/query_taobao.py`)
   - 美团联盟 (`scripts/query_meituan.py`)
3. 标准化各平台返回数据，提取：商品名、价格、优惠券、到手价
4. 按到手价排序，生成对比表格
5. 附上各平台跳转链接

### 外卖比价流程

1. 解析用户指定的外卖商家/菜品
2. 调用美团联盟API查询美团外卖价格
3. 调用折淘客API查询饿了么价格
4. 对比展示：商家名、菜品名、原价、红包后价格、红包金额
5. 提供领红包入口链接

### 红包查询流程

1. 根据用户所在平台和地理位置
2. 调用对应平台API获取当前可领红包列表
3. 展示：红包金额、使用条件、有效期、领取链接
4. 优先展示无门槛红包和大额红包

---

## 输出格式

比价结果使用以下格式输出：

```
## 比价结果：[商品名称]

| 平台 | 商品名 | 原价 | 券后价 | 到手价 | 链接 |
|------|--------|------|--------|--------|------|
| 京东 | ... | ... | ... | ... | [前往购买] |
| 淘宝 | ... | ... | ... | ... | [前往购买] |
| 美团 | ... | ... | ... | ... | [前往购买] |

💡 最便宜：平台名 ¥价格（含券/红包）
```

外卖比价格式：

```
## 外卖比价：[商家名/菜品名]

🍜 美团外卖：¥XX（可领¥X红包）
🍱 饿了么：¥XX（可领¥X红包）

💡 推荐：[平台名]，到手价¥XX
[领红包入口]
```

---

## 小程序集成

本Skill可作为一券省小程序的功能模块集成，集成方式：

1. 将 `assets/miniprogram_api.js` 导入小程序项目
2. 配置 `app.json` 添加比价页面路由
3. 在首页添加"比价"和"红包"入口按钮
4. 调用对应API完成查询展示

---

## 注意事项

- 京东联盟授权Key有效期至2027-03-04，到期需更新
- 淘宝联盟授权30天过期，需定期续期
- 好单库需联系开通supersearch权限
- 饿了么直连AppSecret待用户提供
- 所有API调用需处理签名/加密逻辑（参见各平台文档）
