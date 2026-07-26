---
name: text-to-video
description: 从文本/资料/口播脚本一站式生成可交付的视频 MP4。流程：planner 阶段产出脚本+分镜+素材清单+TTS 配置 → hyperframes 阶段自动 init 项目、生成 HTML composition、合成 TTS 音频、渲染 MP4。适用于产品讲解、口播视频、概念解释、教育科普等场景。
---

# Text-to-Video (text-to-video)

一站式**文本 → MP4** pipeline。结合了：

- **`text-to-video-planner`**：策划阶段 —— 文本分析、脚本生成、分镜设计、素材搜集、TTS 配置
- **`hyperframes`**：渲染阶段 —— HTML composition 创作、动画编排、Chrome 无头渲染到 MP4

目标：用户给一段文本/口播稿/资料，得到一份**可直接发布的视频文件**。

## 何时使用

当用户希望"把这段文字/讲稿/资料变成一个视频"时触发。典型场景：

- **产品讲解/营销视频**：产品介绍文 → 60~90s 竖屏讲解
- **口播视频**：人声讲稿 → 口播+卡片的视频
- **概念解释/科普**：文章/笔记 → 30~60s 横屏或竖屏讲解
- **教育内容**：课程讲义 → 教学视频
- **社交短视频**：金句/段子 → 9:16 竖屏卡点视频

**不要用**：

- 已有视频要加字幕/包装 → 用 `embedded-captions` / `graphic-overlays`（hyperframes 子 skill）
- 已有完整 HTML composition 只想要 MP4 → 直接用 `hyperframes`
- 只需要分镜方案不要视频 → 用 `text-to-video-planner`（老 skill）
- 视频 > 3 分钟（长讲解/纪录片） → 此 skill 适合 ≤ 90s 短视频；长视频建议拆段

## 工作流（4 阶段 + 3 确认门）

```
[Stage 1: 文本分析 + 脚本分镜]  ──── 确认门 1: 脚本确认
        ↓
[Stage 2: 素材搜集 + TTS 配置]  ──── 确认门 2: 素材+TTS确认
        ↓
[Stage 3: 搭 hyperframes 项目 + HTML composition + TTS 音频]
        ↓
[Stage 4: lint + inspect + render]  ── 确认门 3: 渲染结果确认 → 输出 MP4
```

### Stage 1: 文本分析 + 脚本分镜

**输入**：用户提供的文本/讲稿/资料（粘贴、URL、文档摘要均可）

**动作**：
1. 提取核心主题 + 关键信息 + 目标受众
2. 估算时长（中文 4~5 字/秒口播）
3. 切分场景（每场景 3~8s，1 个核心信息）
4. 为每个场景写：
   - 时间窗（start/end）
   - 画面描述（人物/物件/动作/数字）
   - 旁白文本
   - 视觉建议（动画方向、字体调性、颜色）
5. 写一份 `[视频标题]_video_plan.md`（用 `templates/video_plan_template.md`）

**确认门 1**：把分镜表给用户看，**必须**用户确认后再继续。可以让用户改：
- 时长太短/太长
- 某个场景不要/要加
- 旁白措辞
- 视觉调性

### Stage 2: 素材搜集 + TTS 配置

**动作**：
1. **TTS 配置**（参考 `references/tts-providers.md`）：
   - 询问供应商（阿里云百炼 / 字节豆包 / OpenAI TTS / macOS `say` / Kokoro-82M 本地）
   - 引导设 API Key 环境变量
   - 选定音色（女声/男声/语速/音调）
2. **真实素材**（按 memory `vibecoding-video-pipeline` 里的免费源）：
   - 真实视频 b-roll：**Mixkit**（`https://assets.mixkit.co/videos/<id>/<id>-720.mp4`，免注册免 key）
   - logo：`cdn.simpleicons.org/<slug>` 或 Wikimedia
   - 真实图片/CC 视频：Wikimedia Commons API
3. **AI 生成素材**（如果需要插画/概念图）：
   - 抽象概念：GSAP/SVG 内联绘制
   - 写实场景：建议用户用 Midjourney/Flux 生成
4. 整理**编号清单** + 缩略图

**确认门 2**：展示素材清单 + TTS 配置让用户确认。

### Stage 3: 搭 hyperframes 项目

**这是核心衔接**。每个分镜场景 = 一个 `card-host clip`。

**动作**：
1. **建项目**：
   ```bash
   npx hyperframes init <项目名> --video <main-video.mp4> --non-interactive
   ```
   或纯卡片视频（无底视频）：
   ```bash
   npx hyperframes init <项目名> --non-interactive
   ```

2. **生成 TTS 音频**（用 hyperframes 内置 TTS 或外部 API）：
   ```bash
   npx hyperframes tts --text "<旁白脚本>" --voice <音色> --output audio.mp3
   ```
   或脚本批量：
   ```bash
   bash scripts/generate_tts.sh <voice_plan.json> audio/
   ```

