---
name: cosplay-photo-set
description: "通用模板：用本机 ComfyUI（z-image-turbo）把任意二次元角色做成「真人 cosplay 套图」——角色检索与确认 → 真人基准图确认 → 同角色卡多姿势成片 → 去油光去反光 → 唯美纯色/渐变影棚背景（按角色配色，无实景、无亮斑、无摄影灯）→ 导出 1–2MB 竖版 JPEG → 附标题、正文与标签。适用于任何角色与平台（视频号/小红书/图集）。"
---

# 真人 cosplay 套图流水线（通用模板 · ComfyUI / z-image-turbo）

## 什么时候用

用户要「真人 cosplay 风格的二次元角色图」「一套同角色不同姿势」「发视频号/小红书/图集」。

本 skill 是**通用模板**：不绑定任何具体角色。角色、服装、背景配色由第 0–2 步填进「角色卡」占位符，之后四张成片逐字复用同一张卡。
核心矛盾：**文生图不开 LoRA 无法天然保证长相一致**，所以靠"逐字复用的角色设定卡"+ 同一光位 + 同一背景来锁一致性，只让 POSE 段变化制造姿势差异。

## 0. 先问清楚（缺哪条补哪条，别自己替用户决定）

- **角色**：用户已指定 → 跳过第 1 步；没指定 → 走第 1 步
- **张数**（默认 4）、**比例**（默认 9:16 竖屏）、**平台**（视频号 / 小红书 / 图集）
- **文件大小**（默认 1–2MB）、**分辨率**（默认 1440×2560）
- **背景**：**固定为「唯美纯色/渐变影棚」**，颜色按角色标志色适配（见 2.1）。**不再提供实景方案**——实测实景偏差大、容易显假；用户若提实景，先说明这一点，默认仍走纯色。
- **是否有参考图**：用户能提供就优先对齐，比模型脑补准得多

## 1. 角色检索与提案（用户指定角色时跳过）

- 用 `web_search` 查「今年最想 cos 的动漫角色 排行 / コスプレ したい キャラ ランキング」「<角色名> costume design 官方设定」，取 2–3 个当前热门、服装辨识度高的角色。
- 提案格式：角色名 + 为什么适合真人化 + 完整形象要素（发型发色、服装逐件、道具、标志色）+ **拟用渐变背景的两个颜色** + 4 个姿势草案。**必须等用户确认角色才能往下走。**
- 服装细节优先按**官方设定**逐件写死；网络抓不到 coser 实拍图时（Bing/Fandom/百科常被拦），在交付里如实说明"按官方文字还原"，并邀请用户发参考图。

## 2. 生成「真人基准角色图」并确认（先出图，再问）

只出一张，先对齐"这张脸 + 这套衣服 + 这个背景配色"。
**试稿用 1152×2048（约 76s），确认后再上 1440×2560（约 230s）**，避免高价返工。

用**英文**长提示词（中文容易在额头生成深色斑块），固定分节，占位符留给具体角色：

```
Photorealistic live-action cosplay photograph of a real 22-year-old East Asian woman cosplaying {{CHARACTER}} from {{SERIES}}, full-length studio portrait on a clean seamless backdrop, the whole figure from hair to boots fits inside the frame with empty backdrop margin above her head and the boots fully visible near the bottom edge.

BACKDROP: {{BACKDROP_SENTENCE}}

HEAD AND HAIR: {{HAIR_STYLE_AND_COLOR}}, center-parted and swept back off the face, forehead completely clear and smooth, no bangs hanging over the forehead, no dark patches, no markings. Hair is clean and dry with individually readable strands, no greasy clumps, no wet-look shine.

FACE: adult East Asian bone structure, {{FACE}}, {{EYE_COLOR}} eyes of natural size (not oversized, not doll eyes), thin natural eyeliner, soft coral lips. Realistic skin with visible pores and slight uneven tone, natural skin tone, dry powder-matte finish on the face, shoulders, arms and back, skin looks freshly powdered like a real cosplayer at a shoot. No beauty retouching, no airbrushing.

COSTUME: {{COSTUME_ITEM_BY_ITEM}}  <!-- 逐件写：外衣/内搭/领口/纽扣数量位置/腰带/下装长度/袜鞋/道具；颜色用 dark navy almost black 这类叠词锁死 -->

POSE: {{POSE}}

HANDS: exactly five fingers on each hand, fingers clearly separated, natural knuckles, no extra or fused fingers.

LIGHTING AND CAMERA: soft key light from camera left slightly above eye level, soft fill from the right, gentle falloff, even exposure with natural skin tone, no blown highlights. Sony A7R IV, 85mm f/1.8, ISO 800, shallow depth of field, fine film grain. The face and eyes are tack-sharp and in critical focus, no motion blur on the subject, the backdrop falls off into a smooth even gradient. Ultra photorealistic, looks like a real person photographed at a cosplay shoot, not anime, not illustration, not 3D render, no plastic waxy skin. Vertical 9:16 composition.
```

