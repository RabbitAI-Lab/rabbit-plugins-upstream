# text-to-video — 文本/讲稿一站式生成可交付的 MP4 短视频

[![Version](https://img.shields.io/badge/version-v1.0-blue)](https://github.com/MinibeanAI/text-to-video/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/MinibeanAI/text-to-video.svg)](https://github.com/MinibeanAI/text-to-video/stargazers)
[![Built with HyperFrames](https://img.shields.io/badge/render-hyperframes-6B5BBA)](https://hyperframes.heygen.com/)

中文 | [English](./README.en.md)

> **AI 不只是"填模板"——它从一段讲稿里读出结构，编排时间线，调用 TTS 配音，最终产出一段可发布的视频。** text-to-video 是一个跑在 Claude Code / claude.ai 里的工作流（"skill"）：把 PDF / 讲稿 / 网页资料丢给 AI，它在本机产出真材实料的 `.mp4`——每个卡片可改、TTS 可换、底视频可换、不锁平台、不锁模型。能力边界 → [能力定位](#能力定位)。

<p align="center">
  <a href="#quick-start"><strong>5 分钟跑通</strong></a> ·
  <a href="./templates/"><strong>模板</strong></a> ·
  <a href="./references/hyperframes-handoff.md"><strong>分镜→HTML 衔接</strong></a> ·
  <a href="#已知踩坑"><strong>踩坑清单</strong></a>
</p>

<p align="center">
  <a href="#示例"><img src="https://img.shields.io/badge/示例-Koubo%20AI%20眼镜-9B5BA8?style=for-the-badge" alt="示例"></a>
  <a href="#适用场景"><img src="https://img.shields.io/badge/时长-≤90s-6B9B8B?style=for-the-badge" alt="时长"></a>
  <a href="#适用场景"><img src="https://img.shields.io/badge/画幅-9:16%20%2F%2016:9-5B89B5?style=for-the-badge" alt="画幅"></a>
</p>

---

## 这是什么

`text-to-video` 是一个 **Claude skill**——一个跑在 Claude Code、Cursor、claude.ai 里的工作流，**输入一段文本/讲稿/资料，输出一个真材实料的 MP4 视频**。

它把两件原本要分开做的事**缝成一条流水线**：

| 阶段 | 干什么 | 工具 |
|---|---|---|
| **策划** | 文本分析 → 脚本 → 分镜 → 素材清单 → TTS 配置 | `text-to-video-planner` |
| **渲染** | HTML composition（GSAP 动画 + CSS 排版）→ MP4 | `hyperframes`（HeyGen） |

中间**自动衔接**——你不用在 Markdown 分镜表和 HTML composition 之间手动翻译。

---

## 能力定位

**如果最后拿到的不是个能在剪辑软件里再编辑的视频，它就不该叫"视频工具"。** 市面上的 AI 视频工具大致分四类，text-to-video 只做最后一类：

| 类别 | 输出 | 元素可单独改？ |
|---|---|:---:|
| 模板填充 | 用固定模板填内容 | 部分——受模板限制 |
| 图文拼贴 | 每张卡片是一张大图 | ❌ 改不动 |
| HTML 演示 | 网页 deck | ❌ 不是 mp4 |
| **原生可编辑（text-to-video）** | **HTML composition → 真 MP4 文件** | ✅ 改 index.html 重跑就行 |

它**不是**一个 SaaS，而是一个工作流（"skill"）——跑在 Claude Code、Cursor、VS Code + Copilot 或 claude.ai 里的：你在 IDE 聊天里说"把这段讲稿做成 60s 竖屏视频"，它按工作流产出一个原生 `.mp4`。你不用写代码，只做三件事：装 Node.js、装一个 AI IDE、把资料丢给 AI。

这种形式带来三个承诺：

- **成本透明可预测** —— skill 本身开源免费，唯一成本是 AI 模型调用费，按 token 付费
- **数据留在本地** —— 你的讲稿不必上传到第三方服务器。除 AI 模型通信外，整条流水线在本机跑
- **不锁平台** —— 工作流不绑任何一家公司。Claude Code / Cursor / claude.ai 都能跑；模型侧支持 Claude、GPT、Gemini

> [!IMPORTANT]
> ### 这是工具，不是许愿机
> `skill + 模型 = 能力` —— text-to-video 只拥有工作流，模型决定上限。推荐 **Claude 大上下文 + 任一 TTS**；其他模型能跑流水线，质量有差距。
>
> 别期望一次就出"完美"成片。本工具的价值是把 80% 的繁琐工作吃掉，剩下的润色是你自己的——一个**原生可编辑**的 MP4 存在的意义，恰恰是可以继续改，不是冻成一张不能动的图。

---

## 跟谁合得来

### [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) — AI 生成原生可编辑 PPTX

> 一个微软风格的 PPT skill 编排器，**和我互补**：它做的是 PPT/Keynote 演示文稿，我做的是 mp4 短视频。同一个作者哲学——"AI 出的产物应当保持人类可编辑"。

<table align="center">
<tr>
<td align="center" valign="middle" width="50%">

**text-to-video**（本仓库）
- 输入: 讲稿 / 资料
- 输出: 1080×1920 mp4
- 适用: 短视频 / 社媒 / 口播讲解
- 技术栈: HTML composition + GSAP + ffmpeg

</td>
<td align="center" valign="middle" width="50%">

**ppt-master**（hugohe3）
- 输入: 文档 / 报告
- 输出: 16:9 .pptx
- 适用: 演示 / 路演 / 报告
- 技术栈: SVG + python-pptx

</td>
</tr>
</table>

<details>
<summary><strong>常见组合用法</strong></summary>

- **同主题**双输出：先用 ppt-master 出发布会 PPT，再用 text-to-video 出 60s 预告视频
- **互为素材**：text-to-video 的分镜表 = ppt-master 的章节大纲
- **共用 TTS**：两边都用阿里云百炼 / macOS `say`

</details>

---

## 示例

| 场景 | 描述 | 适合 |
|---|---|---|
| **Koubo 口播剪辑** | 66s 竖屏，10 段分镜，AI 硬件主题，原作者本人出镜 + 卡片 | 微信公众号 / 视频号 |

> 本 skill 出片示例来自本机 `~/videos/koubo-hf/renders/final.mp4`（66s / 1080×1920 / 10MB）。整个流水线（策划→TTS→HTML→渲染）端到端约 10 分钟。

---

## 适用场景

✅ **适合**：
- 产品讲解 / 营销视频（60~90s 竖屏）
- 知识科普 / 概念解释（30~60s 横屏或竖屏）
- 个人口播 + 卡片包装
- 教育课件（短片段）
- 社交短视频（抖音 / Reels / 小红书）

❌ **不适合**（改用其他工具）：
- 已有视频要加字幕/包装 → 用 `embedded-captions` / `graphic-overlays`
- 已有 HTML composition 只想要 MP4 → 直接用 `hyperframes`
- 只想分镜方案不要视频 → 拆出 `text-to-video-planner`
- 长视频 > 3 分钟 → 拆段 / 用 NLE 工具

---

## Quick Start

### 1. 前置依赖

**你只需要装两样：[Node.js](https://nodejs.org/) 22+ 和 [FFmpeg](https://ffmpeg.org/download.html)**。其他依赖 skill 装好后一行搞定。

```bash
# macOS
brew install node ffmpeg jq

# Ubuntu / Debian
sudo apt install nodejs ffmpeg jq python3-pip
```

> [!NOTE]
> **Python 3.14 太新**——Kokoro-82M 本地 TTS 装不上。TTS 用 macOS `say` / 阿里云 / OpenAI 都 OK。

### 2. 安装 skill

**方式 A**：skill 市场（推荐）

```
/plugin marketplace add MinibeanAI/text-to-video
/plugin install text-to-video@text-to-video
```

**方式 B**：手动 unzip

```bash
mkdir -p ~/.claude/skills/text-to-video
unzip text-to-video.skill -d ~/.claude/skills/text-to-video
# 重启 Claude Code / claude.ai session 让 skill 加载
```

### 3. 装 TTS 客户端（按需）

| 供应商 | 命令 | 备注 |
|---|---|---|
| macOS `say` | （系统自带）| 零配置，适合草稿 |
| 阿里云百炼 | `pip install dashscope` | 需 `DASHSCOPE_API_KEY` |
| OpenAI TTS | `pip install openai` | 需 `OPENAI_API_KEY` |

### 4. 在 Claude 里说一句话

**最关键的一步**——把工作目录指向 skill 装好的位置（方式 A 不用，方式 B 装好后 `cd ~/.claude/skills/text-to-video`），然后在 AI 聊天里给一段讲稿。

```
You: 把这段讲稿做成 60s 竖屏视频: [粘贴讲稿]
```

或者直接给文件：

```
You: 用 ~/Desktop/notes/q3-product.md 做一段 90s 横屏讲解
```

AI 会先确认设计规格：

```
AI:  好。先确认设计规格：
     [风格]   9:16 竖屏
     [时长]   ~60s
     [底视频] 用你的口播 / 纯卡片
     [TTS]    阿里云百炼 longxiaobai
     ...
```

### 5. 跟完 3 个确认门

| 确认门 | 你审什么 | 不通过会怎样 |
|---|---|---|
| **1. 脚本/分镜** | 场景切分、时间窗、旁白措辞、视觉调性 | agent 改方案包 |
| **2. 素材 + TTS** | 头像/logo/字体齐全，TTS 音色试听 | agent 重新搜集/换音色 |
| **3. 渲染结果** | 抽关键帧看 5/15/25/40/55s 截图 | agent 改 index.html 重跑 |

通过 → 拿到 `~/videos/<项目>/renders/final.mp4`。

> **输出**：原生可编辑的 HTML composition + MP4。HTML 在 `index.html`，改完跑 `npx hyperframes render` 重出片。

---

## 文档索引

| | 文档 | 说明 |
|---|------|------|
| 📘 | [SKILL.md](./SKILL.md) | 核心工作流 + 4 阶段 3 确认门（**新用户先看这里**）|
| 🎯 | [能力定位](#能力定位) | 与其他 AI 视频工具的对比 |
| 🔄 | [分镜→HTML 衔接](./references/hyperframes-handoff.md) | 把 Markdown 分镜表翻译成 hyperframes `index.html` 的完整规则 |
| 🗣 | [TTS 供应商对比](./references/tts-providers.md) | 5 家 TTS 选型 + 调用范式 |
| 📋 | [分镜方案包模板](./templates/video_plan_template.md) | Stage 1 用的 Markdown 模板 |
| 💀 | [HTML composition 骨架](./templates/composition_skeleton.html) | 1080×1920 竖屏起步模板 |
| 🛠 | [scripts/generate_tts.sh](./scripts/generate_tts.sh) | 批量 TTS 脚本（dashscope/say/openai）|
| 💼 | [示例项目](https://github.com/MinibeanAI/koubo-hf) | 完整跑通的口播视频项目 |
| 🏗 | [技术设计](./SKILL.md#已知踩坑) | Rule 3 视频直系、timeline 注册、确定性原则等硬约束 |
| ❓ | [FAQ](#faq) | 模型选型、字体下载失败、TTS 限流 |

---

## 已知踩坑

参考 `SKILL.md` 完整列表。最常踩的 5 个：

1. **`<video>` / `<audio>` 必须放在 host root 直接子位置**，不能套 `<div>`，否则黑屏
2. **video muted + 独立 `<audio>` 元素**（同源也要拆开两个标签）
3. **GSAP 时间线必须 `paused: true` + 注册到 `window.__timelines["<id>"]`**，id 严格匹配 `data-composition-id`
4. **每个 timed 元素**：`data-start` / `data-duration` / `data-track-index` 三件套 + `class="clip"`
5. **不要在 `setTimeout` / `Promise` / `async` 里构造 GSAP 时间线**——必须同步写在 `<script>` 顶部

字体：所有用到的字体必须 `@font-face` 声明；系统字体（PingFang SC / Songti SC）用 `src: local("...")`。

`npx hyperframes` 每次联网校验版本——网络抖时用缓存路径：

```bash
node /Users/douer/.npm/_npx/702923228c2ce1e6/node_modules/hyperframes/dist/cli.js
```

---

## 技术栈

- **[`text-to-video-planner`](https://github.com/)** —— 策划侧
- **[`hyperframes`](https://hyperframes.heygen.com/)** (HeyGen) —— 渲染侧
- **[GSAP](https://gsap.com/)** —— 动画引擎
- **[FFmpeg](https://ffmpeg.org/)** —— 视频编码
- **[阿里云百炼 / 字节豆包 / OpenAI TTS / macOS `say` / Kokoro-82M]** —— TTS 供应商

---

## FAQ

**Q: 跟 `hyperframes` skill 有什么区别？**
A: `hyperframes` 只做渲染（HTML→MP4）。本 skill 是 **planner 策划 + hyperframes 渲染**的合集，**包含自动衔接**，目标用户是"我有讲稿想出视频"。

**Q: 跟 `text-to-video-planner` skill 有什么区别？**
A: `text-to-video-planner` 只出分镜方案包（Markdown），不出视频。本 skill 是**它的下游**——会自动接 hyperframes 出片。

**Q: 支持哪些画幅？**
A: 9:16 竖屏（抖音/Reels/小红书）、16:9 横屏（B站/YouTube）、1:1 方形（Instagram），改 `data-width` / `data-height` + 卡片几何即可。

**Q: 视频太长会怎样？**
A: ≤ 90s 是甜蜜点。> 3min 拆段跑，每段独立成片。

**Q: TTS 必须用哪一家？**
A: 都可以。商业项目推荐阿里云百炼；草稿用 macOS `say` 零成本。

**Q: 报错 `npx hyperfonts` / `fonts` 加载失败？**
A: 删 `fonts/` 下的 woff2 重新下载，或在 `@font-face` 用 `src: local("系统字体")` 兜底。

---

## 版本

- **v1.0** （2026-07-09）—— 初版，组合 `text-to-video-planner` 策划 + `hyperframes` 渲染

---

## 许可

[MIT](LICENSE)

---

## 联系

- 💬 **问题 & 分享** — [GitHub Discussions](https://github.com/MinibeanAI/text-to-video/discussions)
- 🐛 **Bug 报告 & 功能请求** — [GitHub Issues](https://github.com/MinibeanAI/text-to-video/issues)

---

<sub>Distribution: <a href="https://github.com/MinibeanAI/text-to-video">GitHub</a>. 自由使用，MIT 许可——保留署名即可。</sub>

[⬆ 回到顶部](#text-to-video--文本讲稿一站式生成可交付的-mp4-短视频)
