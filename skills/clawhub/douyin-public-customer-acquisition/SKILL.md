---
name: douyin-public-customer-acquisition
description: 视频平台公域流量精准获客工具。基于评论区数据挖掘，支持竞品截流、意向客户筛选、舆情转化及私域引流，适用于短视频营销、销售线索挖掘、精准获客与流量变现，助力企业低成本获取高意向客户。
version: 1.0.0
license: MIT
metadata:
  enabled: true
  type: command
  runtime: "nodejs@16.14.0+"
  requires:
    bins:
      - "node"
    env:
      - "GUAIKEI_API_TOKEN"
  category:
    - "Growth Hacking"
    - "Sales & Leads"
    - "Marketing Automation"
  tags:
    - "customer-acquisition"
    - "lead-generation"
    - "competitor-interception"
    - "public-traffic"
    - "douyin"
    - "sales"
    - "marketing"
    - "conversion"
    - "automation"
  schemas:
    - name: "搜索入参"
      file: "assets/search_cli_req.schema.json"
    - name: "搜索出参"
      file: "assets/search_cli_resp.schema.json"
    - name: "作品入参"
      file: "assets/post_cli_req.schema.json"
    - name: "作品出参"
      file: "assets/post_cli_resp.schema.json"
    - name: "热榜出参"
      file: "assets/hot_cli_resp.schema.json"
    - name: "评论入参"
      file: "assets/comment_cli_req.schema.json"
    - name: "评论出参"
      file: "assets/comment_cli_resp.schema.json"
  examples:
    - name: 搜索"装修"寻找潜在客户
      command: 'node src/douyin/search-cli.js --keyword "装修"'
      description: 快速定位有装修需求的公域流量，挖掘潜在销售线索
    - name: 搜索"竞品品牌"进行截流
      command: 'node src/douyin/search-cli.js --keyword "竞品品牌" --sort 1'
      description: 监控竞品爆款视频，在评论区寻找意向客户进行转化
    - name: 监控近期"AI工具"热点需求
      command: 'node src/douyin/search-cli.js --keyword "AI工具" --time 7'
      description: 追踪近期热点趋势，把握内容窗口期，快速切入市场
    - name: 获取竞品爆款视频评论区线索
      command: 'node src/douyin/comment-cli.js --url "https://www.douyin.com/video/xxx"'
      description: 深度挖掘评论区高意向评论，分析用户痛点，精准截流获客
    - name: 获取抖人 MS4wLjABxxx 粉丝画像
      command: 'node src/douyin/post-cli.js --url "https://www.douyin.com/user/MS4wLjABxxx"'
      description: 分析对标账号内容策略，复制其成功获客路径
    - name: 获取抖音实时热搜榜单
      command: "node src/douyin/hot-cli.js"
      description: 实时掌握平台热点，快速响应热门话题，借势营销获客
---

# 🚀 公域流量精准获客与竞品截流系统

> **💡一句话价值**：从海量公域评论区中“淘金”，帮你精准定位意向客户，低成本截流竞品流量，实现销售线索倍增。
>
> **🔥核心优势**
>
> - **精准获客**：直达评论区，筛选“求带”、“怎么买”等高意向用户，拒绝无效流量
> - **竞品截流**：监控对标账号爆款视频，在评论区挖掘其潜在客户，实现精准转化
> - **安全隐蔽**：无需登录抖音账号，规避风控风险，保护主号安全
> - **高效转化**：批量获取结构化线索数据，直接对接CRM或销售团队，缩短转化路径
> - **轻量灵活**：无需部署复杂服务，Node.js一键运行，适配各种营销场景

## 1. ✅ 我能帮你解决什么（10 秒判断）

- 🔍 **寻找精准线索**：按关键词搜索视频，定位有明确需求的公域用户
- 🦸 **竞品流量转化**：批量抓取对标账号评论区，将竞品的粉丝转化为你的客户
- 💬 **挖掘用户痛点**：分析高赞评论和提问，优化销售话术，直击用户痛点
- 📡 **热点借势营销**：实时获取热榜，结合热点发布内容，获取平台自然流量
- 📊 **销售线索导出**：自动生成结构化线索日志，方便销售团队跟进和二次触达

