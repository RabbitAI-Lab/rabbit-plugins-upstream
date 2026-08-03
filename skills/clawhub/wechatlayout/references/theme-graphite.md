# 公众号排版主题：石墨灰（Graphite）

> 极简留白、呼吸感强、文字承重。适合设计/科技评论/专业观点/高端品牌。
> 几乎不用彩色，全部依靠灰阶层次。整体气质：编辑部内刊、专业杂志、设计周刊。

---

## 一、设计变量速查表

| 变量 | 色值 | 用途 |
|------|------|------|
| 主色 | `#374151` | 章节编号、少量锚点 |
| 主色浅 | `#6b7280` | 辅助强调、引用文字 |
| 浅底色 | `#f9fafb` | 卡片底色（极少用） |
| 浅边框 | `#f3f4f6` | 极细边框、表格行线 |
| 高亮色 | `#f3f4f6` | 灰底高亮（不用彩色） |
| 高亮渐变终色 | `#e5e7eb` | 荧光笔渐变终色 |
| 标题色 | `#111827` | 标题、加粗文字 |
| 正文色 | `#4b5563` | 正文段落 |
| 辅助文字色 | `#9ca3af` | 日期、署名、说明 |
| 分割线色 | `#e5e7eb` | 分割线 |
| 下划线色 | `#9ca3af` | 关键词下划线 |
| 深底白字背景 | `#1f2937` | 深色引用底 |

---

## 二、各组件完整 HTML

### 1. 全局容器

```html
<section style="max-width:677px;margin:0 auto;padding:0 16px;">
<!-- 所有内容组件放在此 section 内 -->
</section>
```

### 2. 封面/标题区

```html
<section style="margin:40px 0 36px;text-align:center;">
<p style="margin:0 0 14px;line-height:1.6;font-size:13px;color:#9ca3af;letter-spacing:2px;"><span leaf="">栏目名称</span></p>
<p style="margin:0;line-height:1.5;font-size:26px;font-weight:bold;color:#111827;letter-spacing:1px;"><span leaf="">文章标题</span></p>
<p style="margin:18px 0 0;line-height:1.6;font-size:14px;color:#9ca3af;"><span leaf="">2026.01.07 · 副标题或一句导读</span></p>
</section>
```

### 3. 引言卡

```html
<section style="margin:28px 0;padding:28px 24px;background:#f9fafb;border-radius:6px;">
<p style="margin:0;line-height:1.9;font-size:15px;color:#4b5563;letter-spacing:0.5px;"><span leaf="">这里是开头引言或导读内容，用克制的浅灰底卡片承托，营造呼吸感。</span></p>
<section style="margin:16px 0 0;text-align:right;">
<p style="margin:0;line-height:1.6;font-size:13px;color:#9ca3af;"><span leaf="">—— 署名或来源</span></p>
</section>
</section>
```

### 4. 目录导读

```html
<section style="margin:36px 0;">
<section style="margin:0 0 18px;">
<p style="margin:0;line-height:1.6;font-size:13px;color:#9ca3af;letter-spacing:1px;"><span leaf="">导读</span></p>
</section>
<section style="margin:0 0 16px;display:flex;align-items:baseline;">
<p style="margin:0 12px 0 0;line-height:1;font-size:22px;color:#d1d5db;font-weight:bold;"><span leaf="">01</span></p>
<p style="margin:0;line-height:1.6;font-size:15px;color:#374151;"><span leaf="">第一个核心看点标题</span></p>
</section>
<section style="margin:0 0 16px;display:flex;align-items:baseline;">
<p style="margin:0 12px 0 0;line-height:1;font-size:22px;color:#d1d5db;font-weight:bold;"><span leaf="">02</span></p>
<p style="margin:0;line-height:1.6;font-size:15px;color:#374151;"><span leaf="">第二个核心看点标题</span></p>
</section>
<section style="margin:0;display:flex;align-items:baseline;">
<p style="margin:0 12px 0 0;line-height:1;font-size:22px;color:#d1d5db;font-weight:bold;"><span leaf="">03</span></p>
<p style="margin:0;line-height:1.6;font-size:15px;color:#374151;"><span leaf="">第三个核心看点标题</span></p>
</section>
</section>
```

### 5. 章节标题

```html
<section style="margin:48px 0 20px;">
<p style="margin:0 0 6px;line-height:1;font-size:30px;color:#d1d5db;font-weight:bold;letter-spacing:2px;"><span leaf="">01</span></p>
<p style="margin:0;line-height:1.4;font-size:20px;font-weight:bold;color:#111827;letter-spacing:0.5px;"><span leaf="">章节标题</span></p>
</section>
```

### 6. 子标题

```html
<section style="margin:32px 0 12px;">
<p style="margin:0;line-height:1.5;font-size:17px;font-weight:bold;color:#111827;"><span leaf="">子标题文字</span></p>
</section>
```

### 7. 正文段落

```html
<p style="margin:0 0 22px;line-height:1.9;font-size:16px;color:#4b5563;letter-spacing:0.3px;"><span leaf="">这是标准正文段落。行距宽裕，呼吸感强，文字承重。每个段落之间保持充足留白，让阅读节奏舒缓而不紧迫。</span></p>
```

### 8. 关键词下划线

```html
<span leaf="" style="border-bottom:2px solid #9ca3af;padding-bottom:1px;">关键词</span>
```

### 9. 加粗标记

```html
<span leaf="" style="color:#111827;font-weight:bold;">加粗文字</span>
```

### 10. 高亮标记

