# API 接口参考文档

本文档汇总所有平台的 API 调用方式和注意事项。

---

## 1. 微信小程序

| 字段 | 值 |
|------|-----|
| AppID | `wx8e1a349cc6158954` |
| AppSecret | `ff1319dece322828351fb9475bc98d5b` |
| JWT Secret | `drCNFHm5j7Ww7KauvUdH2tFsFIUVyE95` |

**用途**: 小程序登录、获取用户 session、生成 JWT token

**官方文档**: https://developers.weixin.qq.com/miniprogram/dev/OpenApi/

---

## 2. 美团联盟

| 字段 | 值 |
|------|-----|
| AppKey | `e04be35c176a4a5d8400b46c29ec4132` |
| AppSecret | `0af8998613c54f7e9cb3ededb7203031` |
| 回调密钥 | `25d9esTrBn` |
| 媒体名称 | `券汇省` |
| 回调地址 | `https://mini.juanshenghui.com/callback/meiTu` |

### API 规则

| 业务类型 | platform | bizLine | topiId |
|----------|----------|---------|--------|
| 外卖 | 1 | 0 | 2 |
| 搜索 | - | - | 0 |
| 团购 | 2 | 1 | 3 |

**签名方式**: MD5(appSecret + 按key排序的参数拼接 + appSecret)

**官方文档**: https://open.meituan.com/

---

## 3. 京东联盟

| 字段 | 值 |
|------|-----|
| AppKey | `0577957bee925536b09ac062dfda3db8` |
| AppSecret | `44560303245f4ae19cccc1360e30f51c` |
| 授权Key | `6ef3fbb8dfe5d8e2f712b99abc77faa9375c84f0b3276421b8f6d11403b7da4bd2a116baf402fc46` |
| 有效期至 | `2027-03-04` |

**接口地址**: `https://api.jd.com/routerjson`

**签名方式**: MD5(appSecret + 按key排序拼接 + appSecret)，大写

**官方文档**: https://union.jd.com/

---

## 4. 折淘客（淘宝/饿了么代理）

| 字段 | 值 |
|------|-----|
| Appkey | `8cbd7852d5fc4c04a956049683c2a645` |
| sid | `187029` |
| 平台地址 | `https://www.zhetaoke.com` |
| 饿了么端点 | `https://api.zhetaoke.com:10001/api/open_eleme_generateLink.ashx` |
| 京东搜索端点 | `http://api.zhetaoke.com:20000/api/open_jing_union_open_goods_query.ashx` |

**注意**:
- 淘宝联盟授权30天过期，需续期
- `result` 字段是 JSON 字符串，需二次解析

---

## 5. 好单库（淘宝搜索API）

| 字段 | 值 |
|------|-----|
| apikey | `F52D1486CC51` |
| API地址 | `http://v2.api.haodanku.com` |
| 搜索接口 | `/supersearch/apikey/{apikey}/keyword/{keyword}/back/{back}/min_id/{min_id}` |

**back参数**: 仅支持 `1/2/5/10/20/50/100`

**注意**:
- 关键词需**两次URL编码**
- 需联系好单库开通 `supersearch` 权限

**官方文档**: https://www.haodanku.com/

---

## 6. 饿了么联盟（直连）

| 字段 | 值 |
|------|-----|
| AppKey | `2ec59ae85af24f8da79e6bbe1f5d3312` |
| AppSecret | **待提供** |

**注意**: AppSecret 需用户补充后才能使用直连方式

---

## 9. 智谱 AI

| 字段 | 值 |
|------|-----|
| access_key | `6embGPvAl7fDzHTLCG3GElg4601yJYN9` |
| app_key | `LVFHqz1vkdIQO76D` |

**用途**: AI 比价分析、商品推荐文案生成

---

## 10. 阿里云百炼

| 字段 | 值 |
|------|-----|
| AccessKeyId | `LTAI5t9U6M6rV2DPaizB68ws` |
| AccessKeySecret | `usk5WrBr9buuQPgmkgfQHXbfQuqDMO` |
| DashScope API Key | `sk-26ae09517efd42668d0b2dff14e147e7` |

**可用模型**: `qwen-turbo`, `qwen-plus`, `qwen-max`

**官方文档**: https://dashscope.aliyun.com/

---

## 11. 百度千帆

| 字段 | 值 |
|------|-----|
| API Key | `bce-v3/ALTAK-DkUdVkl8KeLYqgQ0gDk2U/806aa625c259a4b02a6a7ec4be3ec3cca21d0024` |
| 可用模型 | `ernie-3.5-8k`（永久免费）、`ernie-speed-pro-128k` |

**官方文档**: https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html

---

## 12. 服务器与后台

| 字段 | 值 |
|------|-----|
| 服务器IP | `121.37.41.147` |
| SSH密码 | `qsh@2026` |
| Workerman端口 | `8790` |
| 宝塔面板 | `https://121.37.41.147:22148/cd078cc0` |
| 宝塔账号 | `dvflytht` |
| 数据库名 | `unionpush` |
| 数据库用户 | `unionpush` |
| 数据库密码 | `6sjbF5yB3HEy26iP` |
| 管理后台 | `https://mini.juanshenghui.com/admin/login` |
| 后台账号 | `admin / 111111` |

---

## 通用注意事项

1. **所有 API Key 为敏感信息，不得硬编码在前端代码中**
2. **小程序端所有 API 调用应通过后端中转**，后端存储密钥
3. **签名生成时注意编码问题**，中文参数需 UTF-8 编码
4. **定时检查授权有效期**，京东 Key 2027-03-04 到期，淘宝授权30天续期
5. **API 调用频率限制**，各平台均有 QPS 限制，注意限流