把结果发给用户，并给一张「错→对」对照表说明这版改了什么。**等用户确认后再出成片。**

### 2.1 背景与灯光硬规则（本 skill 的核心约束）

背景只用这一句，四张**逐字不变**：

```
BACKDROP: a flat seamless paper studio backdrop with an extremely smooth vertical gradient from {{COLOR_A}} at the top to {{COLOR_B}} at the bottom, colors taken from the character's signature palette, perfectly smooth and empty, the shot contains only the woman against the empty backdrop, gentle even light falloff.
```

配色适配角色（两色都取角色标志色，一浅一深，同色相或邻近色相）：

| 角色示例 | COLOR_A（顶部） | COLOR_B（底部） |
|---|---|---|
| 甘雨 | pale ice blue | soft periwinkle blue |
| 胡桃 | warm ivory | muted terracotta |
| 雷电将军 | pale lilac | deep indigo violet |
| 芙宁娜 | pearl white | pale aqua |
| 纳西妲 | soft cream | light jade |

**禁止出现的词（正向、负向都不行）**：`softbox`、`light stand`、`strobe`、`reflector`、`wide`、`wide-angle`、`camera three meters back`、`灯架`、`柔光箱`、`反光板`、`器材`。
原因（实测教训）：写 `no softbox / no light stand` 会被模型当成正向元素，直接把柔光箱和灯架画进画面；写 `wide` 会拉宽视角，把棚拍设备一起收进构图。
**灯光段只描述光的软硬与方向，不描述任何灯具**；背景段只写"无缝纸背景 + 平滑渐变 + 空"。

### 2.2 构图硬规则

- 全身入画：`full-length`、`boots fully visible`、`a generous strip of empty floor below her boots`，靴底与地面留白必须有，避免裁脚。
- 头顶留白：`empty backdrop margin above her head`。
- 不要写 `wide`，改用 `85mm` 的远距离全身构图描述。
- 1440×2560 比 1152×2048 更容易裁脚，**正式出图前先 1152 试稿确认构图**。

### 2.3 常见翻车对照表（通用，遇症状先查这里）