```html
<span leaf="" style="background:#f3f4f6;color:#374151;padding:2px 4px;border-radius:3px;">高亮文字</span>
```

### 11. 荧光笔

```html
<span leaf="" style="background:linear-gradient(180deg,transparent 55%,#e5e7eb 55%);padding:0 2px;">荧光标记</span>
```

### 12. 引用块

```html
<section style="margin:28px 0;padding:10px 0 10px 20px;border-left:3px solid #374151;">
<p style="margin:0;line-height:1.9;font-size:15px;color:#6b7280;font-style:italic;"><span leaf="">这是一段极简引用文字，左竖条用深灰色，文字用辅助灰，保持克制。</span></p>
</section>
```

### 13. 数据卡

```html
<section style="margin:36px 0;text-align:center;padding:28px 20px;background:#f9fafb;border-radius:6px;">
<p style="margin:0;line-height:1;font-size:38px;font-weight:bold;color:#111827;letter-spacing:1px;"><span leaf="">98%</span></p>
<p style="margin:14px 0 0;line-height:1.6;font-size:14px;color:#9ca3af;"><span leaf="">数据说明文字</span></p>
</section>
```

### 14. 表格

```html
<section style="margin:28px 0;">
<section style="display:flex;padding:12px 16px;background:#f9fafb;border-bottom:1px solid #e5e7eb;">
<p style="margin:0;flex:1;line-height:1.5;font-size:14px;font-weight:bold;color:#374151;"><span leaf="">列标题 A</span></p>
<p style="margin:0;flex:1;line-height:1.5;font-size:14px;font-weight:bold;color:#374151;"><span leaf="">列标题 B</span></p>
</section>
<section style="display:flex;padding:12px 16px;border-bottom:1px solid #f3f4f6;">
<p style="margin:0;flex:1;line-height:1.5;font-size:14px;color:#4b5563;"><span leaf="">内容 A1</span></p>
<p style="margin:0;flex:1;line-height:1.5;font-size:14px;color:#4b5563;"><span leaf="">内容 B1</span></p>
</section>
<section style="display:flex;padding:12px 16px;">
<p style="margin:0;flex:1;line-height:1.5;font-size:14px;color:#4b5563;"><span leaf="">内容 A2</span></p>
<p style="margin:0;flex:1;line-height:1.5;font-size:14px;color:#4b5563;"><span leaf="">内容 B2</span></p>
</section>
</section>
```

### 15. 分割线

```html
<section style="margin:44px auto;width:40px;border-top:1px solid #e5e7eb;"></section>
```

### 16. 作者签名区/CTA

```html
<section style="margin:48px 0 0;padding:32px 0 0;border-top:1px solid #f3f4f6;text-align:center;">
<p style="margin:0 0 8px;line-height:1.6;font-size:14px;color:#9ca3af;"><span leaf="">作者：{{作者名}}</span></p>
<p style="margin:0;line-height:1.6;font-size:13px;color:#9ca3af;"><span leaf="">关注获取更多深度内容</span></p>
</section>
```

### 17. 产品徽章

```html
<section style="display:inline-block;padding:3px 10px;background:#f3f4f6;border-radius:3px;">
<p style="margin:0;line-height:1.5;font-size:12px;color:#6b7280;font-weight:bold;letter-spacing:0.5px;"><span leaf="">产品名称</span></p>
</section>
```

---

## 三、完整文章模板骨架

```
全局容器
├─ 封面/标题区
├─ 引言卡
├─ 目录导读
├─ 章节标题 01
│   ├─ 子标题
│   ├─ 正文段落 ×N（含关键词下划线/加粗/高亮标记）
│   ├─ 引用块（按需）
│   ├─ 数据卡（按需）
│   └─ 分割线（按需）
├─ 章节标题 02 + …（同上）
├─ 章节标题 03 + …（同上）
├─ 分割线
└─ 作者签名区/CTA
```

---

## 四、文章类型 → 组件组合配方表

| 文章类型 | 核心组件组合 |
|---------|-------------|
| 设计/科技评论 | 封面标题区 → 引言卡 → 章节标题 → 正文段落 + 关键词下划线 → 引用块 → 作者签名区 |
| 专业观点/深度分析 | 封面标题区 → 目录导读 → 章节标题 → 正文段落 + 加粗标记 → 数据卡 → 引用块 → 作者签名区 |
| 禅意/极简随笔 | 封面标题区 → 引言卡 → 章节标题 → 正文段落 → 分割线 → 引用块 → 作者签名区 |
| 高端品牌/案例复盘 | 封面标题区 → 目录导读 → 章节标题 → 正文段落 + 产品徽章 → 数据卡 → 表格 → 作者签名区 |

---

## 五、Markdown → 组件映射规则表

| Markdown 元素 | 映射组件 |
|--------------|---------|
| `# 标题` | 封面/标题区 |
| `> 开头引用` | 引言卡 |
| `## 章节标题` | 章节标题（自动编号 01/02/03） |
| `### 子标题` | 子标题 |
| 普通段落 | 正文段落 |
| `**加粗**` | 加粗标记 |
| `==高亮==` | 高亮标记 |
| `<u>下划线</u>` | 关键词下划线 |
| `> 引用`（非开头） | 引用块 |
| `![说明](url)` | 通用库图片组件（主色替换为 `#374151`） |
| `` ```code``` `` | 通用库代码块（主色替换为 `#374151`） |
| `---` | 分割线 |
| `\| 表格 \|` | 表格 |
| 列表项 | 正文段落（带缩进）或目录导读 |
