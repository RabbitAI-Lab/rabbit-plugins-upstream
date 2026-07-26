---
slug: "css-free"
name: "css-free"
version: "1.0.0"
displayName: "CSS样式引擎(免费版)"
summary: "现代CSS布局、动画、响应式设计与组件样式生成，支持Flexbox/Grid/Tailwind。免费版"
summary_zh: "现代CSS布局、动画、响应式设计与组件样式生成，支持Flexbox/Grid/Tailwind。免费版"
license: "MIT"
description: |-
  CSS样式与布局辅助引擎（免费版），覆盖现代CSS布局、动画效果、响应式设计与
  组件样式生成。核心能力：
  - 现代CSS布局（Flexbox/Grid/Container Queries）
  - CSS动画与过渡效果（@keyframes/transition/scroll-driven）
  - 响应式设计（断点策略/移动优先/暗色模式）
  - 组件样式生成（BEM/CSS Modules/Tailwind工具类）
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 创意
  - 图像
  - css
  - grid
  - flexbox
  - rem
  - 布局
category: "Automation"
---
# CSS样式引擎(免费版)

CSS样式与布局辅助引擎，覆盖现代CSS布局、动画效果、响应式设计与组件样式生成.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | CSS样式引擎(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 现代CSS布局
```css
/* Flexbox 居中 */
.center { display: flex; align-items: center; justify-content: center; }
// ...
/* Grid 响应式网格 */
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}
// ...
/* Holy Grail 布局 */
.holy-grail {
  display: grid;
  grid-template: auto 1fr auto / auto 1fr auto;
  grid-template-areas:
    "header header header"
    "nav    main   aside"
    "footer footer footer";
  min-height: 100vh;
}
// ...
/* Container Queries */
@container sidebar (min-width: 400px) {
  .card { flex-direction: row; }
}
```

### 2. CSS动画与过渡效果
```css
/* 过渡效果 */
.btn { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.btn:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.15); }
// ...
/* @keyframes 动画 */
@keyframes slideIn {
  from { opacity: 0; transform: translateX(-30px); }
  to { opacity: 1; transform: translateX(0); }
}
.animate-slide-in { animation: slideIn 0.5s ease-out forwards; }
// ...
/* Scroll-driven Animations */
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
.scroll-fade {
  animation: fade-in linear;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
```

- 异常时参考错误处理章节进行恢复
- 关键参数: `css动画与过渡效果` 选项

### 3. 响应式设计
```css
/* 移动优先断点策略 */
.container {
  width: 100%;
  padding: 1rem;
}
@media (min-width: 768px) {
  .container { max-width: 720px; padding: 2rem; }
}
@media (min-width: 1024px) {
  .container { max-width: 960px; }
}
// ...
/* 暗色模式 */
:root { --bg: #ffffff; --text: #1a1a1a; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #0f172a; --text: #f1f5f9; }
}
// ...
/* clamp() 流体排版 */
h1 { font-size: clamp(1.5rem, 4vw, 3rem); }
```

- 异常时参考错误处理章节进行恢复
- 关键参数: `响应式设计` 选项

### 4. 组件样式生成
支持多种CSS方法论：
- **BEM**：`.block__element--modifier`
- **CSS Modules**：局部作用域类名
- **Tailwind**：工具类组合
- **CSS-in-JS**：styled-components/emotion模式

#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|---:|---:|---:|
| 布局实现 | 布局描述+目标 | Flexbox/Grid CSS代码 |
| 动画效果 | 动效描述 | @keyframes + transition代码 |
| 响应式适配 | 设计稿+断点 | 媒体查询CSS |
| 组件样式 | 组件描述+风格 | BEM/Tailwind样式代码 |

**不适用于**：Canvas/WebGL渲染、SVG路径动画、CSS预处理器编译.
## 使用流程

1. 明确布局需求（类型/响应式/浏览器兼容性）
2. 选择CSS方法论（原生/BEM/Tailwind/CSS Modules）
3. 生成CSS代码（含兼容性注释）
4. 提供HTML结构配合示例
5. 标注浏览器兼容性要求

#
## 示例

### 示例1：响应式卡片网格
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}
// ...
.card {
  background: var(--surface, #fff);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
// ...
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.12);
}
// ...
@media (max-width: 640px) {
  .card-grid { grid-template-columns: 1fr; padding: 1rem; }
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| Flexbox子元素溢出不换行 | 未设置`flex-wrap`或`min-width` | 添加`flex-wrap: wrap`，子元素设置`min-width`防止压缩过小，或使用`flex: 0 0 auto` |
| Grid布局在旧浏览器不显示 | IE不支持CSS Grid | 添加`@supports (display: grid)`渐进增强，旧浏览器回退到Flexbox或Float布局 |
| `position: sticky`不生效 | 父元素设置了`overflow: hidden`或高度不足 | 移除父元素的`overflow: hidden`，确保滚动容器是sticky元素的直接或间接父级，检查父元素是否有固定高度 |
| CSS变量在旧浏览器报错 | IE不支持`var()` | 使用PostCSS插件`postcss-custom-properties`编译为静态值，或提供回退值`color: #3b82f6; color: var(--primary)` |

## 常见问题

### Q1: Flexbox和Grid什么时候用哪个？
Flexbox用于一维布局（行或列），适合导航栏、工具栏、按钮组、卡片内容排列。Grid用于二维布局（行和列同时控制），适合页面整体布局、画廊网格、仪表盘面板。经验法则：如果需要在两个方向上对齐和控制间距用Grid，如果只是沿一个方向排列用Flexbox。两者可以嵌套使用——Grid控制页面布局，Flexbox控制组件内部排列.
### Q2: 如何实现真正的垂直居中？
现代CSS推荐三种方式：1) Flexbox：`display: flex; align-items: center; justify-content: center;`（最常用）；2) Grid：`display: grid; place-items: center;`（最简洁）；3) 绝对定位+transform：`position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);`（兼容性最好但需定位上下文）。避免使用`line-height`或`vertical-align`，它们只适用于行内元素.
### Q3: Tailwind和手写CSS如何选择？
Tailwind适合快速原型开发和团队协作（工具类即标准），减少命名负担。手写CSS适合需要高度定制动画、复杂选择器、CSS变量主题系统的场景。混合策略：用Tailwind处理布局和间距（`flex gap-4 p-6`），用`@layer components`或CSS文件处理复杂组件样式和动画。如果项目已有设计系统token，Tailwind配置映射token值可两者兼得.
## 已知限制

- 无法实时预览渲染效果（仅输出代码）
- 浏览器兼容性需用户自行测试
- CSS-in-JS方案需配合对应框架运行

## 升级提示

本免费版提供基础功能。升级到完整版 css 获取全部能力和高级特性.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "CSS样式引擎(免费版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "css"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
