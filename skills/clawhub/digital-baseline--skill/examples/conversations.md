# 筑栈建站 Skill — 对话示例

## 场景 1：咖啡店建站（完整流程）

**用户**：帮我做一个精品咖啡店的网站

**AI**：好的！几个信息确认一下：
- 店名叫什么？在哪个城市？
- 大概多久历史？什么风格？
- 需要展示哪些内容？（菜单 / 故事 / 位置 / 活动）

**用户**：叫「质馆咖啡」，上海静安区，开了 5 年，精品手冲为主。需要菜单和位置

**AI**：（调用建站 API）
```
POST /api/v1/ai/generate
{"prompt":"质馆咖啡，上海静安区，5年精品手冲咖啡店，需要菜单展示和位置信息"}
```

→ 收到 site_id=45 → 轮询状态 → live

> 📍 网站已上线！
> - 🌐 https://zhiguan-coffee.buildstack.com.cn
> - ✅ 首页 / 菜单 / 咖啡故事 / 联系我们
> - 📱 手机版自动适配
> - 🔍 已生成 SEO 优化（标题/描述/结构化数据）
>
> 需要调整什么内容吗？

---

## 场景 2：试用到期引导

**用户**：帮我再做一个花店网站

**AI**：（调用 API → 422 trial_expired）

> 你的 7 天免费试用已经到期了 🤏
>
> 花店网站的内容我已经规划好了，随时可以上线——升级到 STARTER 就行：
> - 🏪 3 个站点（可以保留咖啡店 + 新建花店 + 还能再建一个）
> - 🌐 支持自有域名
> - 📦 产品管理 / 客服组件
> - 💰 ¥49/月（或 ¥499/年，省 ¥89）
>
> 👉 https://buildstack.com.cn/upgrade
>
> 升级后告诉我，我立刻帮你上线花店网站！

---

## 场景 3：发布文章

**用户**：给咖啡店发一篇「如何在家冲出一杯好手冲」的文章

**AI**：（调用 GPT 生成文章内容 → 调用 CMS API）
```
POST /api/v1/sites/45/articles
{"title":"如何在家冲出一杯好手冲","content":"<p>...</p>","status":"published","tags":["手冲","教程"]}
```

> 📝 文章已发布！
> - 📖 https://zhiguan-coffee.buildstack.com.cn/news/home-brew-guide
> - 🏷️ 标签：手冲 · 教程
> - 📊 内容约 800 字，包含 3 个步骤图解
>
> 要不要我同时生成 SEO 优化（标题/描述/关键词）？

---

## 场景 4：修改内容

**用户**：咖啡店的「关于我们」页面把「5年」改成「6年历史」

**AI**：
```
PUT /api/v1/sites/45/blocks/about
{"content": {"description":"质馆咖啡，创立于 2020 年，6 年专注精品手冲..."}}
```

> ✅ 已更新！刷新页面即可看到：
> https://zhiguan-coffee.buildstack.com.cn

---

## 场景 5：跨平台 SEO 诊断

**用户**：检查一下我咖啡店的 SEO

**AI**：
```
GET /api/v1/sites/45/seo-status
```

> 📊 GEO 诊断报告 — 质馆咖啡（85/100）
>
> ✅ llms.txt：完整，包含 3 个 priority 标记
> ✅ JSON-LD：Organization + Website + MenuItem
> ✅ sitemap.xml：12 个 URL
> ✅ Open Graph：完整
> ⚠️ 未设置 sameAs 链接（知乎/大众点评/小红书）
> ⚠️ FAQ 只有 3 条（建议 10+ 条）
>
> 要我帮你补充吗？
