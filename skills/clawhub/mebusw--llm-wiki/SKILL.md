---
name: llm-wiki-admin
compatibility:
  required_skills:
    - /obsidian
    - /markitdown
description: 管理 Karpathy LLM-Wiki 理念知识库，四大操作包括：初始化项目、摄入新原始资料（编译为 wiki 页面）、回答基于 wiki 的查询、执行健康检查（lint）。当用户想要初始化知识库、ingest/摄入新文章或笔记、从 wiki 查询知识、维护 wiki 健康、或提到 llm-wiki / llm_wiki / schema.md / 第二大脑 / Karpathy wiki / Obsidian wiki / 知识编译 时，必须使用此技能。即使用户只说"帮我把这篇文章加进 wiki"或"wiki 里有关于 X 的内容吗"，也要触发此技能。
---

# LLM-Wiki 知识库管理员

## 核心理念

> **不是 RAG，是编译。** RAG 每次查询都重新推导；Wiki 把知识编译一次，持续复利积累。原始资料是真相来源，LLM 负责编译——摘要、交叉引用、标注矛盾、综合洞见。用户负责提供资料和提问，LLM 负责其余一切。

### 三层 + 领域双轴架构

```
raw/                ← 原始资料（只读，永不修改）
wiki/               ← LLM 编写并维护的知识页面
  ├─ domains/       ← 领域索引层（主题导航，解决 index 膨胀）★
  ├─ concepts/      ← 类型层（内容形态分类）
  ├─ entities/
  ├─ sources/
  ├─ ...
  ├─ index.md       ← 只列顶层领域，永不膨胀
  ├─ log.md
  └─ overview.md
schema.md           ← Wiki 结构规则（页面类型、格式、命名、工作流）
purpose.md          ← 项目目标与范围（LLM 的"北极星"）
```

**关键创新：领域层（domains/）**

> 原版 LLM Wiki 的核心问题：`index.md` 是所有页面的扁平列表，页面一多就爆炸。
> 领域层把"按类型找页面"变成"按主题找领域，再在领域内找页面"——
> `wiki/index.md` 永远只有 5–20 个顶层领域条目；每个领域自己的索引页可以很大但局部可控；
> 领域可以随内容增长**自动演化**（拆分 / 合并 / 重命名），且每次演化都在 `_meta.json` 留下足迹。

`schema.md` + `purpose.md` 是系统的"宪法"——让 LLM 从通用助手变为专业领域知识管理员。

---

## 四种操作模式

根据用户意图，进入对应模式：

| 用户说 | 进入模式 |
|--------|---------|
| 初始化 / 新建 wiki / 配置项目 | → **[INIT] 初始化** |
| 摄入 / ingest / 把这个加进 wiki / 读这篇文章 | → **[INGEST] 摄入** |
| wiki 里有没有 / 查一下 / 问题 | → **[QUERY] 查询** |
| 健康检查 / lint / 孤立页面 / 检查 wiki | → **[LINT] 健康检查** |

意图不明确时，直接问："你是想把新资料加进 wiki，还是查询现有 wiki 中的内容？"

> **所有 4 种操作都必须维护领域层**：INIT 时创建初始领域并写 `_meta.json`；INGEST 时识别/创建领域；QUERY 时按领域导航；LINT 时检查领域健康并建议演化。

---

## [INIT] 初始化

用于首次建立知识库项目。

### Step 1：访谈（一次问卷）

向用户提出以下问题（一次发出，不要逐条等待）：

```
初始化你的 LLM Wiki，请回答以下几个问题：

1. 使用场景（选一个）：
   A 🔬 研究调研   B 📚 阅读积累   C 🌱 个人成长   D 💼 商业/团队   E 📄 通用

2. 主题领域：（自由填写，可写多个，逗号分隔）

3. 主要资料类型（可多选）：
   论文 / 书籍 / 网文 / 笔记 / 会议记录 / 其他

4. 写作语言：
   A 跟随资料语言   B 统一中文   C 统一英文
```

收到用户回复后，继续 Step 2。如果用户只回答了部分，用合理默认值补全（场景默认 E 通用，语言默认跟随资料）。

### Step 2：生成配置文件

