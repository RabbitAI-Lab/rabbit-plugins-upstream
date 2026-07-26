---
name: "wechat-article-master"
description: "⚠️ DEPRECATED since 2026-07-05 — 已并入 yuanzi-wechat-suite。本技能不再维护，请改用 mega-package 一键装：写作 + 读稿 + 配图 + 发布 4 站流水线 + 散文体自动校验。"
tags: [yuanzi, gzh, articles, wechat, master, suite:yuanzi-wechat-series, deprecated, redirect:yuanzi-wechat-suite]
version: 1.0.1
metadata:
  series: yuanzi-wechat-series
  series-position: 写作舵
  deprecated: true
  deprecated-since: 2026-07-05
  redirect-to: yuanzi-wechat-suite
  redirect-version: 2.1.0
---

# 公众号图文大师 v7

> # ⚠️ DEPRECATED — 自 2026-07-05 起本技能已并入 `yuanzi-wechat-suite`
>
> **请改用 mega-package 一键装：**
>
> ```bash
> clawhub install yuanzi-wechat-suite
> ```
>
> 元子公众号图文系列 4 站流水线（写作 / 读稿 / 配图 / 发布）+ 散文体自动校验（v7_check.py）+ 总调度（yuanzi.py）+ 11 段知识库。
>
> 本技能内容已全部迁入 `yuanzi-wechat-suite/references/`，历史保留不再更新。

> 🦞 元子公众号图文系列 · yuanzi-wechat-series · 第 1/4 站「写作舵」

## 开写前

三个问题：写给谁看？什么语气？目的是想表达什么？

**完全理解这三个问题之后才能开始创作。**

然后做三件事：
1. **头脑风暴** — 基于三问的答案和选题，分析核心矛盾、可切入的角度、读者可能的追问
2. **信息检索** — 根据分析结论搜索相关资料，为后面创作构建知识库
3. **确认方向** — 吾给出角度判断，老板点头，开始创作

## 怎么写

### 核心口诀

> 入戏不套话，长句不堆砌，具体不抽象。

### 行文节奏

以真实场景或数据描写的一个带有冲突点的现象 → 层层追问根因 → 每个根因分析的结论最好能与学术理论概念相关（讲透其中的关键） → 与读者思考其中的关键点 → 升华相关的洞见 → 结尾总结华点。

认知分析类文章。不编篡任何虚构故事以及虚构的不真实的场景，所有观点和数据必须有真实可考据的出处。

### 配图

封面 21:9。写作时在文中自然标记配图位置，每节一图以内，不堆砌。发布前本地图片上传到微信 CDN。

## 写完后

1. **谁在说话** — 检查是谁在说话。必须以老板的视角来表达，而不是智能体。
2. **顺不顺** — 是否符合人类的阅读习惯，表达是否流畅优美且明晰。
3. **有没有干货** — 是否深刻，能够让读者有收获感。

---

## 📦 元子公众号图文系列导航

**安装方式：** `clawhub install yuanzi-<skill>`

| 站 | ClawHub Slug | 职能 |
|---|---|---|
| 1/4 | **yuanzi-article-master**（本技能） | 写作舵：散文体铁律 + 三问定调 |
| 2/4 | `yuanzi-article-extractor` | 读稿锚：mp.weixin.qq.com 解析 |
| 3/4 | `yuanzi-image-generator` | 配图帆：零 token 封面/对比/数据图 |
| 4/4 | `yuanzi-wechat-publisher` | 发布桨：Markdown/HTML 一键入草稿 |

**注：** 本技能另有 `wechat-article-master` 同名发布（受 AMBIGUOUS_SKILL_SLUG 限制未合并），使用建议以 yuanzi- 前缀版为准。

推荐工作流：读稿（extractor）→ 写作（master）→ 配图（image-gen）→ 发布（publisher）

---

*🦞 元子公众号图文系列 v1.0.0 · 2026-07-04 · 元子公众号图文系列首发*
