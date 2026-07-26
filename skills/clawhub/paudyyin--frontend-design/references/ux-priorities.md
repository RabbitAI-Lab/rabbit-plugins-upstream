# UX Priorities — 10级优先级检查清单

> 来源：UI UX Pro Max v2.0。按优先级从高到低排列，AI 生成 UI 代码时依次检查。

## 优先级速查表

| # | 类别 | 影响度 | 关键检查项 | 反模式 |
|---|------|--------|------------|--------|
| 1 | 无障碍 | CRITICAL | 对比度4.5:1, Alt文本, 键盘导航, Aria标签 | 移除focus ring, 无标签图标按钮 |
| 2 | 触摸交互 | CRITICAL | 最小44×44px, 8px间距, 加载反馈 | 仅hover交互, 0ms状态变化 |
| 3 | 性能 | HIGH | WebP/AVIF, 懒加载, CLS<0.1 | 布局抖动, 累积布局偏移 |
| 4 | 风格选择 | HIGH | 匹配产品类型, SVG图标, 一致性 | 混搭flat+skeuomorphic, emoji当图标 |
| 5 | 布局响应式 | HIGH | 移动优先, 视口meta, 无水平滚动 | 固定px宽度, 禁用缩放 |
| 6 | 排版色彩 | MEDIUM | 基准16px, 行高1.5, 语义化token | 正文<12px, 灰底灰字, 原始hex |
| 7 | 动画 | MEDIUM | 150-300ms, 有意义运动, 空间连续性 | 纯装饰动画, 动画width/height |
| 8 | 表单反馈 | MEDIUM | 可见标签, 错误就近, 辅助文本 | 仅placeholder标签, 错误只在顶部 |
| 9 | 导航模式 | HIGH | 可预测返回, 底部导航≤5, 深链接 | 过载导航, 破坏返回行为 |
| 10 | 图表数据 | LOW | 图例, 工具提示, 无障碍色彩 | 仅靠颜色传达信息 |

---

## 1. 无障碍 (CRITICAL)

### 必须做到
- **color-contrast**: 正常文本最小 4.5:1 比率（大文本 3:1）
- **focus-states**: 交互元素可见 focus ring（2-4px）
- **alt-text**: 有意义的图片必须有描述性 alt 文本
- **aria-labels**: 图标按钮必须有 aria-label
- **keyboard-nav**: Tab 顺序匹配视觉顺序，完整键盘支持
- **form-labels**: 使用 `<label for="...">` 关联输入框
- **skip-links**: 提供"跳到主内容"链接
- **heading-hierarchy**: h1→h6 顺序不跳级
- **color-not-only**: 不靠颜色单独传达信息（加图标/文本）
- **dynamic-type**: 支持系统文本缩放
- **reduced-motion**: 尊重 `prefers-reduced-motion`
- **escape-routes**: 模态框和多步流程提供取消/返回

### 绝对禁止
- 移除 focus ring（`outline: none` 无替代）
- 无标签的图标按钮
- 仅靠颜色区分状态

---

## 2. 触摸交互 (CRITICAL)

### 必须做到
- **touch-target-size**: 最小 44×44pt (Apple) / 48×48dp (Material)
- **touch-spacing**: 触摸目标间最小 8px 间距
- **hover-vs-tap**: 主要交互使用 click/tap，不依赖 hover
- **loading-buttons**: 异步操作时禁用按钮 + 显示 spinner
- **cursor-pointer**: 可点击元素添加 `cursor: pointer`
- **press-feedback**: 按下时视觉反馈（ripple/highlight）

### 绝对禁止
- 依赖 hover 才能触发的交互
- 小于 44px 的触摸目标
- 触摸目标间距 < 8px

---

## 3. 性能 (HIGH)

### 必须做到
- **image-optimization**: WebP/AVIF, srcset/sizes, 懒加载
- **image-dimension**: 声明 width/height 或 aspect-ratio（防 CLS）
- **font-loading**: `font-display: swap`，预载关键字体
- **critical-css**: 首屏 CSS 内联或优先加载
- **lazy-loading**: 非首屏组件动态导入
- **virtualize-lists**: 50+ 项列表虚拟化
- **progressive-loading**: 骨架屏/shimmer 替代长时间 spinner

