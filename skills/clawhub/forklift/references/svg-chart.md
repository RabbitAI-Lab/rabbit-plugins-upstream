<!--
Copyright (c) 2026 杨鹏飞 / 微信公众号「叉车技术老炮」
Licensed under the MIT License - 完整协议见 ../LICENSE.md
-->
# 叉车图表生成模块（SVG 默认输出）

> 本模块自 **v2.4** 起为**图表输出的默认路径**。
> 核心变更:凡属"数值对比 / 份额 / 趋势 / 排行"类图表,
> **默认生成自包含 SVG 图片**,ASCII 图降级为**离线兜底或纯文本终端**场景下的可选方案。
>
> 触发范围:销售排行、市场份额、月度走势、品牌对比、区域分布、TCO 分解、
> 维保成本对比等一切"本该配图"的回答。

---

## 一、为什么默认改 SVG（v2.4 变更动因）

| 维度 | ASCII 柱状图（v2.3 默认） | SVG 图片（v2.4 默认） |
|------|--------------------------|----------------------|
| 可读性 | 字符对齐依赖字体,移动端易折行 | 精确排版,任意端一致 |
| 表达能力 | 仅横向条形 | 柱/条/折线/饼/环形/堆叠/散点 |
| 信息密度 | 单系列,1 个维度 | 多系列、双轴、标注、数据标签 |
| 复用性 | 复制即乱 | 可截图、可嵌入公众号、可转 PNG |
| 依赖 | 无（纯文本） | 无（内联 SVG,不引 CDN） |
| 场景 | 终端、纯文本渠道 | 网页 / App / 图文 / 报告 |

> ⚠️ **兼容声明**:ASCII 图**并未删除**,而是从"默认"降为"备选"。
> 用户明确说"要文本图""终端里看""不要图片"时,仍按 `sales-news.md`
> 第 6 节的 ASCII 规则输出。

---

## 二、硬规则（给 LLM 的执行约束）

1. **默认 SVG**:凡涉及数值对比/份额/趋势,输出 **1 个及以上内联 SVG**。
2. **零外部依赖**:不得引用 CDN、外链字体、外部 JS。字体用系统字体栈。
3. **自包含**:SVG 必须能单独存成 `.svg` 文件后直接打开渲染。
4. **中文可读**:`font-family` 必须回退到中文字体
   (`-apple-system, "PingFang SC", "Microsoft YaHei", sans-serif`)。
5. **色彩规范**:沿用作者视觉规范——主色 **深蓝 `#1a2a4a`**,
   强调色 **橙 `#ff6b35`**;对比组可用 `#2e7d32`(绿) / `#9e9e9e`(灰)。
6. **必须带数据标签**:每根柱子/每个扇区直接标数值,不靠读者目测。
7. **必须带标题与来源**:图表内含 `<title>` 与底部来源行
   ("数据来源:xxx,检索日期 YYYY-MM-DD")。
8. **必须带无障碍属性**:根 `<svg>` 带 `role="img"` 与 `<title>`/`<desc>`。
9. **配色对比度**:文字与背景对比度 ≥ 4.5:1,禁止浅灰字配白底。
10. **超量程处理**:数值差距 > 20 倍时用对数映射或断裂标记,并显式注明。
11. **禁止占位图**:不得输出 example.com 之类的假图片链接。
12. **表格必留**:SVG 之外仍保留 Markdown 表格（精确值 + 可复制）。

---

## 三、SVG 骨架模板（直接套用）

### 3.1 横向条形图（品牌销量对比 / 排行）

