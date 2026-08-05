# 行为快照与怪癖登记(2026-07-23 · Phase 0 测绘;2026-07-27 · P0/P1 重建)

重构期间的行为契约:**任何阶段结束时,下列判定必须全部成立。**

## 一、三层等价判定(golden harness)

| 层 | 判定物 | 基线位置 | 判定方式 |
|---|---|---|---|
| L1 提取层 | 每页 extractPrimitives 产出 | `scripts/test/golden/prims/*.json`(38 页) | 规范化(键排序+浮点4位截断)后深比较 |
| L2 输出层 | playlist 转换后 pptx 内 slide/notes XML | `scripts/test/golden/xml/*.xml`(54 个) | 字符串精确相等(不比 zip 二进制,含时间戳) |
| L3 渲染层 | 每页 1920×1080 浏览器截图 | `scripts/test/golden/shots/*.png`(38 张,不入 git) | PNG 字节相等;不等时落 `.actual.png` 人工复核 |

用法:`node test/golden.js update|verify [--l1|--l2|--l3] [--only <子串>]`。
夹具:`scripts/test/fixtures.json` → `scripts/test/fixtures/slides/` 30 页(22 playlist + 8 独立页)。
2026-07-27 起夹具已 vendored 进技能目录(原位于 ~/dev/html2pptx),路径相对 scripts/test/ 解析,技能目录自包含。
2026-07-23 基线双跑 verify 全绿(100 项),截图在本机字节稳定。

### 2026-07-27 P0 基线重建(全绿 110 项:L1 33 + L2 44 + L3 33)

P0 保真度加固引入的行为变更,逐条复核后一次性重建基线:
1. **box-shadow 真实值化**:`shadow:true` → `{angle,distance,blur,color,opacity}` 对象;命中 07-journey-map、data-limit-boundary 两页(各 4/7 处,均为预期内旧页阴影)。
2. **斜体提取**:runs 新增 `italic:true`;命中 49-four-layer-overview(4 处)、chip-market-share(1 处)——此前斜体被静默丢弃,属缺陷修复。
3. **新增条件键**(只在非默认时写入,旧页零 diff):runs 的 underline/strike/link/fontFace、shape 的 rotate、border 的 dash。
4. **新夹具页** `90-p0-features.html`:锚定斜体/下划线/删除线/超链接/run 级字体/text-transform/虚线+点线边框/真实阴影/纯旋转全链路(入 playlist,L1+L2+L3 三层)。
5. **截图 2x DPI**:`capture.scale:2`,L2 内嵌位图 2 倍像素(L2 只比 slide/notes XML,不含 media 二进制,故 XML 无 diff)。
6. validate 基线:30 文件 / 0 ERROR / 31 WARN(box-shadow 文案随真实值化更新 + 新页 1 条)。

### 2026-07-27 P1 基线重建(全绿 118 项:L1 35 + L2 48 + L3 35)

P1 表现形式扩展引入的行为变更,逐条复核后一次性重建基线:
1. **边框宽度 px→pt 修复**:shape/border-strips 的 line width 改用 `units.pt`(1 CSS px = 0.5 pt);旧实现按 1px=1pt 输出偏粗一倍。影响所有带 border 的形状 L2(8 个 slide XML)。
2. **新基元**:image(`<img>`)/ table / chart(`data-chart`)—— 各自独立提取+渲染;canvas/视觉特效/图标字体走 capture 短路。
3. **文字增强**:LI 直接含文字挂原生 bullet/number;pre/code 保留空白;CODE/KBD/SAMP/TT/VAR 入内联集。
4. **golden 字体时序加固**:collectL1/L3 增 `document.fonts.ready` 等待(封顶 2s),消除 webfont 加载时序导致的 L1 height 抖动(advice-for-newcomers 旧基线 37px 在字体就绪后稳定为 39px)。
5. **新夹具页** `91-p1-forms.html`(img/table/list/pre·code/border-pt)、`92-p1-chart-visual.html`(canvas/chart/blend/clip/icon-font),入 playlist,L1+L2+L3 三层。
6. validate 基线:32 文件 / 0 ERROR / 33 WARN(+2 页各带 mix-blend/clip-path WARN)。
7. **1.6 原生线性渐变(opt-in)延后**:依赖 XML 后处理注入 a:gradFill,风险较高且默认关;保持截图路径(2x DPI 已达标观感),留待 P2 评估。

