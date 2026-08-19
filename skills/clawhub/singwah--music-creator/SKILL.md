---
name: music-creator
description: "全能音乐创作助手——交互式选曲风格（说唱、R&B、儿歌、流行、摇滚、电子、爵士、古典、民谣、鬼畜音MAD等40+子风格），从歌词创作到HappyShrimp风格提示词一站式输出。支持中文/英文/双语/日语。当用户要求写歌曲、创作音乐、做儿歌、写Rap、R&B、流行歌曲、编曲、作曲、鬼畜、音MAD时使用。"
version: 5.2.0
---

# 全能音乐创作助手 (Music Creator v5.2)

纯 HappyShrimp（快乐虾米）驱动的音乐创作：交互式选风格 → 歌词创作 → 作曲编曲 → HappyShrimp 风格提示词 → 输出包。
覆盖流行、摇滚、嘻哈、电子、R&B、爵士、古典、民谣/世界音乐、鬼畜音MAD 共 9 大类 40+ 子风格。

---

## Step 0: 交互式选择 (必须先执行)

**收到创作请求后，使用 AskUserQuestion 收集需求。分两轮：**

### 第一轮：大类风格

```
header: "音乐大类"
options:
  - label: "嘻哈 Hip-Hop"
    description: "Old School / Boom Bap / Trap / Drill / Conscious / Melodic"
  - label: "流行 Pop / R&B"
    description: "Synth-pop / Dance-pop / K-Pop / C-Pop / Motown / Neo-Soul"
  - label: "摇滚 Rock / 电子 EDM"
    description: "Classic / Punk / Metal / Alt / House / Techno / Trance / Dubstep"
  - label: "更多风格"
    description: "爵士/古典/民谣/国风/拉丁/鬼畜音MAD/儿歌 (选此项后追问具体风格)"
multiSelect: false
```

### 第二轮：子风格 + 主题 + 语言

根据第一轮选择，展示对应子风格（见下方完整列表）。同时收集：

```
header: "主题情绪"
options:
  - label: "欢快/正能量"
  - label: "伤感/抒情"
  - label: "热血/燃"
  - label: "反讽/搞笑/鬼畜"
multiSelect: false

header: "语言声音"
options:
  - label: "中文 + 男声"
  - label: "中文 + 女声"
  - label: "英文"
  - label: "中英/日语混搭"
multiSelect: false
```

如果用户选了"更多风格"，追问具体风格名称（如"爵士 Swing"、"鬼畜 RAP鬼畜"、"儿歌"等）。

**收集完毕 → 进入创作流程。**

---

## Step 1: Match Style (风格匹配)

根据选择确定子风格和 HappyShrimp 声场参数。完整风格列表：

### 流行 Pop
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| Synth-pop | 110-130 | Am, Em | 合成器, 复古80年代, 洗脑hook |
| Dance-pop | 120-130 | Am, Fm | 四拍底鼓, 欢快, 精致制作 |
| Indie Pop | 100-120 | G, D | 清脆吉他, lo-fi, 梦幻 |
| K-Pop | 110-130 | Am, Fm | 动态, 舞蹈感, hook密集 |
| C-Pop | 100-125 | Am, Gm | 华语流行, 抒情, 情歌质感 |

### 摇滚 Rock
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| Classic Rock | 110-130 | E, A | 电吉他riff, 驱动鼓点 |
| Punk | 150-200 | E, A | 快速, 粗粝, 强力和弦, 叛逆 |
| Metal | 120-180 | Em, Dm | 失真吉他, 双踩, 重型 |
| Alternative Rock | 100-140 | Em, Am | 动态对比, 效果器 |
| Grunge | 90-120 | Em, Dm | 泥泞,  quiet-loud, 愤怒 |
| Post-Rock | 70-120 | Am, Em | 电影感, 层层递进, 器乐 |

### 嘻哈 Hip-Hop
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| Old School | 90-105 | Am, Dm | funky律动, DJ搓碟, 愉悦 |
| Boom Bap | 85-100 | Am, Cm | 灵魂乐采样, 硬鼓, 歌词向 |
| Trap | 130-150 (half) | Am, F#m | 808贝斯, 三连音hi-hat, 暗黑弹跳 |
| Drill | 130-145 | Cm, Dm | 滑音808, 暗黑旋律, 攻击性 |
| Conscious Rap | 85-100 | Am, Em | 爵士beat, 内省, 叙事 |
| Melodic Rap | 120-140 | Am, Dm | autotune, 吉他/钢琴, 情绪化 |