| 症状 | 触发原因 | 解法 |
|---|---|---|
| 画面出现柔光箱/灯架/白色亮块 | 提示词写了 `softbox / light stand / wide`，或写了否定的 `no softbox` | 全部删掉，灯光只写光质与方向；背景只写无缝纸+渐变 |
| 背景有抹布状纹理/亮斑/脏边 | 背景句写了 `studio`、`light falloff toward edges` 过强，或出现 `spotlight` | 用 2.1 的固定句，`extremely smooth`，不写 spotlight/光斑/vignette |
| 额头出现深色斑块/污渍 | 提示词里有「刘海/碎发/鬓发」类描述 | 删掉，改写成 `center-parted and swept back off the face` |
| 皮肤油光、汗珠反光 | 正向写了 `natural shine / dewy / glossy / 油光 / 自然光泽` | 全删；改 `matte skin, dry powder-matte finish, no specular hotspots`。**不要用负向去写 "shine"**，模型会把关键词当正向画上去 |
| 头发一缕缕发亮、像抹了发油 | 只描述发型没描述质感 | 加 `clean and dry, individually readable strands, no greasy clumps, no wet-look shine` |
| 脸/整体发糊、不清晰 | 景深描述过强或加了 motion blur | 加 `tack-sharp eyes, critical focus on the face, no motion blur on the subject`，模糊只留给背景 |
| 眼睛过大像娃娃 | 只写颜色没写大小 | 加 `eyes of natural size (not oversized, not doll eyes)` |
| 靴子/脚被裁 | 1440 竖构图 + 没写全身留白 | 加 `full-length`、`boots fully visible`、`empty floor below her boots`；先 1152 试稿 |
| 双角/双耳只画出一只 | 3/4 侧身、远侧被头发挡住 | 写 `two short curved horns clearly visible on both sides of her head`；仍不行就换机位，不要硬堆词 |
| 裙子/外衣总被画长 | 只写 knee-length | 加 `ends just below the knee, calves and ankles visible` / `waist-length, ends at the hips, clearly shorter than the skirt` |
| 发色渐变方向反了 | 只说「渐变」 | 写 `only the last few centimeters of the tips dyed ...` |
| 背景抢戏、道具乱入 | 场景描述太长 | 背景压到一句；纯色背景明确 `no props, no clutter` |

## 3. 出成片（同背景多姿势）

- 角色卡（BACKDROP / HEAD / FACE / COSTUME / LIGHTING）**逐字不变**，只替换 POSE 句。
- 4 个姿势建议覆盖不同机位高度与动作类型：站姿回眸、低机位半蹲、倚靠静立、走姿抓拍，避免四张构图雷同。
- 每张独立种子。不要在角色卡里加"第 2 张"这类序号描述。
- 顺序：4 个 POSE 先各出一张 1152×2048 试稿 → 用户确认背景/构图/服装方向 → 再 1440×2560 正式出（实测 220–233s/张）。
- 无 LoRA 时，四张的脸与服装细节必然有漂移（例如上衣黑白先后不一致），交付时如实说明，不要假装是同一张脸。

## 4. 质检清单（逐张看，不合格就重出或后处理）

**背景与构图（先看这三条，不合格直接重出）**
1. 背景是干净的纯色/渐变，**没有亮斑、白色光块、灯架、柔光箱、地面杂物**
2. 渐变方向与色相一致（四张同一套），四边无脏边、无抹布纹理
3. 全身入画：头顶有留白、靴子完整、靴下有地面留白

**干净度**
4. 额头/脸颊干净，没有斑块、纹身状污渍
5. **脸部不油腻**：没有油光、汗珠亮点、蜡感反光
6. **头发不油腻**：发丝根根分明，不成绺、不反光成塑料假发
7. 皮肤哑光，有真实肤质（毛孔、轻微肤色不均）

**清晰度**
8. **脸部与眼睛必须锐利**：眼神光在、睫毛/瞳孔细节可辨，主体不糊、不抖
9. 模糊只出现在背景（景深合理），人物轮廓与服装边缘清楚
10. 放大到 100% 看：没有水彩糊块、没有重影、没有 AI 涂抹感

**还原与一致**
11. 手指 5 根、结构正常、无粘连；脚趾数量正确
12. 服装要素逐项对得上（款式、内搭、领口、纽扣、腰带配色、下装长度、鞋袜）
13. 道具在正确侧（刀在左腰等）、比例合理
14. 四张之间：发型、发色、服装、妆容一致，只有姿势/机位不同
15. 背景统一（同一渐变描述），颜色与角色气质匹配

## 5. 本机技术参数（z-image-turbo / 8GB）

