# 全网比价+外卖比价 Skill 使用文档

## 📋 目录

- [简介](#简介)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [命令参考](#命令参考)
- [小程序集成](#小程序集成)
- [API 参考](#api-参考)
- [常见问题](#常见问题)

---

## 简介

**全网比价+外卖比价** 是一个支持 12 个平台商品价格对比的 WorkBuddy Skill，覆盖：

| 平台 | 类型 | 状态 |
|------|------|------|
| 京东 | 电商 | ✅ 已接入 |
| 淘宝（好单库/折淘客） | 电商 | ✅ 已接入 |
| 美团 | 外卖/团购 | ✅ 已接入 |
| 饿了么（折淘客代理） | 外卖 | ✅ 已接入 |
| 饿了么（直连） | 外卖 | ⚠️ AppSecret待提供 |
| 滴滴联盟 | 出行 | 📋 待开发 |
| 唯品会 | 电商 | 📋 待开发 |

**核心功能：**
- 🔍 关键词搜索全网最低价
- 🍔 美团 vs 饿了么外卖实时比价
- 🎁 各平台红包/优惠券查询与领取入口
- 📊 标准化结果输出，支持终端、Web、小程序

---

## 快速开始

### 方式一：在 WorkBuddy 中使用（推荐）

安装 Skill 后，直接对话：

```
帮我比价 手机壳
美团和饿了么哪个便宜 黄焖鸡
看看今天有什么红包可以领
京东上XX多少钱
```

### 方式二：命令行使用

```bash
# 全网比价
python scripts/compare_all.py "螺蛳粉"

# 外卖比价
python scripts/compare_all.py "黄焖鸡" --city 1

# 只看红包
python scripts/compare_all.py --coupons

# JSON 格式输出（供程序调用）
python scripts/compare_all.py "手机" --json

# 指定平台
python scripts/query_jd.py "键盘"
python scripts/query_taobao.py "鼠标"
python scripts/query_meituan.py "快餐"
python scripts/query_eleme.py "奶茶"
```

---

## 配置说明

### 环境变量

创建 `.env` 文件（参考 `.env.example`）：

```bash
# 美团联盟（必须）
MEITUAN_APPKEY=e04be35c176a4a5d8400b46c29ec4132
MEITUAN_APPSECRET=0af8998613c54f7e9cb3ededb7203031

# 京东联盟（必须）
JD_APPKEY=0577957bee925536b09ac062dfda3db8
JD_APPSECRET=44560303245f4ae19cccc1360e30f51c
JD_AUTH_KEY=6ef3fbb8dfe5d8e2f712b99abc77faa9375c84f0b3276421b8f6d11403b7da4bd2a116baf402fc46

# 折淘客（淘宝/饿了么代理，必须）
ZHETAOKE_APPKEY=8cbd7852d5fc4c04a956049683c2a645
ZHETAOKE_SID=187029

# 好单库（淘宝搜索，必须）
HAODANKU_APIKEY=F52D1486CC51

# 饿了么直连（可选，AppSecret待提供）
ELEME_APPKEY=2ec59ae85af24f8da79e6bbe1f5d3312
ELEME_APPSECRET=
```

### 饿了么 AppSecret 说明 ⚠️

饿了么联盟直连的 **AppSecret 当前标注为"待提供"**。

**替代方案：** 本 Skill 已集成**折淘客代理**方式调用饿了么 API，无需 AppSecret 即可使用外卖比价和红包查询功能。

如需直连（更高稳定性），请：
1. 登录 [饿了么开放平台](https://open.ele.me/)
2. 获取 AppSecret
3. 填入环境变量 `ELEME_APPSECRET`

---

## 命令参考

### compare_all.py - 综合比价引擎

```bash
python scripts/compare_all.py <关键词> [选项]

选项:
  --city <ID>     城市ID，默认1（外卖用）
  --size <N>      每页数量，默认20
  --coupons       仅查询红包
  --json          JSON格式输出

示例:
  python scripts/compare_all.py "机械键盘"
  python scripts/compare_all.py "火锅" --city 1 --json
  python scripts/compare_all.py --coupons
```

### 单平台查询

| 脚本 | 平台 | 用法 |
|------|------|------|
| `query_jd.py` | 京东 | `python query_jd.py "手机"` |
| `query_taobao.py` | 淘宝 | `python query_taobao.py "连衣裙"` |
| `query_meituan.py` | 美团 | `python query_meituan.py "快餐"` |
| `query_eleme.py` | 饿了么 | `python query_eleme.py "奶茶"` |

### 输出格式

所有结果统一为以下 JSON 结构：

```json
{
  "platform": "京东",
  "title": "商品名称",
  "price": 99.00,
  "coupon_amount": 20.00,
  "after_price": 79.00,
  "url": "https://...",
  "shop": "店铺名",
  "sales": 1234,
  "rating": 4.8
}
```

---

## 小程序集成

### 集成步骤

**1. 复制文件**

将 `assets/miniprogram_api.js` 放入小程序项目 `utils/api.js`

**2. 在 app.js 中引入**

```javascript
const API = require('./utils/api')
App({
  API,
  onLaunch() { /* ... */ }
})
```

**3. 在页面中使用**

```javascript
const API = require('../../utils/api')

Page({
  data: {
    results: [],
    loading: false,
  },

  // 全网比价
  async onSearch(e) {
    this.setData({ loading: true })
    try {
      const result = await API.compareAll(e.detail.value)
      this.setData({ results: result.results })
      wx.showToast({ title: `找到${result.count}个结果` })
    } catch (err) {
      wx.showToast({ title: err.message, icon: 'none' })
    } finally {
      this.setData({ loading: false })
    }
  },

  // 外卖比价
  async onWaimaiCompare(keyword) {
    const result = await API.compareWaimai(keyword, 1)
    console.log('美团:', result.meituan)
    console.log('饿了么:', result.eleme)
    console.log('最优:', result.best)
  },

  // 查看红包
  async onLoadCoupons() {
    const coupons = await API.getAvailableCoupons('all')
    console.log('美团红包:', coupons.meituan)
    console.log('饿了么红包:', coupons.eleme)
  },

  // 领取红包
  async onClaimCoupon() {
    const result = await API.claimCoupon('meituan', 'coupon_id')
    wx.showModal({ title: '领取成功', content: '红包已发放' })
  },
})
```

### 后端部署要求

小程序需要后端中转 API 调用。后端地址默认：
```
https://mini.juanshenghui.com/api
```

修改 `miniprogram_api.js` 顶部的 `API_BASE` 为你的后端地址。

---

## API 参考

### 小程序端 API

| 方法 | 说明 | 参数 |
|------|------|------|
| `compareAll(keyword, options)` | 全网比价 | keyword, {cityId, page, pageSize, platforms} |
| `compareWaimai(keyword, cityId)` | 外卖比价 | keyword, cityId |
| `getAvailableCoupons(platforms)` | 获取红包 | 'all' 或 'meituan,eleme' |
| `claimCoupon(platform, id)` | 领取红包 | platform, couponId |
| `searchSuggest(keyword)` | 搜索建议 | keyword |
| `getSearchHistory(page)` | 搜索历史 | page |
| `clearSearchHistory()` | 清空历史 | - |
| `getCouponHistory(page)` | 红包记录 | page |

### Python 脚本 API

| 脚本 | 导出函数 |
|------|----------|
| `query_jd.py` | `query_jd_products()`, `query_jd_coupons()`, `format_result()` |
| `query_taobao.py` | `query_taobao()`, `format_result()` |
| `query_meituan.py` | `query_meituan_waimai()`, `query_meituan_search()`, `query_meituan_tuangou()`, `get_meituan_coupons()` |
| `query_eleme.py` | `query_eleme_zhetaoke()`, `get_eleme_coupons_zhetaoke()`, `query_eleme_direct()` |
| `compare_all.py` | `compare_all()`, `get_all_coupons()` |

---

## 常见问题

### Q: 为什么淘宝查不到结果？

A: 需要在好单库开通 `supersearch` 权限。联系好单库客服申请。

### Q: 饿了么查不到怎么办？

A: 饿了么直连 AppSecret 待提供。当前通过折淘客代理调用，大多数情况下可用。如需100%稳定，请联系饿了么开放平台获取 AppSecret。

### Q: 如何添加新平台？

A: 在 `scripts/` 目录下创建新文件（参考 `query_jd.py`），然后在 `compare_all.py` 顶部添加导入即可。

### Q: 小程序提示"网络错误"？

A: 检查后端服务器 `121.37.41.147` 是否正常运行，Workerman 端口 `8790` 是否开放。

### Q: API 密钥会泄露吗？

A: 本 Skill 通过环境变量管理密钥，ClawHub 公开发布版本已替换为占位符。请勿将真实密钥提交到公开仓库。

---

## 项目结构

```
price-compare/
├── SKILL.md                  # Skill 主文件
├── README.md                 # 项目说明
├── USAGE.md                  # 本文件
├── .env.example              # 环境变量模板
├── scripts/
│   ├── compare_all.py        # 综合比价引擎
│   ├── query_jd.py           # 京东查询
│   ├── query_taobao.py       # 淘宝查询
│   ├── query_meituan.py      # 美团查询
│   └── query_eleme.py        # 饿了么查询
├── assets/
│   └── miniprogram_api.js    # 小程序集成代码
└── references/
    └── api_docs.md           # API 密钥参考
```

---

> 📅 最后更新: 2026-06-08 | 版本: 1.0.0
