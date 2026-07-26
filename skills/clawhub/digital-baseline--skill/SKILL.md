---
name: buildstack-site-builder
description: 筑栈 BuildStack AI 建站 — AI 驱动的一键网站部署。选模板→填信息→上线，支持 AI 建站、CMS 管理、GEO 优化。集成订阅体系自动感知套餐限额。
metadata:
  openclaw:
    emoji: "🏗️"
  skillhub:
    category: "开发工具"
    tags: ["建站", "AI建站", "网站部署", "CMS", "GEO", "SEO", "SaaS"]
    homepage: "https://buildstack.com.cn"
    author: "筑栈 BuildStack"
    version: "1.0.0"
---

# 筑栈 BuildStack — AI 建站 Skill

通过筑栈 API，AI Agent 可以帮用户完成**一句话建站**、**CMS 内容管理**、**GEO 优化**等全部操作，无需打开浏览器。

## 前置条件

用户需要一个筑栈账号 + API Key。获取方式：

1. 注册筑栈账号：https://buildstack.com.cn/register
2. 登录后进入 Dashboard → API 密钥 → 创建新密钥
3. 将 `sk_xxxxxxxxxxxx` 设为环境变量 `BUILDSTACK_API_KEY`

**所有 API 请求必须带 Header**：
```
Authorization: Bearer sk_xxxxxxxxxxxx
Content-Type: application/json
```

API 地址：`https://buildstack.com.cn/api/v1`

## 建站流程（核心能力）

### 第一步：获取可用的行业和模板

```bash
# 列出可用模板（按行业筛选）
curl -s https://buildstack.com.cn/api/v1/skills?industry=education \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY"
```

返回示例：
```json
{
  "templates": [
    {"id": 1, "name": "教育机构通用版", "slug": "education-default", "industry": "education"}
  ],
  "skills": [...]
}
```

### 第二步：AI 一句话建站（推荐）

如果你知道用户的业务信息，直接调用 AI 生成站点：

```bash
curl -s -X POST https://buildstack.com.cn/api/v1/ai/generate \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "一个北京的钢琴培训工作室，名叫「星河音乐」，5位老师，提供钢琴/吉他/小提琴课程，面向4-16岁孩子",
    "industry": "education",
    "template_id": 1
  }'
```

AI 会自动生成：公司名称、页面内容、联系方式、FAQ、结构化数据。返回 `site_id` 和部署状态。

### 第三步：手动创建站点（精细控制）

如果需要精细控制每个字段：

```bash
curl -s -X POST https://buildstack.com.cn/api/v1/sites \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "星河音乐工作室",
    "slug": "xinghe-music",
    "template_id": 1,
    "locale": "zh-CN",
    "domain": "",
    "features": {"products_mode": "cms"}
  }'
```

参数说明：
| 字段 | 必填 | 说明 |
|------|:--:|------|
| `name` | ✅ | 网站标题，也是 SEO title（≤50字符） |
| `slug` | ✅ | URL 标识，仅含字母数字和连字符，如 `xinghe-music` |
| `template_id` | - | 模板 ID（不传则用默认模板） |
| `locale` | - | zh-CN / en / zh-TW，默认 zh-CN |
| `domain` | - | 自有域名（留空自动分配 `slug.buildstack.com.cn`） |
| `features` | - | `{"products_mode":"cms"}` 开启产品管理 |

### 第四步：等待部署完成

创建站点后系统自动部署（约 15-30 秒），轮询状态：

```bash
curl -s https://buildstack.com.cn/api/v1/sites/{site_id} \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY" | grep status
```

状态说明：
- `deploying` → 部署中
- `live` → ✅ 上线完成，返回 URL 给用户
- `error` → 部署失败，查看 `seo_config.build_error`

## 上线后操作

### CMS 内容管理