### 电子 EDM
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| House | 120-130 | Am, Fm | 四拍底鼓, 钢琴stab, 律动 |
| Techno | 125-140 | Am, Dm | 极简, 重复, 工业感 |
| Trance | 130-145 | Am, Em | 欣快, 升华breakdown, 琶音 |
| Dubstep | 130-150 (half) | Fm, Gm | wobble bass, 重drop, 攻击性 |
| Drum & Bass | 160-180 | Am, Em | 快速碎拍, 深贝斯, 高能 |
| Ambient | 60-90 | any | 氛围, 纹理, 无鼓点 |
| Future Bass | 140-160 (half) | Am, Fm | 超级锯齿和弦, 变调人声, 明亮drop |

### R&B / 灵魂乐
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| Motown | 100-120 | C, F | 铜管, 铃鼓, 呼应式 |
| Funk | 90-115 | Em, Am | slap贝斯, wah吉他, 紧凑律动 |
| Neo-Soul | 80-100 | Gm, Cm | 爵士和弦, 温暖贝斯, 律动 |
| Contemporary R&B | 80-110 | Dm, Fm | 丝滑键盘, 柔滑人声, 现代 |

### 爵士 / 布鲁斯
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| Swing | 120-160 | Bb, F | 大乐队, walking bass, 铜管stab |
| Bebop | 180-260 | Bb, F | 快速即兴, 复杂和弦 |
| Cool Jazz | 90-120 | Dm, Gm | 松弛, 旋律性, 刷鼓 |
| Fusion Jazz | 100-140 | Dm, Am | 电声乐器, 摇滚能量+爵士 |
| Delta Blues | 70-100 | E, A | 原声吉他, 滑棒, 粗粝人声 |
| Chicago Blues | 90-120 | E, A | 电声布鲁斯, shuffle, 口琴 |

### 古典
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| 巴洛克 Baroque | 80-120 | Dm, Am | 羽管键琴, 对位法, 华丽 |
| 古典主义 Classical | 90-130 | C, G | 均衡, 优雅, 弦乐四重奏 |
| 浪漫主义 Romantic | 60-120 | Cm, Eb | 激情, 管弦乐, 动态 |
| 极简主义 Minimal | 60-100 | any | 重复音型, 渐变 |
| 歌剧 Opera | varies | varies | 戏剧性, 管弦乐, 人声炫技 |
| 室内乐 Chamber | 80-120 | G, D | 亲密, 小编制 |

### 民谣 / 世界音乐
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| 国风 Chinese | 70-110 | Am, Em | 古筝, 二胡, 中国五声音阶, 诗意 |
| 凯尔特民谣 Celtic | 90-130 | D, G | 小提琴, 锡哨, 手鼓 |
| Reggaeton | 85-100 | Am, Dm | dembow节奏, 拉丁, 都市 |
| Salsa | 150-250 | C, F | 铜管, clave节奏, 高能 |
| Afrobeats | 100-115 | Am, Gm | 复合节奏, 律动, 打击乐 |
| Reggae | 70-90 | Am, G | 反拍吉他, 悠闲, 重贝斯 |

### 鬼畜 / 音MAD
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| 技术向音MAD | 130-180 | Am, Em | glitch, 变调人声, 快速剪切 |
| 叙事鬼畜剧 | 90-120 | Am, Dm | 戏剧性, 剧场感, 采样密集 |
| RAP鬼畜 | 85-140 | Am, Cm | rap beat, 人声切片, flow |
| 全明星/哲学系 | 100-130 | Am, Gm | 梗采样, 史诗, 哲学 |
| 治愈系唯美音MAD | 70-100 | C, Am | 氛围, 空灵, 混响, 唯美 |

### 儿歌 / 童谣
| 子风格 | BPM | 调性 | 风格关键词 |
|---|---|---|---|
| 欢快儿歌 | 100-130 | C, G | 尤克里里, 拍手, 明亮童声, 洗脑 |
| 摇篮曲 | 60-80 | C, G | 温柔钢琴, 八音盒, 轻柔, 梦幻 |
| 童谣说唱 | 90-110 | C, G | 趣味beat, 教育性, 跟唱 |