### 2026-07-27 P2 基线重建(全绿 126 项:L1 37 + L2 52 + L3 37)

P2 首批(2.3 上下标/run 级字距 + 2.4 预设几何 + 1.6 原生线性渐变)引入的行为变更:
1. **上下标**:runs 新增 `sup`/`sub` 条件键(`<sup>`/`<sub>` 标签或 `vertical-align:super/sub`);pptxgenjs 映射 `baseline="30000"`(sup)/`baseline="-40000"`(sub)。旧页零 diff(条件写入)。
2. **run 级字距**:runs 新增 `charSpacing` 条件键(span 级 `letter-spacing` 与 box 级不同时写入);pptxgenjs 映射 `spc`(centipoints)。旧页零 diff。
3. **预设几何**:`data-shape="triangle"` 等属性 → pptxgenjs 80+ 预设形状(`a:prstGeom prst="triangle"` 等);validate 加白名单校验(PRESET_SHAPES 集合)。旧页零 diff(无 data-shape 属性 → 走默认 rect/roundRect/ellipse 判定)。
4. **原生线性渐变(1.6,D2 已拍板)**:`nativeGradient:false` 默认关 → 旧页零 diff。开启时 `linear-gradient` → `gradient` 基元 → 占位色 `addShape` → XML 后处理替换 `a:solidFill` 为 `a:gradFill`(`a:gsLst` + `a:lin ang`);alpha<1/radial/conic 回退截图。角度转换:CSS deg → PPTX `((cssDeg+270)%360)×60000`;色停位置全 null → 均匀分布。
5. **新夹具页** `93-p2-sup-sub-geo.html`(sup/sub/charSpacing/15 种预设几何)、`94-p2-gradient.html`(10 种线性渐变 + radial 回退),入 playlist。
6. validate 基线:34 文件 / 0 ERROR / 41 WARN(+2 页 8 WARN:line-height/box-shadow/rgba 文字)。
7. golden.js 修复:`unlinkSync` 被 genie-safe-delete shim 拦截 → 改用 `rmSync({force:true})` + try/catch;L2 update 逻辑改为覆盖写 + 仅删过期文件。
8. **XML 后处理基础设施**:`core/post-process.js`(JSZip 读 PPTX → 正则替换占位色 → 写回),为 P2 2.5 svgBlip 铺路。

### 2026-08-02 Phase G · golden 样张治理

1. **退役 11 页**:06/16/18(md5 证实重复:05=06、15=16=18)+ 01-21 精简 21→10(留 01/02/03/05/08/09/11/12/15/21;删页均无单页行为锚点)。游离 8 页全保留(行为锚点),其中 4 页(07-journey/49-four/advice/data-limit)进 playlist 补 L2 覆盖。
2. **样张层 12 页**:96-99 + 新增 100-107(议程/大字观点/引用/分栏/对照/时间线/表格/仪表盘),全部新设计语言;`test/exemplar-checks.js` 设计门禁(design.tier=presentation,断言 0 ERROR/0 WARN)。首轮门禁即抓出 9 处问题(填充不足 3 页/正文过小 6 处),逐页修复后全过——门禁有效性实证。
3. **覆盖补齐**:107-dashboard 锚 pie/doughnut/area(chart 全类型齐);fixtures/slides.config.json 开 master(pageNumbers+footer,L2 全体 32 页含 sldNum+golden-fixture);playlist 96-100 挂 fade/push/wipe/cover/split 五档转场(L2 slide21-25 含 p:transition)。
4. **覆盖台账**:`test/FEATURE-COVERAGE.md` 建立(特性→锚定页矩阵+登记硬规则+已知缺口+退役清单)。
5. **基线重建**:L1 39 + L2 64 + L3 39 = 142 项全绿;playlist 重排后 slideN.xml 位移,master 注入(sldNum/页脚)与转场注入为预期变更。survey 重跑:DOM≠z 序页 32→30、重叠倒挂 6 对不变、validate 基线 36 文件/0 ERROR/44 WARN(退役页均 0 WARN，总数不变)。
6. **validate 设计检查二度加固**(样张门禁实证驱动):文字溢出限定固定高度盒+余量随字号缩放(自动高度盒/CJK 度量差豁免);正文下限启发加底部注释区(top≥840)豁免。

