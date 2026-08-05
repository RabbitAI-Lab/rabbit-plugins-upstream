# 反向提示词系统 L11 (5种基础画像 + 页面级微调)

反向提示词=告诉AI绘图模型"不要画什么"，与正向提示词配套输出。

---

## 基础画像 (5选1)

### R-GOBE标准画像 (GOBE轨道默认)
```
no photorealistic, no 3D effects, no gradients, no drop shadows,
no bevels, no embossing, no glossy buttons, no skeuomorphic icons,
no realistic textures, no photographic images, no stock photos,
no cluttered layout, no more than 3 font families, no comic sans,
no decorative borders, no rainbow colors, no dark backgrounds,
no hand-drawn sketch style(unless specified), no watermarks,
no excessive ornamentation, no inconsistent icon styles
```

### R-GOBE变体画像 (GOBE轨道-教程/安全等变体页)
R-GOBE标准画像 + 追加:
```
no playful illustrations, no cartoon characters, no cute mascots,
no overly bright saturated colors beyond brand orange,
no ambiguous diagrams, no missing labels on arrows/shapes
```
**触发**: P-Tutorial / P-Security / P-Strategy 等变体前缀时使用

### R-平安企业标准画像 (平安橙轨道默认)
```
no casual fonts, no handwritten styles, no bright neon colors,
no asymmetric layouts, no cluttered information density,
no inconsistent with Ping An orange brand style guidelines,
no non-brand color accents(beyond orange/black/white/gray),
no playful illustrations, no cartoon elements,
no gradient backgrounds, no texture overlays
```
**触发**: 轨道=平安橙系时使用

### R-封面专属画像 (仅封面)
```
no text-heavy layout, no dense information, no small fonts below 14pt,
no generic template look, no clip art, no low-resolution elements,
no cluttered composition, no weak visual hierarchy,
no missing brand logo placement
```
**触发**: P-Cover前缀时。注意: 封面反向约束更关注"视觉冲击力破坏因素"

### R-特殊页画像 (信息密度极高的综合页)
R-GOBE标准画像 + 追加:
```
no missing alignment guides, no inconsistent spacing,
no overflow content outside visible area, no truncated text,
no overlapping elements, no unclear visual hierarchy among sections
```
**触发**: Layout 12混合布局 / 图标密度>20 的页面

---

## 页面级微调矩阵 (在基础画像上叠加)

| 页面特征 | 额外追加的反向规则 |
|---------|-------------------|
| 含数据图表 | `no distorted axes, no missing units, no misleading scales` |
| 含流程图 | `no broken arrow chains, no circular references(unless intended)` |
| 含对比内容 | `no same-color for both sides, no missing ✅❌ indicators` |
| 含编号列表 | `no misaligned numbers, no skipped sequence numbers` |
| 含金句通栏 | `no buried highlight text, no same font size as body` |
| 安全合规页 | `no relaxed visuals, no cheerful colors for warnings` |

### 用法
1. 选择最匹配的**基础画像**(R1-R5)
2. 根据页面特征从**微调矩阵**中追加对应规则
3. 组合输出完整反向提示词
