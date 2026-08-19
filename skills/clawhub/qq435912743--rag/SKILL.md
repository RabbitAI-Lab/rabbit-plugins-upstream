---
name: rag
description: 检索增强生成（Retrieval-Augmented Generation）。把本地文档建索引、按问题检索 top-k 相关分块并产出带引用的回答。支持离线抽取式与可选 LLM 生成式两种模式，纯 Python 无重依赖。当用户需要"基于自有资料问答""知识库检索""文档问答""RAG""让模型引用来源"时使用。
agent_created: true
visibility: public
---

# RAG · 检索增强生成

让 agent 在回答前先从**自有资料**中检索证据，并**标注引用来源**——这是逼近"可信、可溯源"一线大模型能力的关键一步。

## 何时用
- "基于我的笔记/文档回答…"、"从知识库里找…"、"这句话出自哪份文件？"
- 需要**可溯源**的回答（带 [n] 引用），而非模型凭记忆生成。
- 长文档问答、私有知识库问答、法规/论文/手册检索。

## 三步流程
1. **建索引**（一次性）：`python scripts/rag_index.py --docs <目录> --out <index.json>`
   - 递归扫描 .md/.txt/.json/.csv/.log，按滑动窗口分块，做 TF-IDF 向量化。
2. **检索**：`python scripts/rag_query.py --index <index.json> --question "..." --topk 5`
   - 返回 top-k 相关分块，含 `doc` 出处、`score`、引用片段。
3. **合成回答**：`python scripts/rag_synthesize.py --index <index.json> --question "..." --out answer.md`
   - **离线抽取式**（默认）：从命中分块抽取相关句子，拼成带 [n] 引用的结构化回答，无需任何外部服务。
   - **LLM 生成式**（可选）：设置环境变量 `OPENAI_API_KEY` + `OPENAI_BASE_URL` + `OPENAI_MODEL`，把检索上下文作为 evidence 注入 prompt，产出生成式回答（仍带 [n] 引用）。用标准库 urllib 调用，无第三方依赖。

## 设计要点
- `raglib.py` 提供分词 / TF-IDF / 余弦相似度的纯 Python 实现，离线可跑、可验证。
- 稠密向量（sentence-transformers / faiss）可作为升级路径：替换 `rag_index` 的向量化与 `rag_query` 的相似度即可，接口不变。
- 索引把向量单独存 `vectors` 字段，运行时合并，兼顾可读性与体积。

## 自进化
本技能内置 learner（`scripts/learner.py`）。每次检索/合成后调用：
`python scripts/learner.py record --skill rag --op "<操作>" --result success|fail --detail "<说明>"`
循环据此复盘检索质量、调参（chunk 大小、topk、是否启用 LLM）。
