# 页面原型库(page-archetypes · 20 个原型 22 款)

> **人类专业 PPT 的页面类型学。** 写页先选原型,再填内容——原型决定"这一页怎么摆",配方(`layout-recipes.md`)只管容器内部写法。
> 每个原型:用途 / 何时别用 / 填充行为(满填|airy) / HTML 骨架 / 参数表 / 反 AI 味要点。
> 骨架全部遵循 `design-principles.md`(分区/字号阶/scale-to-fill)与 `html-spec.md`(转换契约);字号以**演讲档**标注,其他档位按 design-principles 字号阶等比换算。
> 选原型流程:访谈 Q5 大纲确认时给每页指派原型 → 写入 deck-brief 大纲表 → 写页时只查 brief 指定的原型小节。

## 索引

| 组 | 原型 | 填充 | 一句话 |
|---|---|---|---|
| 开场导航 | 1 封面·深底大字 | airy | 深底+超大标题+细强调条 |
| | 2 封面·浅底编辑 | airy | 浅底+左对齐巨标+底部信息行 |
| | 3 议程 | 满填 | 大数字编号裸列表 |
| | 4 章节分隔 | airy | 超大编号+章节名 |
| | 5 大字观点 | airy | 一句话占满页 |
| | 6 引用页 | airy | 巨引号+引文+署名 |
| 论述 | 7 编辑文字页 | 满填 | action title+双栏文字,零卡片 |
| | 8 要点列表 | 满填 | 粗体引导裸排要点+细分隔线 |
| | 9 不对称分栏 7:5 | 满填 | 主栏论述+辅栏深面/数据 |
| | 10 图文页 | 满填 | 左图右文(可镜像) |
| | 11 全出血大图页 | 出血满填 | 图满画布+左下文字块 |
| 对比流程 | 12 双栏对照 | 满填 | 旧vs新/AvsB+中缝 |
| | 13 流程步骤 | 满填 | 横向步骤带(大数字或 chevron) |
| | 14 时间线 | 满填 | 横轴虚线+节点交替标签 |
| | 15 2×2 象限 | 满填 | 坐标轴+四象限+点位 |
| | 16 层级 | 满填 | 3-4 层横条,上窄下宽 |
| 数据 | 17 大数字带 | 满填 | 3-4 个巨数字+标签,细线分隔 |
| | 18 图表主角 | 满填 | 大图表(1100px)+右侧解读栏 |
| | 19 表格主角 | 满填 | 大表格居中,表头深色 |
| | 20 仪表盘 | 满填 | KPI 行+图表+表格(阅读/混合档) |
| 收尾 | 21 行动号召 | airy | 深底+大字行动句+联系方式 |
| | 22 附录指引 | 满填 | 资料清单编辑式排版 |

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
    <div style="font-size:18px;line-height:1.4;color:var(--on-navy-dim);">汇报人 · 机构 · 2026-08</div>
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
    <div style="font-size:18px;line-height:1.4;color:var(--text-secondary);">作者 · 日期 · 版本</div>
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
      <div style="font-size:20px;line-height:1.4;color:var(--text-secondary);margin-top:6px;">一句话说明这章回答什么问题</div>
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
    <div style="font-size:22px;line-height:1.5;color:var(--text-secondary);text-align:center;">—— 一个数字或来源作佐证</div>
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
    <div style="font-size:20px;line-height:1.5;color:var(--text-tertiary);">—— 姓名 · 头衔 · 出处</div>
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
    <div style="font-size:22px;line-height:1.65;color:var(--text-primary);margin-top:24px;">论证正文 4-6 行,自然往下排。主栏不装盒子,保持编辑感。</div>
  </div>
  <!-- 辅栏:深色面(证据区) -->
  <div data-object="true" data-layout-w="5fr" style="background:var(--deep-navy);border-radius:10px;padding:40px;">
    <div style="font-size:20px;font-weight:600;letter-spacing:2px;color:var(--accent-orange);">关键证据</div>
    <div class="num" style="font-size:72px;font-weight:800;line-height:1.1;color:var(--on-navy-text);margin-top:16px;">87<span style="font-size:36px;">%</span></div>
    <div style="font-size:20px;line-height:1.55;color:var(--on-navy-sub);margin-top:16px;">证据说明 1-2 行</div>
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
  <div style="font-size:22px;line-height:1.65;color:var(--text-primary);margin-top:20px;">解读 3-5 行。图与文同高,底部对齐页脚区。</div>
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
    <div style="font-size:20px;line-height:1.4;color:#C9D2DC;">补充说明一行 · 来源</div>
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
  <div style="font-size:22px;line-height:1.7;color:var(--text-primary);margin-top:24px;">
    · 痛点一,一行说清<br>· 痛点二<br>· 痛点三
  </div>
