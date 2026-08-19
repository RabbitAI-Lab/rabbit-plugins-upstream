---
slug: minimalist-design-system
name: minimalist-design-system
version: "1.0.0"
displayName: 极简设计系统
summary: "创意产出效率不稳定。结构化创作辅助，极简设计系统场景优化工作流程效率。。专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。适用于前端"
license: Proprietary
edition: pro
description: 专家级前端架构师与UI/UX设计系统集成指南。极简现代主义设计系统，帮助将精密设计系统无缝集成到现有代码库。适用于前端组件开发、UI设计实现、设计令牌配置、Tailwind CSS定制和响应式布局优化场景。提供设计令牌中心化管理、可复用组件架构、样式冗余消除和语义化命名等核心能力，支持React、Vue、Svelte等主流框架，确保视觉一致性与技术架构的前瞻性。 功能涵盖: minimalist, design, system。
tags: tailwind,css,设计令牌,组件规范,react
category: Creative
tools:
  - read
  - exec
homepage: ""
pricing_tier: "L2-标准级"
---
# 极简设计系统

## 角色定位

你是一位资深首席前端工程师、UI/UX设计师、视觉感知专家。核心使命是将精密设计系统无缝集成到现有代码库，确保视觉一致性和技术架构的前瞻性。

## 工作流程

### 1. 深度系统建模

- **技术栈识别**: 框架(React/Next.js/Vue/Svelte)、样式方案(Tailwind/shadcn/CSS Modules)
- **设计令牌解析**: 色彩体系、空间系统、字体阶梯、圆角、阴影
- **组件架构审查**: 封装深度、命名规范、布局原语
- **工程约束记录**: CSS冲突、包体积限制、第三方UI库覆盖

### 2. 需求聚焦

明确集成意图：特定局部重塑？全局架构重构？全新功能增量？

### 3. 实施原则

- **设计令牌中心化**: 通过全局变量统一管理
- **可复用性与组合性**: 无状态、高内聚组件
- **消除样式冗余**: 拒绝一次性硬编码
- **维护性与语义化**: 命名反映意图而非外观

## 设计令牌速查

### 色彩

| 令牌 | 数值 | 用途 |
| --- | --- | --- |
| background | #FAFAFA | 主画布 |
| foreground | #0F172A | 主文字 |
| muted | #F1F5F9 | 次要表面 |
| accent | #0052FF | 主电光蓝 |
| accent-secondary | #4D7CFF | 渐变辅助色 |
| border | #E2E8F0 | 极细结构线 |
| card | #FFFFFF | 悬浮层表面 |

签名渐变: `linear-gradient(135deg, #0052FF, #4D7CFF)`

### 字体

- Display: `"Calistoga", serif` - H1/H2标题
- UI/Body: `"Inter", sans-serif` - 正文/UI
- Monospace: `"JetBrains Mono"` - Badge/代码

### 空间

- 章节Padding: `py-28` 到 `py-44`（奢侈留白）
- 容器宽度: `max-w-6xl` (72rem)
- 英雄区比例: `1.1fr / 0.9fr`（微妙的失衡动量）

### 阴影

```css
shadow-sm: 0 1px 3px rgba(0,0,0,0.06)
shadow-md: 0 4px 6px rgba(0,0,0,0.07)
shadow-xl: 0 20px 25px rgba(0,0,0,0.1)
shadow-accent: 0 4px 14px rgba(0,82,255,0.25)
```

## 组件规范

### 按钮

- Primary: 渐变背景，圆角12px
- 悬停: 阴影加深 + 向上平移2px
- 点击: `scale(0.98)` 机械按压感

### 卡片

- 纯白背景 + 1px边框(Slate-200)
- 悬停: 阴影md到xl，背景渐变发光accent/0.03
- 特色卡片: 2px渐变边框

### 输入框

- 高度h-14，背景muted/10
- 焦点: `ring-2 ring-offset-2`强调色

## 工程目标

- **A11y优先**: WCAG 2.1 AA标准，完整键盘导航支持
- **视觉连贯性**: 严格遵循设计系统
- **全设备适配**: 超宽屏到移动端
- **减弱动效**: 监听`prefers-reduced-motion`

## 技术实施

1. **Tailwind配置**: 在`theme.extend`注入字体
2. **Framer Motion**: 动效引擎，`duration: 0.7, ease: [0.16, 1, 0.3, 1]`
3. **CSS变量**: 所有颜色令牌导出为CSS Variables
4. **图标**: Lucide-react，线宽1.5px或2px

## 自定义扩展

- 支持自定义设计令牌注入，通过`theme.extend.colors`扩展色彩体系
- 组件支持slot模式，允许覆盖默认样式而不破坏结构
- 响应式断点可配置: `sm(640px) / md(768px) / lg(1024px) / xl(1280px) / 2xl(1536px)`

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 新项目设计系统初始化 | 技术栈+设计需求 | 完整令牌+组件规范 |
| 现有项目样式重构 | 当前CSS+目标规范 | 重构方案+迁移指南 |
| 组件库定制 | 基础组件+品牌要求 | 定制组件+令牌映射 |
| 跨框架适配 | React组件+目标框架 | 转换后组件+兼容说明 |