---

## Step 2: Write Lyrics (歌词创作)

按风格类型使用对应结构。

### 通用歌曲结构 (Pop / Rock / R&B / Folk)
```
[Intro] (4-8 bars)
[Verse 1] (8-16 bars)
[Pre-Chorus] (4 bars, optional)
[Chorus] (8 bars)
[Verse 2] (8-16 bars)
[Chorus] (8 bars)
[Bridge] (8 bars)
[Chorus] (8 bars)
[Outro] (4-8 bars)
```

### 说唱结构
```
[Intro] (4 bars)
[Verse 1] (16 bars)
[Chorus] (8 bars)
[Verse 2] (16 bars)
[Chorus] (8 bars)
[Outro] (4 bars)
```
- 押韵：至少 AABB，优先双押/三押
- Ad-libs: (yeah!) (skrt!) (ayy!)

### 电子/EDM 结构
```
[Intro] (8-16 bars, build-up)
[Drop 1] (16-32 bars, main hook)
[Breakdown] (8-16 bars, melodic)
[Build-up] (4-8 bars)
[Drop 2] (16-32 bars)
[Outro] (8 bars)
```
- 歌词极简：1-2 句 vocal hook 循环
- 注重节奏感而非叙事

### 古典/器乐
- 无歌词，输出乐曲描述/乐章说明
- HappyShrimp 风格描述中描述乐器编制和情绪变化

### 鬼畜/音MAD
```
[Intro] (采样素材描述)
[Section A] (鬼畜段落, 节奏变化描述)
[Bridge] (过渡/反差段落)
[Section B] (高潮鬼畜)
[Outro] (收尾)
```
- 歌词 = 素材来源 + 鬼畜技法描述
- 风格描述强调 glitch, 变调, 采样切片

### 儿歌
```
[Intro] (2-4 bars, 问候)
[Verse 1] (8 bars)
[Chorus] (4-8 bars)
[Verse 2] (8 bars)
[Chorus] (4-8 bars)
[Outro] (2-4 bars)
```
- 词汇简单（小学常用字）, 每句 5-7 字
- 大量重复, 拟声词, 教育性

### 作词技巧库 (Songwriting Craft)

**押韵方案：**
- AABB: 相邻两句押韵，适合叙事，简单直接
- ABAB: 交叉押韵，增加层次感
- AAAA: 连押（说唱常用），冲击力强
- XAXA: 偶句押韵，副歌常用，留白感
- 双押/三押: "角度/温度/态度" — 说唱进阶技巧，连续多字押韵
- 内韵: 同一句内部押韵，增加flow流畅度

**中文押韵注意：**
- 开口韵 (a/ang/ai): 力量感、释放感，适合副歌高潮
- 闭韵 (i/in/ing): 细腻、内省，适合主歌叙事
- 圆唇韵 (u/o/ou): 忧郁、深沉，适合抒情慢歌
- 同一首歌可换韵：主歌用闭韵叙事 → 副歌换开口韵爆发

**修辞与意象：**
- 画面感: 用具体场景代替抽象情感（"空荡的房间" > "我很孤独"）
- 对比法: 副歌与主歌形成情绪反差（平静叙述 → 爆发宣泄）
- 重复钩子: 核心句反复出现，强化记忆（"我就是我"式宣言）
- 留白: 不说完，让听众自己补全（"如果那天……"）
- 通感: 跨感官比喻（"你的声音是蓝色的"、"思念有重量"）

**Hook 写法：**
- 旋律钩子: 短小、重复、音程跳跃大（3-5度跳进最抓耳）
- 歌词钩子: 1-2句核心，全曲重复3次以上
- 节奏钩子: 独特的节奏型（如切分、停顿后爆发）
- 位置: 副歌开头或结尾最有效
- 检验标准: 听一遍就能哼出来 = 好hook

**音节与节奏匹配：**
- 每句音节数标注（如 7-5-7-5），方便 HappyShrimp 对齐旋律
- 说唱标注 flow 模式: ↑加速 / ↓减速 / →平稳 / ⏸停顿
- 副歌音节应比主歌更简洁有力（少音节 + 长音 = 记忆点）

**中文四声与旋律：**
- 一声（高平）→ 适合高音或长音
- 二声（上扬）→ 适合上行旋律
- 三声（先降后升）→ 适合转折旋律
- 四声（下降）→ 适合下行或重拍
- 关键句避免"倒字"（声调与旋律方向矛盾导致听感别扭）

