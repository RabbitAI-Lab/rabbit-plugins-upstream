# Wiki 编译参考

> 索引页：所有 references/ 文档的导航。从这里跳转到各专题详情。

## 📚 文档索引

| 文档 | 适用阶段 | 说明 |
|------|---------|------|
| [folder-organization.md](folder-organization.md) | 阶段 0 | 知识库结构诊断 + 多层文件夹归类 |
| [tagging.md](tagging.md) | 阶段 4-6 | 标签设计 + 应用 + 审查 |
| [security.md](security.md) | 全流程 | 破坏性操作保护（删除、重命名、移动）|
| [api-reference.md](api-reference.md) | 全流程 | IMA OpenAPI 端点 + 错误码 + 通用函数 |
| [guide-template.md](guide-template.md) | 阶段 4 | 主题导览笔记的 4 章节结构 + 写作规范 |
| [versioning.md](versioning.md) | 阶段 2 | 主题导览笔记的版本控制 |
| [incremental-update.md](incremental-update.md) | 阶段 4 | 增量更新 6 步法 |
| [link-handling.md](link-handling.md) | 阶段 3 | 链接特性预获取 + 链接策略 |
| [write-and-verify.md](write-and-verify.md) | 阶段 5 | 写入笔记 + 验证流程 |
| [maintenance.md](maintenance.md) | 阶段 6 | 健康检查 + 知识补充 + 标签审查 |
| [troubleshooting.md](troubleshooting.md) | 全流程 | 常见错误 + 解决方案 |
| [cases/quantitative-investing.md](cases/quantitative-investing.md) | 案例 | 量化投资知识库试跑经验 |

## 🎯 核心概念速查

### 传统 RAG vs Wiki 编译

| 特性 | Wiki 编译（本技能） | 传统 RAG |
|------|-------------------|----------|
| 核心 | 知识编译，生成结构化文档 | 信息检索，查找相关片段 |
| 存储 | 知识库文件夹 + 文档 | 向量数据库 |
| 检索 | LLM 基于文档结构"内生理解" | 基于向量相似度的外部检索 |
| 知识积累 | 产出可回流，系统持续演化 | 每次问答相对独立 |
| 可追溯性 | 强，答案可定位到具体文档 | 弱，依赖检索片段 |
| 适用规模 | 中等规模（数百篇） | 海量规模（企业级） |

### 文件夹设计模式

详见 [folder-organization.md](folder-organization.md) 第 0.6 节。

**模式 A：扁平**（推荐用于中等规模）

```
知识库根
├── 文件夹 1
├── 文件夹 2
└── 文件夹 3
```

**模式 B：2 层嵌套**（推荐用于复杂领域）

```
知识库根
├── 文件夹 1
├── 文件夹 2（复杂主题）
│   ├── 子文件夹 A
│   ├── 子文件夹 B
│   └── 子文件夹 C
└── 文件夹 3
```

### 标签与文件夹的协同

详见 [folder-organization.md](folder-organization.md) 第 0.7 节和 [tagging.md](tagging.md)。

| 维度 | 文件夹 | 标签 |
|------|:---:|:---:|
| 主导维度 | 主题分类 | 多维关联 |
| 结构 | 树状（一文件一父）| 网状（一文件多标签）|
| 人类友好 | 高（导览）| 低（API）|
| 机器友好 | 低 | 高 |

**核心原则**：
- 职责不重叠：文件夹负责"内容组织"，标签负责"维度标记"
- 互为补充：标签给文件夹扩展维度，文件夹给标签赋予语义
- 低耦合：任一失效，另一方仍可独立工作
- 演化同步：增量更新时联动，但不强依赖

## 🚀 快速跳转

- 不知道从哪开始？→ 看 SKILL.md 的"快速开始"章节
- 遇到错误？→ [troubleshooting.md](troubleshooting.md)
- 不知道 API 怎么调用？→ [api-reference.md](api-reference.md)
- 担心破坏性操作？→ [security.md](security.md)
- 想看实际案例？→ [cases/quantitative-investing.md](cases/quantitative-investing.md)
