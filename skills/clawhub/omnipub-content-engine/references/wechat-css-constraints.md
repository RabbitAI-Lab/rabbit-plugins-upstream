# 微信公众号 CSS 兼容性约束

> 本文档基于实际推送验证（2026-08-14/15），通过 draft/get 回读 + Headless Chrome 渲染截图对比确认。

## 微信渲染器会静默丢弃的 CSS 属性

以下属性在微信草稿存储层（draft/add → draft/get）100% 无损保留，但**微信文章渲染器会直接忽略**，不产生任何视觉效果：

| 属性 | 状态 | 替代方案 |
|------|------|----------|
| `border-radius` | ❌ 忽略 | 用纯色边框代替，接受直角 |
| `box-shadow` | ❌ 忽略 | 用 `border` 代替 |
| `text-shadow` | ❌ 忽略 | 用 `color` / `font-weight` 代替 |
| `linear-gradient` | ❌ 忽略 | 用纯色 `background` 代替 |
| `radial-gradient` | ❌ 忽略 | 同上 |
| `letter-spacing` | ❌ 忽略 | 无替代，接受默认字间距 |
| `opacity` | ❌ 忽略 | 用 `rgba` 代替（但 rgba 也可能被剥） |
| `rgba()` | ⚠️ 部分 | alpha 通道被丢弃，颜色变实色 |
| `background-clip` | ❌ 忽略 | 无 |
| `text-fill-color` | ❌ 忽略 | 无 |
| `backdrop-filter` | ❌ 忽略 | 无 |
| `filter` | ❌ 忽略 | 无 |
| `transition` | ❌ 忽略 | 微信文章无动画 |
| `animation` | ❌ 忽略 | 同上 |
| `transform` | ❌ 忽略 | 同上 |

## 微信渲染器支持的 CSS 属性

以下属性经实测确认在微信渲染器中正常工作：

| 属性 | 状态 | 备注 |
|------|------|------|
| `color` | ✅ 支持 | |
| `background` / `background-color` | ✅ 支持 | 仅纯色，不含渐变 |
| `font-size` | ✅ 支持 | |
| `font-weight` | ✅ 支持 | |
| `font-family` | ✅ 支持 | |
| `line-height` | ✅ 支持 | |
| `text-align` | ✅ 支持 | |
| `margin` | ✅ 支持 | |
| `padding` | ✅ 支持 | |
| `border` | ✅ 支持 | |
| `border-left` / `border-top` 等 | ✅ 支持 | |
| `display` | ✅ 支持 | `block` / `flex` / `inline` / `none` |
| `max-width` | ✅ 支持 | |
| `width` / `height` | ✅ 支持 | |
| `word-break` | ✅ 支持 | |
| `white-space` | ✅ 支持 | |
| `position` | ⚠️ 有限 | `relative` 可用，`absolute`/`fixed` 不稳定 |

## 关键教训

1. **存储层 vs 渲染层**：微信 draft/add API 存储 HTML 时 100% 无损（所有内联 style 原样保存），但前端渲染器有独立 CSS 过滤层
2. **草稿删除导致图片失效**：草稿删除后，其引用的 mmbiz.qpic.cn 图片 URL 会失效，不可复用
3. **每次推送必须重新上传图片**：即使 Markdown 中已有 mmbiz URL，也必须重新上传本地图片获取新 URL
4. **headless Chrome 验证法**：用 `--headless --screenshot` 渲染对比本地 HTML 和 draft/get 回读 HTML，可确认存储无损