---

**输出文件：**
- **lyrics.txt** — 完整歌词（含注释）
- **happyshrimp-ready.txt** — HappyShrimp 输入版（干净歌词 + section tags）

---

## Step 3: Compose (作曲编曲)

为歌词设计音乐框架。此步骤输出供创作者参考的作曲思路，同时优化 HappyShrimp 提示词。

### 和弦进行库 (Chord Progressions)

**流行/抒情常用进行：**
- I-V-vi-IV (C-G-Am-F): 经典万能，积极明亮，适合正能量/励志
- vi-IV-I-V (Am-F-C-G): 史诗感循环，适合副歌
- I-vi-IV-V (C-Am-F-G): 50年代经典，复古甜美
- IV-V-iii-vi (F-G-Em-Am): "王道进行"（日系），虐心感
- vi-V-IV-V (Am-G-F-G): 日式抒情，情感递进

**说唱/嘻哈：**
- i-VII-VI-V (Am-G-F-E): 暗黑说唱标配
- i-iv-i-V (Am-Dm-Am-E): 经典boom bap
- i-VI-III-VII (Am-F-C-G): melodic rap 常用

**摇滚：**
- I-IV-V (E-A-B): 经典摇滚三和弦
- i-VII-III (Em-D-G): 力量进行
- I-bVII-bVI-V (E-D-C-B): 安达卢西亚进行，戏剧感

**民谣/国风：**
- i-VII-VI-V (Am-G-F-E): 叙事民谣
- Am-Em-F-C: 指弹常用，温暖
- Am-G-Em-C: 国风标配，诗意

**R&B/爵士：**
- ii-V-I (Dm7-G7-Cmaj7): 爵士经典
- I-IV-V-IV (C-F-G-F): R&B 基础
- vi-ii-V-I (Am-Dm-G-C): 流畅循环

**电子/EDM：**
- i-VI-III-VII (Am-F-C-G): Future Bass 标配
- i-i-i-i (持续小调): Techno/Minimal，催眠感
- I-V-vi-IV + sidechain: House 经典

### 动态映射 (Dynamics Map)

为每个段落标注能量等级（1-5），设计情绪曲线：

```
[Intro]     ██░░░  2/5  — 引入，留白
[Verse 1]   ███░░  3/5  — 叙事，收敛
[Pre-Chorus]████░  4/5  — 爬升，张力
[Chorus]    █████  5/5  — 爆发，全力
[Verse 2]   ███░░  3/5  — 回落，新信息
[Chorus]    █████  5/5  — 再次爆发
[Bridge]    ██░░░  2/5  — 转折，意外
[Chorus]    █████  5/5  — 最终爆发（可升key +1）
[Outro]     █░░░░  1/5  — 渐弱，余韵
```

### 编曲建议 (Arrangement)

根据风格自动匹配编曲层次：

**层次设计：**
- 节奏层: 鼓/打击 → 提供律动骨架
- 和声层: 吉他/键盘/合成器 → 填充和声色彩
- 低音层: 贝斯 → 连接节奏与和声
- 旋律层: 主奏乐器 → 与人声呼应
- 氛围层: pad/效果 → 空间感和情绪底色

**风格→编曲对照：**
- Pop: 钢琴/吉他 + 合成器pad + 电子鼓 + 贝斯 + 弦乐点缀
- Rock: 电吉他(失真) + 贝斯 + 真鼓 + 偶尔键盘
- Trap: 808贝斯 + hi-hat三连音 + dark pad + 偶尔钢琴/长笛
- R&B: 电钢琴(Rhodes) + 干净吉他 + 电子鼓 + 贝斯
- 国风: 古筝/琵琶 + 二胡/笛子 + 轻鼓 + pad
- EDM: 合成器lead + pad + 电子鼓 + sidechain压缩 + FX riser
- 民谣: 木吉他(指弹) + 口琴/小提琴 + 轻打击 + 贝斯

**编曲递进技巧：**
- Verse 1: 精简（1-2层乐器 + 人声）
- Chorus 1: 加入节奏层 + 低音层，能量提升
- Verse 2: 比V1多一层（如加pad或吉他点缀），保持新鲜感
- Chorus 2: 全编制，最饱满
- Bridge: 突然精简（去掉鼓/贝斯），制造反差
- Final Chorus: 全编制 + 升key或加和声/合唱