```html
<svg viewBox="0 0 720 420" width="100%" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-labelledby="t1 d1"
     font-family='-apple-system,"PingFang SC","Microsoft YaHei",sans-serif'>
  <title id="t1">2026年X月 中国叉车品牌销量排行（万台）</title>
  <desc id="d1">横向条形图，安徽合力 4.2 万台居首，杭叉集团 3.8 万台次之。</desc>

  <!-- 背景 -->
  <rect width="720" height="420" fill="#ffffff"/>

  <!-- 标题 -->
  <text x="24" y="36" font-size="18" font-weight="700" fill="#1a2a4a">
    中国叉车品牌销量排行
  </text>
  <text x="24" y="58" font-size="12" fill="#6b7280">单位：万台　截至 2026-08</text>

  <!-- 坐标轴基线 -->
  <line x1="140" y1="80" x2="140" y2="360" stroke="#d1d5db" stroke-width="1"/>
  <line x1="140" y1="360" x2="680" y2="360" stroke="#d1d5db" stroke-width="1"/>

  <!-- 网格线（可选，4 条） -->
  <g stroke="#f3f4f6" stroke-width="1">
    <line x1="140" y1="290" x2="680" y2="290"/>
    <line x1="140" y1="220" x2="680" y2="220"/>
    <line x1="140" y1="150" x2="680" y2="150"/>
  </g>

  <!-- 数据条：y 每行 46px，条高 26px -->
  <!-- 第 1 行（强调色 / 第一名用橙色） -->
  <rect x="140" y="88"  width="480" height="26" rx="3" fill="#ff6b35"/>
  <text x="132" y="106" font-size="13" fill="#1a2a4a" text-anchor="end">安徽合力</text>
  <text x="628" y="106" font-size="13" font-weight="700" fill="#ffffff" text-anchor="end">4.20</text>

  <!-- 第 2 行 -->
  <rect x="140" y="134" width="432" height="26" rx="3" fill="#1a2a4a"/>
  <text x="132" y="152" font-size="13" fill="#1a2a4a" text-anchor="end">杭叉集团</text>
  <text x="580" y="152" font-size="13" font-weight="700" fill="#ffffff" text-anchor="end">3.78</text>

  <!-- 第 3 行起按同规则递增 y=46 -->

  <!-- 底部来源 -->
  <text x="24" y="398" font-size="11" fill="#9ca3af">
    数据来源：CITA 工业车辆分会　检索日期 2026-09-12
  </text>
</svg>
```

**条形宽度换算公式**：

```
bar_width = 最大条宽 480 × (本项数值 / 最大值)
text_x    = 140 + bar_width - 8      # 白色数字右对齐于条内
row_y     = 88 + (行号 - 1) × 46
```

### 3.2 分组柱状图（国内 vs 国外 / 多年份对比）

```html
<svg viewBox="0 0 720 400" width="100%" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-labelledby="t2"
     font-family='-apple-system,"PingFang SC","Microsoft YaHei",sans-serif'>
  <title id="t2">国内品牌 vs 国外品牌在华销量对比</title>
  <rect width="720" height="400" fill="#ffffff"/>
  <text x="24" y="36" font-size="18" font-weight="700" fill="#1a2a4a">
    国内品牌 vs 国外品牌（在华销量 · 万台）
  </text>

  <!-- 图例 -->
  <rect x="470" y="22" width="14" height="14" fill="#1a2a4a"/>
  <text x="490" y="34" font-size="12" fill="#1a2a4a">国内品牌</text>
  <rect x="566" y="22" width="14" height="14" fill="#ff6b35"/>
  <text x="586" y="34" font-size="12" fill="#1a2a4a">国外品牌</text>

  <!-- 轴 -->
  <line x1="70" y1="70" x2="70" y2="330" stroke="#d1d5db"/>
  <line x1="70" y1="330" x2="680" y2="330" stroke="#d1d5db"/>

  <!-- 分组：每组 2 柱，组宽 120，柱宽 44，间隙 8 -->
  <!-- 第 1 组 x=110 -->
  <rect x="110" y="120" width="44" height="210" rx="2" fill="#1a2a4a"/>
  <text x="132" y="112" font-size="12" font-weight="700" fill="#1a2a4a" text-anchor="middle">12.60</text>
  <rect x="162" y="265" width="44" height="65" rx="2" fill="#ff6b35"/>
  <text x="184" y="257" font-size="12" font-weight="700" fill="#ff6b35" text-anchor="middle">3.90</text>
  <text x="158" y="352" font-size="12" fill="#1a2a4a" text-anchor="middle">2026-08</text>

  <text x="24" y="382" font-size="11" fill="#9ca3af">
    数据来源：CITA / 海关总署　检索日期 2026-09-12
  </text>
</svg>
```

### 3.3 折线图（月度 / 年度趋势）