**必须先读取** `references/templates.md`，获取对应场景的模板（含 `_meta.json` 领域元数据模板），然后：
1. 用主题领域替换模板占位符
2. 根据语言偏好调整语言规则说明
3. 把主题领域转换为初始领域列表（见下方"场景 → 初始领域映射"）
4. 生成以下文件：

| 文件 | 说明 |
|------|------|
| `schema.md` | Wiki 结构规则（项目根目录）|
| `purpose.md` | 项目目标与范围（项目根目录）|
| `wiki/index.md` | 顶层领域列表（LLM 维护，永不直接列页面）|
| `wiki/log.md` | 操作日志，只追加不覆盖 |
| `wiki/overview.md` | 知识库总览（初始为待填模板）|
| `wiki/domains/_meta.json` | 领域注册表 + 演化历史 |
| `wiki/domains/{domain}.md` | 每个初始领域一个索引页 |
| `CLAUDE.md` | 供 Claude Code 默认的提示文件，内容固定为 `read purpose.md, schema.md, and wiki/domains/_meta.json` |

> **路径约定**：`schema.md` 和 `purpose.md` 在项目**根目录**（与 `wiki/` 同级），这是标准的三层架构约定。

**场景 → 初始领域映射**（仅作为种子，领域会随内容演化）：

| 场景 | 初始领域示例（可由用户改写） | 场景专属类型子目录 |
|------|---------------------------|-----------------|
| research | `domain: 主题领域` | methodology, findings, thesis |
| reading | `domain: 书名/题材`, `domain: 主题领域` | characters, themes, plot-threads, chapters |
| personal | `domain: 生活领域1`, `domain: 生活领域2` | goals, habits, reflections, journal |
| business | `domain: 业务领域1`, `domain: 业务领域2` | meetings, decisions, projects, stakeholders |
| general | 用户填写的"主题领域" | （无） |

**关键原则**：场景专属类型子目录（methodology / characters / meetings 等）**仅用于内容形态分类**，不与领域层冲突。每个内容页面**必须**在 frontmatter 用 `domains: [...]` 标注所属领域，无论它物理上放在哪个类型子目录。

### Step 3：写入 Obsidian

使用 `/obsidian` skill 将所有文件写入用户的 Obsidian Vault。如用户未指定路径，询问："Wiki 项目根目录在 Vault 中的位置？"

> **前置条件**：`/obsidian` skill 必须已安装，这是本技能的硬依赖。

### Step 4：完成确认

告知用户：已生成的文件列表、初始领域列表、下一步操作：把第一批资料放入 `raw/` 后开始 Ingest。

---

## [INGEST] 摄入新资料

将新原始资料"编译"为 wiki 页面。这是最重要的操作。

### 摄入前（告知用户）

**不要直接开始写文件。** 先简短告诉用户你发现了什么：
- 核心实体、主要论点、与现有 wiki 的关联
- **该资料所属领域**（已有则列出；新领域则提议创建）
- 哪些现有页面会被更新，哪些需要新建
- 是否发现矛盾

然后再写文件。若资料很长，提议分段处理。

### 摄入步骤

1. **读取** 原始资料全文。
   - 纯文本格式（MD/HTML/CSV/JSON/XML）直接读取。
   - 遇到PDF/PPTX/WORD/EXCEL等格式，可调用`/markitdown`将其解析成md文件，并以独特且可追踪的文件名保存在`/raw`目录下，如解析出图片等媒体文件，则以相关联的文件名存到`/raw/assets`下，并链接到解析后的md文件中。
2. **读取** `wiki/index.md` 和 `wiki/domains/_meta.json`，了解现有领域结构
3. **读取** `schema.md`，获取本项目的页面类型和格式规范
4. **识别资料所属领域**：
   - 已有领域匹配 → 归入现有领域
   - 属于现有领域的子主题 → 检查是否需要新建子领域
   - 全新主题 → **先**创建 `wiki/domains/{new-domain}.md` 索引页 + 更新 `_meta.json`，**再**写内容页
5. **识别** 资料中的实体、概念、案例、来源
6. **判断** 每个概念：
   - 已有对应 Wiki 页面 → 追加或更新内容（**不覆盖，整合**）
   - 尚无对应页面 → 新建页面
7. **必须保留**：所有数字、百分比、时间盒数值、案例细节、原始故事线、贡献者原话
8. **强制 frontmatter 字段**：
   - `domains: [domain1, domain2]`（必填，**所有内容页**）
   - `tags: [...]`、`created`、`updated`（必填）
