# 特性覆盖矩阵(FEATURE-COVERAGE)

> golden fixtures 的"特性 → 锚定页"台账(2026-08-02 Phase G 建立)。
> **登记规则(硬约束)**:
> 1. 新增转换器特性(基元/样式/元素/配置)时,必须指定锚定页并更新本表;无锚定页的特性不得合并。
> 2. 删除夹具页前,先查本表确认它不是某特性的唯一锚点。
> 3. 样张页(96-107)同时受 `test/exemplar-checks.js` 设计门禁(0 ERROR/0 WARN)。
> 页面角色:fidelity 锚(01-21 精简页/游离页/特性页)= 转换保真;exemplar 样张(96-107)= 保真+设计纪律双锚。

## 一、文字类

| 特性 | 锚定页 | 备注 |
|---|---|---|
| 斜体 `<i>/<em>` | 90-p0-features、49-four-layer、chip-market-share | 49-four/chip 是历史缺陷修复锚 |
| 下划线 / 删除线 / 超链接 | 90-p0-features | run 级 |
| run 级字体 fontFace | 90-p0-features、96-107(`.num`) | `.num` Inter 混排是真实场景锚 |
| text-transform | 90-p0-features | uppercase/lowercase |
| 上下标 `<sup>/<sub>` | 93-p2-sup-sub-geo | baseline 30000/-40000 |
| run 级字距 charSpacing | 93-p2-sup-sub-geo | 与 box 级独立 |
| 原生列表 `<ul>/<ol>` bullet | 91-p1-forms | LI 直接含文字挂 bullet |
| pre/code 空白保留 | 91-p1-forms | white-space:pre |
| 竖排 writing-mode | 49-four-layer | 实验性 eaVert(基线 WARN) |
| 混合字号行 | 98-statband、107-dashboard | 大数字+单位,行高按最大 run |
| 500 字重退化 WARN | advice-for-newcomers、ai-trends-2026、four-revolutions | validate 基线锚 |

## 二、形状/装饰类

| 特性 | 锚定页 | 备注 |
|---|---|---|
| 纯色形状 / 圆角 / 正圆 | 全体 | 基础 |
| 统一边框 | 02 等 | px→pt(0.5 倍) |
| 非统一边框逐边细条 | 02、12 | 圆角共存 WARN 锚 |
| 虚线/点线 dashType | 90-p0-features | dashed→dash,dotted→sysDot |
| box-shadow 真实参数 | 07-journey-map、data-limit-boundary、90 | 历史缺陷修复锚(行为红线) |
| 纯旋转 rotate | 90-p0-features、93-p2-sup-sub-geo | origin 居中约束 |
| data-shape 预设几何 | 93-p2-sup-sub-geo | 15 种(白名单 80+) |
| 不透明度 opacity 折算 | 全体(基础路径) | 形状填充折算 |

## 三、背景/媒体类

| 特性 | 锚定页 | 备注 |
|---|---|---|
| 渐变(截图路径,默认) | 01、94-p2-gradient | 2x DPI |
| 原生线性渐变 a:gradFill | **已知缺口(有意)** | `nativeGradient` 默认关;开启路径由 convert 冒烟覆盖,未入 golden(见"五") |
| `<img>` 原生图片 | 91-p1-forms | object-fit 映射;file:// 路径(注意环境漂移) |
| `<table>` 原生表格 | 91-p1-forms、106-table-focus | colspan/底纹/边框/右对齐 |
| `<canvas>` 截图 | 92-p1-chart-visual | 可见化保底 |
| data-chart:bar | 92-p1-chart-visual | 原生图表 |
| data-chart:line | 99-archetype-chart | |
| data-chart:pie / doughnut / area | 107-dashboard | 2026-08-02 Phase G 补锚 |
| `<svg>` 截图 | data-limit-boundary | 整体截图含文字 |
| `<video>` / `<audio>` | 95-p2-master-media | addMedia;poster 封面 |
| 图标字体自动截图 | 92-p1-chart-visual | iconFonts 命中 |
| mix-blend-mode / clip-path 转截图 | 92-p1-chart-visual | 视觉特效 |

## 四、布局/页面级

| 特性 | 锚定页 | 备注 |
|---|---|---|
| 方式 A 绝对定位 | 全体 | |
| 方式 B flex/grid 流式 | 02、96-editorial、104-comparison | |
| 方式 C data-layout(columns/grid) | 98-statband、103-split-7-5、107-dashboard | 解析器改写 |
| 母版 pageNumbers + footer | **全体 L2 页**(fixtures/slides.config.json) | 2026-08-02 Phase G 开启 |
| 转场 fade/push/wipe/cover/split | 96/97/98/99/100(playlist 项) | 2026-08-02 Phase G 开启,五档齐 |
| 深底容器背景导出 | 97-archetype-divider、01 | |
| 演讲者备注 template | 全体 | notesSlide XML |
| 增量缓存 | L2 全 deck | hash 命中/失效 |

## 五、行为锚点(回归红线活证据,删页红线)

| 页 | 锚定的历史行为 |
|---|---|
| 49-four-layer-overview | 斜体提取修复(4 处)+ 竖排 eaVert |
| chip-market-share | 斜体提取修复(1 处) |
| 07-journey-map | box-shadow 真实值化(4 处) |
| data-limit-boundary | box-shadow 真实值化(7 处)+ SVG 截图 |
| advice-for-newcomers | 字体时序加固(L1 height 抖动 37→39px) |
| ai-trends-2026 / four-revolutions | 500 字重 WARN 基线 |

## 六、已知缺口(有意/待办)

| 缺口 | 状态 | 说明 |
|---|---|---|
| 原生渐变(nativeGradient:true)渲染路径 | 有意未入 golden | D2 拍板默认关;建议后续建第二 playlist(独立 config)锚定 |
| validate ERROR 触发路径 | 未系统锚定 | 目前以 0 ERROR 通过反向验证;ERROR 构造用例散见于开发期,低优先 |
| 全出血大图页(原型 11)/ 图文页(原型 10) | 样张未含 | 图片型页面已有 91 img 锚定;后续按需要补样张 |

## 七、corpus 账本(2026-08-02 Phase G 定稿)

- L1/L3:36 页 + 模板 3(extraPages)= 39
- L2 playlist:32 页(10 精简 deck + 4 游离 + 6 特性 + 12 样张)
- 退役:06/16/18(重复)+ 04/07/10/13/14/17/19/20(精简)= 11 页
