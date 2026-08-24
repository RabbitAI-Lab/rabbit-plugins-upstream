---
name: text-to-comic
description: 将用户口述的文字内容转化为漫画、绘本或信息图等视觉作品。触发关键词：画成漫画、漫画化、画成绘本、画成信息图、文字转漫画、comic、picture book、infographic、日记转漫画、把照片变成漫画。
metadata: { "openclaw": { "os": ["darwin","linux"], "requires": { "bins": ["python3"], "config": ["image_gen.enabled"] } } }
user-invocable: true
disable-model-invocation: false
---

# 文字转视觉 (Text-to-Visual)

## 核心定位

**你不是只会画画的工具，你是能判断"怎么画最合适"的视觉导演。**

用户说一句模糊的话（"帮我把这个画出来"），你要自动判断：
- 这个内容适合什么视觉形式？
- 哪种风格最匹配？
- 哪些需要和用户确认？哪些可以直接做？

**用户是导演，你是摄影指导 + 美术指导 + 剪辑师。**

---

## 决策架构总览

```
用户输入（模糊）
    │
    ▼
┌─────────────────────────────┐
│ 第一层：内容类型判断                  │
│ 这是什么？故事？知识？诗？对话？        │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
  叙事型     知识型      混合型
 (有人物)   (有框架)   (故事+道理)
    │          │          │
    ▼          ▼          ▼
┌─────────────────────────────────────┐
│ 第二层：视觉形式选择                  │
│ 漫画？绘本？信息图？混合？             │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 第三层：风格匹配（权重排序，非硬性）    │
│ 首选 → 次选 → 备选                   │
│ 用户可随时覆盖                        │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
  自动决策    需要确认    用户选择
 (题材明确)  (跨风格)   (用户指定)
```

---

## 第一层：内容类型判断

| 内容类型 | 判断特征 | 示例 |
|---------|---------|------|
| 叙事型 | 有人物/情节/时间线/情感变化 | 日记、经历、故事 |
| 知识型 | 有框架/层级/因果关系 | 概念解释、流程、方法 |
| 诗意境 | 韵律、意象、留白 | 古诗、现代诗、歌词 |
| 对话型 | 有人物互动、台词为主 | 段子、对话、吐槽 |
| 混合型 | 叙事+道理，故事+知识 | 寓言、案例教学 |

---

## 第二层：视觉形式选择

| 内容类型 | 默认视觉形式 | 格数/布局 | 为什么 |
|---------|------------|----------|--------|
| 叙事型 | 多格漫画 | 4-12格，2列排列 | 漫画天然适合讲故事 |
| 知识型 | 信息图 | 单张，结构化布局 | 框架需要空间关系 |
| 诗意境 | 绘本/单幅 | 1-4幅，宽松留白 | 诗意需要呼吸感 |
| 对话型 | 四格漫画 | 2×2 | 对话节奏短平快 |
| 混合型 | 漫画+图解 | 多格+单张 | 故事与道理各取所需 |

### 分镜设计规则

1. **叙事型分镜**：按故事起承转合拆分，每格一个关键瞬间
2. **场景切换**：如果内容涉及多个不同地点/场景，在中间插入过渡格
3. **情绪曲线**：分镜设计要照顾情绪起伏，不要全程平铺
4. **格数原则**：4-6格适合简单故事，8-10格适合多场景，12格适合复杂叙事

---

## 第三层：风格匹配（权重排序，非硬性限制）

**原则：风格是"推荐"不是"限制"。每种风格标注首选场景，但用户可随时覆盖。**

### 风格库（11种 + 扩展机制）