9. **添加** 双向 `[[Wikilink]]`：在每个页面正文末尾用 `## Related` section 列出关联页面，**不放在 YAML frontmatter**（Obsidian 不支持 frontmatter 中的 wikilink）
10. **更新对应领域索引页** `wiki/domains/{domain}.md`：追加新条目，按"概念 / 实体 / 来源"分组列出
11. **矛盾处理**：不同来源有冲突时，在页面内注明两种说法及来源，用 `> ⚠️ 矛盾：...` 标记，**不擅自裁决**
12. **更新** `wiki/index.md`（**仅当新建/删除/重命名领域时**，平常不动）
13. **更新** `wiki/domains/_meta.json`（**仅当领域有演化时**，记录 action / date / from / to）
14. **追加** `wiki/log.md`（格式：`## [YYYY-MM-DD] ingest | 来源标题`，**逆序**：最新条目插入文件顶部）
15. **更新** `wiki/overview.md`（2-5 段综述，反映最新状态）

### 摄入后（汇报用户）

"已更新 4 个页面，新建 2 个：`xxx.md`、`yyy.md`。归入领域 `[[domain-a]]` 和 `[[domain-b]]`。发现 1 处矛盾，已在 `zzz.md` 标注。"

### 必须遵守

- **绝对禁止**修改 `raw/` 目录中的任何文件
- 一次摄入通常涉及 5–15 个 wiki 页面，不要跳过交叉引用
- 若发现矛盾，停下来展示两个版本，再继续
- **所有新建内容页必须在 frontmatter 标注 `domains`**，否则 LINT 会报警

---

## [QUERY] 查询

基于 wiki 回答用户问题。**领域层是 QUERY 的主要导航手段**。

### 查询步骤

1. **读取** `wiki/index.md`，定位问题涉及的**领域**（不要直接读所有页面）
2. **读取** 涉及的领域索引页 `wiki/domains/{domain}.md`，找到该领域内的相关概念/实体/来源
3. **读取** 2-5 个最相关的 wiki 页面（**不是**重新翻查原始资料）
4. 如需原始细节，再查对应 `raw/` 来源
5. 回答时引用**原始数据**和**案例**，使用 `(→ [[page-name]])` 内联引注，并注明所属领域 `(→ 领域: [[domain]] )`
6. 追加到 `wiki/log.md`（格式：`## [YYYY-MM-DD] query | 问题摘要`）

### 询问是否保存

回答结束后，询问："要把这个分析保存为 wiki 页面吗？好的洞见不应消失在对话历史里。"
若用户同意，**必须**询问新页面应归入哪个领域（已在领域列表则用现有；否则新建）。

---

## [LINT] 健康检查

定期扫描 wiki 健康状态。**领域健康是 LINT 的核心检查项**。

### 检查项

| 检查项 | 说明 |
|--------|------|
| 孤立页面 | 没有任何入链的页面 |
| 缺失页面 | 被 `[[Wikilink]]` 引用但尚不存在的页面 |
| 矛盾内容 | 不同页面对同一概念描述相互冲突 |
| 未索引页面 | 在 `wiki/` 存在但未出现在 `wiki/index.md` 或对应领域索引页的页面 |
| 缺失 frontmatter | 页面缺少必要字段（**特别是 `domains`**） |
| 过时内容 | `status: outdated` 的页面未被更新 |
| **领域健康**（核心）| 见下方独立章节 |

### 领域健康检查（domain health）

LINT **必须**执行以下领域层检查，并在报告中独立列出：

| 检查 | 触发条件 | 建议操作 |
|------|---------|---------|
| 领域过载 | 任一领域下内容 > 20 个 | 建议**拆分**为更细的子领域 |
| 领域重叠 | 多个领域共享 > 30% 内容 | 建议**合并** |
| 领域过空 | 领域下内容 < 3 个且长期无新增 | 建议**合并**到父领域或**删除** |
| 命名不一致 | 同一概念在不同领域有不同别名 | 建议**重命名** + 在 `_meta.json` 记录 |
| 孤立领域 | 在 `index.md` 列出但无任何内容 | 建议**移除**或激活 |
| 缺失领域索引页 | `_meta.json` 登记但 `domains/{name}.md` 不存在 | 建议**创建** |
| 跨领域引用断裂 | A 领域页面大量引用 B 领域内容但 B 不知道 A | 建议在 B 领域索引页添加"来自 A 的相关条目" |

