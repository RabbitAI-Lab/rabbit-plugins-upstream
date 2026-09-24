# 触发词编写清单 / Trigger Writing Guide

本文件是「触发词优化」的静态替代方案（无 CLI 环境也适用）。用它来打磨 SKILL.md 的 `description` 字段——这是模型决定「要不要用这个 skill」的唯一依据。

## 为什么 description 是唯一触发依据 / Why description is the only trigger

模型只有在「判断这个 skill 能帮上忙」时才会加载它。判断依据是 frontmatter 里的 `name` + `description`，其中 `description` 起决定作用。正文写得再好，description 写得差，skill 就永远不会被触发。

## 核心原则：反「欠触发」/ Fight undertriggering

模型有个通病：**该用 skill 的时候不用**（欠触发）。因为它会高估自己「直接做也能做好」。所以 description 要写得「主动一点」（pushy），主动声明适用范围，而不是只写一句干巴巴的功能名。

对比 / Compare:

- ❌ 差：「How to build a dashboard to display data.」
- ✅ 好：「How to build a simple fast dashboard to display internal data. Use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display company data — even if they don't explicitly say 'dashboard.'」

关键差异：好的 description 不只说「做什么」，还穷举「用户在什么情境下、说什么话」就该用。

## description 四要素 / Four required elements

| 要素 | 说明 | 必须 |
|---|---|---|
| 做什么 | 一句话说清核心任务 | ✅ |
| 何时用 | 具体触发情境、用户说法 | ✅ |
| 关键能力 | 提供什么独特价值 | ✅ |
| 触发短语 | 用户真实会说的原话 | ✅ |

## 触发词挖掘步骤 / How to mine trigger phrases

1. 收集 3—5 句用户真实会说的原话（保留口语、省略、错别字，不「美化」）。
2. 提炼触发短语，别用只有制作者知道的专业词替代用户的话。
3. 补充「用户没点名领域词、但实际需要这个 skill」的说法。
4. 收集 2—3 句关键词相近、但**不该触发**的 near-miss。
5. 把上述内容写进 description。

**完成标准**：不点名 skill 名称、不点名领域术语时，目标场景仍能触发；相近但不同的任务不误触发。

## 反例（near-miss）怎么用 / How to use near-misses

near-miss 的价值在「收窄边界」。举例：一个「PDF 转 Word」的 skill，near-miss 是「帮我生成一份 PDF」——都有 PDF 关键词，但后者是「生成」不是「转换」，不该触发。把这些边界写进 description 或正文开头，能显著降低误触发。

## 快速自查清单 / Quick checklist

- [ ] description 含「做什么 + 何时用 + 关键能力 + 触发短语」四要素
- [ ] 用了 3—5 句用户真实原话，不是专业术语
- [ ] 明确写了「即使用户没明说，也优先考虑用我」这类主动声明
- [ ] 标注了 2—3 条 near-miss 边界，防止误触发
- [ ] description 长度 20—1024 字符

## 触发测试怎么做 / How to test triggering

1. 写 2—3 条正例（用户原话）+ 1—2 条 near-miss。
2. 用独立对话逐条测试，看 skill 是否被触发。
3. 正例全触发、near-miss 全不触发 = 通过。
4. 正例漏触发 → 补 description 里的真实说法；near-miss 误触发 → 收窄边界。
5. 无法观察 skill 是否加载时，记录「未验证」，不得宣称通过。