- 端点：shim `http://127.0.0.1:8200`（OpenAI 兼容，`/v1/images/generations`、`/v1/images/edits`）→ ComfyUI `127.0.0.1:8188`
- 采样：steps 6 / cfg 2 / shift 3 / res_multistep + simple（8GB 显存上的最优解）
- **不要**把 cfg 提到 3、steps 提到 12：结果更"动漫塑料"，负向提示词也救不回来
- 尺寸：`1152x2048` 约 75–80s（试稿）；`1440x2560` 约 220–233s（成片）；4K 竖图在 8GB 上必 OOM
- 图生图（`/v1/images/edits`）denoise 固定 0.85 且不可调：**改姿势不可行**，会保留原构图、只把服装画漂移 → 姿势差异只能靠文生图重画
- 皮肤友好：默认不要 ESRGAN、不要锐化，4x 放大会把毛孔放大成脏点

**启动与沙箱（Windows 本机实测）**
- ComfyUI 的 `SaveImage` 默认写 `ComfyUI\output`，在沙箱下会 `Permission denied` → 启动加 `--output-directory <项目目录>`（如 `D:\DSH\workspace\comfyui_out`），必要时也加 `--input-directory`。
- 用 `Start-Process` 起的服务会随父 shell 退出被杀 → 用常驻后台进程/后台任务（如 `run_in_background`）跑 ComfyUI 与 shim。
- 调 shim 的最小请求体：
  ```json
  {"model":"z-image-turbo","prompt":"...","size":"1152x2048","quality":"low","n":1,"response_format":"b64_json"}
  ```
  返回 `data[0].b64_json`；seed 由 shim 随机。

## 6. 去油光/去反光后处理（可选，用户明确说"不要油腻/不要反光"时建议做）

高光 = "高亮度 + 低饱和"的小块（额头、颧骨、鼻梁、发顶最容易出现）。

做法：numpy 算亮度 `L` 与饱和度 `S` → 在脸/头发区域画柔边椭圆遮罩 → 对 `L > 0.80 && S < 0.45` 的像素把亮度往 ~0.72 压（强度 0.6）→ 遮罩大半径高斯羽化后混合。只压高光，不改结构、不磨皮。
头发区域可单独再跑一遍，压掉"发油反光"。

## 7. 导出交付

- PNG（约 3MB）→ JPEG 质量扫描：从 q100 往下找到第一个 ≤1.95MB 的档位，`subsampling=0, optimize, progressive`；实测 1440×2560 落在 1.2–1.9MB
- 命名：`01_姿势名.jpg`…`04_姿势名.jpg`，另存 `00_基准角色_<角色>.jpg`、`00_四张预览.jpg`（2×2 拼图）
- 单独建项目文件夹：`D:\DSH\workspace\cosplay_<角色拼音>\`

## 8. 交付时必须一起给（硬性要求）

每次交付成片，**同时**给出发布文案包，不要让用户再问一遍：

1. **标题** 3 条（≤20 字，有情绪钩子，不夸张标题党）
2. **正文** 2–3 句（第一人称、有具体细节：光线、动作、服装还原点）
3. **标签** 8–12 个：`#角色名` `#作品名` `#cosplay` `#真人cos` `#二次元` + 场景/情绪向
4. 平台差异：视频号偏"画面质感 + 一句话故事"；小红书偏"过程感 + 可抄作业"；两套各给一份
5. 用 `present` 发布 4 张成片，正文内嵌图片，并附文件链接与本次"做了什么/没解决什么"

## 9. 沟通节奏（重要：确认环节必须出图）

- **任何需要用户确认或修改的节点，都必须先生成实际图片，再把图片发给用户**（1152×2048 试稿即可）。禁止只发提示词、参数或代码让用户脑补结果——用户看不到代码，只能看到图。
- 改稿时给「上一版 → 这一版」的对照图 + 一句话说明改了什么、为什么；不要只说"已优化"。
- 第 1 步的角色提案可以纯文字；**第 2 步起每次确认都附带新生成的图片**。
- 用户一旦把某个角色/风格定下来，把那张「角色卡」存成项目内的 `character_card.txt`，下次改姿势直接复用。
- 明确模型边界：无 LoRA 时人脸一致性靠提示词，不是同一张脸像素级一致；写实天花板有限，双角/细配件容易漂移。
