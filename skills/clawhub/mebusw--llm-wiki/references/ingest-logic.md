# llm_wiki 摄入流程详解

> 本文件记录两步摄入流程的提示词逻辑。供高级用户定制 schema.md 时参考，或在 claude.md 中补充工作流说明。
>
> **关键更新**：本版本加入了**领域识别**步骤（Step 1 末尾）和**领域更新**动作（Step 2 中）。任何摄入都必须先回答"这条资料属于哪个/哪些领域"，否则生成的页面会成为领域层的孤儿。

---

## 摄入两步流程

### Step 1：分析（Analysis）

系统提示词核心：
```
You are an expert research analyst. Read the source document and produce a structured analysis.

## Language Rule
- ALWAYS match the language of the source document.

Your analysis should cover:

## Key Entities
- Name and type
- Role in the source (central vs. peripheral)
- Whether it likely already exists in the wiki (check the index)

## Key Concepts
- Name and brief definition
- Why it matters in this source
- Whether it likely already exists in the wiki

## Main Arguments & Findings
- Core claims or results
- Evidence supporting them
- Strength of the evidence

## Connections to Existing Wiki
- What existing pages does this source relate to?
- Does it strengthen, challenge, or extend existing knowledge?

## Contradictions & Tensions
- Does anything in this source conflict with existing wiki content?
- Are there internal tensions or caveats?

## Recommendations
- What wiki pages should be created or updated?
- What should be emphasized vs. de-emphasized?
- Any open questions worth flagging?

## ★ Domain Identification (领域识别，**必填**)
For this source, identify:

### Primary Domain(s) — 该资料的核心主题
- One or more existing domains from `wiki/domains/_meta.json`
- Or a proposed NEW domain (give slug + description + why it doesn't fit any existing one)
- Be specific: prefer `nlp/transformers` over `ai` if the source is specifically about transformers

### Secondary Domain(s) — 跨领域关联
- Domains that the source touches tangentially
- Used for cross-domain navigation

### Sub-domain Candidates
- If any existing domain has > 20 pages (per `_meta.json`), suggest whether this content fits a sub-domain

### Domain Evolution Signals
- Does this source reveal a need to split an existing domain?
- Does it reveal a need to merge two existing domains?
- Does it reveal a missing area that needs a new domain?
```

### Step 2：生成（Generation）

系统提示词核心（关键约定）：

**文件块格式**（LLM 输出必须遵守）：
```
---FILE: path/to/filename.md---
(complete file content with YAML frontmatter)
---END FILE---
```

**必须生成的文件**（**按顺序**）：

1. **领域层更新**（如适用）：
   - `wiki/domains/{new-domain}.md` — 新领域索引页（仅当新领域）
   - `wiki/domains/_meta.json` — 注册新领域 / 追加 history
   - 现有领域索引页 `wiki/domains/{existing-domain}.md` — 追加新条目

2. **来源摘要页**：`wiki/sources/{source-basename}.md`（**frontmatter 必须含 `domains:`**）

3. **实体页**：`wiki/entities/` 下的关键实体（**frontmatter 必须含 `domains:`**）

4. **概念页**：`wiki/concepts/` 下的关键概念（**frontmatter 必须含 `domains:`**）

5. **其他类型页**：findings、methodology、characters 等场景专属目录（**frontmatter 必须含 `domains:`**）

6. **`wiki/index.md`**（**仅在领域有变动时**更新顶层领域列表；平常不动）

7. **`wiki/log.md`**（格式：`## [YYYY-MM-DD] ingest | Title`，逆序）

8. **`wiki/overview.md`**（2-5 段综述）

**Frontmatter 强制要求**：
- 每个内容页**必须**含 `domains: [...]` 字段（**关键创新**）
- 每个内容页**必须**含 `sources: ["原始文件名"]` 字段
- 使用 `[[wikilink]]` 语法跨页引用
- kebab-case 文件名
- 领域 slug 与 `wiki/domains/{domain}.md` 文件名严格一致

**领域更新规则**：

| 情况 | 动作 |
|------|------|
| 现有领域匹配 | 在该领域索引页追加新条目（按"概念 / 实体 / 来源"分组） |
| 全新领域 | **先**创建 `wiki/domains/{slug}.md` + 更新 `_meta.json` + 渲染 `index.md`，**再**写内容页 |
| 跨领域 | 在**所有**相关领域索引页追加该页（同一页面可出现在多个领域） |
| 父子领域 | 内容页 `domains: [parent, child]`，索引页之间通过 Related 互链 |

**审核块格式**（Review Items）：
```
---REVIEW: type | Title---
Description of what needs the user's attention.
OPTIONS: Create Page | Skip
PAGES: wiki/page1.md, wiki/page2.md
SEARCH: search query 1 | search query 2 | search query 3
---END REVIEW---
```

审核类型：
- `contradiction`：来源与现有 wiki 内容冲突
- `duplicate`：实体/概念可能已以不同名称存在于 wiki
- `missing-page`：重要概念被引用但没有专属页面
- `suggestion`：值得进一步研究的话题或关联来源
- `★ domain-evolution`：领域需要拆分/合并/重命名（新增）

---

## log.md 追加逻辑

`wiki/log.md` 是特殊文件——只追加，从不覆盖，**逆序排列**（最新条目在文件顶部）：

