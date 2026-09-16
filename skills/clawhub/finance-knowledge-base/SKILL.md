---
name: Financial Industry Knowledge Base Manager
slug: finance-knowledge-base
description: AI-powered financial industry knowledge base manager — covers document organization, knowledge graph construction, semantic search, and intelligent Q&A. Built for financial institutions' internal knowledge management. Keywords: knowledge management, knowledge base, document management, semantic search, RAG, 知识库, 知识管理, 文档管理, 语义搜索, RAG, 知识图谱, 智能问答, 文档检索, 内部知识库, 企业知识管理.
version: 5.0.3

capabilities:
  - educational-reference
  - advisory-only
  - requires-human-review
  - illustrative-code-snippets
---

# Financial Industry Knowledge Base Manager / 金融行业知识库

> **⚠️ SECURITY NOTICE / 安全声明**
> - **Type:** Educational reference / analytical framework ONLY
> - **Code snippets in this document are illustrative reference material** — they show a
>   structure you can adapt in your own environment. Nothing here is executed, and no
>   scripts, binaries, or installers are bundled.
> - **No persistent storage, network calls, background execution, or credential collection**
> - **All outputs are for reference only and require human review before real-world application**
> - **This skill does NOT provide financial, legal, or insurance advice**
> - **Users must exercise their own judgment and consult qualified professionals**

> **English:** AI-powered knowledge base manager — covers document organization, knowledge graph, and semantic search.
>
> **中文:** 知识库管理器——覆盖文档组织、知识图谱、语义搜索、版本治理与智能问答。

---

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | 量化基线（示例口径） | Solution / 本Skill解决方案 |
|------------------|-------------|-------------------|------------------------|
| **知识分散** | 文档散落各处，难找 | 平均查找一份制度耗时 10–20 分钟 | 统一知识库管理 |
| **知识孤岛** | 部门间知识不共享 | 同一问题在三处重复起草 | 跨部门知识共享与唯一来源 |
| **更新滞后** | 制度更新后知识未同步 | 新旧版本并存，误用旧口径 | 知识版本管理与失效标记 |
| **检索不准** | 关键词搜索效果差 | 关键词命中但答非所问 | 语义搜索 + 重排 |
| **口径不一** | 同一指标多种解释 | 同一报表出现 2 套口径 | 指标口径登记与唯一来源 |
| **无人负责** | 知识无人维护 | 文档平均两年未复核 | 责任人 + 复核周期 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** knowledge management, knowledge base, document management, semantic search, RAG, knowledge graph

**中文触发词（优先）：** 知识库 / 知识管理 / 文档管理 / 语义搜索 / 知识图谱 / RAG / 文档检索 / 知识治理 / 口径登记 / 制度归档 / 内部知识库

> 触发边界：本技能面向**金融机构内部知识管理**场景（制度、产品、流程、口径类知识）。
> 通用笔记整理、个人待办、日程安排等不属于本技能范围。

---

## Core Capabilities / 核心能力

### 1. Document Organization / 文档组织

```python
# 示例：知识分类骨架（供参考，可按机构实际调整）
KNOWLEDGE_STRUCTURE = {
    "regulations": {
        "banking": ["监管法规", "合规要求", "检查清单"],
        "insurance": ["监管法规", "产品规则", "偿付能力"],
        "securities": ["证监会规则", "交易所规则", "自律规则"]
    },
    "products": {
        "banking": ["存款产品", "贷款产品", "理财", "信用卡"],
        "insurance": ["寿险", "财险", "健康险", "团险"],
        "securities": ["股票", "债券", "基金", "期权"]
    },
    "processes": {
        "操作规程": ["受理", "审批", "复核", "归档"],
        "风险控制": ["识别", "计量", "监测", "报告"],
        "客户服务": ["咨询", "办理", "投诉", "回访"]
    },
    "metrics": {
        "口径登记": ["指标名", "计算公式", "数据来源", "责任人"]
    }
}
```

**知识分层与责任人对照表**

| 层级 | 内容示例 | 更新频率 | 责任人 | 未更新后果 |
|-----|---------|---------|-------|-----------|
| 一级：监管依据 | 法律、部门规章、监管通知 | 随发布更新 | 合规条线 | 合规风险 |
| 二级：内部制度 | 管理办法、操作规程 | 按修订 | 制度牵头部门 | 执行口径混乱 |
| 三级：业务知识 | 产品说明、话术要点 | 按产品变更 | 业务条线 | 对外表述不一致 |
| 四级：口径与指标 | 指标定义、取数规则 | 按季度复核 | 数据条线 | 报表口径打架 |
| 五级：经验沉淀 | 案例、常见问题 | 持续补充 | 各条线 | 重复踩坑 |

**命名与归档规范（示例）**

