# llm-wiki

> 把 LLM 变成你的专属知识库管理员——不是问答，是编译。具备四种基本的操作模型，化繁为简，完全覆盖个人和企业的知识管理需要。

基于 [Andrej Karpathy 的 LLM Wiki 理念](https://x.com/karpathy/status/1793562750870294638)构建的 Claude Skill。让 LLM 把你读过的一切编译成持久增长的结构化知识库，而不是每次查询都从零推导。

**v2 核心升级**：引入**领域层（Domain Layer）**架构——借鉴自 [dragonfly-llmwiki](https://github.com/lchrennew/dragonfly-llmwiki/blob/master/AGENTS.md) 的领域索引系统。**根治 `index.md` 膨胀**：无论内容页增长到多少，根索引始终只列 5–20 个顶层领域；同时领域可**自动演化**（拆分 / 合并 / 重命名）以适应内容增长。

---

## 核心理念

**RAG vs Wiki 的本质区别：**

| | RAG | LLM Wiki |
|---|---|---|
| 工作方式 | 每次查询重新检索推导 | 编译一次，持续积累 |
| 知识状态 | 无状态 | 有状态，持续复利 |
| 矛盾处理 | 静默混合 | 显式标注，保留两方 |
| 交叉引用 | 无 | 自动维护 wikilink |
| **可扩展性** | 受限于检索窗口 | **领域层** 拆解，永不膨胀 |

原始资料是不可变的真相来源，LLM 负责编译——摘要、交叉引用、标注矛盾、综合洞见。你负责提供资料和提问，LLM 负责其余一切。

---

## 目录结构（领域层 + 类型层）

```
your-wiki-project/
├── schema.md           ← Wiki 结构规则（LLM 的"宪法"）
├── purpose.md          ← 项目目标与范围
├── raw/                ← 原始资料（只读，永不修改）
│   ├── article1.md
│   ├── notes.pdf
│   └── assets/         ← 解析出的图片等附件
└── wiki/               ← LLM 编写并维护的知识页面
    ├── index.md        ← ★ 只列顶层领域（5-20 行，永不膨胀）
    ├── log.md
    ├── overview.md
    ├── domains/        ← ★ 领域层（核心创新）
    │   ├── _meta.json  ←   领域注册表 + 演化历史
    │   ├── deep-learning.md   ←   领域索引页
    │   ├── software-engineering.md
    │   └── ...
    ├── concepts/       ← 类型层（按内容形态分类）
    ├── entities/
    ├── sources/
    ├── comparisons/
    ├── synthesis/
    └── [场景专属类型]  ← methodology / characters / meetings / goals 等
```

### 双层索引原理

```
wiki/index.md (5-20 领域)        ← 永远轻量
  ↓ 引用
wiki/domains/{name}.md (N 页)   ← 局部大但局部可控
  ↓ 包含（按 type 分组）
wiki/concepts/, entities/, ...  ← 内容页
  ↓ frontmatter: domains: [name]
```

**为什么这样能"支持比原文更多的数据量"**：

| 页面总数 | 领域数 | `index.md` 大小 | 单个领域索引页大小 |
|---------|-------|----------------|------------------|
| 100 | 5 | 5 行 | ~20 行 |
| 1000 | 20 | 20 行 | ~50 行 |
| 10000 | 50 | 50 行 | ~200 行 |

领域数增长很慢（可能数月一个），内容页增长很快——`index.md` 永远人类可读。

---

## 四种操作模式

### 🏗️ INIT — 初始化

首次建立知识库。回答几个问题后，自动生成：
- `schema.md`、`purpose.md`、`wiki/index.md`、`wiki/log.md`、`wiki/overview.md`
- **`wiki/domains/_meta.json`**（领域注册表）
- **`wiki/domains/{domain}.md`**（每个初始领域一个索引页）

支持五种预设场景，各有专属子目录结构和推荐初始领域：

| 场景 | 适用 | 类型专属目录 | 推荐初始领域 |
|------|------|------------|------------|
| 🔬 研究调研 | 论文、田野调查 | methodology / findings / thesis | 主题 + `methodology` + `open-questions` |
| 📚 阅读积累 | 读书笔记、书评 | characters / themes / chapters | 书名 + `themes` + `characters` |
| 🌱 个人成长 | 习惯、目标、反思 | goals / habits / reflections | 1-3 个生活领域 + `self-knowledge` |
| 💼 商业/团队 | 会议、决策、项目 | meetings / decisions / projects | 业务领域 + `operations` |
| 📄 通用 | 什么都行 | — | 1-N 个主题领域 |

### 📥 INGEST — 摄入

把新资料"编译"进 wiki。**领域识别是必填项**：

1. **Step 1 分析**：识别资料所属领域（已有 / 新建 / 跨领域）
2. 先告知用户将更新哪些页面、哪些领域，是否发现矛盾
3. 必要时**先**创建领域索引页 + 更新 `_meta.json`，**再**写内容页
4. 新建或整合 wiki 页面（不覆盖，整合）
5. **强制 frontmatter 字段 `domains:`** —— 所有内容页都必须有
6. 在所属领域索引页追加新条目
7. 保留原始数字、百分比、故事线、贡献者原话
8. 维护双向 `[[Wikilink]]`
9. 汇报变更摘要（含"归入领域 X、Y"）

一次摄入通常涉及 5–15 个 wiki 页面。

### 🔍 QUERY — 查询

基于 wiki 回答问题。**领域导航是 QUERY 的主要手段**：

1. 读 `wiki/index.md` 找到相关**领域**
2. 读对应 `wiki/domains/{name}.md` 找到领域内相关页面
3. 读 2-5 个最相关页面作答，引用原始数据和案例
4. 标注引用所属领域

好的分析可选择保存为新 wiki 页面（必须询问归入哪个领域）。

### 🩺 LINT — 健康检查

扫描 wiki 健康状态。**领域健康是核心检查项**：

- 孤立页面（无入链）
- 缺失页面（被引用但不存在）
- 矛盾内容
- 未索引页面
- 缺失 frontmatter（特别是 `domains` 字段）

**领域健康**：
- 领域过载（>20 内容）→ 建议**拆分**
- 领域重叠（>30% 共享）→ 建议**合并**
- 领域过空（<3 内容长期无新增）→ 建议**合并**或删除
- 命名不一致 → 建议**重命名**
- 孤立领域 / 缺失索引页 → 建议创建

所有发现先展示，用户确认后再处理。每次领域演化都在 `_meta.json` 的 `history` 留下足迹。

---

## 安装

**前置依赖：** `/obsidian` skill（用于写入 Obsidian Vault）

### Claude.ai / ClawhHub

1. 下载 `llm-wiki.skill`
2. 在 Claude.ai 设置 → Skills 中安装
3. 确保已安装 `/obsidian` skill
4. 对话中说"初始化我的 wiki"即可开始

### 手动安装

```
your-skills/
└── llm-wiki/
    ├── SKILL.md
    └── references/
        ├── templates.md
        └── ingest-logic.md
```

---

## 使用示例

```
用户：帮我初始化一个研究调研 wiki，主题是"大语言模型推理能力"

Claude：好的，请回答以下几个问题：
        1. 使用场景：A 研究调研 ✓
        2. 主题领域：大语言模型推理能力
        ...

用户：把这篇论文加进 wiki → [附上 paper.pdf]

Claude：读完了，发现以下内容：
        - 资料所属领域：[[deep-learning]]（已存在）、[[reasoning]]（新领域，需要创建）
        - 新实体：Chain-of-Thought（需新建页面）
        - 更新页面：scaling-laws.md（有新数据）
        - ⚠️ 矛盾：与 wei-2022 在 few-shot 结论上不一致
        确认后开始写入？

用户：wiki 里关于 few-shot 的内容有哪些？

Claude：根据 [[deep-learning]] 领域索引，相关的概念/实体有 12 个……
        （引用原始数据作答）
        要把这个分析保存为 wiki 页面吗？归入哪个领域？

用户：帮我做一次 lint

Claude：发现以下问题：
        1. 领域 ai 概念数 25 > 20，建议拆分为 ai-fundamentals / deep-learning / ai-applications
        2. 页面 xxx.md 缺少 domains 字段
        3. 3 个孤立页面
        逐项确认后处理？
```

---

## 设计原则

- **原始资料永不修改**：`raw/` 是只读的真相来源
- **矛盾优于干净**：发现冲突就标注，不擅自裁决
- **编译前先告知**：摄入前汇报计划，摄入后汇报变更
- **Obsidian 兼容**：wikilink 只在正文 `## Related` section 中使用，不放 YAML frontmatter
- **语言跟随资料**：中文资料生成中文页面，英文资料生成英文页面
- **领域层是导航骨架**：所有内容页必须有 `domains:`，所有领域变动都要写 `_meta.json.history`
- **领域可演化**：拆分/合并/重命名是 LINT 的一部分，必要时让 wiki 自己重组

---

## 文件说明

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 主体，定义四种操作模式 + 领域管理 |
| `references/templates.md` | 五种场景的 schema + purpose + `_meta.json` 完整模板 + 领域层规范 |
| `references/ingest-logic.md` | 摄入两步流程（分析→生成）+ 领域识别 + 领域演化操作 |

---

## 致谢

- 理念来源：[Andrej Karpathy — "LLMs as a new kind of memory"](https://x.com/karpathy/status/1793562750870294638)
- 领域层架构灵感：[dragonfly-llmwiki](https://github.com/lchrennew/dragonfly-llmwiki/blob/master/AGENTS.md)