示例条目：
```
## [2026-06-01] ingest | Wei et al. 2022: Chain-of-Thought Prompting
新建 3 个页面、更新 5 个页面。归入领域 [[deep-learning]] 和 [[prompting-techniques]]。
新实体：[[wei]]；新概念：[[chain-of-thought]]。
矛盾：在 few-shot 表现上与 [[brown-2020-gpt3]] 不一致，已在 [[chain-of-thought]] 标注。

## [2026-05-30] lint | 拆分领域 ai
触发条件：ai 领域概念数 25 > 20。
动作：ai → [[ai-fundamentals]], [[deep-learning]], [[ai-applications]]
影响：23 个页面更新 domains 字段
```

---

## 摄入缓存机制

Wiki 系统内置摄入缓存：如果资料内容未变更，跳过重复摄入。
缓存基于文件内容哈希，存储已写入的 wiki 页面列表。

---

## 领域操作（Domain Operations）

以下操作仅在 LINT 中执行，**不要在 INGEST 时擅自做**。

### 创建领域

触发：摄入 Step 1 识别出"全新主题不属于任何现有领域"。

```
1. 在 wiki/domains/{slug}.md 创建索引页（参考 templates.md 中的领域索引页模板）
2. 在 wiki/domains/_meta.json 注册：
   {
     "date": "YYYY-MM-DD",
     "action": "create",
     "domain": "slug",
     "reason": "..."
   }
3. 重新渲染 wiki/index.md（仅顶层领域部分）
4. 在 wiki/log.md 追加 ingest 条目
```

### 重命名领域

触发：发现命名不一致 / 用户改名 / 同义词合并。

```
1. 修改 wiki/domains/{new-slug}.md（重命名文件 + 更新 title）
   - 把 old-slug 加入 aliases
2. 更新 _meta.json：
   { "date": "YYYY-MM-DD", "action": "rename", "from": "old-slug", "to": "new-slug", "reason": "..." }
3. 全局替换：所有内容页 frontmatter 的 domains 字段中 old-slug → new-slug
4. 重新渲染 wiki/index.md
5. wiki/log.md 追加 lint 条目
```

### 拆分领域

触发：领域下概念 > 20 且子主题清晰可分。

```
1. 与用户确认拆分方案（列出来源、目标领域、每个页面的新归属）
2. 创建子领域索引页：wiki/domains/{child-1}.md, {child-2}.md, ...
3. 父领域索引页：移除被拆走的页面，更新 children 字段
4. 被拆走的内容页：frontmatter 的 domains 字段更新
5. _meta.json：
   { "date": "YYYY-MM-DD", "action": "split", "from": "parent", "to": ["child-1", "child-2"], "reason": "概念数 > 20" }
6. 重新渲染 wiki/index.md
7. wiki/log.md 追加 lint 条目
```

### 合并领域

触发：多个领域共享 > 30% 内容 / 都 < 3 个且不再需要。

```
1. 与用户确认合并方案
2. 保留目标领域，源领域页面更新 domains 字段（删除源领域、加入目标领域）
3. 源领域：可保留为 alias 指向目标，或从 _meta.json 删除
4. _meta.json：
   { "date": "YYYY-MM-DD", "action": "merge", "from": "old-slug", "to": "new-slug", "reason": "..." }
5. 重新渲染 wiki/index.md
6. wiki/log.md 追加 lint 条目
```

---

## 语言规则（关键）

```typescript
export const LANGUAGE_RULE = "## Language Rule\n- ALWAYS match the language of the source document. If the source is in Chinese, write in Chinese. If in English, write in English. Wiki page titles, content, and descriptions should all be in the same language as the source material."
```

此规则在摄入分析和生成两步中都强制执行。在 schema.md 末尾加上此语言规则，可确保 LLM 一致遵守。

---

## 领域层与类型层的关系（理解整个系统）

```
                ┌─────────────────────────────────┐
                │      wiki/index.md              │  ← 顶层领域列表（不列页面）
                │      (5-20 entries)             │
                └─────────────────────────────────┘
                              ↓ 引用
                ┌─────────────────────────────────┐
                │   wiki/domains/{name}.md        │  ← 领域索引页（按类型分组列页面）
                │   + _meta.json（真实状态）      │
                └─────────────────────────────────┘
                              ↓ 包含
        ┌──────────────┬──────────────┬──────────────┐
        │  concepts/   │  entities/   │  sources/    │  ← 类型层（按内容形态分类）
        │  *.md        │  *.md        │  *.md        │
        │  domains:[]  │  domains:[]  │  domains:[]  │  ← 每个页面用 frontmatter 标注所属领域
        └──────────────┴──────────────┴──────────────┘
                              ↓ 引用
                ┌─────────────────────────────────┐
                │  raw/                           │  ← 原始资料（只读）
                └─────────────────────────────────┘
```

**核心原则**：一个页面在文件系统中的位置（哪个类型目录）由其**内容形态**决定；一个页面在领域索引中的出现（哪个领域）由其**主题**决定。两者正交，可独立变化。

**举例**：
- `wiki/concepts/transformer.md` 的 `domains: [deep-learning, nlp]`
  - 出现在 `wiki/domains/deep-learning.md` 的 "Concepts" 段
  - 出现在 `wiki/domains/nlp.md` 的 "Concepts" 段
  - 不出现在 `wiki/index.md`（只列领域）
- `wiki/sources/vaswani-2017.md` 的 `domains: [deep-learning]`
  - 出现在 `wiki/domains/deep-learning.md` 的 "Sources" 段
- `wiki/domains/deep-learning.md` 出现在 `wiki/index.md`（顶层领域）