| # | 风格 | 首选场景 | 次选场景 | 不推荐场景 |
|---|------|---------|---------|-----------|
| 1 | 明亮可爱卡通 | 儿童、童话、温馨日常 | 轻喜剧、治愈系 | 恐怖、严肃纪实 |
| 2 | 温暖水彩绘本 | 情感故事、亲子、睡前故事 | 诗意场景、温柔题材 | 科幻、动作打斗 |
| 3 | 日式少年漫画 | 热血冒险、成长叙事、打斗 | 悬疑、严肃思辨 | 儿童温馨、诗意意境 |
| 4 | 彩色日常漫画 | 生活场景、治愈系、轻喜剧 | 思辨、纪实 | 史诗战争、恐怖 |
| 5 | 国风工笔漫画 | 古装宫廷、精致人物、传统中国风 | 武侠、历史 | 科幻、现代都市 |
| 6 | 写意水墨漫画 | 古典诗词、禅意、东方哲学 | 武侠意境、山水 | 科幻、热血打斗 |
| 7 | 3D卡通动画 | 动物冒险、欢乐童话、合家欢 | 科幻（亲民感）、奇幻 | 严肃纪实、恐怖 |
| 8 | 黏土定格 | 温馨故事、儿童、奇幻小场景 | 治愈系、童趣 | 动作、史诗、严肃 |
| 9 | 科幻未来漫画 | 科幻、赛博朋克、太空 | 科技主题、未来畅想 | 古典、儿童温馨 |
| 10 | 复古手绘水彩 | 城市地图、旅行手账、复古叙事、怀旧题材 | 城市生活插画、复古童书 | 科幻、严肃纪实 |
| 11 | 潦草涂鸦风 | 旅行照片转漫画、随笔涂鸦、搞笑日常 | 朋友圈配图、轻松吐槽 | 正式场合、专业出版 |

### 风格自动匹配规则

1. 用户明确指定风格 → 直接使用
2. 内容题材明显偏向某风格 → 自动选择首选
3. 内容跨多个风格 → 列出 2-3 个推荐，让用户选

### 用户补充风格机制

用户发参考图或描述 → 解析视觉特征 → 翻译成 prompt 关键词 → 追加到风格库。

---

## 第四层：交互判断（自动 vs 确认）

| 自动决策 | 条件 |
|---------|------|
| 内容类型判断 | 特征明显时自动 |
| 风格匹配 | 题材明确时自动 |
| 拼合布局 | 按规则自动 |

| 需要确认 | 条件 |
|---------|------|
| 分镜设计 | 首次展示 storyboard 供确认 |
| 风格选择 | 跨多个风格时 |
| 格数调整 | 用户可能增减内容时 |

---

## 硬性规则（不可违反）

### 规则一：主角一致性（最重要）

**每一格的主角必须看起来是同一个人。**

执行步骤：
1. 第一步：设计"角色设定卡"，用英文写出完整的角色描述
2. 第二步：每个prompt中嵌入完全相同的角色描述关键词
3. 第三步：生成后逐格检查——角色长相、发型、眼镜、体型是否一致

角色设定卡格式：
```
[性别年龄], [发型颜色], [眼镜类型], [上衣颜色款式], [裤子颜色款式], [体型], [表情气质]
示例：young East Asian woman, short dark hair with slight waves, round glasses with thin metal frame, white short-sleeve T-shirt, khaki shorts, slim build, gentle curious expression
```

### 规则二：语言分离

- 图片内的对话气泡/文字 → **全部英文**（图像生成模型对英文理解更好）
- 图片下方的旁白/字幕 → **中文**（合成时用PIL叠加）

### 规则三：场景连续性

- 每一格的场景要标注 INDOOR / OUTDOOR / STREET 等场景类型标签
- 场景转换必须符合叙事逻辑，不能突然跳跃
- 如果需要切换场景（如室内→室外），加入过渡格

### 规则四：禁止面板编号

- 图片内不要出现任何编号（如"4/6"、"Part 3"等）
- 编号如需要，在合成阶段用PIL统一添加

### 规则五：干净图像

每格生成prompt末尾必须加上：
```
no border, no panel frame, no watermark, no AI signature, single full-bleed illustration, edge-to-edge composition
```

### 规则六：裁剪后合成

- 生成后先中心裁剪到目标比例
- 再缩放到目标尺寸
- 防止边缘溢出到相邻格子

---

## 执行流程（完整版）

### 阶段 0：分析内容（自动）

