# 页面原型库(page-archetypes · 30 个原型)

> **口径(2026-08-06 第六轮 P1 归一)**:全库 **30 个编号原型**(`### 原型 1` … `### 原型 30`)。
> 此前标题写"28 个原型 30 款"、而 narrative-skeletons/creative-layouts 写"20 原型"——
> 三处三个数,且"20 原型"的说法让**图示组(23-30)在引用方的自我描述里不存在**。
> 现统一为"30 个原型",由 `test/generation-checks.js` D1 实测编号数并断言各文档措辞一致。

> ⚠️ **别通读本文件(1000+ 行)。** 用法是**查索引 → 跳到那一个原型小节 → 读完即走**。
> 全文只有下面的「索引」表需要扫一遍;30 个原型小节按需单点查阅。
> (2026-08-06 第五轮 P4:此前它被列为"写页首选起点",导致每次写页都通读,
> 挤占了真正该读的两份契约的注意力。)

> **人类专业 PPT 的页面类型学。** 写页先选原型,再填内容——原型决定"这一页怎么摆",配方(`layout-recipes.md`)只管容器内部写法。
> 每个原型:用途 / 何时别用 / 填充行为(满填|airy) / HTML 骨架 / 参数表 / 反 AI 味要点。
> 骨架全部遵循 `design-principles.md`(分区/字号阶/scale-to-fill/**视觉形式**)与 `html-spec.md`(转换契约);字号以**演讲档**标注,其他档位按 design-principles 字号阶等比换算。
> **选原型流程(二级,2026-08-05 起)**:访谈 Q5 大纲确认时**先定视觉形式**(文字/图示/图表/图片/混合,写入 brief 形式列,按 Q8c 档位与信息结构)→ **再从该形式组选原型** → 写页时只查 brief 指定的原型小节。

## 索引

| 组 | 原型 | 形式 | 填充 | 一句话 |
|---|---|---|---|---|
| 开场导航 | 1 封面·深底大字 | 文字(airy) | airy | 深底+超大标题+细强调条 |
| | 2 封面·浅底编辑 | 文字(airy) | airy | 浅底+左对齐巨标+底部信息行 |
| | 3 议程 | 文字 | 满填 | 大数字编号裸列表 |
| | 4 章节分隔 | 文字(airy) | airy | 超大编号+章节名 |
| | 5 大字观点 | 文字(airy) | airy | 一句话占满页 |
| | 6 引用页 | 文字(airy) | airy | 巨引号+引文+署名 |
| 论述 | 7 编辑文字页 | 文字 | 满填 | action title+双栏文字,零卡片 |
| | 8 要点列表 | 文字 | 满填 | 粗体引导裸排要点+细分隔线 |
| | 9 不对称分栏 7:5 | 混合 | 满填 | 主栏论述+辅栏深面/数据 |
| | 10 图文页 | 图片 | 满填 | 左图右文(可镜像) |
| | 11 全出血大图页 | 图片 | 出血满填 | 图满画布+左下文字块 |
| 对比流程 | 12 双栏对照 | 文字 | 满填 | 旧vs新/AvsB+中缝 |
| | 13 流程步骤 | 文字/图示(chevron 款) | 满填 | 横向步骤带(大数字或 chevron) |
| | 14 时间线 | 图示 | 满填 | 横轴实线+圆点+交替标签 |
| | 15 2×2 象限 | 图示 | 满填 | 坐标轴+四象限+点位 |
| | 16 层级 | 图示 | 满填 | 3-4 层横条,上窄下宽 |
| 数据 | 17 大数字带 | 文字 | 满填 | 3-4 个巨数字+标签,细线分隔 |
| | 18 图表主角 | 图表 | 满填 | 大图表(1100px)+右侧解读栏 |
| | 19 表格主角 | 图表 | 满填 | 大表格居中,表头深色 |
| | 20 仪表盘 | 图表 | 满填 | KPI 行+图表+表格(阅读/混合档) |
| 收尾 | 21 行动号召 | 文字(airy) | airy | 深底+大字行动句+联系方式 |
| | 22 附录指引 | 文字 | 满填 | 资料清单编辑式排版 |
| **图示(2026-08-05 新增)** | 23 图标要点网格 | 图示 | 满填 | 2×2/2×3 图标卡:图标+标题+说明 |
| | 24 chevron 流程带 | 图示 | 满填 | 3-5 步箭头链+下方说明列 |
| | 25 转化漏斗 | 图示 | 满填 | trapezoid 叠层收窄+左右侧注 |
| | 26 金字塔 | 图示 | 满填 | 三角+梯形真分层(3-4 层) |
| | 27 循环图 | 图示 | 满填 | SVG 环形箭头+中心命题+4 节点 |
| | 28 中心辐射 | 图示 | 满填 | 中心圆+4 卫星卡+细连接线 |
| | 29 对比卡阵 | 图示 | 满填 | 双卡对决+中央 VS 徽章+图标行 |
| | 30 色带分节页 | 图示 | 满填 | 横向纯色带 stack,每带一主张 |

---

## 组 1 · 开场导航

### 原型 1 · 封面 · 深底大字(airy)

**用途**:deck 第一页;产品发布/路演/汇报通用。**何时别用**:全浅基调 deck(用原型 2)。
**填充**:airy —— 文字块垂直居中偏上,底部信息行贴页脚区。

```html
<div class="slide-container" style="background:var(--deep-navy);">
  <!-- 细强调条(装饰 1 件) -->
  <div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:420px;width:120px;height:6px;background:var(--accent-orange);"></div>
  <!-- 主标 88-120px,最多两行 -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:460px;width:1600px;">
    <div style="font-size:104px;font-weight:800;line-height:1.15;color:var(--on-navy-text);letter-spacing:-1px;">
      标题一句话,<br>最多两行
    </div>
  </div>
  <!-- 副标:一句话承诺 28-32px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:720px;width:1400px;">
    <div style="font-size:30px;font-weight:400;line-height:1.4;color:var(--on-navy-sub);">一句话承诺或定位</div>
  </div>
  <!-- 底部信息行:汇报人/日期,18px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:980px;width:1720px;">
    <div style="font-size:22px;line-height:1.4;color:var(--on-navy-dim);">汇报人 · 机构 · 2026-08</div>
  </div>
</div>
```

| 参数 | 调什么 |
|---|---|
| 主标字号 | 88-120px,一行能放下就取大值 |
| 强调条位置 | 主标上方 40px;是唯一装饰 |
| 深底 | `var(--deep-navy)` 或品牌深底色 |

**反 AI 味要点**:❌ 不加 kicker/徽章/渐变英雄区/装饰图形;✓ 克制 = 一根强调条 + 三级文字。标题即定位,不写"XX 汇报 PPT"。

---

### 原型 2 · 封面 · 浅底编辑(airy)

**用途**:全浅基调 deck(阅读档/学术/编辑杂志风)。**何时别用**:需要开场冲击力(用原型 1)。
**填充**:airy —— 巨标靠上 1/3,信息行贴底。

```html
<div class="slide-container" style="background:var(--off-white);">
  <!-- 眉题:机构/性质,20px 字距 4px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1200px;">
    <div style="font-size:20px;font-weight:600;letter-spacing:4px;color:var(--text-tertiary);">机构名 · 报告性质</div>
  </div>
  <!-- 巨标 96-120px 左对齐 -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:200px;width:1700px;">
    <div style="font-size:110px;font-weight:800;line-height:1.12;color:var(--charcoal);letter-spacing:-1.5px;">
      编辑式大标题,<br>像杂志封面
    </div>
  </div>
  <!-- 细分隔线 -->
  <div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:920px;width:1720px;height:1px;background:var(--border-medium);"></div>
  <!-- 信息行 -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:950px;width:1720px;">
    <div style="font-size:22px;line-height:1.4;color:var(--text-secondary);">作者 · 日期 · 版本</div>
  </div>
</div>
```

**反 AI 味要点**:巨标是唯一主角;❌ 不要色块/渐变/卡片。编辑感靠**字号反差 + 留白**。

---

### 原型 3 · 议程(满填)

**用途**:第 2 页,给全 deck 导航。**何时别用**:≤5 页的短 deck(直接进内容)。
**填充**:满填 —— 条目在内容区 320-940 **均匀分布**(条目少就拉大间距与字号)。
**丰富档(2026-08-02 测试反馈)**:副题写"这章会怎么讲"(例子/问题/承诺),不要只写章节名——"从 X 说起""每个都问:它改变了谁的工作"这类带钩子的副题,让议程页有信息量而非占位。

```html
<!-- 页标题(action title 可省,议程页允许"议程/今天讲三件事"式) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.15;color:var(--charcoal);">今天讲三件事</div>
</div>
<!-- 编号裸列表:方式 B,条目纵向分布 -->
<div style="position:absolute;left:100px;top:320px;width:1720px;display:flex;flex-direction:column;gap:0;">
  <!-- 条目 1:大数字 + 标题 + 一句话,底部细线 -->
  <div data-object="true" data-object-type="shape" style="height:200px;border-bottom:1px solid var(--border-light);display:flex;align-items:center;gap:40px;">
    <div class="num" style="font-size:64px;font-weight:800;color:var(--lenovo-red);line-height:1;">01</div>
    <div>
      <div style="font-size:30px;font-weight:700;line-height:1.3;color:var(--charcoal);">章节标题</div>
      <div style="font-size:24px;line-height:1.4;color:var(--text-secondary);margin-top:6px;">一句话说明这章回答什么问题</div>
    </div>
  </div>
  <!-- 条目 2、3 同构;height 按 620/条目数 均分 -->
</div>
```

| 参数 | 调什么 |
|---|---|
| 条目数 | 3-5 条;条目高 = 620÷N(3 条 ≈ 200px,5 条 ≈ 124px) |
| 数字字号 | 条目高 ≥180px 时 64px;否则 48px |
| 末条细线 | 最后一条去 border-bottom |

**反 AI 味要点**:❌ 不装卡片、不套圆圈;✓ 大数字+细线就是最专业的议程。章节名必须与后续分隔页/kicker 一致。
**图示化升级**:章节 3-4 个且形式偏好为丰富型 → 改原型 30 色带分节页(每带一章)。

---

### 原型 4 · 章节分隔(airy)

**用途**:章与章之间换节奏。**何时别用**:≤6 页短 deck 或单章 deck。
**填充**:airy —— 超大编号+章节名居中偏左;可深可浅(与封面同底最稳)。

```html
<div class="slide-container" style="background:var(--deep-navy);">
  <!-- 超大编号 240px,半透明感用预算混合深色(非 rgba 文字) -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:80px;top:180px;width:800px;">
    <div class="num" style="font-size:240px;font-weight:800;line-height:1;color:var(--deep-navy-light);">02</div>
  </div>
  <!-- 章节名 64px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:560px;width:1500px;">
    <div style="font-size:64px;font-weight:800;line-height:1.2;color:var(--on-navy-text);">章节标题</div>
  </div>
  <!-- 一句话 24px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:680px;width:1400px;">
    <div style="font-size:24px;line-height:1.5;color:var(--on-navy-sub);">这一章回答的一个问题</div>
  </div>
</div>
```

**反 AI 味要点**:编号用"比深底浅一号"的混合色做水印感;❌ 不加渐变条/徽章/装饰图形。浅底变体:编号 `--border-light`、标题 `--charcoal`。

---

### 原型 5 · 大字观点(airy)

**用途**:全 deck 最重要的一句话(主张/转折/结论前置);呼吸页。**何时别用**:没有值得独占一页的话。
**填充**:airy —— 文字垂直居中。

```html
<div class="slide-container" style="background:var(--off-white);">
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:200px;top:400px;width:1520px;">
    <div style="font-size:72px;font-weight:800;line-height:1.25;color:var(--charcoal);text-align:center;">
      全 deck 最重要的那句话,<br>独占一页
    </div>
  </div>
  <!-- 可选:一行佐证 22px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:200px;top:640px;width:1520px;">
    <div style="font-size:26px;line-height:1.5;color:var(--text-secondary);text-align:center;">—— 一个数字或来源作佐证</div>
  </div>
</div>
```

| 参数 | 调什么 |
|---|---|
| 字号 | ≤20 字 → 80px;20-35 字 → 72px;>35 字 → 删字,不降 64px 以下 |
| 强调 | ≤1 处 span 变色(主色),全页唯一高亮 |

**反 AI 味要点**:这是"居中崇拜"的合法场景之一;❌ 不加 kicker/页码/装饰。深底变体同原型 4 配色。

---

### 原型 6 · 引用页(airy)

**用途**:金句/客户证言/专家观点;呼吸页。**何时别用**:没有真引用(不要编造)。
**填充**:airy。

```html
<div class="slide-container" style="background:var(--off-white);">
  <!-- 巨引号 200px,主色 -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:140px;top:200px;width:300px;">
    <div style="font-size:200px;font-weight:800;line-height:1;color:var(--lenovo-red);">"</div>
  </div>
  <!-- 引文 40-48px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:180px;top:440px;width:1400px;">
    <div style="font-size:44px;font-weight:600;line-height:1.4;color:var(--charcoal);">引文一到两句,保持原话</div>
  </div>
  <!-- 署名 20px -->
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:180px;top:700px;width:1400px;">
    <div style="font-size:22px;line-height:1.5;color:var(--text-tertiary);">—— 姓名 · 头衔 · 出处</div>
  </div>
</div>
```

**反 AI 味要点**:❌ 不用渐变左边框+斜体的"AI 引用块"(那是旧模式 6);✓ 巨引号+正体。引文 >3 行就删减,不降字号。

---

## 组 2 · 论述

### 原型 7 · 编辑文字页(满填)—— 去 AI 味主力

**用途**:讲清一个道理(背景/分析/论证);替代"三卡片"的首选。**何时别用**:真并列实体(用原型 9/12)。
**填充**:满填 —— 双栏文字从 320 排到 940。

```html
<!-- action title 两行 60px -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">
    结论式标题:这一页只讲一个道理,<br>标题把它说完
  </div>
</div>
<!-- 双栏文字:方式 B,栏宽 840/840 gap 80 -->
<div style="position:absolute;left:100px;top:340px;width:1720px;display:flex;gap:80px;">
  <div data-object="true" data-object-type="textbox" style="flex:1;">
    <div style="font-size:24px;line-height:1.7;color:var(--text-primary);">
      <span style="font-weight:700;color:var(--charcoal);">粗体引导句。</span>正文段落,每段 3-4 行,讲清一个论据。行距 1.7 是编辑感的来源。
      <br><br>
      第二段,段间用空行而不是缩进。全栏 4-8 行,自然排到底。
    </div>
  </div>
  <div data-object="true" data-object-type="textbox" style="flex:1;">
    <div style="font-size:24px;line-height:1.7;color:var(--text-primary);">第二栏继续论证或给例证、数据引用。</div>
  </div>
</div>
```

| 参数 | 调什么 |
|---|---|
| 栏数 | 2 栏为主;阅读档可 3 栏(gap 60) |
| 正文字号 | 演讲档 24px/行高 1.7;每栏 4-8 行 |
| 引导句 | 每段 1 句粗体,是唯一"强调"(反模式 9) |

**反 AI 味要点**:❌ 零卡片、零 kicker、零图标;✓ 像《经济学人》内页。这页是"内容密度"与"专业感"兼得的原型,演讲档每 deck 至少 2 页。
**图示化升级**:论据为 2-4 个并列点 → 改原型 23 图标网格;分节主张 → 改原型 30 色带。

---

### 原型 8 · 要点列表(满填)

**用途**:3-6 个要点(结论清单/建议/原则)。**何时别用**:要点是并列实体(产品/方案)→ 原型 12 或卡片矩阵(限额内)。
**填充**:满填 —— 条目均分内容区。
**丰富档(2026-08-02 测试反馈)**:每页 2 条"例子/证据"——要点页只写判断会显得"素"。写法:要点区收窄(每条 150px),下方加一行 26px 例子(如"效果(真实试点):检索耗时 11→6.4 分钟")+ 一行 16px 来源注。克制是纪律,内容单薄是失误。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">三个判断,结论先行</div>
</div>
<div style="position:absolute;left:100px;top:320px;width:1720px;display:flex;flex-direction:column;">
  <!-- 条目:粗体引导词 + 说明,底部细线 -->
  <div data-object="true" data-object-type="shape" style="height:150px;border-bottom:1px solid var(--border-light);display:flex;align-items:center;">
    <div style="font-size:26px;line-height:1.5;color:var(--text-primary);">
      <span style="font-weight:700;color:var(--charcoal);">判断一:</span>一句话说清这个判断,不超过两行
    </div>
  </div>
  <!-- 条目 2、3 同构;4 条 → 每条高 155px,3 条 → 每条 200px 且字号 28px -->
</div>
```

| 参数 | 调什么 |
|---|---|
| 条目数/高度 | 3 条 ×200px(字号 28)｜4 条 ×155px(26)｜5-6 条 ×125/105px(24) |
| 引导词 | 2-6 字粗体(判断一/建议 2/原则③),后接冒号 |
| 细线 | 相邻条目间 1px `--border-light`;末条无 |

**反 AI 味要点**:❌ 序号圆圈、卡片、图标全免;✓ 粗体引导词+细线。需要编号就用 40px 大数字裸排(放引导词前,gap 32px)。
**图示化升级**:要点 ≥4 且各项有图标语义 → 升级原型 23 图标网格;有严格先后 → 原型 24 chevron 带。

---

### 原型 9 · 不对称分栏 7:5(满填)

**用途**:主辅双栏——左论述+右证据(数据/引文/图)。**何时别用**:两栏同等重要(用原型 12)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">主栏观点的 action title</div>
</div>
<!-- 方式 C:7:5 分栏 -->
<div data-layout="columns" data-layout-gap="60" style="position:absolute;left:100px;top:340px;width:1720px;height:560px;">
  <!-- 主栏:裸排版论述(无边框无底色) -->
  <div data-object="true" data-layout-w="7fr">
    <div style="font-size:26px;font-weight:700;line-height:1.35;color:var(--charcoal);">核心论述一段,粗体开场</div>
    <div style="font-size:26px;line-height:1.65;color:var(--text-primary);margin-top:24px;">论证正文 4-6 行,自然往下排。主栏不装盒子,保持编辑感。</div>
  </div>
  <!-- 辅栏:深色面(证据区) -->
  <div data-object="true" data-layout-w="5fr" style="background:var(--deep-navy);border-radius:10px;padding:40px;">
    <div style="font-size:20px;font-weight:600;letter-spacing:2px;color:var(--accent-orange);">关键证据</div>
    <div class="num" style="font-size:72px;font-weight:800;line-height:1.1;color:var(--on-navy-text);margin-top:16px;">87<span style="font-size:36px;">%</span></div>
    <div style="font-size:24px;line-height:1.55;color:var(--on-navy-sub);margin-top:16px;">证据说明 1-2 行</div>
  </div>
</div>
```

**反 AI 味要点**:辅栏深色面是"对比"不是"卡片";主栏留白不装盒。7:5 之外可 3:2、2:1;**主辅必须分明**,等宽即失败。

---

### 原型 10 · 图文页(满填)

**用途**:产品图/截图/照片 + 解读。**何时别用**:没有图——不要用图库凑数(降级为原型 7/8)。
**填充**:满填。图片契约:`<img>` 显式 `object-fit`(html-spec 5.2.1)。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">图为证,标题说图的结论</div>
</div>
<!-- 左图 5 份 -->
<img data-object="true" src="../assets/img/example.png" alt=""
     style="position:absolute;left:100px;top:320px;width:700px;height:580px;object-fit:cover;border-radius:10px;">
<!-- 右文 7 份 -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:860px;top:320px;width:960px;">
  <div style="font-size:26px;font-weight:700;line-height:1.4;color:var(--charcoal);">看图先看这一句</div>
  <div style="font-size:26px;line-height:1.65;color:var(--text-primary);margin-top:20px;">解读 3-5 行。图与文同高,底部对齐页脚区。</div>
</div>
```

| 参数 | 调什么 |
|---|---|
| 图:文 | 5:7(图小文大)或 7:5(图为主);图高 580-620px 撑满内容区 |
| object-fit | 照片 `cover`;截图 `contain`+底色 `--card-bg` |
| 镜像 | 图右文左亦可,同 deck 内统一一边 |

**反 AI 味要点**:❌ 不给图加圆角卡片底+阴影+边框三件套;✓ 单圆角或直角。截图务必 `contain`,裁切失真比留白更难看。

---

### 原型 11 · 全出血大图页(出血满填)

**用途**:一张图说一件事(场景/产品/数据可视化大图)。**何时别用**:图质量低/与论点无关。
**填充**:图满画布(出血),文字区 airy。装饰图用 `background-image`(截图路径);内容图用 `<img>`。

```html
<div class="slide-container" style="background:var(--charcoal);">
  <!-- 全画布图(装饰/背景走 background-image;内容照片换 <img object-fit:cover>) -->
  <div data-object="true" data-object-type="shape" style="position:absolute;left:0;top:0;width:1920px;height:1080px;background-image:url('../assets/img/hero.png');background-size:cover;background-position:center;"></div>
  <!-- 左下文字块:深底图上用白字,可垫预算混合深色条 -->
  <div data-object="true" data-object-type="shape" style="position:absolute;left:0;top:820px;width:1920px;height:260px;background:#14181D;"></div>
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:870px;width:1500px;">
    <div style="font-size:40px;font-weight:700;line-height:1.3;color:#FFFFFF;">图说的一句话结论</div>
  </div>
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:950px;width:1500px;">
    <div style="font-size:22px;line-height:1.4;color:#C9D2DC;">补充说明一行 · 来源</div>
  </div>
</div>
```

**反 AI 味要点**:文字垫条用**预算混合纯色**(非 rgba);❌ 不用渐变蒙版+居中巨标的"AI 英雄区"。图上文字 ≤2 行。

---

## 组 3 · 对比流程

### 原型 12 · 双栏对照(满填)

**用途**:旧 vs 新 / A vs B / 前后对比。**何时别用**:三方以上对比(用表格原型 19)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">对比结论先行的标题</div>
</div>
<!-- 左栏:旧/痛点 -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:340px;width:800px;">
  <div style="font-size:22px;font-weight:600;letter-spacing:2px;color:var(--text-tertiary);">过去</div>
  <div style="font-size:30px;font-weight:700;line-height:1.3;color:var(--charcoal);margin-top:12px;">旧方式</div>
  <div style="font-size:26px;line-height:1.7;color:var(--text-primary);margin-top:24px;">
    · 痛点一,一行说清<br>· 痛点二<br>· 痛点三
  </div>
</div>
<!-- 中缝细线 -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:940px;top:360px;width:1px;height:520px;background:var(--border-medium);"></div>
<!-- 右栏:新/方案(主色强调) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:1020px;top:340px;width:800px;">
  <div style="font-size:22px;font-weight:600;letter-spacing:2px;color:var(--lenovo-red);">现在</div>
  <div style="font-size:30px;font-weight:700;line-height:1.3;color:var(--charcoal);margin-top:12px;">新方式</div>
  <div style="font-size:26px;line-height:1.7;color:var(--text-primary);margin-top:24px;">
    · 解法一<br>· 解法二<br>· 解法三
  </div>
</div>
```

**反 AI 味要点**:❌ 双卡片+顶边色条+图标(旧模式 7);✓ 裸双栏+中缝线。"新"侧可用一处主色,全页唯一高亮。
**图示化升级**:双方各有 ≥3 条特征清单 → 升级原型 29 对比卡阵(VS 徽章+图标行)。

---

### 原型 13 · 流程步骤(满填)

**用途**:3-5 步流程/方法论/实施路径。**何时别用**:纯时间顺序(用原型 14)。
**填充**:满填。两款:**大数字裸排款**(首选)与 **chevron 款**(步骤有严格先后箭头语义时)。
**丰富档(2026-08-02 测试反馈)**:步骤卡下方留 1-2 行"例子(个人)/例子(团队)"真实场景,把抽象步骤落地成"我也能抄"的模板——只放步骤名+说明的流程页,是"内容单薄"的高发区。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">三步落地,标题说路径</div>
</div>
<!-- 大数字裸排款:方式 C 三列 -->
<div data-layout="columns" data-layout-gap="60" style="position:absolute;left:100px;top:360px;width:1720px;height:480px;">
  <div data-object="true" data-layout-w="1fr" style="border-top:3px solid var(--charcoal);padding-top:24px;">
    <div class="num" style="font-size:56px;font-weight:800;line-height:1;color:var(--charcoal);">1</div>
    <div style="font-size:28px;font-weight:700;line-height:1.3;color:var(--charcoal);margin-top:16px;">步骤名</div>
    <div style="font-size:24px;line-height:1.6;color:var(--text-secondary);margin-top:12px;">这一步做什么、产出什么,2-3 行。</div>
  </div>
  <!-- 步骤 2、3 同构;当前步/关键步 border-top 换主色 -->
</div>
```

| 参数 | 调什么 |
|---|---|
| 步骤数 | 3 步高 480px / 4-5 步高 400px;说明字号 20px |
| 强调步 | 仅 1 步:border-top 主色 + 数字主色 |
| chevron 款 | `data-shape="chevron"` 横排+文字叠加(见 creative-layouts 模式 2),每 deck ≤1 页 |

**反 AI 味要点**:❌ 序号圆圈+卡片(旧配方 4);✓ 顶线+大数字。步骤间不需要箭头图形——数字本身就是顺序。
**图示化升级**:步骤有强箭头语义或形式偏好为丰富型 → 升级原型 24 chevron 带(chevron 属结构形状,原"每 deck ≤1 页"装饰限额已解除,仅守"同原型不连续 >2 页")。

---

### 原型 14 · 时间线(满填)

**用途**:历程/路线图/里程碑(有真实日期)。**何时别用**:无时间属性的"步骤"(用原型 13)。
**填充**:满填。横向款(4-6 节点)为主;纵向款(>6 节点)用议程式排版。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">路线图的 action title</div>
</div>
<!-- 横轴实线(非虚线) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:560px;width:1720px;height:2px;background:var(--border-medium);"></div>
<!-- 节点 1:圆点+上方日期+下方事件 -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:140px;top:548px;width:24px;height:24px;border-radius:50%;background:var(--lenovo-red);"></div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:460px;width:200px;">
  <div class="num" style="font-size:28px;font-weight:800;color:var(--charcoal);">Q1</div>
</div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:600px;width:260px;">
  <div style="font-size:24px;line-height:1.5;color:var(--text-primary);">里程碑事件,两行内</div>
</div>
<!-- 节点 2-4 同构,x 均匀分布(间隔 1720/N);已完成节点主色,未来节点边框白心 -->
```

**反 AI 味要点**:❌ 旋转标签/渐变圆/虚线(旧模式 4 的炫技三件套);✓ 实线+圆点+正立文字。当前位置用主色,是唯一点缀。
**图示化升级**:里程碑需带详情 → 节点说明改小卡片变体;闭环流程 → 原型 27 循环图。

---

### 原型 15 · 2×2 象限(满填)

**用途**:双维度定位(优先级/风险评估/竞争地图)。**何时别用**:维度不成立(为显得专业硬凑 XY 轴是最大的外行特征)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">标题说象限结论(如:先打右上)</div>
</div>
<!-- 象限区:方式 C 2x2 grid -->
<div data-layout="grid" data-layout-cols="2" data-layout-gap="2" style="position:absolute;left:260px;top:340px;width:1300px;height:560px;">
  <div data-object="true" data-layout-h="280" style="background:var(--card-bg);padding:32px;">
    <div style="font-size:24px;font-weight:700;color:var(--charcoal);">象限名(高X低Y)</div>
    <div style="font-size:24px;line-height:1.55;color:var(--text-secondary);margin-top:10px;">点位/说明</div>
  </div>
  <!-- 其余三象限;目标象限底换 --deep-navy、文字换 on-navy 组 -->
</div>
<!-- 轴标签 -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:260px;top:920px;width:1300px;text-align:center;">
  <div style="font-size:22px;color:var(--text-tertiary);">X 轴名 →</div>
</div>
```

**反 AI 味要点**:象限底色用 `--card-bg`/白,目标象限唯一深色;❌ 四色渐变象限。轴标签 18px 灰色,别画箭头森林。

---

### 原型 16 · 层级(满填)

**用途**:金字塔/分层模型(战略→战术→执行;需求层次)。**何时别用**:层级关系不成立(并列项别堆成塔)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">层级模型的 action title</div>
</div>
<!-- 3 层横条,上窄下宽:方式 B -->
<div style="position:absolute;left:100px;top:340px;width:1720px;display:flex;flex-direction:column;gap:16px;align-items:center;">
  <div data-object="true" data-object-type="shape" style="width:700px;height:180px;background:var(--deep-navy);border-radius:8px;display:flex;align-items:center;justify-content:center;">
    <div style="text-align:center;">
      <div style="font-size:28px;font-weight:700;color:var(--on-navy-text);">顶层:一句话</div>
      <div style="font-size:24px;color:var(--on-navy-sub);margin-top:8px;line-height:1.4;">支撑说明</div>
    </div>
  </div>
  <div data-object="true" data-object-type="shape" style="width:1100px;height:180px;background:var(--deep-navy-light);border-radius:8px;display:flex;align-items:center;justify-content:center;">…中层…</div>
  <div data-object="true" data-object-type="shape" style="width:1500px;height:180px;background:var(--off-white);border:1px solid var(--border-medium);border-radius:8px;display:flex;align-items:center;justify-content:center;">…底层…</div>
</div>
```

**反 AI 味要点**:层宽递进(700/1100/1500)就是金字塔,❌ 不需要画三角 SVG。层数 3-4;色彩由深到浅单向,❌ 彩虹分层。

---

## 组 4 · 数据

### 原型 17 · 大数字带(满填)

**用途**:3-4 个关键数字(业绩/效果/规模)。**何时别用**:数字 >4(拆页或改仪表盘)、数字无说服力。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">标题说数字的结论(如:效率提升四成)</div>
</div>
<!-- 方式 C 3-4 列,细线分隔无卡片 -->
<div data-layout="columns" data-layout-gap="40" style="position:absolute;left:100px;top:380px;width:1720px;height:420px;">
  <div data-object="true" data-layout-w="1fr" style="border-left:1px solid var(--border-light);padding-left:40px;">
    <div class="num" style="font-size:88px;font-weight:800;line-height:1;color:var(--charcoal);">87<span style="font-size:40px;">%</span></div>
    <div style="font-size:26px;line-height:1.4;color:var(--text-secondary);margin-top:20px;">指标说明,一两行</div>
    <div style="font-size:22px;line-height:1.4;color:var(--signal-green);margin-top:12px;">↑ 同比 +12pp</div>
  </div>
  <!-- 列 2-4 同构;首列去 border-left -->
</div>
```

| 参数 | 调什么 |
|---|---|
| 数字字号 | 3 列 88px / 4 列 72px;单位 40-45% 主数字 |
| 增减行 | 18px;增 `--signal-green` 减 `--signal-red`,全页仅此处用信号色 |
| 强调列 | 至多 1 列数字用主色,其余 `--charcoal` |

**反 AI 味要点**:❌ KPI 卡片+渐变底+上标(旧模式 3);✓ 细线分隔裸排。大数字 = 自信,盒子 = 心虚。
**图示化升级**:指标有图标语义(成本/用户/时效)→ 数字上方加同色系小图标;KPI >4 且需图表 → 原型 20(阅读/混合档)。
**填充提示(2026-08-05 试点反馈)**:3 列数字+两行说明只占内容区上半截时,数字上调 96-104px(scale-to-fill),并在底部加一条浅底"怎么读/口径"补充条(顶 780-800,高 90,22px 单行)——别让数字带悬空。

---

### 原型 18 · 图表主角(满填)

**用途**:一页一图,图是论据主角。**何时别用**:图说不清楚(先改图,不是加字)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:56px;font-weight:700;line-height:1.2;color:var(--charcoal);">标题=图表的结论(不是"销售趋势图")</div>
</div>
<!-- 大图表 1080px:原生 data-chart -->
<div data-object="true" data-chart='{"type":"bar","labels":["Q1","Q2","Q3","Q4"],"series":[{"name":"营收","values":[120,180,240,310]}]}'
     style="position:absolute;left:100px;top:320px;width:1080px;height:580px;"></div>
<!-- 右侧解读栏 560px -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:1260px;top:320px;width:560px;">
  <div style="font-size:24px;font-weight:700;line-height:1.4;color:var(--charcoal);">怎么读这张图</div>
  <div style="font-size:24px;line-height:1.65;color:var(--text-primary);margin-top:20px;">
    · 解读一:拐点在哪<br><br>· 解读二:说明什么<br><br>· 解读三:下一步
  </div>
  <div style="font-size:16px;line-height:1.5;color:var(--text-tertiary);margin-top:32px;">来源:数据口径与时间</div>
</div>
```

**反 AI 味要点**:图无卡片底、无边框;解读栏裸排。图表系列数受密度档上限(演讲 ≤3)。

---

### 原型 19 · 表格主角(满填)

**用途**:结构化数据必须全列出(对比矩阵/清单/参数表)。**何时别用**:行数超档(拆页/附录)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:56px;font-weight:700;line-height:1.2;color:var(--charcoal);">标题说表格结论</div>
</div>
<div data-object="true" data-object-type="table" style="position:absolute;left:100px;top:320px;width:1720px;">
  <table style="width:100%;border-collapse:collapse;font-size:22px;">
    <tr style="background:var(--deep-navy);color:#FFF;">
      <th style="padding:20px 24px;text-align:left;font-weight:700;">列一</th>
      <th style="padding:20px 24px;text-align:left;font-weight:700;">列二</th>
      <th style="padding:20px 24px;text-align:right;font-weight:700;">数字列</th>
    </tr>
    <tr style="border-bottom:1px solid var(--border-light);">
      <td style="padding:18px 24px;line-height:1.4;">行内容</td>
      <td style="padding:18px 24px;line-height:1.4;">行内容</td>
      <td class="num" style="padding:18px 24px;text-align:right;line-height:1.4;">1,024</td>
    </tr>
    <!-- 行数 ≤ 档内上限(演讲 ≤6 含表头);偶数行可 zebra --card-bg -->
  </table>
</div>
```

**反 AI 味要点**:表头深色、行线细分、数字右对齐;❌ 全框线网格+居中所有列。字号 22px(演讲)/18px(阅读)。

---

### 原型 20 · 仪表盘(满填 · 阅读/混合档向)

**用途**:KPI 全景(复盘/月报)。**何时别用**:演讲档(信息过载;拆成原型 17+18 两页)。
**填充**:满填。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:100px;width:1720px;">
  <div style="font-size:52px;font-weight:700;line-height:1.2;color:var(--charcoal);">月度复盘的 action title</div>
</div>
<!-- KPI 行:3 大数字(原型 17 压缩款,无卡) -->
<div data-layout="columns" data-layout-gap="40" style="position:absolute;left:100px;top:260px;width:1720px;height:200px;">
  <div data-object="true" data-layout-w="1fr" style="border-left:1px solid var(--border-light);padding-left:32px;">
    <div class="num" style="font-size:64px;font-weight:800;line-height:1;color:var(--charcoal);">87<span style="font-size:32px;">%</span></div>
    <div style="font-size:24px;color:var(--text-secondary);margin-top:12px;">指标</div>
  </div>
</div>
<!-- 下区:图表 + 表格 双拼 -->
<div data-object="true" data-chart='{"type":"line","labels":["1月","2月","3月"],"series":[{"name":"趋势","values":[10,14,19]}]}'
     style="position:absolute;left:100px;top:520px;width:840px;height:380px;"></div>
<div data-object="true" data-object-type="table" style="position:absolute;left:980px;top:520px;width:840px;">
  <table style="width:100%;border-collapse:collapse;font-size:18px;">…4 行内…</table>
</div>
```

**反 AI 味要点**:三区分明(KPI/图/表),区间 40px 留白分隔;❌ 渐变 KPI 卡堆叠。仅混合/阅读档使用。

---

## 组 5 · 收尾

### 原型 21 · 行动号召(airy)

**用途**:最后一页:明确的下一步。**何时别用**:没有行动(用原型 5 大字观点收尾)。
**填充**:airy。

```html
<div class="slide-container" style="background:var(--deep-navy);">
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:200px;top:400px;width:1520px;">
    <div style="font-size:64px;font-weight:800;line-height:1.25;color:var(--on-navy-text);text-align:center;">
      希望您做的一件事
    </div>
  </div>
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:200px;top:600px;width:1520px;">
    <div style="font-size:24px;line-height:1.5;color:var(--on-navy-sub);text-align:center;">
      联系方式 / 链接 / 时间承诺
    </div>
  </div>
</div>
```

**反 AI 味要点**:❌ 徽章按钮/渐变 CTA 条;✓ 一句话+一行联系。"谢谢聆听"是废话,行动句才是收尾。

---

### 原型 22 · 附录指引(满填)

**用途**:附录封面或资料清单(数据来源/参考/详细参数入口)。**何时别用**:无附录。
**填充**:满填(它是内容页)。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:56px;font-weight:700;line-height:1.2;color:var(--charcoal);">附录:数据与资料</div>
</div>
<div style="position:absolute;left:100px;top:320px;width:1720px;display:flex;flex-direction:column;">
  <div data-object="true" data-object-type="shape" style="height:120px;border-bottom:1px solid var(--border-light);display:flex;align-items:center;">
    <div style="font-size:26px;line-height:1.5;color:var(--text-primary);">
      <span style="font-weight:700;color:var(--charcoal);">数据来源:</span>口径、时间范围、样本说明
    </div>
  </div>
  <!-- 参考资料/术语表/详细参数入口 同构 -->
</div>
```

**反 AI 味要点**:与议程页同构(首尾呼应);条目含真实出处,❌ 不写"详见相关资料"。

---

## 组 6 · 图示(2026-08-05 新增;结构形状,非装饰——反模式豁免见 design-principles 第四章总则)

> 本组 8 款是"形式丰富"的主力。共性纪律:**先有信息结构,后选图示**(并列→23/29,先后→24,递减→25,分层→26,循环→27,辐射→28,分节→30);图标从 `assets/icons.md` 复制(**stroke 必须显式 hex,禁 currentColor**——截图时 currentColor 会变透明);全页图标同一色系。

### 原型 23 · 图标要点网格(满填)—— 并列信息的首选图示

**用途**:3、4 或 6 个并列要点(特性/能力/原则/优势)——"万物皆卡片"的合法出口(反模式 2/7 结构豁免:不计入卡片矩阵限额)。**何时别用**:要点有先后/层级(用 24/26);纯结论清单无图标语义(原型 8 更省);5 个要点(网格不齐,改 9 或 8)。
**填充**:满填 —— 2×2:卡高 290(320+290+40+290=940 铺满);2×3:列数改 3;1×3:单行三列纵向卡(卡高 460)。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">四个能力,标题把结论说完</div>
</div>
<!-- 2×2 网格:方式 C grid -->
<div data-layout="grid" data-layout-cols="2" data-layout-gap="40" style="position:absolute;left:100px;top:320px;width:1720px;">
  <div data-object="true" data-layout-h="290" style="background:var(--white);border:1px solid var(--border-light);border-radius:12px;padding:40px;">
    <div style="display:flex;align-items:center;gap:20px;">
      <!-- 图标:assets/icons.md 复制,stroke 显式 hex,全页同色 -->
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#E2231A" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2" fill="#E2231A" stroke="none"/></svg>
      <div style="font-size:30px;font-weight:700;line-height:1.3;color:var(--charcoal);">要点标题</div>
    </div>
    <div style="font-size:26px;line-height:1.6;color:var(--text-primary);margin-top:20px;">说明 2 行以内:这个要点是什么、为什么重要。</div>
    <div style="font-size:22px;line-height:1.5;color:var(--text-tertiary);margin-top:14px;">例子/证据一行(丰富档必备,可选)</div>
  </div>
  <!-- 卡 2-4 同构,换图标/标题/说明 -->
</div>
```

| 参数 | 调什么 |
|---|---|
| 布局 | 4 点 → 2×2(cols 2,h 290);6 点 → 2×3(cols 3,h 290,卡内 padding 32);3 点 → 1×3(cols 3,h 460,纵向卡:图标在上,标题 margin-top:18px,说明 21px) |
| 图标 | 48px;全页同一 hex(主色或炭灰);深底卡上换亮色系 |
| 标题行 | 横向(图标左+标题右)为主;窄卡(2×3/1×3)改纵向(图标在上) |
| 说明 | 22px ≤2 行;例子行 18px 灰色 |

**反 AI 味要点**:❌ 每卡一色的彩虹图标(全页同色);❌ 阴影+边框+圆角三件套(只取"细边框+圆角"或"浅底+圆角"其一);❌ 无语义凑数图标。✓ 这是结构卡片:卡上有图标+信息,合法且不计装饰件。

---

### 原型 24 · chevron 流程带(满填)

**用途**:3-5 步严格先后的流程(实施路径/方法论/转化步骤),箭头语义强。**何时别用**:并列要点(23);时间属性强(14);闭环(27)。
**填充**:满填。chevron 属结构形状——旧"每 deck ≤1 页"装饰限额**已解除**(2026-08-05),仅守"同原型不连续 >2 页"。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">四步落地,标题说路径</div>
</div>
<!-- chevron 带(4 步,w424 gap8;首步 homePlate 平头;带高 120,顶 380) -->
<div data-object="true" data-object-type="shape" data-shape="homePlate" style="position:absolute;left:100px;top:380px;width:424px;height:120px;background:var(--deep-navy);"></div>
<div data-object="true" data-object-type="shape" data-shape="chevron" style="position:absolute;left:532px;top:380px;width:424px;height:120px;background:var(--deep-navy-light);"></div>
<div data-object="true" data-object-type="shape" data-shape="chevron" style="position:absolute;left:964px;top:380px;width:424px;height:120px;background:var(--deep-navy-light);"></div>
<div data-object="true" data-object-type="shape" data-shape="chevron" style="position:absolute;left:1396px;top:380px;width:424px;height:120px;background:var(--lenovo-red);"></div>
<!-- 叠字(DOM 在形状后;左右各让 48px 避开箭头缺口;line-height=带高做单行居中) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:148px;top:380px;width:328px;height:120px;text-align:center;">
  <div style="font-size:26px;font-weight:700;color:#FFFFFF;line-height:120px;">1 诊断</div>
</div>
<!-- 步骤 2-4 叠字同构(x 同 chevron,左右各让 48px) -->
<!-- 说明列:与 chevron 同 x 同宽,顶 540 -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:540px;width:424px;">
  <div style="font-size:26px;line-height:1.6;color:var(--text-primary);">这一步做什么、产出什么,2-3 行说透。</div>
  <div style="font-size:22px;line-height:1.5;color:var(--text-tertiary);margin-top:12px;">例子:真实场景一句话(≤20 字)。</div>
</div>
<!-- 说明列 2-4 同构 -->
<!-- 口径条(贯穿补充:口径/周期/负责,浅底单行) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:780px;width:1720px;height:90px;background:var(--card-bg);border:1px solid var(--border-light);border-radius:10px;"></div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:140px;top:780px;width:1640px;height:90px;">
  <div style="font-size:22px;line-height:90px;color:var(--text-secondary);">口径:收益以季度复盘为准 · 周期:每步 6 周 · 负责:数字化转型办</div>
</div>
```

| 参数 | 调什么 |
|---|---|
| 3 步 | w 568 gap 8,x = 100/676/1252 |
| 4 步 | w 424 gap 8,x = 100/532/964/1396(带高 120,顶 380) |
| 5 步 | w 336 gap 10,x = 100/446/792/1138/1484;带高可降 96,说明列/口径条不动 |
| 配色 | 同色系递进(深→浅);**仅关键步用主色**(上图第 4 步);禁每步一色彩虹 |
| 口径条 | 顶 780,高 90(底 870);单行 22px,放口径/周期/负责等贯穿信息 |

**反 AI 味要点**:✓ 首步 `homePlate`(平头)、后续 `chevron`(咬合感);❌ 每步叠图标+徽章的堆砌;说明列与 chevron 严格同 x 同宽(对齐即专业)。

---

### 原型 25 · 转化漏斗(满填)

**用途**:逐级递减模型(转化/筛选/审核漏斗)。**何时别用**:无递减语义的层级(用 26/16);仅 2 级(用 12 双栏)。
**填充**:满填。结构:`trapezoid` + `transform:rotate(180deg)`(窄边朝下)+ 居中层叠 + 左右侧注。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">漏斗标题:从 X 到 Y 的转化</div>
</div>
<!-- 漏斗层(4 层,w 1200/950/700/450,h120 gap16,顶 360;rotate(180) 窄边朝下) -->
<div data-object="true" data-object-type="shape" data-shape="trapezoid" style="position:absolute;left:360px;top:360px;width:1200px;height:120px;background:var(--deep-navy);transform:rotate(180deg);"></div>
<div data-object="true" data-object-type="shape" data-shape="trapezoid" style="position:absolute;left:485px;top:496px;width:950px;height:120px;background:var(--deep-navy-light);transform:rotate(180deg);"></div>
<div data-object="true" data-object-type="shape" data-shape="trapezoid" style="position:absolute;left:610px;top:632px;width:700px;height:120px;background:#4A6A96;transform:rotate(180deg);"></div>
<div data-object="true" data-object-type="shape" data-shape="trapezoid" style="position:absolute;left:735px;top:768px;width:450px;height:120px;background:var(--lenovo-red);transform:rotate(180deg);"></div>
<!-- 层内叠字(单行居中,line-height=层高) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:360px;top:360px;width:1200px;height:120px;text-align:center;">
  <div style="font-size:24px;font-weight:700;color:#FFFFFF;line-height:120px;">线索(全部触达)</div>
</div>
<!-- 层 2-4 叠字同构 -->
<!-- 左侧阶段标签(右对齐) + 右侧数值(主色) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:404px;width:220px;text-align:right;">
  <div style="font-size:22px;font-weight:600;color:var(--text-secondary);line-height:44px;">阶段一</div>
</div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:1600px;top:404px;width:220px;">
  <div class="num" style="font-size:28px;font-weight:800;color:var(--lenovo-red);line-height:44px;">10,000</div>
</div>
<!-- 层 2-4 侧注同构,y 各 +136(404/540/676/812) -->
```

| 参数 | 调什么 |
|---|---|
| 3 层 | w 1200/850/500,h 140,y = 360/516/672(底 812,下方可补一行结论) |
| 4 层 | 如骨架:1200/950/700/450,h 120,y 360/496/632/768(底 888) |
| 配色 | 同色系由深到浅单向;末层可用主色(转化终点) |
| 侧注 | 左=阶段名(右对齐灰),右=数值/转化率(主色 num) |

**反 AI 味要点**:✓ 递减语义才画漏斗;❌ 层间加渐变/阴影;`transform-origin` 保持默认居中(契约要求),叠字不随转。

---

### 原型 26 · 金字塔(满填)

**用途**:分层模型(战略→战术→执行/需求层次/能力栈),图示感强于原型 16(横条收窄)。**何时别用**:并列关系(23);递减语义(25)。
**填充**:满填。顶层 `triangle` + 下层 `trapezoid`(预设顶边约为底边一半,天然成塔)。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">三层模型,标题说结构</div>
</div>
<!-- 3 层(h180 gap16,顶 340;顶层三角 w500,中梯 w1000,底梯 w1500) -->
<div data-object="true" data-object-type="shape" data-shape="triangle" style="position:absolute;left:710px;top:340px;width:500px;height:180px;background:var(--deep-navy);"></div>
<div data-object="true" data-object-type="shape" data-shape="trapezoid" style="position:absolute;left:460px;top:536px;width:1000px;height:180px;background:var(--deep-navy-light);"></div>
<div data-object="true" data-object-type="shape" data-shape="trapezoid" style="position:absolute;left:210px;top:732px;width:1500px;height:180px;background:#E8EEF5;border:1px solid var(--border-medium);"></div>
<!-- 层内叠字(上层白字,底层深字;两行:层名 26 粗 + 一句 18) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:710px;top:360px;width:500px;text-align:center;">
  <div style="font-size:26px;font-weight:700;color:#FFFFFF;line-height:1.3;">战略层</div>
  <div style="font-size:22px;color:#C9D2DC;margin-top:8px;line-height:1.4;">一句话说明</div>
</div>
<!-- 中/底层叠字同构(y 556/752;底层文字换 --charcoal 系) -->
```

| 参数 | 调什么 |
|---|---|
| 3 层 | 如骨架(底 912);层宽 500/1000/1500 |
| 4 层 | w 400/800/1200/1600,h 140,y = 330/486/642/798(底 938) |
| 配色 | 深→浅单向;底层用**浅主色预算混合色**(#E8EEF5 类)+细边框+深字——❌ 勿用与页面同底色(off-white 页面配 off-white 底层会隐形,2026-08-05 样张实测踩过) |
| 叠字 | 顶层三角内文字偏下(top 留出尖角);层名 ≤6 字 |

**反 AI 味要点**:✓ 层间 16px 缝比无缝拼接更干净(预设梯形顶边比例固定,微差不强求);❌ 彩虹分层、❌ 每层加图标。

---

### 原型 27 · 循环图(满填)

**用途**:闭环流程(PDCA/增长飞轮/运营闭环)。**何时别用**:单向流程(24);仅 3 节点(chevron 更直给)。
**填充**:满填。结构:**内联 SVG 圆环+箭头(整体截图)** + 中心圆(原生)+ 4 张卫星卡(原生,盖住环的四正点)。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">飞轮标题:转起来的是什么</div>
</div>
<!-- 环形箭头(内联 SVG;圆心=画布 960,630;四正点被卫星卡盖住) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:700px;top:420px;width:520px;height:420px;">
  <svg width="520" height="420" viewBox="0 0 520 420" fill="none" stroke="#4A4F55" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><circle cx="260" cy="210" r="150"/><polyline points="371 301 366 316 381 311"/><polyline points="169 321 154 316 159 331"/><polyline points="149 119 154 104 139 109"/><polyline points="351 99 366 104 361 89"/></svg>
</div>
<!-- 中心命题圆 -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:850px;top:520px;width:220px;height:220px;border-radius:50%;background:var(--deep-navy);"></div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:850px;top:520px;width:220px;height:220px;text-align:center;">
  <div style="font-size:26px;font-weight:700;color:#FFFFFF;line-height:220px;">核心命题</div>
</div>
<!-- 4 卫星卡(N 790,330 / E 1160,560 / S 790,790 / W 420,560;340×140) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:790px;top:330px;width:340px;height:140px;background:var(--white);border:1px solid var(--border-light);border-radius:12px;padding:24px 28px;">
  <div style="font-size:24px;font-weight:700;color:var(--charcoal);line-height:1.3;">① 环节名</div>
  <div style="font-size:24px;line-height:1.5;color:var(--text-secondary);margin-top:8px;">一句说明,一行半内。</div>
</div>
<!-- E/S/W 卡同构 -->
```

| 参数 | 调什么 |
|---|---|
| 节点数 | 固定 4(N/E/S/W);3 或 ≥5 换原型 |
| 环色 | 单色(炭灰或主色);箭头同色;禁分段彩虹 |
| 中心圆 | 220px 深底白字;命题 ≤8 字 |
| 卫星卡 | 340×140;图标可选(加则 4 张全加) |

**反 AI 味要点**:✓ 环交给 SVG(截图)最干净,节点/文字全原生;❌ 别用 4 个预设箭头形状拼环(对不齐反而业余);卡片盖环点是刻意穿线效果,DOM 序必须环先卡后。

---

### 原型 28 · 中心辐射(满填)

**用途**:一个核心 + 4 个辐射维度(平台+场景/中台+前台/总目标+分领域)。**何时别用**:维度间有流向(27/24);≥5 个辐射点(23 网格)。
**填充**:满填。结构:中心圆 + 正交细连接线(横平竖直,免旋转计算)+ 4 卫星卡。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">一个核心,四个支撑</div>
</div>
<!-- 连接线(先画,在卡下):N 竖线/S 竖线/W 横线/E 横线 -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:958px;top:500px;width:4px;height:20px;background:var(--border-medium);"></div>
<div data-object="true" data-object-type="shape" style="position:absolute;left:958px;top:740px;width:4px;height:20px;background:var(--border-medium);"></div>
<div data-object="true" data-object-type="shape" style="position:absolute;left:560px;top:628px;width:290px;height:4px;background:var(--border-medium);"></div>
<div data-object="true" data-object-type="shape" style="position:absolute;left:1070px;top:628px;width:290px;height:4px;background:var(--border-medium);"></div>
<!-- 中心圆 -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:850px;top:520px;width:220px;height:220px;border-radius:50%;background:var(--deep-navy);"></div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:850px;top:520px;width:220px;height:220px;text-align:center;">
  <div style="font-size:28px;font-weight:700;color:#FFFFFF;line-height:220px;">核心</div>
</div>
<!-- 4 卫星卡(N 770,330 / S 770,760 / W 180,545 / E 1340,545;380×170) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:770px;top:330px;width:380px;height:170px;background:var(--white);border:1px solid var(--border-light);border-radius:12px;padding:26px 30px;">
  <div style="font-size:26px;font-weight:700;color:var(--charcoal);line-height:1.3;">维度名</div>
  <div style="font-size:26px;line-height:1.5;color:var(--text-secondary);margin-top:10px;">说明两行内,讲清与核心的关系。</div>
</div>
<!-- S/W/E 卡同构(S 770,760;W/E 180/1340,545);其中一张可换浅主色底强调(至多一张) -->
```

| 参数 | 调什么 |
|---|---|
| 卫星数 | 4(N/E/S/W);3 个则撤一条线(别留断线) |
| 连接线 | 4px 灰细线,**无箭头**(辐射非流向) |
| 中心圆 | 220px;词 ≤6 字;可换主色 |
| 强调 | 至多 1 张卫星卡用浅主色底 |

**反 AI 味要点**:✓ 正交连接线(横平竖直)永远不会错;❌ 斜线连接(旋转对不齐即业余)、❌ 卫星卡加阴影堆质感。

---

### 原型 29 · 对比卡阵(满填)

**用途**:A/B 方案对决、新旧对照的图示版(裸排版见原型 12)。**何时别用**:三方以上(19 表格);无对立语义(23)。
**填充**:满填。结构:双卡(800×560)+ 中央 VS 徽章(语义标记,反模式 6 豁免)+ 卡内图标特征行。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">对比结论先行的标题</div>
</div>
<!-- 左卡:旧/保守(白底细边框) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:340px;width:800px;height:560px;background:var(--white);border:1px solid var(--border-light);border-radius:12px;padding:44px;">
  <div style="font-size:22px;font-weight:600;letter-spacing:2px;color:var(--text-tertiary);">过去 / 方案 A</div>
  <div style="font-size:34px;font-weight:700;color:var(--charcoal);margin-top:10px;line-height:1.25;">旧方式名</div>
  <div style="display:flex;align-items:center;gap:14px;margin-top:34px;">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#9AA0A6" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><line x1="9" y1="9" x2="15" y2="15"/><line x1="15" y1="9" x2="9" y2="15"/></svg>
    <div style="font-size:26px;line-height:1.5;color:var(--text-primary);">痛点特征一</div>
  </div>
  <!-- 特征行 2-4 同构,margin-top:22px;左右卡行数对齐 -->
</div>
<!-- 右卡:新/推荐(深底) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:1020px;top:340px;width:800px;height:560px;background:var(--deep-navy);border-radius:12px;padding:44px;">
  <div style="font-size:22px;font-weight:600;letter-spacing:2px;color:var(--accent-orange);">现在 / 方案 B</div>
  <div style="font-size:34px;font-weight:700;color:#FFFFFF;margin-top:10px;line-height:1.25;">新方式名</div>
  <div style="display:flex;align-items:center;gap:14px;margin-top:34px;">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#6BCB77" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="8 12.5 11 15.5 16.5 9"/></svg>
    <div style="font-size:26px;line-height:1.5;color:#E8ECF1;">解法特征一</div>
  </div>
  <!-- 特征行 2-4 同构 -->
</div>
<!-- 中央 VS 徽章(DOM 在双卡之后,压缝) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:905px;top:565px;width:110px;height:110px;border-radius:50%;background:var(--lenovo-red);"></div>
<div data-object="true" data-object-type="textbox" style="position:absolute;left:905px;top:565px;width:110px;height:110px;text-align:center;">
  <div style="font-size:36px;font-weight:800;color:#FFFFFF;line-height:110px;">VS</div>
</div>
```

| 参数 | 调什么 |
|---|---|
| 双卡 | 800×560 at (100,340)/(1020,340),底 900 |
| 特征行 | 3-4 行/卡,左右行数必须相等(视觉天平) |
| 图标 | 左侧灰 x / 右侧绿勾(语义对立);或两侧同用中性圆点 |
| VS 徽章 | 110px 主色圆,白 36px;压缝位置 x905 居中 |

**反 AI 味要点**:✓ 一侧浅一侧深 = 视觉立场;❌ 双卡同深同浅分不出立场、❌ 每行换图标色。徽章是语义件非装饰件。

---

### 原型 30 · 色带分节页(满填)

**用途**:3-4 个分节论述(每带 = 主张+一句支撑+右侧证据位),替代纯文字条目的"重"版本;章节内导航亦可。**何时别用**:并列特性有图标语义(23 更轻);严格流程(24)。
**填充**:满填。结构:横向纯色带 stack(结构色带,合法——渐变装饰条仍禁,反模式 4 不变)。

```html
<div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
  <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">三个主张,逐层推进</div>
</div>
<!-- 色带 stack(3 带,h180 gap20,y=330/530/730,底 910) -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:330px;width:1720px;height:180px;background:var(--deep-navy);border-radius:10px;display:flex;align-items:center;padding:0 48px;">
  <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#F39800" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2" fill="#F39800" stroke="none"/></svg>
  <div style="margin-left:32px;flex:1;">
    <div style="font-size:28px;font-weight:700;color:#FFFFFF;line-height:1.3;">主张一,一句话说完</div>
    <div style="font-size:22px;line-height:1.5;color:#C9D2DC;margin-top:8px;">支撑一句:数据或例子。</div>
  </div>
  <div class="num" style="font-size:56px;font-weight:800;color:#F39800;line-height:1;">01</div>
</div>
<!-- 带 2(--deep-navy-light)/ 带 3(浅底 --card-bg + 深字 + 编号换主色)同构 -->
```

| 参数 | 调什么 |
|---|---|
| 带数/高度 | 3 带 h180(y 330/530/730);4 带 h140 gap 16(y 330/486/642/798) |
| 配色 | 深→浅单向递进(深深/深浅/浅底深字);编号列统一主色 |
| 带内 | 图标 44px(浅带换主色);主张 28px;支撑 22px;右侧编号 56px num |
| 变体 | 左侧深栏导航:480px 深栏(x100,章节目录)+ 右侧 2-3 色带(x620,w1200) |

**反 AI 味要点**:✓ 纯色带是结构分带;❌ 渐变带(装饰指纹)、❌ 每带一色;带内文字 ≤2 行,编号/图标二选一在右侧或左侧,别双侧堆满。

---

## 使用纪律(摘要)

1. 选原型 = **二级选择**:先按 brief 形式列定视觉形式(文字/图示/图表/图片/混合),再从该形式组选原型;写页时只看 brief 指定的原型小节
2. 同原型不连续 >2 页;每 deck ≥6 原型;**纯文字卡片矩阵 ≤2 页**(图标网格不受此限,见反模式 7 结构豁免)
3. **形式分布**按 `design-principles.md` 第五章档位执行(平衡型:纯文字内容页 ≤50%、同形式连排 ≤3 页、每内容页 ≥1 个非文字视觉元素)
4. airy 页(1/2/4/5/6/21)承担节奏,每 3-4 页 1 张;满填页执行内容区 ≥85% 利用率
5. 所有骨架字号为演讲档;换档按 `design-principles.md` 字号阶等比;内容量 <60% 时按 scale-to-fill 上调
6. 原型可组拼(如 18+19 = 20),但一页只用一种"主角"
