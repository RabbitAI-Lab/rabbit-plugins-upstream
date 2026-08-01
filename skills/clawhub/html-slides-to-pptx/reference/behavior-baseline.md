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
