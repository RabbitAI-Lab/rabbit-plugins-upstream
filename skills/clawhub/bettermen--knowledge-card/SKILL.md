---
name: knowledge-card
version: 1.0.0
description: Generate high-density knowledge cards in Kindle e-reader paper style. Pure HTML + Tailwind CDN, zero dependencies. Supports three auto-adaptive layouts: process flow, comparison framework, and concept insight. Triggers on: knowledge card, 知识卡片, 知识卡片, kindle card, 铸卡, 知识图卡, 图形卡片.
description_zh: 生成 Kindle 纸书风格高密度知识卡片。纯 HTML + Tailwind CDN，零依赖。支持三种自动适配布局：流程步骤型、对比框架型、单概念洞见型。触发词：知识卡片、生成卡片、kindle卡片、铸卡、知识图卡、图形卡片。
user-invocable: true
argument-hint: 粘贴知识素材文本，或描述你想要制作卡片的知识观点
---

# 知识卡片生成器 (Kindle 纸书风格)

你是一位知识可视化设计师。你的任务是将用户提供的知识素材转化为高密度 Kindle 纸书风格知识卡片。

## 核心原则

1. **内容决定形式** — 不锁死模板，根据内容类型自动适配布局
2. **单文件输出** — 只生成 `index.html`，不留中间文件
3. **零依赖运行** — 纯 HTML + Tailwind CDN，浏览器直接打开
4. **固定配色** — Kindle 纸书暖色体系，不可修改

## 配色系统（锁定，不可修改）

```
外背景   #e8e0d5
卡片底色  #f5f0eb
Header   #3c3a37
强调色   #b8a088
分割线   #e0d5c8

摘要文字  #3c3a37
正文字   #7a7062
辅助文字  #8a8072
Footer   #b0a898

Header标题 #f0ebe4
Header英文 #a09888
Header编号 #8a8072
认知组灰底 #ede6dc
```

## 输入识别

- **主题/观点描述** → 提取为 cardData，生成一张卡片
- **已有结构化数据**（JSON/YAML）→ 直接填充模板
- **要求批量生成** → 依次生成多张独立卡片（每张一个 HTML）

## 处理流程

### 第一步：分析素材，判断内容类型

阅读用户素材，判断属于哪种内容类型：

| 内容特征 | body_type | 布局 |
|---------|-----------|------|
| 有步骤/阶段/方法论 | `process` | 摘要 + 机制 + 行动 1234 |
| 有对比/多维分析/框架 | `compare` | 摘要 + 机制 + 分区对比 |
| 单一洞见/概念/名言 | `concept` | 摘要 + 展开 + 行动 1-2 项 |

### 第二步：提取 cardData

从素材中提取以下结构化数据：

```json
{
  "tag": "英文大写标签",
  "number": "3位数字",
  "title": "≤8个汉字",
  "subtitle": "英文全大写副标题",
  "summary": "一句话概要（1-2句）",
  "mechanism": "机制解释（可选，2-4句）",
  "body_type": "process | compare | concept",
  "actions": [
    { "step": "①", "title": "简短标题", "desc": "详细描述" }
  ],
  "groups": [
    { "label": "英文", "badge": "中文标签", "title": "标题", "desc": "描述", "color": "red|yellow|green|blue|purple" }
  ],
  "quote": "金句（可选）",
  "author": "署名"
}
```

**字段约束：**
- `tag`：COGNITION / WEALTH / GROWTH / STRATEGY / CREATIVITY / LEADERSHIP / SCIENCE / PHILOSOPHY
- `number`：3 位数字，如 "001"
- `title`：不超过 8 个汉字
- `subtitle`：英文全大写，简洁有力
- `actions`：流程型必有 1-4 项，单概念型 1-2 项
- `groups`：对比型必有 2-5 项，每项设 color
- `quote`：可选，有则用斜体呈现

### 第三步：选择布局，组装 HTML

根据 `body_type` 选择布局，读取 [卡片 HTML 模板](references/card-template.html) 进行填充：

**流程型 (process) body_content：**
```html
<div class="action-group">
  <div class="action-title">◈ {自定义行动组标题}</div>
  <div class="action-list">
    <div class="action-item">
      <span class="action-step">①</span>
      <div class="action-content">
        <div class="action-name">{行动标题}</div>
        <div class="action-desc">{行动描述}</div>
      </div>
    </div>
    <!-- ... 重复 1-4 项 -->
  </div>
</div>
```

**对比型 (compare) body_content：**
```html
<div class="compare-groups">
  <div class="compare-group {color}">
    <div class="group-label">{英文标签}</div>
    <span class="group-badge">{中文标签}</span>
    <div class="group-title">{标题}</div>
    <div class="group-desc">{描述}</div>
  </div>
  <!-- ... 重复 2-5 项 -->
</div>
```

**单概念型 (concept) body_content：**
如果 actions 有值，使用流程型结构（1-2项）；否则留空，仅摘要+机制+金句即可。

**机制区块（可选）：**
```html
<div class="mechanism-block">
  <p class="mechanism-text">{机制文字}</p>
</div>
```

**金句区块（可选）：**
```html
<div class="quote-block">
  <p class="quote-text">{金句文字}</p>
</div>
```

### 第四步：写出 index.html

1. 读取 [模板文件](references/card-template.html) 的完整内容
2. 将 `{{PLACEHOLDER}}` 替换为实际数据
3. 写出到用户工作目录的 `index.html`
4. 不要修改配色 CSS、不要改布局结构

**替换规则：**
- `{{TAG}}` → tag 值
- `{{NUMBER}}` → number 值（3 位补零）
- `{{TITLE}}` → title 值
- `{{SUBTITLE}}` → subtitle 值
- `{{SUMMARY}}` → summary 值
- `{{MECHANISM_BLOCK}}` → 机制 HTML（无则留空）
- `{{BODY_CONTENT}}` → 执行组或对比分区 HTML
- `{{QUOTE_BLOCK}}` → 金句 HTML（无则留空）
- `{{AUTHOR}}` → author 值

### 第五步：浏览器预览

写完 index.html 后，自动在浏览器中预览。

## 质量检查

生成后逐项验证：
- [ ] 配色是否完全符合 Kindle 暖色体系（未修改任何颜色值）
- [ ] 布局层级是否正确（Header → Body(认知组 → 执行组/对比) → Footer）
- [ ] 内容是否精炼（title ≤ 8 汉字，summary 1-2 句，actions 语义清晰）
- [ ] 是否只生成了单个 index.html（无中间文件）
- [ ] 浏览器预览是否正常

## 禁区

- ❌ 不修改配色系统的任何颜色
- ❌ 不修改布局层级结构
- ❌ 不生成中间文件（如 JSON、草稿 HTML 等）
- ❌ 不嵌入其他格式（表格、图表、iframe）
- ❌ 不使用非 Kindle 暖色体系外的颜色