1. **环境漂移基线重建**:技能目录改名(html-slides→html-slides-to-pptx)致 91-p1-forms 图片 file:// 路径漂移(L1/L2 各 1 项不等价);人工复核确认为纯路径前缀差异,全量重建基线。
2. **golden.js --only 合并修复**:`update --only` 原先把整份 L1 合并基线覆盖成子集;改为 --only 时先载入既有基线再合并(全量 update 仍整体重写顺带 prune)。回归:--only 后 38 键完整。
3. **原型样张入库**:新增 4 页原型夹具(96-editorial/97-divider/98-statband/99-chart)并入 playlist;基线扩展为 L1 42 + L2 62 + L3 42 = 146 项。
4. **validate 设计检查(tier-gated,旧页零新增 WARN)**:`slides.config.json` 配 `design.tier` 才启用;未配置时 validate 行为与旧版逐字一致(39 文件 / 0 ERROR / 44 WARN 不变)。新检查:文字适配(仅固定高度盒;溢出余量 = max(8, 字号×0.12),CJK 度量差豁免;欠载按内容底边推算)、字号下限(绝对 14px;>20 字正文启发;底部注释区 top≥840 且 ≥ 档内注释下限豁免)、画布填充(页脚区 top≥980 不计;airyPages 配置 + 深底/超大字启发豁免)、对齐(边缘离群簇/等距网格突变/自带视觉子级溢出)。
5. **preview.js 新增**:Step 3.5 视觉自查截图;必须注入 LAYOUT_SCRIPTS 并 resolveAll 后再截图(否则方式 C 页面呈现为堆叠假象)。
6. **主题变量扩容(ADD-only)**:`--zone-*`/`--text-*`/`--space-*` 加入 assets/theme.css 与 16 套预设(parity 全绿);fixtures vendored theme.css 仅同步新变量,字体栈保持 YaHei-first 不动。

### 2026-07-27 P2 第二批(2.1 母版 / 2.2 转场 / 2.6 音视频)

三项均**配置驱动或元素级**,对旧页零 diff(无 video/audio 元素、无 master/transition 配置 → 旧行为不变):
1. **2.1 母版**:`config.master`(pageNumbers/footer/footerColor);`defineSlideMaster` 用 `slideNumber` 属性创建 `sldNum` 占位符(pptxgenjs 4.0.1 的 `objects` 不写入 XML,故页脚用逐页 `addText` 兜底)。
2. **2.2 转场**:playlist 项支持 `{file, transition}` 对象(向后兼容字符串);`postProcessTransitions` 注入 `<p:transition>`(fade/push/wipe/cover/split)。
3. **2.6 音视频**:`<video>`/`<audio>` → media 基元 → `addMedia`;poster 截图做封面;本地文件解析为 data URI;validate 从 ERROR 改为条件 WARN(缺 src/poster 提示)。
4. **新夹具页** `95-p2-master-media.html`(video/audio 元素 + 母版/转场说明),入 playlist。
5. validate 基线:35 文件 / 0 ERROR / 44 WARN(+1 页 3 WARN:audio 画布外/video 缺 src/video 缺 poster)。

## 二、7 条回归红线(2026-07-21 修复,重构中逐条对应保护)

1. 字号换算 1px = 0.5pt(PT_PER_PX = PX2IN × 72,必须与几何同比例)
2. 行高用绝对磅值 spcPts,非百分比(多行才设;单行靠 valign 居中)
3. 截图前隐藏**页面上全部文字**(`capture.hideTextCss`,默认 `*{color:transparent !important; text-shadow:none !important;}`),避免文字烙进 PNG 重影。
   ⚠️ 2026-07-23 修复:旧实现只隐藏 `[data-object-type="textbox"]` 内的文字;方式 B/C 下文字可作为 shape 对象子元素存在,导致烙字重影。
   依据:任何可见文字都会被提取为原生文本框,故截图不应保留任何文字。回归测试 `test/capture-text-test.js`(像素级颜色断言)。
4. SVG 元素无法拆原生形状 → 整体截图还原(SVG 内文字走 fill 渲染,不受 color 隐藏影响,整体保留在截图中,语义正确)
5. 非统一边框逐边画细条(各边用自己的宽度/颜色)
6. flex/grid 容器子元素块级化递归提取,不拍平成一行
7. 元素 opacity 折算进形状填充透明度(文字仍按不透明处理)

## 三、4 项怪癖决策(Phase 0 测绘结论)