```html
<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-labelledby="t3"
     font-family='-apple-system,"PingFang SC","Microsoft YaHei",sans-serif'>
  <title id="t3">锂电叉车渗透率走势</title>
  <rect width="720" height="380" fill="#ffffff"/>
  <text x="24" y="36" font-size="18" font-weight="700" fill="#1a2a4a">
    锂电叉车渗透率走势（%）
  </text>

  <!-- 坐标轴 -->
  <line x1="70" y1="70" x2="70" y2="310" stroke="#d1d5db"/>
  <line x1="70" y1="310" x2="680" y2="310" stroke="#d1d5db"/>

  <!-- 折线：x 均分 (680-70)/(n-1)，y = 310 - (值-下限)/(上限-下限)*240 -->
  <polyline points="70,220 190,196 310,168 430,140 550,110 670,86"
            fill="none" stroke="#ff6b35" stroke-width="3"
            stroke-linejoin="round" stroke-linecap="round"/>

  <!-- 数据点 + 标签 -->
  <circle cx="70"  cy="220" r="4" fill="#1a2a4a"/>
  <text x="70"  y="200" font-size="11" fill="#1a2a4a" text-anchor="middle">52</text>
  <circle cx="190" cy="196" r="4" fill="#1a2a4a"/>
  <text x="190" y="176" font-size="11" fill="#1a2a4a" text-anchor="middle">58</text>
  <!-- ... 依次补全 -->

  <!-- 底部刻度标签 -->
  <text x="70"  y="332" font-size="11" fill="#6b7280" text-anchor="middle">2025-03</text>
  <text x="670" y="332" font-size="11" fill="#6b7280" text-anchor="middle">2026-08</text>

  <text x="24" y="362" font-size="11" fill="#9ca3af">
    数据来源：CITA 工业车辆分会　检索日期 2026-09-12
  </text>
</svg>
```

### 3.4 环形图（市场份额 / 结构占比）

```html
<svg viewBox="0 0 720 400" width="100%" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-labelledby="t4"
     font-family='-apple-system,"PingFang SC","Microsoft YaHei",sans-serif'>
  <title id="t4">叉车动力结构占比</title>
  <rect width="720" height="400" fill="#ffffff"/>
  <text x="24" y="36" font-size="18" font-weight="700" fill="#1a2a4a">动力结构占比</text>

  <!-- 环形用 stroke-dasharray 实现，r=90，周长 = 2πr ≈ 565.5 -->
  <g transform="translate(200,210)">
    <circle r="90" fill="none" stroke="#e5e7eb" stroke-width="42"/>
    <!-- 锂电 68% -->
    <circle r="90" fill="none" stroke="#ff6b35" stroke-width="42"
            stroke-dasharray="384.5 565.5" transform="rotate(-90)"/>
    <!-- 铅酸 22%：绕到 68% 起点（244.8°） -->
    <circle r="90" fill="none" stroke="#1a2a4a" stroke-width="42"
            stroke-dasharray="124.4 565.5" transform="rotate(154.8)"/>
    <!-- 内燃 10%：绕到 90% 起点（324°） -->
    <circle r="90" fill="none" stroke="#9ca3af" stroke-width="42"
            stroke-dasharray="56.6 565.5" transform="rotate(234)"/>
    <text y="4" font-size="26" font-weight="700" fill="#1a2a4a" text-anchor="middle">68%</text>
    <text y="24" font-size="12" fill="#6b7280" text-anchor="middle">锂电占比</text>
  </g>

  <!-- 图例：右侧纵向排列 -->
  <g transform="translate(420,150)">
    <rect width="14" height="14" fill="#ff6b35"/>
    <text x="22" y="12" font-size="13" fill="#1a2a4a">锂电 68%</text>
    <rect y="34" width="14" height="14" fill="#1a2a4a"/>
    <text x="22" y="46" font-size="13" fill="#1a2a4a">铅酸 22%</text>
    <rect y="68" width="14" height="14" fill="#9ca3af"/>
    <text x="22" y="80" font-size="13" fill="#1a2a4a">内燃 10%</text>
  </g>

  <text x="24" y="382" font-size="11" fill="#9ca3af">
    数据来源：CITA 工业车辆分会　检索日期 2026-09-12
  </text>
</svg>
```

**扇形换算公式（环形）**：

```
C        = 2πr                      # r=90 → 565.5
segment  = C × 占比
起始角度  = 90% 累计占比 × 360 - 90      # 从 12 点钟方向顺时针
transform= rotate(起始角度)
```

---

## 四、图表选型决策表