```bash
# 获取站点所有内容块
curl -s https://buildstack.com.cn/api/v1/sites/{site_id}/blocks \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY"

# 更新 hero 区域
curl -s -X PUT https://buildstack.com.cn/api/v1/sites/{site_id}/blocks/hero \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "星河音乐工作室", "subtitle": "让孩子爱上音乐", "content": {"cta_text":"预约试课"}}'
```

常用 block_key：`hero` / `about` / `features` / `team` / `courses` / `faq` / `contact` / `footer`

### 发布文章

```bash
curl -s -X POST https://buildstack.com.cn/api/v1/sites/{site_id}/articles \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "为什么 4 岁是学钢琴的最佳年龄",
    "content": "<p>...(HTML正文)...</p>",
    "status": "published",
    "tags": ["钢琴", "教育"]
  }'
```

## 套餐限额 & 错误处理（关键）

筑栈根据套餐等级限制操作。你要**自然地向用户解释**，不要干巴巴抛错误码：

### 站点数量限制

| HTTP 状态 | 含义 | 你对用户说的话 |
|-----------|------|---------------|
| `422` with `"detail":"trial_expired"` | 7 天试用过期 | 「你的免费试用已经到期，无法创建新站。升级到 STARTER（¥49/月）就可以继续建站了 👉 https://buildstack.com.cn/upgrade」 |
| `422` with `"detail":"site_limit_reached"` | 站点数用完 | 「你的 FREE 套餐只能创建 1 个站点，已经用完了。升级到 STARTER 可以建 3 个站 👉 https://buildstack.com.cn/upgrade」 |
| `402` | 需要付费功能 | 「这个功能需要 STARTER 套餐。升级后马上就能用 👉 https://buildstack.com.cn/upgrade」 |

### 通用错误

| HTTP | 含义 | 处理 |
|------|------|------|
| `401` | API Key 无效或过期 | 让用户去 Dashboard → API密钥 重新生成 |
| `404` | site_id 不存在 | 确认 site_id 是否正确，或站点是否已删除 |
| `429` | 请求过频 | 等 5 秒后重试 |
| `500` | 服务器错误 | 告知用户「筑栈服务暂时异常，稍后重试」，不要自动重试超过 3 次 |

**核心原则：错误时永远提供升级/修复途径，不要让用户卡住。**

## SEO / GEO 操作

```bash
# 获取站点 GEO 评分
curl -s https://buildstack.com.cn/api/v1/sites/{site_id}/seo-status \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY"

# 刷新 SEO 配置（sitemap + llms.txt + 结构化数据）
curl -s -X POST https://buildstack.com.cn/api/v1/sites/{site_id}/rebuild-seo \
  -H "Authorization: Bearer $BUILDSTACK_API_KEY"
```

## 典型对话范例

### 场景 1：用户要建站
> 用户：帮我做个咖啡店网站

你的回答应该包括：
1. 收集关键信息（店名、城市、特色、是否需要产品展示）
2. 确认后调用 API 建站
3. 部署完成返回 URL：「✅ 咖啡店网站已上线！https://xxx.buildstack.com.cn」

### 场景 2：免费用户建第二个站
> 用户：再帮我建一个花店网站

API 返回 `422 site_limit_reached`，你应该说：
> 「你目前是 FREE 套餐，只能建 1 个网站。花店网站已经规划好了，随时可以上线——只需要升级到 STARTER（¥49/月，可建 3 个站）👉 https://buildstack.com.cn/upgrade」

### 场景 3：更新已有站点
> 用户：给我的咖啡店网站加个「本月特惠」板块

1. 先 `GET /sites` 找到 site_id
2. `PUT /sites/{id}/blocks/special-offers` 创建/更新内容块
3. 内容块生效后告诉用户：「已添加。刷新 https://xxx.buildstack.com.cn 看看效果」

## 限制与边界

- 不要替用户决定套餐升级（只提供链接，让用户自己操作）
- 不要在 SKILL 对话中收集用户的支付宝/信用卡信息
- 每个 API Key 每天最多创建 10 个站点
- 生成的内容不要包含色情、赌博、政治敏感信息