### H1 · FONT_MAP —— 2026-07-23 起默认开启(用户决策)
历史上 `mapFont` 曾是死代码(从未调用),PPTX 写入页面原字体名;重构后修复为可配置。
**决策(2026-07-23 用户拍板):默认开启字体映射**——Noto Sans SC / PingFang SC → Microsoft YaHei,Inter → Arial。
理由:PPTX 受众(Windows/Office)大多没装 Noto Sans SC / Inter,原字体名会随机回退。
需要原字体名时,在项目级 `slides.config.json` 设 `{ "applyFontMap": false }`。
L2 黄金基线已于当日按新默认重建(变更经剔除 typeface 后 XML 逐字节一致验证)。

### H2 · 嵌套 data-object 会被双重提取 —— 定为非法
`querySelectorAll('[data-object="true"]').forEach(walk)` 会把内层对象既当外层后代、又当独立 root 各走一遍。
**测绘:29 页嵌套数为 0。**
**决策**:Phase 2 起嵌套标记 = validate ERROR;提取器加去重护栏(内层 root 跳过,作为外层后代仍被提取)。护栏对基线无影响(为 0)。

### H3 · z 序 = DOM 遍历序,不是 z-index —— 保持 DOM 序,修订规范
提取器按 DOM 遍历 `zSeq++` 发号,PPTX 按此序叠放;规范却写"z-index 决定叠放"。
**测绘:28/29 页 DOM 序 ≠ z-index 序**(z-index 只影响浏览器合成即截图层;不一致多为不重叠元素,无视觉分叉)。
**决策**:语义保持 DOM 序(否则 28 页基线全变);规范改述为"PPTX 叠放由 DOM 顺序决定;**有重叠时须让 DOM 顺序与期望叠放一致**(z-index 仅影响浏览器内合成)"。Phase 2 validator 新增:重叠 data-object 的 z-index 与 DOM 序倒挂 → WARN。

### H4 · grid 子元素未块级化 —— 修复安全
`hasBlockChild` 只认 `display.includes("flex")`;CSS 规范中 grid item 同样块级化,"grid 容器+纯内联子级"会被错误拍平成一个文本段。
**测绘:29 页无此形态(0 处)。**
**决策**:Phase 2 修复为 flex||grid 均块级化,对基线零影响。

### H5 · 新样式键一律条件写入(2026-07-27 P0 纪律)
runs/基元上的新能力键(italic/underline/strike/link/fontFace/rotate/dash)**只在非默认时出现**,
保证不含对应写法的旧页面 L1 零 diff —— P0 期间旧 29 页仅阴影与斜体两类预期 diff。
**决策**:后续新增基元字段默认遵守同一纪律;确需恒写时单独评审。

### H6 · 旋转还原的双轨几何(2026-07-27)
纯色形状/文字:未旋转几何(offset 链)+ 原生 rotate 参数;渐变/图片/SVG(截图类):
用旋转后包围盒截图、不标 rotate(图像已含旋转视觉)。两类不得混用。
`transform-origin` 非居中 → validate WARN(PPTX 恒绕中心旋转)。
`unrotatedRectOf` 用 offsetWidth/Height(整数,≤0.5px 误差),链断回退 getBoundingClientRect。

### H7 · currentColor 在截图时变透明(2026-08-05 第三轮 B0 实测)
`capture.hideTextCss = "*{color:transparent !important}"` → SVG 的 `stroke/fill="currentColor"`
在截图 pass 中解析为透明,产出空白 PNG(浏览器预览正常,转换后图标消失,极隐蔽)。
**纪律**:SVG 图标的 stroke/fill 一律显式 hex(或 `style="stroke:var(--色)"`——CSS 属性不受 color 隐藏影响);
layout-checks 规则 0 静态 WARN 兜底;`assets/icons.md` 全库遵守。
**附带结论**:`<use href="外部.svg#id">` 在 file:// 页面中不渲染(B0.3)→ 图标库走纯内联片段,不建 symbol 集。

### H8 · data-shape 的浏览器预览近似(2026-08-05 第三轮)
浏览器不认识 pptxgenjs 预设几何,data-shape 元素在网页端渲染为矩形,PPTX 端才是真形状。
preview.js 截图前注入 **clip-path 近似**(triangle/trapezoid/chevron/homePlate 等 14 种),
仅影响自查截图(页面文件不动、convert 走原生形状;比例为近似值,供视觉对位)。
L3 golden 截图不含 clip-path(走 golden.js 自身管线),基线语义不变。

