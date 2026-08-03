# 胭红主题组件库（rose）

> 适合时尚／美妆／节庆／促销活动文章。红色调传递热情和活力，适合吸引眼球的内容。
> 主色 `#E11D48` 只在锚点出现（全文 ≤5 处），大面积白底＋灰阶，彩色只做点缀。

---

## 一、设计变量速查表

| 变量 | 色值 | 用途 |
|------|------|------|
| 主色 | `#E11D48` | 章节编号、CTA 背景、加粗锚点（≤5 处） |
| 主色浅 | `#FB7185` | 英文标签、子标题竖条、装饰点 |
| 浅底色 | `#FFF1F2` | 引言卡、引用块、数据卡背景 |
| 浅边框 | `#FECDD3` | 表格边框、徽章边框 |
| 高亮色 | `#FFE4E6` | 粉底高亮起始色 |
| 高亮渐变终色 | `#FECDD3` | 粉底高亮结束色 |
| 标题色 | `#1C1917` | 文章标题、章节标题、子标题 |
| 正文色 | `#44403C` | 正文段落 |
| 辅助文字色 | `#A8A29E` | 副标题、说明文字、日期 |
| 分割线色 | `#E7E5E4` | 封面底部分割线、表格行线 |
| 下划线色 | `#FB7185` | 关键词下划线 |
| 深底白字背景 | `#BE123C` | CTA 区域、表头背景 |

---

## 二、各组件完整 HTML

### 1. 全局容器

最外层 `<section>`，包裹整篇文章。

```html
<section style="max-width:677px;margin:0 auto;padding:20px 16px;">
<!-- 文章内容 -->
</section>
```

### 2. 封面／标题区

文章标题＋副标题／日期，顶部带主色装饰条。

```html
<section style="margin:0 0 32px;">
<section style="width:36px;height:4px;background:#E11D48;border-radius:2px;margin-bottom:16px;"></section>
<p style="margin:0 0 10px;line-height:1.4;font-size:24px;font-weight:bold;color:#1C1917;"><span leaf="">文章标题</span></p>
<p style="margin:0;line-height:1.6;font-size:14px;color:#A8A29E;"><span leaf="">副标题或日期信息</span></p>
<section style="margin-top:20px;height:1px;background:#E7E5E4;"></section>
</section>
```

### 3. 引言卡

开头导读，浅底卡片，含署名槽位。

```html
<section style="margin:0 0 28px;padding:20px 24px;background:#FFF1F2;border-radius:8px;">
<p style="margin:0 0 12px;line-height:1.8;font-size:15px;color:#44403C;"><span leaf="">这是一段引言或导读文字，用浅底卡片突出文章核心价值，帮助读者快速判断是否继续阅读。</span></p>
<p style="margin:0;line-height:1.6;font-size:13px;color:#E11D48;text-align:right;"><span leaf="">—— {{作者名}}</span></p>
</section>
```

### 4. 目录导读

精选 3 个核心看点，不是全量章节列表。

```html
<section style="margin:0 0 32px;padding:20px 24px;background:#FAFAF9;border-radius:8px;">
<p style="margin:0 0 16px;line-height:1.5;font-size:14px;font-weight:bold;color:#1C1917;"><span leaf="">本文看点</span></p>
<section style="margin:0 0 12px;display:flex;align-items:flex-start;">
<section style="flex-shrink:0;margin-right:10px;width:20px;height:20px;background:#E11D48;border-radius:4px;display:flex;align-items:center;justify-content:center;"><p style="margin:0;line-height:1;font-size:11px;color:#ffffff;font-weight:bold;"><span leaf="">1</span></p></section>
<p style="margin:0;line-height:1.6;font-size:15px;color:#44403C;"><span leaf="">核心看点一描述</span></p>
</section>
<section style="margin:0 0 12px;display:flex;align-items:flex-start;">
<section style="flex-shrink:0;margin-right:10px;width:20px;height:20px;background:#E11D48;border-radius:4px;display:flex;align-items:center;justify-content:center;"><p style="margin:0;line-height:1;font-size:11px;color:#ffffff;font-weight:bold;"><span leaf="">2</span></p></section>
<p style="margin:0;line-height:1.6;font-size:15px;color:#44403C;"><span leaf="">核心看点二描述</span></p>
</section>
<section style="margin:0;display:flex;align-items:flex-start;">
<section style="flex-shrink:0;margin-right:10px;width:20px;height:20px;background:#E11D48;border-radius:4px;display:flex;align-items:center;justify-content:center;"><p style="margin:0;line-height:1;font-size:11px;color:#ffffff;font-weight:bold;"><span leaf="">3</span></p></section>
<p style="margin:0;line-height:1.6;font-size:15px;color:#44403C;"><span leaf="">核心看点三描述</span></p>
</section>
</section>
```