| 要素 | 规范 | 反例 |
|-----|------|------|
| 文件命名 | `类型-主题-版本-生效日期` | "最新版终版2.docx" |
| 版本标识 | 与制度正式版本号一致 | 用日期代替版本号 |
| 生效日期 | 必填，与发布批次对应 | 留空或写"即日" |
| 失效标记 | 旧版本显式标注"已失效" | 旧新版本并存不区分 |

---

### 2. Knowledge Graph Construction / 知识图谱构建

**实体与关系示例**

| 实体类型 | 示例 | 关键属性 |
|---------|------|---------|
| 制度 | 某业务管理办法 | 版本、生效日期、责任部门 |
| 产品 | 某净值型产品 | 风险等级、适当性要求 |
| 角色 | 客户经理 | 职责、审批权限 |
| 指标 | 某项比率 | 公式、数据来源、口径 |
| 事件 | 监管检查 | 时间、结论、整改要求 |

| 关系类型 | 示例 | 用途 |
|---------|------|------|
| 依据关系 | 内部制度 → 依据 → 监管规定 | 追溯合规来源 |
| 适用关系 | 制度 → 适用 → 产品 | 判断某项业务受哪些约束 |
| 责任关系 | 流程节点 → 责任 → 角色 | 明确到人 |
| 版本关系 | 新版本 → 替代 → 旧版本 | 避免误用旧口径 |
| 关联关系 | 指标 → 引用 → 报表 | 口径变更影响面分析 |

**图谱构建四步**

| 步骤 | 动作 | 交付要点 |
|-----|------|---------|
| 1 定实体 | 确定要管住的几类核心对象 | 类型不超过 6 类，避免过度建模 |
| 2 定关系 | 只建"会用于判断"的关系 | 每个关系都要能回答一个实际问题 |
| 3 挂来源 | 每个实体标注出处与版本 | 无出处的实体不入库 |
| 4 设复核 | 按层级设定复核周期 | 到期未复核自动降权提示 |

---

### 3. Semantic Search & RAG / 语义搜索与检索增强

```python
class KnowledgeBaseSearch:
    """知识库语义搜索（结构示意）"""

    def semantic_search(self, query: str, top_k: int = 5) -> dict:
        # 1. 查询向量化
        query_vector = embed_text(query)

        # 2. 向量相似度召回
        results = vector_search(query_vector, top_k)

        # 3. 重排（按相关性、版本有效性、权威层级）
        reranked = rerank(query, results)

        # 4. 组织答案（必须带出处与版本）
        context = "\n".join([r["content"] for r in reranked])
        answer = compose_answer(query, context)

        return {"answer": answer, "sources": reranked}
```

**分块策略对照表**

| 分块方式 | 适用内容 | 优点 | 风险 |
|---------|---------|------|------|
| 按条款 | 监管规定、制度条文 | 引用精确 | 条款过短时上下文不足 |
| 按章节 | 操作规程、产品说明 | 上下文完整 | 检索定位较粗 |
| 按表格 | 指标、费率、限额 | 数据完整 | 需保留表头 |
| 按问答对 | 常见问题、客服知识 | 命中率高 | 覆盖面依赖积累 |

**检索效果评估表**

| 指标 | 含义 | 测法示例 | 目标方向 |
|-----|------|---------|---------|
| 召回率 | 该找到的是否都找到 | 用已标注问题集测 | 越高越好 |
| 精确率 | 返回的是否都相关 | 人工判定前 K 条 | 越高越好 |
| 引用正确率 | 出处与版本是否对得上 | 抽查答案引用 | 应接近 100% |
| 失效内容拦截率 | 旧版本是否被拦住 | 构造已失效问题 | 应接近 100% |
| 拒答率 | 无依据时是否明确说"没有依据" | 构造超范围问题 | 应有明确拒答 |

> **原则：宁可说"未找到依据"，也不要生成一个看起来合理的答案。** 金融知识库的错误代价远高于"没答上"。

---

### 4. Version & Lifecycle Governance / 版本与生命周期治理

**知识生命周期五阶段**

| 阶段 | 关键动作 | 留痕要求 |
|-----|---------|---------|
| 入库 | 校验出处、版本、生效日期 | 记录来源与审核人 |
| 生效 | 标记生效日期，旧版转"已失效" | 记录替代关系 |
| 使用 | 检索时优先返回有效版本 | 保留检索与引用记录 |
| 复核 | 按周期确认仍适用 | 记录复核结论 |
| 归档 | 失效知识可查不可默认引用 | 保留完整版本链 |

**版本冲突处理表**

| 冲突情形 | 判断原则 | 处理动作 |
|---------|---------|---------|
| 新旧制度并存 | 以生效日期晚者为准 | 旧版标失效并说明被谁替代 |
| 上位与下位规定不一致 | 以上位规定为准 | 触发下位文件修订 |
| 同一指标两套口径 | 以口径登记为准 | 修订未登记方并统一 |
| 部门口径与全行口径不同 | 以全行口径为准 | 部门口径改为备注说明 |