### H9 · golden 比对的两个冗余消除(2026-08-05 瘦身)
① L2 的 notesSlide 逐文件锚定是 N 次重复(notes 管线=单一特性)→ **合并为单项比对**,
   失败时 `diffNotesDetail` 逐文件列出差异。② L3 截图对**纯原生页**与 L1 冗余
   (颜色/字体/几何全在 prims 里)→ **仅含 capture 基元的页做 L3**(判定与 L1 同源,
   extract 退化会先触发 L1 失败);页面内容变化会自动重入/退出 L3 集合,自维护。
全量 update 会 prune 无 shot 页的 PNG 与孤儿文件(退役页/.actual 残留)。

### H10 · INLINE_TAGS 补全(2026-08-05 复杂度压测)
原集合只有 SPAN/I/B/A/SUP 等,漏了 U/S/DEL/INS/MARK 等短语内容行内标签。
直接写 `<u>`/`<s>`(html-spec 4.1 宣称支持)时 hasBlockChild 误判 li"有块级子元素"
→ ①li 丢原生 bullet ②标签前的文本节点被 walk 跳过而**丢字**("中间夹<u>u</u>"提取成"夹 u")。
**修复**:INLINE_TAGS 补全 20 个行内标签(U/S/DEL/INS/MARK/SMALL/ABBR/CITE/Q/DFN/BDO/WBR/
LABEL/BUTTON/SELECT/TEXTAREA/OUTPUT/PROGRESS/METER)。90-p0-features 的 u/s demo 行
从碎 textbox+丢字恢复为完整行(基线已重建,复核为修复而非回归)。

### H11 · 原生 bullet 从未真正渲染(2026-08-05 复杂度压测 · P1 遗留缺陷)
extract 挂的 bullet 对象 `{type:"bullet", characterCode:"2022"}` 踩中 pptxgenjs 序列化
**type 优先**逻辑:type 存在且非 "number" → characterCode 分支永不执行 → **PPTX 里从来没有
项目符号**(91-p1-forms 锚定页的 L2 基线一直锁着无 buChar 的 XML;P1 验收抽检看漏)。
OL 的字段名 `numberType` 也无效(pptxgenjs 用 `style`)。
**修复**:UL 去 type(`{characterCode:"2022", indent:14}`);OL 改 `{type:"number", style:"arabicPeriod", indent:14}`。
修复后 91 页 XML 出现 buChar×5,压测页 buChar×3。基线已重建。

### H12 · 表格行级底纹从未生效(2026-08-05 真实场景页 · P1 遗留缺陷)
表格底纹主流写法是 `<tr style="background:...">`,但 CSS background **不继承到 td**,
table.js 只取 `getComputedStyle(td).backgroundColor` → 恒为 transparent → **深蓝表头/zebra
底纹全部丢失**,白字落白底不可见。106-table-focus(表格样张锚定页)正是该写法,
L2 基线一直锁着无底纹 XML;L3 免截纯原生页 → 视觉缺陷全程隐形(与 H11 同款模式)。
**修复**:底纹提取沿 td → tr → table 回溯取第一个非透明背景(`cellBg`);rgba(…,0) 视为无。
修复后 02 页表头 fill=0A2E5C、106 页表头 0A2E5C + zebra FAFBFC。基线已重建。

## 四、validate 基线

35 页现状:**0 ERROR / 44 WARN**(逐字存于 `scripts/test/golden/validate-baseline.txt`)。
后续各阶段对旧 34 页的 validate 输出**不得新增**任何 ERROR/WARN(新规则只对新写法生效)。

### validate 工程约束(2026-07-27 补记)

- `page.evaluate(fn, arg)` **只接受一个参数** —— domChecks 的画布尺寸以 `{w,h}` 单对象传入。
- 静态检查正则须用负向后行 `(?<![\w-])transform\s*:` 排除 `text-transform`。
- transform-origin 居中判定用 `offsetWidth/Height`(未旋转尺寸);getBoundingClientRect 是旋转后包围盒,会误报。

## 五、已知可接受 WARN 类型(基线内)

速查 html-spec.md 第 8 节速查表:box-shadow 近似、rgba 文字退化、writing-mode 实验性等,基线中的 30 条 WARN 均属此类,逐条人工确认过可接受。

## 六、决策点登记(D2-D6,2026-07-27 用户拍板)