**HappyShrimp 提示词增强（带编曲描述）：**
在风格描述中加入编曲关键词可提升生成质量：
- `主歌钢琴伴奏, 副歌全乐队` — 控制段落编曲变化
- `808贝斯, hi-hat三连音` — 精确描述节奏特征
- `弦乐渐强, 副歌爆发` — 引导动态变化
- `古筝lead, 二胡counter-melody` — 描述乐器角色

---

## Step 4: HappyShrimp 风格提示词

为每首歌编写风格描述（HappyShrimp 主打自然语言描述，中文描述识别很好，也可中英混合）：

**公式：**
```
[语言] [子风格], [BPM]bpm, [调性], [乐器关键词], [人声风格], [情绪/氛围]
```
（HappyShrimp 支持自然语言，把以上关键词扩写成一句完整描述效果更好）

**示例：**
- Pop: `中文合成器流行, 120bpm, Am, 复古合成器, 洗脑hook, 女声, 80年代复古感`
- Rock: `中文另类摇滚, 130bpm, Em, 失真吉他, 驱动鼓点, 愤怒男声, 动态对比`
- Trap: `中文trap说唱, half-time 140bpm, Am, 808贝斯, 三连音hi-hat, 暗黑pad, 攻击性男声`
- 国风: `中文古风流行, 90bpm, Am, 古筝, 二胡, 诗意女声, 空灵, 电影感`
- 音MAD: `glitch hop, 160bpm, Am, 变调人声切片, 快速剪切, 混沌, 梗能量`
- 儿歌: `中文儿歌, 120bpm, C, 尤克里里, 拍手, 明亮童声, 欢快, 教育性`

**通用修饰词：**
- 声线: `男声` / `女声` / `童声` / `合唱` / `男女对唱`
- 音色: `低沉` / `沙哑` / `丝滑` / `空灵` / `歌剧腔`
- 能量: `攻击性` / `松弛` / `高能` / `温柔` / `史诗`
- 特效: `autotune` / `混响` / `延迟` / `失真` / `lo-fi`
- HappyShrimp 对中文描述识别良好，无需刻意用英文；中英混搭也可以

---

## Step 5: Deliver (交付)

输出以下文件：

1. **happyshrimp-ready.txt** — HappyShrimp 输入（三段式：风格描述 / 歌词 / 标题）
2. **lyrics.txt** — 完整歌词参考（含注释/flow 标记）
3. **composition.md** — 作曲编曲参考（和弦进行 / 动态映射 / 编曲层次 / 旋律建议）
4. **happyshrimp-guide.md** — HappyShrimp 使用指南（步骤 + 调参技巧）

用链接呈现所有文件，happyshrimp-ready.txt 作为主打。

### HappyShrimp 使用指南模板 (happyshrimp-guide.md)

```markdown
# HappyShrimp（快乐虾米）使用指南

HappyShrimp 是阿里推出的 AI 音乐模型，端到端整曲生成（人声+编曲），中文演唱支持好。

## 步骤
1. 打开 https://www.happyshrimp.cn/（海外入口：https://www.happyshrimp.ai/），注册登录
2. 进入创作页面
3. 将 happyshrimp-ready.txt 中的三段内容分别填入：
   - 风格描述 → 提示词/描述栏（HappyShrimp 理解自然语言，可把关键词扩写成一句完整描述）
   - 歌词 → 歌词栏（选择"自定义歌词"模式）
   - 标题 → 歌曲名称
4. 点击生成，等待约几十秒（每次生成约消耗 20 积分）
5. 通常会生成多个版本，都听一遍选更好的

## 调参技巧
- 人声太弱 → 风格描述加 `人声突出` 或 `强人声`
- 节奏太慢/快 → 调整 BPM 数值
- 想换乐器 → 替换乐器关键词（吉他→钢琴, 合成器→弦乐）
- 风格不纯 → 精简关键词，保留核心 2-3 个
- 中文咬字不清 → HappyShrimp 中文发音本身较好，如仍有问题加 `清晰咬字`
- 不够燃 → 加 `史诗` `燃` `体育场摇滚`
- 想要更电子 → 把 `另类摇滚` 换成 `电子摇滚, 合成器摇滚`
- 想要更金属 → 加 `金属, 双踩, 重失真`

## 进阶玩法
- 生成后不满意 → 微调风格关键词重新生成
- 想要纯音乐 → 用纯音乐模式，或描述中写"纯音乐/器乐"
- 想要童声合唱 → 风格栏写 `童声合唱 + 男声领唱`
- 想要男女对唱 → 风格栏写 `男女对唱/男女合唱`
- 想要8-bit复古 → 风格栏写 `芯片音乐, 8-bit, 复古游戏, 150bpm`
- 没灵感 → 用"灵感骰子"功能生成初始提示词再改

## 注意
- 每次生成消耗积分（约 20 积分/首），建议想好再生成
- 中文/英文风格描述都可以，中文识别更好，自然语言整句也可以
- 歌词中的 section tag（[Verse] [Chorus] 等）HappyShrimp 能识别
- 生成结果适合 Demo 用途，正式发布建议做后期处理
```