3. **写 `index.html`** —— 按分镜生成卡片：
   - root `<div data-composition-id="main" data-width="1080" data-height="1920" data-duration="<总时长>">`
   - 视频底层（如果用底视频）：`<video id="bg-video" src="..." muted>` （必须是 root 直接子！Rule 3）
   - 音轨：`<audio src="audio.mp3" data-start="0" data-duration="<总时长>">` （必须是 root 直接子！Rule 3）
   - 每个场景一个 `<div class="card-host clip" data-start="..." data-duration="..." data-track-index="N">`
   - GSAP 时间线 `gsap.timeline({ paused: true })` 注册到 `window.__timelines["main"]`
   - 字体必须 `@font-face` 声明（下载到 `fonts/`，或 `src: local("系统字体")`）

4. **拷素材到项目**：`assets/`（图片/视频）、`fonts/`（woff2）、`audio/`（TTS 音轨）

详细衔接规则 → `references/hyperframes-handoff.md`

### Stage 3.5: 强调动效（动态 HTML，硬规范）

**核心原则**：「讲到某处需要强调」一律用**动态 HTML DOM + GSAP** 实现，**不**预渲染 GIF、不**用** CSS 纯 `@keyframes` 整段、不**录**段视频绕开。所有强调动效必须在 GSAP 主时间线内运行（由 `data-start` 控制），跟 TTS 时间轴对齐。

#### 范式 1：闪烁高亮（关键词被念到的瞬间）

```html
<div class="card-host clip" data-start="14.0" data-duration="6.0" data-track-index="2">
  <div class="card">
    <h1 class="metric" id="valuation">120<span>亿美元</span></h1>
  </div>
</div>
```

```js
// GSAP 时间线内的写法（紧接 Stage 3 第 4 步 enter/rise）
const card = ".card-host[data-card-id='card-NN']";
tl.fromTo(card + " #valuation",
  { scale: 1, color: "#333" },
  { scale: 1.18, color: "#ff3366", duration: 0.35, ease: "power2.out",
    yoyo: true, repeat: 1 }, 14.5);
// 14.5 = TTS 念到 "120亿" 的时间点；yoyo + repeat=1 实现放大回落强调
```

#### 范式 2：打字机逐字揭示（口播对齐）

```html
<h2 id="hook" data-text="为什么大厂都在做 AI 眼镜？">为什么大厂都在做 AI 眼镜？</h2>
```

```js
// 把字符串拆字，定时逐字显示
const hookEl = document.querySelector("#hook");
const text = hookEl.dataset.text;
hookEl.textContent = "";
tl.call(() => { hookEl.textContent = ""; }, [], 0.8);
tl.to({}, {
  duration: text.length * 0.12,                  // 按字数估算揭示时长
  onUpdate: function() {
    const n = Math.floor(this.progress() * text.length);
    hookEl.textContent = text.slice(0, n);
  },
  ease: "none",
}, 0.8);
// 0.8 = TTS 开始念这条 hook 的时间；时长按字数推算，TTS 念多快就推多快
```

#### 范式 3：计数滚动（数字强调）

```html
<div id="counter" class="metric">0</div>
```

```js
const counterEl = document.querySelector("#counter");
tl.fromTo(counterEl,
  { textContent: 0 },
  { textContent: 120, duration: 1.4, snap: { textContent: 1 },
    ease: "power1.out",
    onUpdate: function() {
      counterEl.textContent = Math.round(counterEl.textContent);
    }
  }, 14.5);
// 14.5 = TTS 念到数字的时间；1.4s 推到目标值，跟口播节奏配
```

#### 禁用清单（遇到要喊停）

- ❌ **GIF / WebP 动图**：不进 GSAP timeline，无法精确卡时间；体积大
- ❌ **纯 CSS `@keyframes` 整段跑**：脱离 hyperframes timeline 控制，inspect 抓不到
- ❌ **预渲染视频替代**：体积 ×2，同步噩梦，lint 会跳过 GSAP 检查
- ❌ **`setTimeout` / `requestAnimationFrame` 驱动**：破坏确定性渲染，hyperframes 会拒收
- ❌ **DOM 已隐藏时启动 GSAP**：`.card-host[style*="visibility:hidden"]` 状态下 GSAP 不渲染

#### hyperframes 协作要点

1. **三件套齐**：强调目标元素所在的 card 必须带 `data-start` / `data-duration` / `data-track-index` + `class="clip"`
2. **timeline 必须注册**：所有强调动效挂在主 timeline 上 → `window.__timelines["<data-composition-id>"]`
3. **时间轴对齐**：强调触发时间（如 `14.5`）要和 TTS 实际念到该处的秒数对齐——建议先跑 `npx hyperframes inspect` 看关键帧时间戳，再微调
4. **`onUpdate` 里操作 DOM 安全**：GSAP 内部回调里改 `textContent` / `class` 是 OK 的，但不**在**回调里 `querySelectorAll` 大范围遍历
5. **同步构建**：所有强调动效跟 enter/exit 一样同步写在 `<script>` 顶部，禁 async/setTimeout

