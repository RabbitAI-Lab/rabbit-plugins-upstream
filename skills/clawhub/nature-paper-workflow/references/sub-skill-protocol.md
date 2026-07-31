# 子 skill 调用协议

> 配套主 skill: [SKILL.md](../SKILL.md)

## 调用流程

### 1. 读取子 skill SKILL.md

```
读取 ~/.claude/skills/<sub-skill>/SKILL.md
```

### 2. 按子 skill 路由协议执行

让子 skill 的 SKILL.md 主导执行。**不要从 router 凭记忆执行**。

### 3. 双层架构处理

如果子 skill 也是 static/dynamic 双层架构（如 nature-reader / nature-writing / nature-polishing），继续读取：

1. 子 skill 的 `manifest.yaml` 检测任务类型
2. 按 axis 加载 `static/` 下的对应片段
3. **不要一次性读全部片段**——按需加载节省 token

## 双层架构子 skill

| Skill | 加载策略 |
|---|---|
| nature-reader | 按 source_format (pdf-text/scanned-pdf/html/doi-arxiv/pasted-text) |
| nature-writing | 按 task/paper_type/section/language/journal |
| nature-polishing | 按 paper_type/section/language/journal |
| nature-figure | 按 backend (Python/R) 或 OpenRouter AI 路线 |
| nature-paper2ppt | 按 paper_type (discovery/methods) |
| nature-citation | 按操作模式 |
| nature-response | 按任务类型 |

## 调用示例

### 示例 1: 读论文（Phase 0a）

```
User: 我有一篇 PDF 想读
Router: 📍 Phase 0a - 读论文
        🎯 路由到：nature-reader
[读取 ~/.claude/skills/nature-reader/SKILL.md]
[按 source_format=pdf-text 加载 static/ 片段]
[执行 reader 流程]
Router: ✅ 完成
        👉 下一步：Phase 0b 文献调研，或 Phase 1a 项目初始化
```

### 示例 2: 起草（Phase 2a）

```
User: 帮我写引言
Router: 📍 Phase 2a - 章节起草
        🎯 路由到：nature-writing
[读取 ~/.claude/skills/nature-writing/SKILL.md]
[按 task=drafting, section=introduction 加载 static/ 片段]
[执行写作流程]
Router: ✅ 完成
        👉 下一步：Phase 2b 结构优化，或 Phase 3a 图规划
```