## 2. 🚀 最快上手（复制就能跑，30 秒出线索）

> **Note:** 请先通过微信 <13395823479> 申请TOKEN ，或访问[社媒获客技能官网](https://www.guaikei.com)开通TOKEN，配置环境变量 `GUAIKEI_API_TOKEN` 后才能正常运行。

### 2.1 🔎 关键词定位潜在客户（最简单）

```bash
node src/douyin/search-cli.js --keyword "装修"
```

### 2.2 🔎 竞品爆款视频截流（最常用）

```bash
node src/douyin/search-cli.js --keyword "竞品品牌名" --sort 1
```

### 2.3 🦸 监控对标账号获客路径

```bash
node src/douyin/post-cli.js --url "https://www.douyin.com/user/MS4wLjABxxx"
```

### 2.4 💬 深度挖掘评论区高意向线索

```bash node src/douyin/comment-cli.js --url "https://www.douyin.com/video/xxx"

```

### 2.5 📡 获取抖音实时热榜借势

```bash
node src/douyin/hot-cli.js
```

## 3. 📌 适用场景（我该不该用？）

- 你需要低成本获取销售线索 → 关键词搜索 + 评论区筛选
- 你需要转化竞品客户 → 监控竞品爆款视频评论区
- 你需要优化销售话术 → 分析用户真实痛点和提问
- 你需要快速切入市场 → 实时获取热榜，结合热点获客
- 你需要做销售报表 → 导出结构化线索数据

## 4. 🔧 参数详解表

> 详细选项参数说明， 可参阅 [完整选项说明](references/options.md)
>
> LLM理解技能的详细选项，可参阅技能 `assets` 目录中文件，其遵循 JSON Schema draft-07 版本规范。
>
> - 抖音关键词搜索，[入参规范](assets/search_cli_req.schema.json)
> - 抖音关键词搜索，[出参规范](assets/search_cli_resp.schema.json)
> - 抖音抖人作品获取，[入参规范](assets/post_cli_req.schema.json)
> - 抖音抖人作品获取，[出参规范](assets/post_cli_resp.schema.json)
> - 抖音评论获取，[入参规范](assets/comment_cli_req.schema.json)
> - 抖音评论获取，[出参规范](assets/comment_cli_resp.schema.json)
> - 抖音热榜获取，[出参规范](assets/hot_cli_resp.schema.json)

## 5. ⚠️ 重要限制（不踩坑）

- 仅抓取抖音公开数据，不支持私密 / 隐藏内容
- 需要配置 GUAIKEI_API_TOKEN 才能正常运行
- 数据仅限个人 / 团队内部使用，禁止违规分发

## 6. ❓ 常见问题（秒解决）

> **💡Q：运行报错，提示无权限？**
>
> A：配置环境变量：
>
> - Windows: `set GUAIKEI_API_TOKEN=你的TOKEN`
> - Linux/MacOS: `export GUAIKEI_API_TOKEN=你的TOKEN`
> - 私有TOKEN申请后请留意使用安全，避免泄露给他人
>
> **💡Q：搜索结果为空？**
>
> A：换常用关键词，或把 `--time` 改为 0（全部时间）
>
> **💡Q：输出文件在哪里？**
>
> A：自动保存在技能目录的 `logs` 文件夹下
>
> - 搜索任务日志: 默认保存为「时间戳\_关键词\_排序\_时间\_时长\_search.json」
> - 抖人作品获取日志: 默认保存为「时间戳\_(抖人sec_uid)\_post.json」
> - 抖音评论获取日志: 默认保存为「时间戳\_(视频aweme_id)\_comment.json」
>
> **💡Q：支持 Windows/Mac/Linux 吗？**
>
> A：全平台支持，仅需安装 Node.js 环境

## 7. 📞 帮助与支持

- 联系微信 13395823479（备注抖音技能）开通TOKEN或获得技能使用支持；
- 或通过 [抖音关键词搜索技能官网](https://www.guaikei.com) 自助开通TOKEN或查阅使用帮助。
  > 🆕 [更新日志](references/changelog.md) 可查阅这里