### Stage 4: 渲染

**动作**：
```bash
npx hyperframes lint          # 0 error 才能 render
npx hyperframes inspect       # 警告审查
npx hyperframes render --output final.mp4 --quality standard
```

**质量档**：
- `draft`：4 workers，~2 分钟出片，文件 10~15MB（迭代用）
- `standard`：~3 分钟，~20MB（投递用）
- `high`：~5~8 分钟，~30~50MB（最终发布）

**确认门 3**：给用户看渲染结果（f 抽 5/15/25/35/45/55s 关键帧截图），确认通过。

## 命令速查

```bash
# 1. init
npx hyperframes init my-video --non-interactive

# 2. lint
npx hyperframes lint

# 3. inspect
npx hyperframes inspect

# 4. render
npx hyperframes render --output final.mp4 --quality standard
npx hyperframes render --quality high --output final-hq.mp4

# 5. tts (hyperframes 内置)
npx hyperframes tts --text "..." --voice af_heart --output audio.mp3
```

## 输入输出

**输入**：
- 文本/讲稿/资料（用户粘贴或给 URL）
- TTS 供应商选择 + API key
- 确认门处的反馈

**输出**：
- `[项目名]_video_plan.md` —— 完整分镜方案包
- `<项目名>/index.html` —— HTML composition
- `<项目名>/assets/`、`fonts/`、`audio/` —— 素材
- `<项目名>/renders/final.mp4` —— 最终视频
- 关键帧截图（用于确认）

## 已知踩坑（重要！）

参考用户 memory `vibecoding-video-pipeline.md` 和 hyperframes-core 规则：

1. **`<video>` / `<audio>` 必须是 host root 直接子**（不能套 `<div>`），否则黑屏
2. **video muted + 独立 `<audio>`**（同源也要拆开）
3. **HTML 注释里别写 `<video>`/`<audio>` 字面标签名**（媒体扫描器当真，产生幽灵元素）
4. **GSAP 时间线 `paused: true` + 注册到 `window.__timelines["<id>"]`**（id 必须严格匹配 `data-composition-id`）
5. **每个 timed 元素 `data-start` / `data-duration` / `data-track-index` + `class="clip"`**
6. **不要 `Math.random()` / `Date.now()` / `network` 驱动动画**（确定性原则）
7. **`npx hyperframes` 每次联网校验版本**，网络抖时用缓存路径：
   ```bash
   node /Users/douer/.npm/_npx/702923228c2ce1e6/node_modules/hyperframes/dist/cli.js
   ```
8. **改完必跑 `lint` + `inspect`**（inspect 抓文字重叠/溢出，line-height 过小会重叠）
9. **中文转写不可行**（hyperframes whisper 缺中文模型），如需字幕用 `embedded-captions` 子 skill
10. **Python 3.14 太新**导致 Kokoro-82M TTS 装不上；如需本地 TTS 备选 macOS `say -v Tingting/美佳`

## 文件结构（一个 text-to-video 项目的产出）

```
~/videos/
  <项目名>/
    index.html              # 主 composition
    hyperframes.json        # 项目配置
    meta.json               # 项目元数据
    package.json            # npm scripts
    input-video.mp4         # 底视频（如有）
    audio.mp3               # TTS 音轨
    assets/                 # 素材
      logo.svg
      broll.mp4
      ...
    fonts/                  # 字体 woff2
      noto-serif-sc-600.woff
    compositions/           # 子 composition（可选）
      overlay.html
    renders/
      draft.mp4
      final.mp4
    [项目名]_video_plan.md  # 分镜方案包（项目根或父目录）
```

## 与上游/下游 skill 的关系

```
text-to-video-planner  ──→  text-to-video  ──→  hyperframes
   (策划,本 skill 包含)        (本 skill)         (渲染,本 skill 调度)
        ↑
   可独立使用
```

本 skill 是**超集**：
- 包含 planner 的策划能力（Stage 1-2）
- 包含 hyperframes 的渲染能力（Stage 3-4）
- 加上两者衔接（hyperframes-handoff.md）

如果用户**只想做策划**不要视频 → 引导用老的 `text-to-video-planner`
如果用户**只想渲染**（已有 HTML） → 引导直接用 `hyperframes`

## 详细参考

- `references/hyperframes-handoff.md` —— 分镜→HTML 的具体转换规则、常见模式
- `references/tts-providers.md` —— 各 TTS 供应商对比、配置、价格
- `templates/video_plan_template.md` —— 分镜方案包模板
- `templates/composition_skeleton.html` —— 标准 HTML composition 骨架（1080×1920 竖屏）
- `scripts/generate_tts.sh` —— 批量 TTS 调用脚本