### 5. 章节标题

带自动编号（01／02／03）和英文标签槽位。

```html
<section style="margin:40px 0 20px;display:flex;align-items:baseline;">
<p style="margin:0 12px 0 0;line-height:1;font-size:40px;font-weight:bold;color:#E11D48;"><span leaf="">01</span></p>
<section>
<p style="margin:0 0 4px;line-height:1.3;font-size:20px;font-weight:bold;color:#1C1917;"><span leaf="">章节中文标题</span></p>
<p style="margin:0;line-height:1.4;font-size:12px;color:#FB7185;letter-spacing:1px;"><span leaf="">ENGLISH LABEL</span></p>
</section>
</section>
```

### 6. 子标题

`###` 级别，左竖条样式。

```html
<section style="margin:28px 0 12px;padding-left:12px;border-left:3px solid #FB7185;">
<p style="margin:0;line-height:1.5;font-size:17px;font-weight:bold;color:#1C1917;"><span leaf="">子标题内容</span></p>
</section>
```

### 7. 正文段落

标准 body paragraph，line-height 1.9，16px。

```html
<p style="margin:0 0 20px;line-height:1.9;font-size:16px;color:#44403C;"><span leaf="">这是标准正文段落，行高 1.9，字号 16px。每个段落之间保持 20px 间距，确保阅读舒适。</span></p>
```

### 8. 关键词下划线

标记正文关键词的 span。

```html
<span leaf="" style="border-bottom:2px solid #FB7185;">关键词</span>
```

段落内使用示例：

```html
<p style="margin:0 0 20px;line-height:1.9;font-size:16px;color:#44403C;"><span leaf="">这段话里有一个<span leaf="" style="border-bottom:2px solid #FB7185;">关键概念</span>需要读者注意。</span></p>
```

### 9. 加粗标记

主色加粗 span，用于最强强调（锚点层，全文 ≤5 处）。

```html
<span leaf="" style="color:#E11D48;font-weight:bold;">加粗文字</span>
```

### 10. 高亮标记

粉底渐变背景高亮 span。

```html
<span leaf="" style="background:linear-gradient(to top,#FFE4E6 0%,#FECDD3 100%);padding:2px 4px;border-radius:3px;">高亮文字</span>
```

### 11. 荧光笔

底部半高亮 span，模拟荧光笔划过效果。

```html
<span leaf="" style="background:linear-gradient(to top,#FFE4E6 40%,transparent 40%);">荧光标记文字</span>
```

### 12. 引用块

浅底引用块，左竖条。

```html
<section style="margin:24px 0;padding:16px 20px;background:#FFF1F2;border-left:3px solid #E11D48;border-radius:0 6px 6px 0;">
<p style="margin:0;line-height:1.8;font-size:15px;color:#44403C;"><span leaf="">引用块内容，用于强调重要观点或补充说明。</span></p>
</section>
```

### 13. 数据卡

突出关键数字或数据的卡片。

```html
<section style="margin:24px 0;padding:24px;background:#FFF1F2;border-radius:8px;text-align:center;">
<p style="margin:0 0 6px;line-height:1;font-size:36px;font-weight:bold;color:#E11D48;"><span leaf="">98%</span></p>
<p style="margin:0;line-height:1.6;font-size:14px;color:#A8A29E;"><span leaf="">数据说明文字</span></p>
</section>
```

### 14. 表格

用 `<section>` ＋ flex 布局模拟表格（`<table>` 在公众号支持不稳定）。

```html
<section style="margin:24px 0;border:1px solid #FECDD3;border-radius:8px;overflow:hidden;">
<section style="display:flex;background:#BE123C;">
<section style="flex:1;padding:12px 16px;"><p style="margin:0;line-height:1.5;font-size:14px;font-weight:bold;color:#ffffff;"><span leaf="">列标题A</span></p></section>
<section style="flex:1;padding:12px 16px;"><p style="margin:0;line-height:1.5;font-size:14px;font-weight:bold;color:#ffffff;"><span leaf="">列标题B</span></p></section>
</section>
<section style="display:flex;border-top:1px solid #FECDD3;">
<section style="flex:1;padding:12px 16px;"><p style="margin:0;line-height:1.5;font-size:14px;color:#44403C;"><span leaf="">数据A1</span></p></section>
<section style="flex:1;padding:12px 16px;"><p style="margin:0;line-height:1.5;font-size:14px;color:#44403C;"><span leaf="">数据B1</span></p></section>
</section>
<section style="display:flex;border-top:1px solid #FECDD3;">
<section style="flex:1;padding:12px 16px;"><p style="margin:0;line-height:1.5;font-size:14px;color:#44403C;"><span leaf="">数据A2</span></p></section>
<section style="flex:1;padding:12px 16px;"><p style="margin:0;line-height:1.5;font-size:14px;color:#44403C;"><span leaf="">数据B2</span></p></section>
</section>
</section>
```