### 绝对禁止
- 无尺寸声明的图片
- 阻塞渲染的 CSS/JS
- 布局抖动（CLS > 0.1）

---

## 4. 风格选择 (HIGH)

### 必须做到
- **style-match**: 风格匹配产品类型
- **consistency**: 全站风格一致
- **no-emoji-icons**: 使用 SVG 图标（Heroicons/Lucide），不用 emoji
- **icon-style-consistent**: 一套图标风格（描边宽度、圆角一致）
- **primary-action**: 每屏一个主要 CTA，次要操作视觉弱化

### 绝对禁止
- emoji 当图标
- 混搭 flat + skeuomorphic
- 每屏多个同等权重的 CTA

---

## 5. 布局响应式 (HIGH)

### 必须做到
- **viewport-meta**: `width=device-width initial-scale=1`
- **mobile-first**: 移动优先设计，向上扩展
- **breakpoint-consistency**: 系统化断点（375/768/1024/1440）
- **readable-font-size**: 移动端最小 16px 正文
- **horizontal-scroll**: 禁止水平滚动
- **spacing-scale**: 4pt/8dp 间距系统

### 绝对禁止
- 水平滚动
- 固定 px 容器宽度
- 禁用缩放（`maximum-scale=1`）

---

## 6. 排版色彩 (MEDIUM)

### 必须做到
- **line-height**: 正文 1.5-1.75
- **line-length**: 每行 65-75 字符
- **font-scale**: 一致的类型比例（12/14/16/18/24/32）
- **color-semantic**: 语义化颜色 token（primary/surface/error）
- **number-tabular**: 数据列使用等宽数字

### 绝对禁止
- 正文 < 12px
- 灰底灰字
- 组件中直接使用原始 hex 值

---

## 7. 动画 (MEDIUM)

### 必须做到
- **duration-timing**: 微交互 150-300ms，复杂过渡 ≤400ms
- **transform-performance**: 只动画 transform/opacity
- **easing**: 进入用 ease-out，退出用 ease-in
- **motion-meaning**: 每个动画表达因果关系
- **exit-faster-than-enter**: 退出动画比进入短（~60-70%）
- **interruptible**: 动画可被用户中断

### 绝对禁止
- 动画 width/height/top/left
- 纯装饰动画
- 不可中断的动画
- 忽略 `prefers-reduced-motion`

---

## 8. 表单反馈 (MEDIUM)

### 必须做到
- **input-labels**: 每个输入框有可见标签
- **error-placement**: 错误信息在对应字段下方
- **submit-feedback**: 提交后显示 loading → success/error
- **inline-validation**: blur 时验证（非 keystroke）
- **input-helper-text**: 复杂输入提供持久辅助文本
- **focus-management**: 提交错误后自动聚焦第一个无效字段

### 绝对禁止
- 仅用 placeholder 当标签
- 错误只在页面顶部显示
- 一次性展示所有复杂选项

---

## 9. 导航模式 (HIGH)

### 必须做到
- **predictable-back**: 返回行为可预测
- **bottom-nav**: 底部导航 ≤5 项
- **deep-linking**: 支持深链接
- **navigation-direction**: 前进左/上，后退右/下

### 绝对禁止
- 过载导航（>7 项）
- 破坏系统返回手势
- 无深链接支持

---

## 10. 图表数据 (LOW)

### 必须做到
- **legends**: 图例清晰
- **tooltips**: 悬停显示详细数据
- **accessible-colors**: 色盲友好的调色板
- **data-labels**: 关键数据点有标签

### 绝对禁止
- 仅靠颜色传达数据差异
- 无图例的多系列图表

---

## 使用方式

```bash
# 搜索特定领域的 UX 准则
python scripts/search.py "touch target" --domain ux

# 搜索无障碍相关
python scripts/search.py "contrast" --domain ux

# 搜索表单最佳实践
python scripts/search.py "form validation" --domain ux
```

---

*来源：UI UX Pro Max v2.0 (MIT License) — 99条UX准则精简为10级优先级*