---

### 5. Intelligent Q&A / 智能问答与质量校验

**答案组织要求**

| 要素 | 要求 | 说明 |
|-----|------|------|
| 结论 | 先给结论 | 一句话回答"是什么/能不能" |
| 依据 | 附制度名称与条款 | 便于人工复核 |
| 版本 | 标注版本与生效日期 | 防止旧口径误用 |
| 边界 | 说明不适用的情形 | 避免过度外推 |
| 提示 | 超出知识库范围时明确拒答 | 不臆测 |

**问答质量抽检表**

| 抽检项 | 合格标准 | 处理方式 |
|-------|---------|---------|
| 依据真实存在 | 引用可定位到原文 | 不实引用立即下线 |
| 版本为有效版本 | 非已失效文件 | 更新检索权重 |
| 结论与依据一致 | 无跳跃推论 | 补中间依据或改为拒答 |
| 敏感数据合规 | 无客户身份信息 | 按数据规范处理 |
| 边界说明充分 | 写明例外情形 | 补写适用范围 |

---

## 知识库治理检查清单 / Governance Checklist

| 检查项 | 通过标准 |
|-------|---------|
| 唯一来源 | 每类知识只有一个权威存放位置 |
| 责任人明确 | 每一层知识都有指定责任人 |
| 版本可追溯 | 能查到任一文件的完整版本链 |
| 失效可识别 | 已失效内容在检索结果中被明确标注 |
| 口径有登记 | 指标类知识统一登记公式与来源 |
| 出处可定位 | 每条知识都能追溯到原始文件 |
| 复核有周期 | 按层级设定复核频率并有到期提醒机制 |
| 权限有边界 | 按岗位设定可见范围 |

---

## 数据使用与安全纪律 / Data Discipline

| 项目 | 要求 |
|-----|------|
| 数据最小化 | 只处理完成当前任务所必需的内容 |
| 去标识化 | 涉及客户信息时先做去标识处理 |
| 权限最小化 | 按岗位授予可见范围，不做超额开放 |
| 访问留痕 | 保留检索与引用记录以备审计 |
| 外部共享 | 未经审批不将内部知识对外提供 |
| 敏感内容 | 涉及客户身份、账户信息的内容不纳入通用知识库 |

---

## Quick Command Templates / 快速指令模板

**整理一批制度文件：**
```
帮我把以下制度文件按知识分层归类，输出：
1. 所属层级与责任人建议
2. 命名规范化后的名称
3. 需要标记失效的旧版本
文件清单：[文件列表]
```

**建立指标口径登记：**
```
整理以下指标的口径登记表，字段包括：
指标名 / 计算公式 / 数据来源 / 责任部门 / 复核周期
指标清单：[指标列表]
```

**评估检索效果：**
```
针对以下问题集合，评估知识库检索效果，
输出召回情况、引用正确性、是否存在失效内容被引用：
问题集合：[问题列表]
```

**核查知识时效：**
```
核查以下知识条目的时效性，
标出已超出复核周期或已被替代的条目：
知识条目：[条目列表]
```

---

## 监管与行业动态 / Regulatory Watch（截至 2026-09-15）

| 动态类型 | 内容摘要 | 对知识库的影响 | 建议动作 | 优先级 |
|---------|---------|--------------|---------|-------|
| 数据治理 | 金融数据分级分类与数据治理要求持续深化 | 知识库需区分数据敏感级别 | 按敏感级别设定可见范围 | 高 |
| 个人信息保护 | 个人信息处理需遵循最小必要原则 | 含客户信息的文档不得进入通用库 | 建立入库存前检查 | 高 |
| 生成式AI治理 | 生成合成内容需可识别、可追溯 | AI 生成的问答内容需标注来源 | 答案强制附出处与版本 | 高 |
| 知识溯源 | 内部制度与监管依据需可追溯 | 需维护制度—监管依据映射 | 建立依据关系登记 | 中 |
| 版本管理 | 制度修订频繁，旧版本误用风险上升 | 需强制失效标记 | 检索结果标失效并降权 | 中 |
| 权限管理 | 岗位权限与信息可见范围需匹配 | 知识库需按岗位授权 | 定期核对权限清单 | 中 |
| 留痕与审计 | 关键操作需可回溯 | 检索与引用记录需保留 | 明确留存范围与期限 | 中 |

> **数据截止**: 2026-09-15 | 来源：监管公开信息与行业实践整理
> **声明**: 以上动态供参考，具体以官方最新发布为准。

---

## Disclaimer

This skill provides knowledge management frameworks and illustrative reference material for
educational purposes. It does not execute code, does not access external systems, and does not
constitute financial, legal, or compliance advice. All classifications, mappings, and answers
produced with its help must be reviewed by the responsible business and compliance functions
before being used in production.
