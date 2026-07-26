# Memory Schema — 三层记忆格式规范

## L1 — 短期记忆格式

L1 存在于对话上下文中，无需持久化文件。Agent 在内部维护以下结构：

```
[L1-001] 任务: 用户要求生成PDF报告
[L1-002] 约束: 必须包含图表，A4横版
[L1-003] 进度: 已完成数据收集，正在生成图表
[L1-004] 反馈: 用户要求字体改为微软雅黑
[L1-005] 工具: reportlab v3.6, 已导入所需模块
```

**字段说明**：

| 字段 | 必填 | 说明 |
|------|------|------|
| 任务 | 是 | 当前任务的一句话描述 |
| 约束 | 否 | 用户指定的限制条件 |
| 进度 | 是 | 当前执行到哪一步 |
| 反馈 | 否 | 用户的修正/偏好指示 |
| 工具 | 否 | 正在使用的工具/库/参数 |
| 假设 | 否 | 尚未验证的推断 |

**压缩标记**：被压缩的条目标记为 `[L1-COMPRESSED]`，保留摘要：
```
[L1-COMPRESSED] 数据收集阶段已完成（3次工具调用），结论：数据源A可用，B超时
```

---

## L2 — 中期记忆格式 {#l2-mid-term-format}

存储位置：`memory/YYYY-MM-DD.md`

### 任务摘要模板

```markdown
## Session: {任务标题}

- **日期**: YYYY-MM-DD
- **触发**: 用户请求 / 定时任务 / 子任务
- **目标**: 一句话描述任务目标
- **关键步骤**:
  1. 步骤一简述
  2. 步骤二简述
  3. 步骤三简述
- **结果**: 成功 / 部分完成 / 失败
- **教训**: 值得记住的经验（如有）
- **后续**: 待跟进事项（如有）
```

### 观察记录模板

```markdown
## 观察: {观察主题}

- **日期**: YYYY-MM-DD
- **类型**: 用户偏好 / 工作模式 / 技术发现
- **内容**: 具体观察
- **置信度**: 高(多次验证) / 中(2次) / 低(首次)
```

### 文件命名与组织

```
memory/
├── 2026-07-01.md    # 按日期组织
├── 2026-06-30.md
├── 2026-06-29.md
└── lessons/          # 从L2晋升的专题经验
    ├── pdf-generation.md
    └── api-integration.md
```

---

## L3 — 长期记忆格式 {#l3-long-term-format}

存储位置：`MEMORY.md`（核心） + `memory/lessons/`（专题）

### 经验教训条目

```markdown
## 规则: {规则化表述}

- **来源**: [失败复盘] YYYY-MM-DD / 用户明确要求
- **错误类型**: [TAG]
- **场景**: 触发条件
- **规则**: 应该/不应该做什么
- **置信度**: ★★★☆☆ (3/5)
- **引用次数**: 0
- **最后验证**: YYYY-MM-DD
```

### 技术决策条目

```markdown
## 决策: {决策标题}

- **日期**: YYYY-MM-DD
- **选择**: 最终方案
- **备选**: 被否决的方案
- **理由**: 为什么选这个
- **前提**: 在什么条件下成立
```

### 用户画像条目

```markdown
## 偏好: {偏好类别}

- **内容**: 具体偏好描述
- **强度**: 强(明确说过) / 中(多次表现) / 弱(推测)
- **适用范围**: 全局 / 特定项目 / 特定工具
```

---

## 记忆操作协议

### 写入协议

```
写入L1: 直接在上下文中维护，无文件操作
写入L2: memory_mh0us7(action="add", target="daily", content=..., title=...)
写入L3: memory_mh0us7(action="add", target="memory", content=...)
```

### 检索协议

```
语义搜索: memory_search_c4dib4(query=关键词, maxResults=6)
精确读取: memory_get_d3arce(path="MEMORY.md")
日期查询: memory_get_d3arce(path="memory/YYYY-MM-DD.md")
```

### 更新协议

```
替换条目: memory_mh0us7(action="replace", target="memory", old_text=..., content=...)
删除条目: memory_mh0us7(action="remove", target="memory", old_text=...)
```

### 优先级标记（Pro）

在条目末尾添加优先级标记：
```
优先级: ★★★ (critical) — 压缩时永不删除
优先级: ★★☆ (normal) — 常规压缩策略
优先级: ★☆☆ (low) — 优先压缩/归档
```

---

## 记忆导出格式（Pro）

### JSON 导出

```json
{
  "exportDate": "2026-07-01T10:00:00+08:00",
  "version": "1.0",
  "layers": {
    "L2_midTerm": [
      {
        "date": "2026-07-01",
        "title": "PDF报告生成",
        "goal": "...",
        "steps": ["...", "..."],
        "result": "success",
        "lesson": "..."
      }
    ],
    "L3_permanent": {
      "rules": [
        {
          "id": "rule-001",
          "rule": "生成PDF时必须嵌入字体文件",
          "source": "2026-06-28 失败复盘",
          "errorType": "FORMAT",
          "confidence": 5,
          "useCount": 3
        }
      ],
      "decisions": [...],
      "preferences": [...]
    }
  }
}
```

### Markdown 导出

按层级分节导出，保持与 MEMORY.md 相同的格式，便于人工审阅和迁移。

---

## 容量管理参考

| 层级 | 目标容量 | 硬上限 | 压缩触发 |
|------|----------|--------|----------|
| L1 | ~2K tokens | ~4K tokens | > 15条 或 > 4K |
| L2（单日） | ~4K tokens | ~8K tokens | > 30天未检索 |
| L3（MEMORY.md） | ~6K tokens | ~10K tokens | > 8K tokens |
| L3（lessons/） | 无硬上限 | 单文件 ~5K | 按需整理 |
