# Digest Template

Use this structure for the final deliverable. Adapt section names when the day's news clearly fits better headings, but keep the header, per-story paragraphs, trend section, and links.

```markdown
# AI 资讯日报 · YYYY-MM-DD（周X）

> 来源：[鱼皮 AI 导航 · AI 资讯](https://ai.codefather.cn/news)　抓取时间：YYYY-MM-DD
>
> 说明：站点当前最新更新日为 X 月 X 日（如与今天不同，明确写出）。当日共 N 条资讯；其中……为同一事件的多来源报道，已合并，最终整理为 M 个独立主题。

## 一、大模型与技术前沿（N 条）

### 1. 标题

3–6 句详细摘要：发生了什么、关键数字/模型名/参与方、技术或商业机制、为什么重要。保留来源中的限定语（"官方称""据外媒报道"）。

- 原文：https://ai.codefather.cn/news/<id>

## 二、Agent 生态与云基础设施（N 条）

### 2. 标题
...

## 三、AI 产品与应用（N 条）

### 3. 标题
...

## 四、资本、企业与行业动态（N 条）

### 4. 标题
...

## 五、AI 安全、治理与社会（N 条）

### 5. 标题
...

## 六、趋势观察

1. **趋势名**：用 1–2 句连接当天多条新闻，说明共同方向，不重复摘要。
2. ...
3. ...
4. ...
5. ...

---

*整理：<agent> ｜ 数据抓取自 ai.codefather.cn/news ｜ YYYY-MM-DD*
```

## Section guidance

- **大模型与技术前沿** — new models, benchmarks, papers, training/inference techniques, formal verification, open-weight releases.
- **Agent 生态与云基础设施** — agent runtimes, standards, APIs, cloud hosting, developer infrastructure.
- **AI 产品与应用** — shipped products, creator tools, video/image/audio models, healthcare/legal/education deployments, app shutdowns.
- **资本、企业与行业动态** — funding, IPOs, M&A, org changes, policy/compliance, manufacturing and robotics strategy.
- **AI 安全、治理与社会** — security incidents, audits, copyright lawsuits, platform rules, public opinion, privacy.

## Style

- Chinese by default; switch to the user's language if they wrote in another language.
- Numbers, model names, company names, and dates must match the source.
- 3–6 sentences is the target for major stories; 2–3 is acceptable for minor ones. Never a bare headline list.
- Include "合并 N 篇" when multiple fetched articles cover the same event.
- Every story gets at least the site link. Add the original-source link when it helps verification.