</div>
<!-- 中缝细线 -->
<div data-object="true" data-object-type="shape" style="position:absolute;left:940px;top:360px;width:1px;height:520px;background:var(--border-medium);"></div>
<!-- 右栏:新/方案(主色强调) -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:1020px;top:340px;width:800px;">
  <div style="font-size:22px;font-weight:600;letter-spacing:2px;color:var(--lenovo-red);">现在</div>
  <div style="font-size:30px;font-weight:700;line-height:1.3;color:var(--charcoal);margin-top:12px;">新方式</div>
  <div style="font-size:22px;line-height:1.7;color:var(--text-primary);margin-top:24px;">
    · 解法一<br>· 解法二<br>· 解法三
  </div>
</div>
```

**反 AI 味要点**:❌ 双卡片+顶边色条+图标(旧模式 7);✓ 裸双栏+中缝线。"新"侧可用一处主色,全页唯一高亮。

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
    <div style="font-size:20px;line-height:1.6;color:var(--text-secondary);margin-top:12px;">这一步做什么、产出什么,2-3 行。</div>
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
  <div style="font-size:20px;line-height:1.5;color:var(--text-primary);">里程碑事件,两行内</div>
</div>
<!-- 节点 2-4 同构,x 均匀分布(间隔 1720/N);已完成节点主色,未来节点边框白心 -->
```

**反 AI 味要点**:❌ 旋转标签/渐变圆/虚线(旧模式 4 的炫技三件套);✓ 实线+圆点+正立文字。当前位置用主色,是唯一点缀。

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
    <div style="font-size:20px;line-height:1.55;color:var(--text-secondary);margin-top:10px;">点位/说明</div>
  </div>
  <!-- 其余三象限;目标象限底换 --deep-navy、文字换 on-navy 组 -->
</div>
<!-- 轴标签 -->
<div data-object="true" data-object-type="textbox" style="position:absolute;left:260px;top:920px;width:1300px;text-align:center;">
  <div style="font-size:18px;color:var(--text-tertiary);">X 轴名 →</div>
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
      <div style="font-size:18px;color:var(--on-navy-sub);margin-top:8px;line-height:1.4;">支撑说明</div>
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
    <div style="font-size:22px;line-height:1.4;color:var(--text-secondary);margin-top:20px;">指标说明,一两行</div>
    <div style="font-size:18px;line-height:1.4;color:var(--signal-green);margin-top:12px;">↑ 同比 +12pp</div>
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
  <div style="font-size:20px;line-height:1.65;color:var(--text-primary);margin-top:20px;">
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
    <div style="font-size:18px;color:var(--text-secondary);margin-top:12px;">指标</div>
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
    <div style="font-size:22px;line-height:1.5;color:var(--text-primary);">
      <span style="font-weight:700;color:var(--charcoal);">数据来源:</span>口径、时间范围、样本说明
    </div>
  </div>
  <!-- 参考资料/术语表/详细参数入口 同构 -->
</div>
```

**反 AI 味要点**:与议程页同构(首尾呼应);条目含真实出处,❌ 不写"详见相关资料"。

---

## 使用纪律(摘要)

1. 选原型 = 访谈 Q5 为每页指派,写入 brief 大纲表;写页时只看 brief 指定的原型小节
2. 同原型不连续 >2 页;每 deck ≥6 原型;卡片矩阵(本库已限额)≤2 页
3. airy 页(1/2/4/5/6/21)承担节奏,每 3-4 页 1 张;满填页执行内容区 ≥85% 利用率
4. 所有骨架字号为演讲档;换档按 `design-principles.md` 字号阶等比;内容量 <60% 时按 scale-to-fill 上调
5. 原型可组拼(如 18+19 = 20),但一页只用一种"主角"