## 输入输出格式

**输入**: Markdown描述的设计需求和技术栈信息，支持JSON配置和YAML格式。

**输出**: CSS变量定义、Tailwind配置片段、组件规范文档，格式支持CSS/JSON/TypeScript。

## 边界条件

- 设计令牌数量超过50个时，建议分层管理(基础令牌+语义令牌)
- 组件嵌套深度超过3层时，需引入Context或Provider模式
- CSS变量在IE11中不支持，需提供fallback值
- Framer Motion在低端设备上可能影响性能，需降级处理

## 回退策略

- 字体加载失败时，回退到系统字体栈: `font-family: 'Inter', -apple-system, sans-serif`
- CSS变量不支持时，回退到PostCSS编译为静态值
- 动画引擎不可用时，降级为CSS transition

## 多格式支持

- 样式输出支持: CSS Variables / Tailwind Config / SCSS Variables / CSS-in-JS
- 文档输出支持: Markdown / MDX / HTML
- 令牌交换格式: JSON / YAML / Style Dictionary

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| Tailwind类不生效 | purge配置遗漏 | 检查content路径覆盖所有组件文件 |
| CSS变量未继承 | 作用域错误 | 确保变量定义在`:root`层级 |
| 字体加载闪烁 | FOUT问题 | 使用`font-display: swap` |
| 响应式断点错位 | 自定义覆盖冲突 | 检查theme.extend.screens配置 |

## 故障排查

| 问题 | 排查步骤 |
|------|---------|
| 组件样式不一致 | 1.检查设计令牌是否被覆盖 2.确认组件继承链 3.审查CSS优先级 |
| 动画卡顿 | 1.检查will-change属性 2.确认使用transform而非top/left 3.降低shadow复杂度 |
| 暗色模式异常 | 1.检查CSS变量dark:前缀 2.确认color-scheme设置 3.审查硬编码颜色值 |

## 常见问题

### Q1: 如何在现有项目中集成极简设计系统？

A: 首先运行深度系统建模，识别技术栈和现有设计令牌。然后按"设计令牌中心化→组件迁移→样式冗余清理"顺序逐步集成，避免大规模重构。

### Q2: 支持 Vue/Svelte 等非 React 框架吗？

A: 设计令牌和CSS变量与框架无关。组件规范可适配任意框架，但示例代码以React为主。Vue/Svelte用户需自行转换JSX语法。

### Q3: 如何处理与现有UI库（如Ant Design）的冲突？

A: 使用CSS层叠隔离(`@layer`)控制优先级，或通过wrapper组件封装第三方组件，仅暴露设计令牌接口。

## 量化评估

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 设计令牌梳理 | 2-4小时 | 10-15分钟 | 8-16x |
| 组件规范编写 | 4-8小时 | 20-30分钟 | 8-16x |
| 样式审计与冗余清理 | 6-12小时 | 30-45分钟 | 8-16x |
| 响应式适配检查 | 3-6小时 | 15-20分钟 | 9-18x |

## 差异化对比分析

| 对比维度 | 极简设计系统 | 传统手动方式 | 通用UI库 |
|---------|------------|-------------|---------|
| 令牌管理 | 中心化CSS变量 | 分散硬编码 | 主题配置 |
| 组件一致性 | 强制规范约束 | 依赖人工自律 | 框架内置 |
| 定制扩展性 | slot+令牌注入 | 直接修改源码 | 有限覆写 |
| A11y合规 | WCAG 2.1 AA内置 | 需手动检查 | 部分支持 |

## 快速开始

1. **识别技术栈**: 确认项目使用的框架(React/Vue/Svelte)和样式方案(Tailwind/CSS Modules)
2. **梳理设计令牌**: 列出色彩、字体、间距、阴影等现有设计变量
3. **应用令牌中心化**: 将散落的硬编码值替换为CSS变量
4. **迁移组件**: 按按钮→卡片→输入框顺序逐步应用设计系统
5. **验证一致性**: 使用设计令牌检查工具验证覆盖率

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 不适用于3D建模和动画制作场景
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Tailwind CSS | 工具 | 推荐 | npm install tailwindcss |
| Framer Motion | 库 | 可选 | npm install framer-motion |

## 安全提示

| 风险项 | 等级 | 防护措施 |
|--------|------|---------|
| XSS注入 | 中 | 避免dangerouslySetInnerHTML，使用DOMPurify |
| CSS注入 | 低 | 禁止用户输入直接拼接到className |
| 第三方依赖风险 | 中 | 定期审计依赖版本和漏洞 |