| 数据形态 | 推荐图表 | 关键参数 |
|----------|----------|----------|
| 单系列绝对量排行 | 横向条形图 | 首名用 `#ff6b35`,其余 `#1a2a4a` |
| 两系列同维度对比 | 分组柱状图 | 国内 `#1a2a4a` / 国外 `#ff6b35` |
| 3 个以上系列 | 堆叠柱状图 | 色阶:`#1a2a4a`→`#ff6b35`→`#2e7d32`→`#9ca3af` |
| 时间序列趋势 | 折线图 | 线宽 3,数据点 r=4 |
| 结构占比（≤5 项） | 环形图 | 中心放核心指标 |
| 结构占比（>5 项） | 100% 堆叠条 | 避免扇区过细 |
| 双指标（量 + 率） | 柱 + 折线组合 | 左轴柱、右轴线(虚线) |
| 正负增长 | 双向条形图 | 正橙/负灰,零轴居中 |

---

## 五、多图编排规则

一张 SVG 装不下的信息,按以下优先级拆分:

```
必选 1：核心结论图     ← 回答主问题的那个数字
可选 2：对比图         ← 国内 vs 国外 / 本期 vs 上期
可选 3：趋势图         ← 时间维度,证明"在涨还是在跌"
上限   ：3 张          ← 超过 3 张改为附录,避免淹没结论
```

> SVG 与 Markdown 表格**并存**:SVG 负责"一眼看懂",
> 表格负责"精确可复制"。二者不可互相替代。

---

## 六、ASCII 降级条件（何时仍用 ASCII）

只有满足以下**任一**条件,才切回 `sales-news.md` 的 ASCII 柱状图:

1. 用户明确要求:"用 ASCII""文本图""终端里看就行""不要图片"
2. 宿主环境明确不支持 HTML/SVG 渲染(如纯 CLI、纯文本渠道)
3. 用户要求把结果粘贴进代码块 / Markdown 纯文本邮件
4. 数量级跨度过大且用户只关心"谁高谁低"

切换时**必须说明一句**:"当前按文本模式输出 ASCII 图,如需图片版请说一声。"

---

## 七、常见错误（避坑）

| ❌ 错误 | 后果 | ✅ 正确做法 |
|--------|------|-----------|
| SVG 里引 CDN 字体/JS | 离线打不开 | 用系统字体栈,纯静态 |
| 忘记 `viewBox` | 缩放错乱 | 必须有 `viewBox="0 0 W H"` |
| 固定 `width` 像素 | 移动端溢出 | `width="100%"` + `viewBox` |
| 不写数据标签 | 读者只能目测 | 每柱/每点/每扇区标数值 |
| 深色底配深色字 | 看不清 | 对比度 ≥ 4.5:1 |
| 一图塞 10+ 系列 | 无法辨识 | 拆分或多图 |
| 无标题无来源 | 不可引用 | `<title>` + 底部来源行 |
| 只用 SVG 删掉表格 | 失去精确值 | SVG + 表格并存 |
| 编造数据画图 | 数据造假 | 图上的每个数必须可溯源 |

---

## 八、与其他模块的协同

| 用户问题 | 图表模块职责 | 数据模块 |
|----------|-------------|----------|
| 销量排行 | 条形图 + 分组柱状图 | `sales-news.md` |
| 市场份额 | 环形图 | `market-trends.md` |
| 招投标汇总 | 区域 + 金额条形图 | `tender-broadcast.md` |
| 标准实施时间线 | 时间轴图 | `standards.md` |
| 维保成本对比 | 分组柱状图 | `maintenance-plan.md` |
| 二手残值曲线 | 折线图 | `used-forklift-evaluation.md` |

---

## 九、不在范围内

- 动态交互图表（hover tooltip、下钻）→ 静态 SVG 不承担,需要时提示用户走 Web 前端方案
- 地图可视化（省界热力图）→ 需要 GeoJSON 数据,超出自包含范围,可用"区域条形图"替代
- 3D 图、动画 → 不适用纯 SVG 静态输出
- 未联网核实的估算值 → 不给图

---

## 十、版本与更新

- 模块版本:**v1.0(2026-09)**
- 配套 Skill:forklift-expert **v2.5**
- 变更要点:图表默认路径由 ASCII 改为 SVG;ASCII 降级为可选兜底
- 已知局限:SVG 在部分 Markdown 渲染器(如某些 IDE 预览、纯 CLI)不渲染,
  此时自动降级并提示