### 15. 分割线

带主题色装饰的分割线，居中三点式。

```html
<section style="margin:32px 0;display:flex;align-items:center;justify-content:center;">
<section style="width:6px;height:6px;background:#FB7185;border-radius:50%;margin:0 5px;"></section>
<section style="width:36px;height:2px;background:#FB7185;border-radius:1px;"></section>
<section style="width:6px;height:6px;background:#FB7185;border-radius:50%;margin:0 5px;"></section>
</section>
```

### 16. 作者签名区／CTA

文末签名＋互动引导，深底白字。

```html
<section style="margin:40px 0 0;padding:28px 24px;background:#BE123C;border-radius:8px;text-align:center;">
<p style="margin:0 0 8px;line-height:1.6;font-size:15px;color:#ffffff;"><span leaf="">如果这篇文章对你有帮助</span></p>
<p style="margin:0 0 16px;line-height:1.6;font-size:15px;color:#ffffff;"><span leaf="">欢迎点赞、在看、转发分享</span></p>
<section style="display:inline-block;padding:6px 20px;background:#ffffff;border-radius:20px;">
<p style="margin:0;line-height:1.5;font-size:14px;font-weight:bold;color:#BE123C;"><span leaf="">{{作者名}}</span></p>
</section>
</section>
```

### 17. 产品徽章

小型产品或工具名称徽章，行内使用。

```html
<section style="display:inline-block;padding:3px 10px;background:#FFF1F2;border:1px solid #FECDD3;border-radius:4px;">
<p style="margin:0;line-height:1.5;font-size:13px;color:#E11D48;font-weight:bold;"><span leaf="">产品名</span></p>
</section>
```

---

## 三、完整文章模板骨架

标准装配顺序：

```
全局容器
 ├─ 封面／标题区
 ├─ 引言卡
 ├─ 目录导读
 ├─ 〔 章节标题            ← 循环 N 次
 │    ├─ 子标题（按需）
 │    ├─ 正文段落（含关键词下划线／加粗／高亮／荧光笔）
 │    ├─ 引用块（按需）
 │    ├─ 数据卡（按需）
 │    ├─ 表格（按需）
 │    ├─ 产品徽章（按需）
 │    └─ 通用库组件：代码块／图片（按需）〕
 ├─ 分割线
 └─ 作者签名区／CTA
```

---

## 四、文章类型 → 组件组合配方表

| 文章类型 | 核心组件组合 |
|---------|------------|
| 时尚／穿搭 | 封面＋引言＋目录＋章节标题＋正文＋产品徽章＋图片（通用库）＋签名 |
| 美妆／测评 | 封面＋引言＋目录＋章节标题＋正文＋数据卡＋产品徽章＋表格＋签名 |
| 节庆／活动 | 封面＋引言＋章节标题＋正文＋高亮标记＋CTA＋签名 |
| 促销／种草 | 封面＋引言＋目录＋章节标题＋正文＋产品徽章＋CTA＋签名 |

---

## 五、Markdown → 组件映射规则表

| Markdown 元素 | 映射组件 |
|--------------|---------|
| `# 标题` | 封面／标题区 |
| `> 引言（开头）` | 引言卡 |
| `## 标题` | 章节标题（自动编号 01／02／03＋英文标签） |
| `### 标题` | 子标题 |
| 正文段落 | 正文段落（每段主动加 1-3 个关键词下划线） |
| `**文字**` | 加粗标记（锚点层，全文 ≤5 处） |
| `==文字==` | 高亮标记 |
| `<u>文字</u>` | 关键词下划线 |
| `> 引用（非开头）` | 引用块 |
| `---` | 分割线 |
| `` \| 表格 \| `` | 表格 |
| `- 项` / `1. 项` | 转为带缩进的正文段落（无序列表前缀「·」） |
| `` `code` `` | 通用库行内代码 |
| ` ``` 围栏 ``` ` | 通用库代码块 |
| `![说明](url)` | 通用库图片组件（有说明文字才加说明） |
