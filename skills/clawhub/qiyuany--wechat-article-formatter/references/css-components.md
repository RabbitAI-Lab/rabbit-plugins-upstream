# 微信公众号排版 — CSS 兼容性详细参考

> 本文件包含完整的 HTML 组件代码模板，供排版时快速查阅和复制。
> 由 SKILL.md 的工作流第三步引用。

---

## 完整兼容性规则

### ✅ 安全保留（微信编辑器支持）

| 样式属性 | 用法示例 | 说明 |
|---------|---------|------|
| `border-left` 彩色竖线 | `border-left:3px solid #07c160` | **最可靠的视觉装饰** |
| `background` 单色浅底 | `background:#f0f7ff` | 浅色背景块/卡片 |
| `color` 文字变色 | `color:#07c160; font-weight:bold` | 关键词高亮、数字强调 |
| `border` 边框 | `border:1px solid #eee` | 分隔线、卡片边框 |
| `border-radius` 圆角 | `border-radius:4px` | 小圆角通常安全 |
| `font-size` / `font-weight` | 字号字重 | 正常使用 |
| `padding` / `margin` | 间距 | 正常使用 |
| `line-height` 行高 | 推荐 `1.75-1.85` | 正文行高 |
| `text-align: center` | 居中 | 金句、结尾CTA |

### ⚠️ 有风险 / 不推荐

| 样式属性 | 风险等级 | 说明 |
|---------|---------|------|
| `display: flex` + `gap` | 🔴 高 | 几乎必然被过滤 |
| `box-shadow: rgba()` | 🔴 高 | rgba 颜色值易被过滤 |
| `linear-gradient` 渐变 | 🔴 高 | 大概率被过滤 |
| SVG 图标/图形 | 🔴 高 | 内联 SVG 会被清除 |
| `position: absolute` | 🟡 中 | 可能导致布局错乱 |
| `transform` 变换 | 🟡 中 | 不保证保留 |
| `::before` / `::after` | 🟡 中 | 可能被过滤 |

### 最佳实践

1. **全部使用内联 style** — 不要用 `<style>` 标签或 class
2. **颜色用 hex 格式** — 如 `#07c160`，不用 `rgb()` 或 `rgba()`
3. **容器宽度限制 677px** — 模拟手机端显示
4. **字体栈**：`-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 配色方案速查

| 角色 | 颜色值 | 用途 |
|------|--------|------|
| 主色调（微信绿） | `#07c160` | 竖线、关键词、正向引导 |
| 强调红 | `#e74c3c` | 数字强调、警示语句 |
| 背景浅蓝 | `#f0f7ff` | 信息卡片、背景知识 |
| 背景浅绿 | `#f0fdf4` | 建议/结论框 |
| 背景暖白 | `#fffbf0` | 结尾关注引导区 |
| 背景浅灰 | `#fafafa` / `#f6f8f7` | 引用块背景 |
| 正文色 | `#333` | 主要段落 |
| 次要文字 | `#555` | 说明性段落 |
| 辅助文字 | `#888` / `#999` | 来源、时间戳 |

---

## 可复用组件 HTML 代码

### 章节标题（带彩色竖线）

```html
<h2 style="font-size:17px; font-weight:bold; color:#000; line-height:1.6;
    margin:28px 0 16px; padding-left:10px; border-left:4px solid #07c160;">
  章节标题
</h2>
```

### 引用块（绿底 — 建议/结论）

```html
<blockquote style="margin:16px 0; padding:12px 14px; background:#f0fdf4;
    border-left:3px solid #07c160; color:#555; font-size:15px; line-height:1.8;">
  引用内容
</blockquote>
```

### 引用块（灰底 — 评论/他人言论）

```html
<blockquote style="margin:16px 0; padding:10px 0 10px 14px;
    border-left:3px solid #ddd; background:#fafafa;
    color:#666; font-size:14px; line-height:1.7;">
  评论内容
</blockquote>
```

### 信息卡片（蓝底圆角）

```html
<section style="margin:18px 0; padding:14px 16px; background:#f0f7ff;
    border-radius:4px;">
  <p style="font-size:15px; line-height:1.85; margin:0; color:#444; text-align:justify;">
    卡片内容，关键词<strong style="color:#07c160;">绿色高亮</strong>，
    数字<span style="color:#e74c3c;font-weight:bold;">红色强调</span>
  </p>
</section>
```

### 视频/图片插入占位符

```html
<section style="margin:18px 0; padding:12px 0;
    border-top:1px solid #f0f0f0; border-bottom:1px solid #f0f0f0;
    text-align:center;">
  <p style="font-size:12px; color:#aaa; margin:0;">图片/视频描述</p>
</section>
```

### 关键词高亮

```html
<!-- 绿色强调 -->
<strong style="color:#07c160;">重要词汇</strong>

<!-- 红色数字 -->
<span style="color:#e74c3c;font-weight:bold;">3811张</span>

<!-- 底色术语标注 -->
<strong style="background:#fffacd;padding:1px 4px;color:#000;">3DGS</strong>
```

### 列表项（分隔线样式）

```html
<ul style="list-style:none; padding:0; margin:0 0 18px;">
  <li style="font-size:15px; line-height:1.8; color:#333;
      padding:10px 0; border-bottom:1px solid #f0f0f0;">
    <strong style="color:#07c160;">标题</strong> 描述文字
  </li>
</ul>
```

### 居中金句

```html
<p style="font-size:17px; font-weight:bold; color:#000;
    line-height:1.7; margin:24px 0 18px; text-align:center;">
  「金句内容」
</p>
```

### 关注引导 CTA（暖白底居中）

```html
<section style="margin:20px 0 8px; padding:18px 16px; background:#fffbf0;
    text-align:center; border-radius:4px;">
  <p style="font-size:14px; color:#666; line-height:1.8; margin:0 0 10px;">
    如果这篇文章让你有点触动
  </p>
  <p style="font-size:13px; color:#999; line-height:1.7; margin:0;">
    欢迎关注「账号名」<br>
    我会持续记录 <strong style="color:#07c160;">"Slogan"</strong> 的时刻 ✦
  </p>
</section>
```

---

## 排版检查清单

生成 HTML 后逐项确认：

- [ ] 所有样式内联，无 `<style>` 标签
- [ ] 无 `flex`/`gap`/`box-shadow: rgba()`/`linear-gradient`/SVG
- [ ] 颜色均为 hex 格式 `#xxxxxx`
- [ ] 容器宽度 `max-width:677px`
- [ ] 正文行高 `line-height:1.75-1.85`
- [ ] 视频/图片占位符已标注清晰
- [ ] 文末有关注引导 CTA
- [ ] 章节标题有左侧彩色竖线