### 领域演化操作

发现需要演化时，**不要擅自执行**——先列出建议，等用户确认。每次演化都必须：

1. 在领域索引页和 `_meta.json` 中同步改动
2. **重命名**：保留旧名作为 `aliases: [...]`，在 `_meta.json` 追加：
   ```json
   {"date": "YYYY-MM-DD", "action": "rename", "from": "old-name", "to": "new-name"}
   ```
3. **拆分**：父领域保留，子领域新建 `wiki/domains/{child}.md` + `_meta.json` 注册；被拆走的页面更新 `domains:` 字段；写入：
   ```json
   {"date": "YYYY-MM-DD", "action": "split", "from": "parent", "to": "child1, child2"}
   ```
4. **合并**：保留目标领域，源领域内容页更新 `domains:` 字段；写入：
   ```json
   {"date": "YYYY-MM-DD", "action": "merge", "from": "old", "to": "new"}
   ```

### Lint 原则

展示所有发现，**再问用户是否处理**，不擅自批量修改。结果追加到 `wiki/log.md`，标记为 `[Lint]`。

---

## 领域管理参考

### 什么是领域

领域（Domain）是知识的**主题**分类，与"内容类型"（概念/实体/来源）正交：
- 同一概念可属于多个领域（`domains: [deep-learning, nlp]`）
- 同一领域可包含多种类型（概念 + 实体 + 来源混合）
- 领域可以有父子关系（`deep-learning` → `transformers`）

### 领域页面格式

```yaml
---
title: 深度学习
type: domain
parent: machine-learning          # 顶层领域留空或 null
children: [transformers, cnns]    # 子领域
aliases: [DL, deep-learning]
description: 神经网络与表示学习
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# 深度学习

> 简要描述本领域。

## Concepts
- [[transformer]] — 自注意力序列模型
- [[cnn]] — 卷积神经网络

## Entities
- [[openai]] — 主要研究机构
- [[ilya-sutskever]] — 关键人物

## Sources
- [[vaswani-2017-attention]] — 奠基论文

## Synthesis
- [[frontier-models-2024]] — 跨领域综述

## Related
- 父领域: [[machine-learning]]
- 兄弟领域: [[nlp]], [[computer-vision]]
```

### `_meta.json` 完整模板

```json
{
  "version": 1,
  "domains": {
    "deep-learning": {
      "parent": "machine-learning",
      "description": "神经网络与表示学习",
      "created": "YYYY-MM-DD",
      "updated": "YYYY-MM-DD"
    }
  },
  "history": [
    {"date": "YYYY-MM-DD", "action": "create", "domain": "deep-learning", "reason": "INIT 初始领域"}
  ]
}
```

### 领域演化触发阈值

| 操作 | 触发条件 | 备注 |
|------|---------|------|
| 拆分 | 概念 > 20 | 父子关系清晰才拆；否则先重命名 |
| 合并 | 重叠 > 30% 或都 < 3 个 | 合并后保留更通用的名字 |
| 重命名 | 同义词 ≥ 2 个 | 用最通用名，旧的作 aliases |
| 嵌套 | 子主题独立 | 父子关系能提升导航效率 |

### 为什么领域能根治 index 膨胀

- 1000 个页面 = 20 个领域（平均 50 页/领域）
- `wiki/index.md` 仍是 20 行，领域索引页各 50 行
- 浏览器加载只需 `index.md` + 1 个领域索引
- 增长：领域数增长很慢（数月一个），内容页增长很快

---

## 内容原则

### 必须保留

- 所有百分比、数字、时间盒数值
- 真实案例的完整故事线
- 实践中的具体对话片段和金句
- 贡献者的原始表达方式

### 绝对禁止

- 修改 `raw/` 目录的任何文件
- 删除或简化原始案例数据
- 未标注来源地合并不同来源的说法
- 静默覆盖矛盾——矛盾是比干净页面更有价值的信号
- **新建内容页而不写 `domains` 字段**——会导致孤立页面和导航失效

---

## 参考文件

- `references/templates.md` — 五种场景的完整 schema + purpose + `_meta.json` 原始模板（INIT 时必读）
- `references/ingest-logic.md` — 摄入两步流程详解（高级定制参考）
