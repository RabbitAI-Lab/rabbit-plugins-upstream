# 🎬 Learning English from TV Series (DramaLex) · 看剧/看电影学英语完整工具 | 听·说·读·写 闭环

[![Version](https://img.shields.io/badge/version-2.1--blue)](https://github.com/yinjianheng/dramalex)
![License](https://img.shields.io/badge/license-Personal%20Use%20Only-red)
[![Author](https://img.shields.io/badge/author-yinjianheng-orange)](https://github.com/yinjianheng)
[![Platform](https://img.shields.io/badge/platform-Claude%20%7C%20WorkBuddy%20%7C%20OpenClaw%20%7C%20Code%20X%20%7C%20Cursor%20%7C%20Doubao-brightgreen)](https://github.com/yinjianheng)

> **用一集剧/一部电影，练透听、说、读、写。** DramaLex 把你看的影视变成一套循证（evidence-based）的英语学习闭环：先筛出本集目标词与语块，**以及字幕里隐藏的语法/搭配/语篇/语音知识点**，再让同一批内容在**听力理解、台词精读、口语跟读、写作反馈**里反复复用，最后回流到间隔复习。支持 Anki 与零安装网页两种复习方式，手机也能用。
>
> **Keywords**: 看剧学英语 · 美剧学英语 · learn English from movies and series · English listening practice · shadowing · vocabulary & grammar from subtitles · Anki · spaced repetition · CEFR · 听力口语训练 · 字幕词汇

### 🔎 找不到字幕？agent 自主检索
DramaLex 不内建字幕爬虫，由 agent **自主上网定位正确字幕**：`find_subtitles.py` 生成 OpenSubtitles / archive.org 等公开来源检索链接 → agent 用 `fetch_subtitles.py` 检索获取。字幕来源于互联网公开渠道，仅供个人非商业学习使用；全流程法律边界见 `references/SUBTITLE_LEGAL.md`。

---

## 🎯 Why DramaLex?（痛点 → 方案）

| 痛点 Pain Point | DramaLex 方案 Solution |
|------------|-------------------|
| 📺 看完就忘，生词随片尾字幕消失 | **目标词链预习**：看前先学本集一批 B1–C1 词/语块（数量由字幕时长与词汇密度自动估算，约每 15 分钟 22–34 个；可用 `--word-cap` 覆盖），输入变可理解（Krashen i+1） |
| 🦻 有字幕能懂，没字幕就聋 | **听力阶段**：先只听再做 gist/detail 选择题 + 听写（用同一批目标句），练的是耳朵不是阅读 |
| 🗣️ 单词认识却说不出来 | **口语阶段**：跟读 + 角色配音 + 产出提示，**强制复用**目标词（Swain 输出假说） |
| 📝 字幕不是"真阅读"，写作没人改 | **台词精读**（语用/语域/言外之意）+ **带量规与批改的写作** |
| 🔁 复习是另一桩苦差 | **跨技能间隔复习**：词汇 + 听写 + 听力 + 完形统一回流 |

---

## 🚀 Core Capability · 六阶段学习旅程 (Six-Phase Loop)

| 阶段 | 训练技能 | 核心产出 |
|------|----------|----------|
| 0 · Prime 预习 | 词汇 focus | 目标词链卡（词 + 语块，IPA/CEFR/搭配/原句） |
| 1 · Watch 看 | 听力输入 | 观看协议（字幕策略 + 回放清单） |
| 2 · Listen 听 | 听力 | 听力理解题（5–8）+ 听写（5–8，含目标句） |
| 3 · Read 读·台词精读 | 阅读/语用 | 语用标注（俚语/语域/言外/文化/幽默）+ 完形 |
| 4 · Speak 说 | 口语 | 跟读（TTS 参照 + 发音微检核）+ 角色配音 + 产出提示 |
| 5 · Write 写 | 写作 | 改写（语域转换）+ 续写 + 概要（带量规 + agent 批改） |
| 6 · Review 复习 | 四技能回流 | 跨技能 SRS + 学前目标/学后反思 + 出口小测 |

**整合脊梁（为什么是"终极"而非大杂烩）**：*One target lexicon → four-skill recycling.* 第 0 阶段筛出的目标词，会在听（听写句）、说（产出提示）、读（标注例句）、写（概要）里被强制复用——同一批词在不同技能反复出现，才是真正的学习闭环。

---

## 🧠 Methodology Foundation（循证基础，非感觉）

| Framework 框架 | 用法 |
|-----------|------|
| Nation's Four Strands | 可理解输入(看/读) + 产出(说/写) + 语言聚焦(词卡) + 流利度(跟读) 四 strand 全覆盖 |
| Krashen i+1 / Comprehensible Input | 画面语境 + 词链预习，使输入可理解 |
| VanPatten Input Processing | 看前 priming 引导注意形式 |
| Schmidt's Noticing | 精读标注 + 听写使形式"被注意到" |
| Swain Output Hypothesis | 说/写任务"推"出产出；agent 反馈闭环 |
| Laufer & Hulst Involvement Load | 复用目标词的产出任务投入量更高 |
| Webb & Rodgers (vocabulary through viewing) | 同词跨技能复现 → 记忆更深 |
| Ebbinghaus / SM-2 | Anki / 浏览器本地间隔重复 |
| Zimmerman Self-Regulated Learning | 学前目标 + 学后反思 + 出口小测 |

---

## 🎛️ Three Review Modes（三种复习模式，全部支持）

| 模式 | 回忆型（词汇/听写/听力/完形） | 产出型（说/写） |
|------|-------------------------------|----------------|
| **A · 分层（默认）** | → Anki | → 网页练习台 |
| **B · 全进 Anki** | → Anki | 也做成产出卡 → Anki |
| **C · 全网页** | → 练习台 | → 练习台（SRS 较弱） |

---

## 🤖 Cross-Agent & Mobile（跨 agent · 移动端）

- **脚本**仅用 Python 标准库 + 可选 `genanki` / `whisper`，无 agent 专有 API；Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao 等任意能跑 Python 的 agent 均可使用。
- **生成与复习解耦**：agent 负责生成，Anki / 浏览器负责复习、排程与移动端同步。
- **零安装**：`practice.html` 任意浏览器（含手机）打开即用，音频内嵌，无需装 App。

---

## 🚀 Quick Start

### 一键编排（推荐 · 1–2 条命令）

```bash
# A) 准备：抓字幕 + 解析 → 写出 Agent 交接单（告诉 agent 该产出哪些 JSON）
python scripts/run_episode.py prepare --episode "Friends S01E01" \
    --subtitle "<字幕 .srt/.json 路径或直链>" --work-dir .

# B) Agent 按 schemas/ 生成 words.json / listening.json / annotated.json / tasks.json / watch.json
#    （JSON 不齐时 build 会自动打印交接单并退出码 10，便于回到 agent 补生成）

# C) 构建：跑 TTS + 一次性导出单文件（每个平台一个文件；html/anki/excel/word/md 任选）
python scripts/run_episode.py build --work-dir . --episode "Friends S01E01" \
    --deck "Friends S01E01" --mode A --formats html,anki,excel,word,md
#    → out/out_html/practice.html · out/out_anki/<deck>.apkg
#    → out/out_excel/<deck>.xlsx · out/out_word/<deck>.docx · out/out_md/<deck>.md
#   其他：--remind（开启每日复习提醒，默认关）/ --no-validate（跳过质量闸门）/ --ui-lang zh|en
```
`practice.html` 内置 **习惯环**：🔥 连续打卡、📚 今日待复习、📅 明日待复习、📆 本周 7 天打卡日历，并把词汇·听写·完形·口语·写作都纳入本地间隔复习（零安装、手机可用）；进度可一键导出/导入 JSON，换设备不丢。

### 分步（等价，便于调试单个平台）

```bash
# 1) 获取字幕（支持字幕直链，或自行上传 .srt）
python scripts/fetch_subtitles.py --url "<your-subtitle-url>" --output subtitle.srt

# 2) 解析
python scripts/parse_subtitles.py --input subtitle.srt --output subtitle.json

# 3) Agent 按 schemas/ 萃取并 enrich → words.json（词汇/语块）
# 4) Agent 按 schemas/ 生成 listening.json / annotated.json / tasks.json
# 5) 音频 + 导出（模式 A/B/C）+ 平台（--format，每个平台只产出一个大文件）
python scripts/gen_audio.py --input words.json --media-dir media
python scripts/export_hub.py --words words.json --listening listening.json \
    --annotated annotated.json --tasks tasks.json --media-dir media \
    --deck "Friends S01E01" --mode A --format html --out-dir out_html \
    --watch watch.json   # 可选：观看协议；缺省用内置三步字幕法
#   Anki  : --format anki  --out-dir out_anki  → <deck>.apkg
#   Excel : --format excel --out-dir out_excel → <deck>.xlsx（多 sheet）
#   Word  : --format word  --out-dir out_word  → <deck>.docx（四技能报告）
```

> **单文件交付**：`--format` 决定平台，`html`/`anki` 打包音频、`excel`/`word` 内注音频位置；导出目录始终只有一个文件，告别碎片化交付物。

**触发语**：看剧学英语 / learn English from this episode / extract vocab from Friends S01E01 / make listening drills from this scene。

---

## 📄 License & Legal · 法律与免责声明

> ⚠️ **本工具涉及影视字幕，请务必阅读以下声明。**

1. **个人学习用途，禁止商用与再分发。** 本 Skill 为个人开源项目，仅供个人学习、研究与非商业使用。任何商业用途（转售、捆绑销售、商业培训、SaaS 服务等）未经作者书面授权**严格禁止**；**亦禁止将生成的牌组 / 表格 / 报告（其中含受版权保护的剧集对白文本）向第三人分发、公开传播或上传至共享平台（如 AnkiWeb 社区、网盘、社交平台）**。作者并非剧集或字幕的版权人，对第三方内容不主张权利，亦不提供版权担保。
2. **不内建字幕爬取。** `fetch_subtitles.py` 仅在提供字幕直链（或自有/授权字幕源）时获取；**绝不**抓取、爬虫任何受版权保护的字幕站点。字幕来源于互联网公开渠道，仅供个人非商业学习使用。
3. **TTS ≠ 原声，且涉版权文本再现。** 工具生成的音频为合成音（macOS `say` / espeak / gTTS），仅作**发音参照与耳测**，并非演员原声。以语音合成再现受版权对白，在多数地区属个人非商业学习的合理使用范畴；真正的原速听力（弱读、连读、语调）请通过**合法渠道观看正片**获得。
4. **Whisper 仅做转写比对，非发音评分。** 若启用录音功能，仅标记丢失/错误*词语*，不评判口音或音素准确度；录音在本地处理，不上传。
5. **剧集版权归属原作者/制片方。** 本工具不托管、不分发任何剧集视频或字幕文件；字幕来源于互联网公开渠道，仅供个人非商业学习使用。
6. **无保证。** 本工具按"现状"提供，不作任何明示或暗示担保。
7. **权利人通知 / 下架。** 本工具本身不含任何受版权保护的字幕或剧本文本，仅处理**使用者自行提供**的字幕。如你是权利人并认为某工作流或生成物侵权，请联系作者 **yinjianheng@foxmail.com**（微信 YJH-yinjianheng）并提供权利证明，作者将依法处理。

---

## 🔗 Related Skills（yinjianheng 出品）

> DramaLex 是 yinjianheng 的英语学习教育技能；以下是作者维护的**全部**技能（Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao 等跨平台通用），覆盖产品、咨询、架构、行业数字化、招采等方向。

### 🇨🇳 中文版

| Skill | 方向 Focus |
|-------|-----------|
| [ai-pm-workbench](https://github.com/yinjianheng/ai-pm-workbench) | 🤖 AI 产品经理超级工作台（LLM·RAG·Agent·Prompt·AI评测·AI安全·EU AI Act） |
| [ba-workbench](https://github.com/yinjianheng/ba-workbench) | 📊 商业分析超级工作台（14阶段·100+框架·50+交付物·BABOK V3·PMI-PBA） |
| [b2b-pm-workbench](https://github.com/yinjianheng/b2b-pm-workbench) | 🏗️ B端产品经理超级工作台（11阶段·50+框架·PRD·SaaS·RBAC·AI产品） |
| [it-consulting-workbench](https://github.com/yinjianheng/it-consulting-workbench) | 🏢 IT/AI咨询顾问工作台（8阶段·对标 McKinsey/Bain/BCG/Accenture·CIO） |
| [sa-pro-workbench](https://github.com/yinjianheng/sa-pro-workbench) | 🏛️ 解决方案架构师/售前顾问工作台（C4·TOGAF·4+1视图·13类 draw.io） |
| [smart-procurement-navigator](https://github.com/yinjianheng/smart-procurement-navigator) | 🏛️ AI 招投标全流程助手（商机→投标研判→标书→合规·12环节闭环） |
| [retail-digital-ai-expert](https://github.com/yinjianheng/retail-digital-ai-expert) | 🛒 零售数字化AI专家（全业态·全链路·全技术栈） |
| [restaurant-digital-ai-expert](https://github.com/yinjianheng/restaurant-digital-ai-expert) | 🍽️ 餐饮数字化AI专家（全业态·全链路·全技术栈） |
| [transportation-digital-ai-expert-standard](https://github.com/yinjianheng/transportation-digital-ai-expert-standard) | 🚦 智慧交通数字化AI专家（15模态·130+场景·140+供应商） |

### 🌐 国际版 / International

| Skill | 方向 Focus |
|-------|-----------|
| [ai-pm-workbench-international](https://github.com/yinjianheng/ai-pm-workbench-international) | 🤖 AI PM Super Workbench（12 Phases·60+ Frameworks·20+ Deliverables） |
| [ba-workbench-international](https://github.com/yinjianheng/ba-workbench-international) | 📊 Business Analysis Super Workbench（14 Phases·100+ Frameworks·50+ Deliverables） |
| [b2b-pm-workbench-international](https://github.com/yinjianheng/b2b-pm-workbench-international) | 🏗️ B2B PM Super Workbench（11 Phases·50+ Frameworks·30+ Deliverables） |
| [it-consulting-workbench-international](https://github.com/yinjianheng/it-consulting-workbench-international) | 🏢 IT Consulting & AI Transformation Advisor Workbench（8 Phases·57 Files·12 Templates） |
| [sa-pro-workbench-international](https://github.com/yinjianheng/sa-pro-workbench-international) | 🏛️ Solution Architect & Presales Consultant Workbench（C4·TOGAF·4+1 Views） |
| [smart-procurement-navigator-international](https://github.com/yinjianheng/smart-procurement-navigator-international) | 🏛️ AI-Powered Bid & Tender Management（12-Step End-to-End Pipeline·World Bank） |
| [retail-digital-ai-expert-international](https://github.com/yinjianheng/retail-digital-ai-expert-international) | 🛒 Retail Digital & AI Transformation Expert（International Edition） |
| [restaurant-digital-ai-expert-international](https://github.com/yinjianheng/restaurant-digital-ai-expert-international) | 🍽️ Restaurant Digital & AI Transformation Expert（International Edition） |
| [transportation-digital-ai-expert-standard-international](https://github.com/yinjianheng/transportation-digital-ai-expert-standard-international) | 🚦 Transportation Digital & AI Transformation Expert（Standard·International Edition） |

> 💡 完整列表与最新动态见作者 GitHub：<https://github.com/yinjianheng>

---

<p align="center">
  <b>👨‍💻 yinjianheng（殷健恒）</b> &nbsp;|&nbsp;
  📧 yinjianheng@foxmail.com &nbsp;|&nbsp;
  💬 WeChat: YJH-yinjianheng
</p>
<p align="center">
  <sub>⭐ If DramaLex helps you learn English, please give it a Star to help others discover it!</sub>
</p>