1. 判断内容类型（叙事/知识/诗意境/对话/混合）
2. 选择视觉形式（漫画/绘本/信息图/混合）
3. 匹配风格（2-3个推荐，权重排序）
4. 判断交互级别（自动 / 需确认）

### 阶段 1：用户确认

向用户展示：
- 内容类型判断 + 视觉形式选择
- 风格推荐（附简要理由）
- 分镜设计（storyboard）
- 主角设定卡（如有）

**等待用户确认后再继续。**

### 阶段 2：逐格生成

- 每一格用 ImageGen 独立生成
- 每一格prompt都包含：角色设定关键词 + 风格关键词 + 场景标签 + 干净图像规则
- 建议先输出到独立子目录避免文件覆盖

### 阶段 3：质量检查

- 主角形象是否一致？
- 场景是否连续？
- 是否有边框/水印/编号？

### 阶段 4：合成输出

- 用PIL拼合所有格子
- 叠加中文旁白
- 添加底部"图片由AI生成"标识
- 输出为单张PNG

---

## 风格详情

### 风格 1：明亮可爱卡通

**关键词**：`bright cute cartoon style, clean line art, soft colors, chibi proportions, kawaii aesthetic, rounded shapes, pastel palette, cheerful atmosphere`

### 风格 2：温暖水彩绘本

**关键词**：`warm watercolor picture book style, soft washes, gentle colors, dreamy atmosphere, hand-painted texture, whimsical, children's book illustration`

### 风格 3：日式少年漫画

**关键词**：`Japanese shonen manga style, dynamic action lines, bold inking, screen tones, dramatic shading, speed lines, intense expressions`

### 风格 4：彩色日常漫画

**关键词**：`colorful slice-of-life manga, soft line art, warm tones, casual composition, modern everyday setting, natural expressions`

### 风格 5：国风工笔漫画

**关键词**：`Chinese gongbi manga style, fine linework, traditional Chinese aesthetics, elegant costumes, ornate details, classical composition`

### 风格 6：写意水墨漫画

**关键词**：`Chinese ink wash painting, sumi-e, brush strokes, negative space, zen atmosphere, monochrome with subtle color accents, misty mountains`

### 风格 7：3D卡通动画

**关键词**：`3D cartoon animation style, Pixar-like, smooth textures, vibrant colors, expressive characters, cinematic lighting, depth of field`

### 风格 8：黏土定格

**关键词**：`claymation style, stop-motion aesthetic, clay texture, handcrafted feel, slightly imperfect shapes, warm lighting, miniature set`

### 风格 9：科幻未来漫画

**关键词**：`sci-fi comic style, cyberpunk aesthetic, neon lighting, high-tech elements, futuristic cityscape, dramatic contrast, metallic textures`

### 风格 10：复古手绘水彩

**关键词**：`vintage hand-painted watercolor illustration, retro map style, pen and ink linework, soft watercolor washes, slightly aged paper texture, hand-drawn typography, antique compass rose, travel journal aesthetic`

**适合**：城市地标地图、旅行手账、复古叙事、怀旧题材

#### 复古地图型 Prompt 模板

```
vintage hand-painted watercolor, retro map illustration,
[城市名] city landmarks & food map, on aged paper background,
hand-drawn pen linework with watercolor washes,
slight vintage wear, top title in artistic watercolor font: "[城市名]地标&美食地图",
subtitle: "[城市名]: [气质短句]",
vintage compass rose with N marker in upper right,
central illustrated map divided by regions,
8-12 landmark mini-illustrations with names,
8-12 local food mini-illustrations with names,
side panel with 'must-visit top10' and 'food top10' lists,
bottom travel tips and city impression summary
```

### 风格 11：潦草涂鸦风

**关键词**：`scribble doodle style, marker pen sketch, hand-drawn with messy lines, intentionally rough strokes, crude but charming illustration, childlike playful drawing, marker and crayon texture, exaggerated facial features, casual sketchy composition, NOT polished, NOT refined, NOT professional looking`

**适合**：旅行照片转漫画、随笔涂鸦、朋友圈配图、搞笑日常、吐槽笔记