### 作曲编曲参考模板 (composition.md)

```markdown
# 《歌曲名》作曲编曲参考

## 基本信息
- 调性: Am (可升 Bm for final chorus)
- BPM: 120
- 拍号: 4/4

## 和弦进行
| 段落 | 和弦 | 级数 | 备注 |
|---|---|---|---|
| Verse | Am - F - C - G | vi - IV - I - V | 叙事，稳定 |
| Pre-Chorus | Dm - Am - F - G | ii - vi - IV - V | 张力爬升 |
| Chorus | F - G - Em - Am | IV - V - iii - vi | 王道进行，虐心 |
| Bridge | Dm - F - Am - G | ii - IV - vi - V | 转折，意外感 |

## 动态映射
[Intro]     ██░░░  2/5  — 钢琴 + pad
[Verse 1]   ███░░  3/5  — +轻鼓 +贝斯
[Pre-Chorus]████░  4/5  — 弦乐渐强, snare roll
[Chorus]    █████  5/5  — 全编制爆发
[Verse 2]   ███░░  3/5  — 回落, 加吉他点缀
[Chorus]    █████  5/5  — 再次爆发
[Bridge]    ██░░░  2/5  — 去鼓, 仅钢琴+人声
[Chorus]    █████  5/5  — 升key + 合唱
[Outro]     █░░░░  1/5  — 渐弱, 钢琴余韵

## 编曲层次
- 节奏层: 电子鼓 (verse轻拍, chorus全力)
- 和声层: 钢琴主导 + 合成器pad铺底
- 低音层: 电贝斯 (verse根音, chorus走旋律)
- 旋律层: 电吉他 (chorus加counter-melody)
- 氛围层: 弦乐pad + 混响

## 旋律建议
- 主歌: 中低音区, 级进为主, 叙事感
- 副歌: 跳进开头(5度上行), 高音区停留, 记忆点
- Bridge: 转关系大调(C), 色彩变化
```

---

## Tips

- **中文歌词**注重押韵自然，避免生硬凑韵
- **儿歌**词汇控制在小学常用字，句子不超 7 字
- **R&B**注意四声与旋律走向匹配，避免倒字
- **鬼畜/音MAD** 在歌词中标注素材来源和鬼畜技法（加速/倒放/重复/变调）
- HappyShrimp 每次生成多个版本，建议都听
- 不满意时调整风格描述中的具体关键词
- 用户指定参考歌手时，描述声音特征而非歌手名字
- **古典/器乐**无需歌词栏，在风格描述中详细描述编制和情绪
- **EDM** 歌词极简，1-2 句 vocal hook 循环即可
- **国风**可加入古诗词引用，五声音阶关键词效果好
- HappyShrimp 是国产模型，中文支持好，优先用中文写风格描述（自然语言整句效果更佳）
- **作曲**: 和弦进行不用太复杂，3-4个和弦循环即可，HappyShrimp 会自动处理和声
- **编曲**: 在风格描述中写核心乐器 2-3 个即可，太多关键词反而让AI困惑
- **动态**: 想要明显的段落起伏，在风格描述加 `动态编曲, 副歌爆发, 主歌收敛`
- **升key**: 最后一遍副歌升半音(+1 semitone)是经典燃点技巧，可在歌词标注 `[Key +1]`

## Additional Resources

- 详细风格参考：[genre-styles.md](genre-styles.md)