> OPTIMIZATION-PLAN.md 第 6 节列出的 6 个决策点,D1 已在 P0 实施时解决(一次性基线重建);D2-D6 经用户拍板,登记如下,作为 P2 实施的硬约束。

### D2 · 原生线性渐变 → 引入但默认关(`nativeGradient:false`),P2 实施
- **决策**:接受建议。配置项已落地(`scripts/config/default.config.js` 新增 `nativeGradient:false` 占位)。
- **范围**:仅 `linear-gradient`。`radial/conic-gradient` 恒走截图,与本开关无关。
- **P2 实施要点**:`extract/primitives/gradient.js`(解析角度+色停)→ 渲染端 XML 后处理注入 `a:gradFill`(pptxgenjs 4.0.1 不支持渐变填充,必须后处理)。色停含 alpha/hint 超集时回退截图(与截图路径零分叉)。
- **回退兜底**:开关关时,渐变走 `capture` 截图(2x DPI),观感达标但不可编辑——**这是当前默认行为**,无回归风险。

### D3 · 不引入 `sharp` 等原生依赖
- **决策**:接受建议。技能依赖保持仅 `playwright` + `pptxgenjs` 两个纯 JS 包。
- **理由**:`sharp` 是平台二进制(node-addon),分发型技能在用户机上 `npm install` 时需编译/下载二进制,增加安装失败面与体积;SVG 高倍渲染/图片预裁用浏览器端 canvas 已够(`<img>` cover 已走 canvas 预裁)。
- **约束**:后续任何 P2 项(svgBlip 2.5、字体子集 2.7、感知 diff 2.9)若需要图像处理,**优先用浏览器端 canvas / Jimp(纯 JS)**,不引入原生模块。

### D4 · 字体嵌入(2.7)延后至 P2 末,先用"字体映射 + 目标机常用字"策略
- **决策**:接受建议。P2 阶段把 2.7 放到**最末**;此前先用现行 H1 FONT_MAP 策略(Noto Sans SC/PingFang SC → Microsoft YaHei,Inter → Arial)。
- **触发条件**:字体嵌入在以下任一条件成立时再评估实施——
  ① 用户明确反馈 PPT 端字形漂移影响观感(且 FONT_MAP 已无法覆盖);
  ② 出现非 Windows/Office 的 PPT 受众(如 macOS Keynote 导入);
  ③ P2 其他项全部完成,工程余量充足。
- **理由**:字体子集化 + `fntdata` 部件注入工作量大、PPT 端兼容性参差(不同 Office 版本对嵌入字体行为不一),投入产出比目前不划算;FONT_MAP 策略在 Windows/Office 受众下已开箱即用。

### D5 · 密度三档参数扩充(表格行数 / 图表系列数上限)→ 已落地
- **决策**:接受建议。`reference/density-tiers.md` 档位参数表新增两行——
  - **单页表格行数上限**:演讲 ≤6 / 混合 ≤8 / 阅读 ≤12(含表头)
  - **单页图表系列数上限**:演讲 ≤3 / 混合 ≤4 / 阅读 ≤6
- **执行规则**(已写入 density-tiers.md 第 5 条):表格超限 → 演讲/混合档拆页或转附件页,阅读档换紧凑行距(仍受"单页正文总行数上限"约束);图表系列超限 → 拆为多图(每图 ≤ 上限),禁止用堆叠/双轴硬塞。可读性优先于信息量。

### D6 · `<img>` 解禁后的契约 → 已落地
- **决策**:接受建议。两种放图方式各司其职:
  - **装饰图**(渐变/几何/抽象纹理)→ 优先 `background-image` on `data-object="shape"`(走截图路径,2x DPI,可叠加圆角/混合模式/clip-path)
  - **内容照片/产品图/可替换图片** → `<img data-object="true">`(原生 `a:blip` 嵌入,可编辑替换)
- **硬契约**:`<img>` **必须显式声明 `object-fit`**(`cover`/`contain`/`fill`/`none`);缺省时 validate 报 WARN(默认 `fill` 会拉伸变形,且与"忘了写"无法区分)。
- **实施状态**:`html-spec.md` 新增 5.2.1 节契约说明 + 速查表行更新;`dom-checks.js` 新增第 10 项 `<img>` 缺 object-fit 的 WARN;新规则对旧 32 页 validate 基线**零影响**(P1 夹具页的 `<img>` 均已显式 object-fit,32 文件 / 0 ERROR / 33 WARN 不变)。