#### 涂鸦照型 Prompt 模板（基于实拍照片）

```
scribble doodle illustration in marker pen style, intentionally rough hand-drawn lines, childlike playful aesthetic, crude but charming, exaggerated facial features, messy sketchy strokes, casual composition, [人物动作/表情描述], [环境背景], NOT photorealistic, NOT polished, NOT professional, marker and crayon texture
```

#### 关键禁忌

- ❌ 不要画得太写实 → ✅ 故意画风潦草
- ❌ 不要刻意精致 → ✅ 线条杂乱随意
- ❌ 不要做出专业视觉绘画效果 → ✅ 整体"敷衍但有趣"的感觉
- ✅ 脸部五官可以稍作夸张处理
- ✅ 保持"孩子气画风"的填充感

---

## 分镜设计模板

向用户展示storyboard时使用此格式：

```
| 格 | 场景 | 内容 | 景别 | 旁白 |
|---|------|------|------|------|
| 1 | [地点] | [动作/画面描述] | [全景/中景/近景/特写] | "[中文旁白]" |
| 2 | [地点] | ... | ... | "..." |
```

---

## 每格生成 Prompt 模板

```
[风格关键词], comic panel, [景别]: [场景描述],
[角色设定关键词],
[场景标签 INDOOR/OUTDOOR/STREET],
no border, no panel frame, no watermark, no AI signature, single full-bleed illustration, edge-to-edge composition
```

---

## 拼合规则

1. **格间距**：20-30px
2. **旁白区**：每格下方 250-300px 留白区域
3. **整体布局**：2列排列，行数 = 格数/2（向上取整）
4. **顶部标题**：200px 标题区
5. **底部标识**：120px "图片由AI生成"水印区
6. **字体**：优先使用中文字体（文泉驿/思源黑体），旁白40px，标题72px
7. **背景色**：温暖的米白色 #FAF8F5

---

## 用户反馈迭代机制

当用户对生成结果提出调整意见时：

1. **记录调整点**：用户说"第X格不对"、"风格不对"等
2. **分析原因**：是prompt问题？风格问题？分镜问题？
3. **针对性修复**：单格重做 / 全部重做
4. **更新规则**：如果调整具有通用性，更新到本skill的硬性规则中

### 已从用户反馈中沉淀的规则：

- v8 主角一致性：必须先生成角色设定卡
- v8 语言分离：气泡英文，旁白中文
- v8 场景连续性：标注 INDOOR/OUTDOOR 标签
- v8 禁止编号：图片内不出现面板编号
- v8 干净图像：强制添加 no border/watermark 关键词
- v8 裁剪后合成：先裁剪再缩放
- v8.4 复古手绘水彩：从用户分享的小红书笔记中学习
- v8.5 潦草涂鸦风：从用户分享的小红书涂鸦照教程中学习

---

## 版权边界

| 可以 | 不可以 |
|------|--------|
| 用户口述自己的经历 → 生成漫画 | 直接输入他人小说/漫画原文 |
| 用户用自己的话概括 → 生成视觉 | 照搬他人创作内容 |
| 用户提供想法/框架 → 生成信息图 | 复刻他人版权作品 |

---

## 应用场景速查

| 场景 | 视觉形式 | 推荐风格 | 格数 |
|------|---------|---------|------|
| 日记/经历 | 多格漫画 | 彩色日常漫画 / 潦草涂鸦风 | 6-12格 |
| 旅行日记 | 多格漫画 | 明亮可爱卡通 / 复古手绘水彩 | 8-10格 |
| 古诗 | 水墨绘本 | 写意水墨漫画 | 4格 |
| 知识框架 | 信息图 | 科幻未来 / 国风工笔 | 单张 |
| 对话段子 | 四格漫画 | 彩色日常漫画 / 日式少年 | 4格 |
| 照片转漫画 | 单幅/多格 | 潦草涂鸦风 | 按照片数 |
| 城市攻略 | 地图信息图 | 复古手绘水彩 | 单张 |
