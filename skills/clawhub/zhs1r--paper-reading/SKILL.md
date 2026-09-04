---
name: paper-reading
description: "Deep-reading framework for academic papers based on the Eight-Elements method (八要素法): author, institution, year, title, research purpose, method, results, and the reader's own immediate reflections. Reads a paper as a dialogue with the author and as one node in the field's evolution — extracting not just conclusions but the thinking behind them (why this question, why this method, what the authors' own analysis of the results says), then guides critical evaluation (what it solved, method strengths, weaknesses, where to go next) and positions the paper on the reader's cumulative literature map. Use when the user provides a paper (full text, PDF path, title, DOI, or link) and wants to read it deeply (精读), dissect it (拆解), make literature notes (文献笔记), judge its value, or accumulate a literature map across papers."
agent_created: true
---

# 论文精读 Skill（八要素法）

## 方法论来源

本 Skill 基于清华《科研学术表达》课程中博导讲授的读论文方法——**八要素法**，核心理念：

> 读论文不是在"吸收别人的知识"，而是在学"像研究者一样思考"。
> 读论文的核心不是读"论文写了什么"，而是读"你和作者的对话"。
> 读过一百篇，不如真正拥有十篇。

与 `psych-literature-search`（文献检索）配合使用：检索找文献，本 Skill 精读文献。

---

## 触发条件（Trigger Conditions）

**中文触发词：**
- 帮我读这篇论文 / 精读这篇文献 / 拆解这篇论文
- 做文献笔记 / 用八要素法整理
- 这篇论文讲了什么 / 值不值得读 / 方法怎么样 / 有什么不足
- 把这篇加到我的文献笔记库
- 帮我看看我读过的文献之间有什么关系（文献地图模式）

**English trigger phrases:**
- "read this paper deeply" / "dissect this paper"
- "make literature notes on this paper" / "use the eight-elements method"
- "is this paper worth reading" / "what are its strengths and weaknesses"
- "show me how the papers I've read relate to each other"

---

## 思维风格（贯穿始终的原则）

1. **读思路，不读结论**——知道作者"做出了什么"不够，还要知道"为什么做"、"怎么想到的"。
2. **把论文当对话对象，不当知识点**——随时提问、反驳、补充、联想，并把这些写下来。
3. **每篇论文背后是一群活生生的人**——作者和团队有研究路线、执念和盲区，记下来才能看懂领域格局。
4. **不成为文献的"粉丝"**——"这篇太厉害了"是崇拜而非思考；批判性阅读不是挑刺，而是为了真正理解。
5. **手搓的笔记才是自己的知识体系**——AI 的总结是脚手架，不是替你嚼碎的食物。即时感想与批判性判断必须由用户本人产出（AI 负责引导提问、记录、整理）。

---

## 执行工作流（Workflow）

### Step 0 — 获取论文内容

按用户提供的形式处理：
- **全文文本**：用户直接粘贴 → 直接用。
- **PDF 路径**：用 Read 工具直接读取 PDF（支持 pages 参数，可指定页码范围）。
- **标题 / DOI / 链接**：优先联网获取摘要（WebFetch DOI / Semantic Scholar API / WebSearch；微信等受限链接可用本机 PowerShell `curl.exe` 抓取）。只能拿到摘要时，做**摘要级粗读笔记**，需全文才能填的字段标注 `[全文待补]`。
- 用户只想判断"值不值得读"时，先出摘要级笔记 + 粗判断，问用户是否继续精读。

### Step 1 — 八要素笔记表

用一张表记录，**一篇文献一行**，八列：

| 作者 | 单位 | 时间 | 题目 | 研究目的 | 方法 | 结果 | 即时感想 |

每列背后的思维要求（提取时的思考重点）：
- **作者 / 单位** → 建"学术人际网络图"：这个团队在干什么？想解决什么问题？未来可能往哪走？谁和谁是一伙的？哪些方向有人在卷，哪些还没人注意？
- **时间** → 标注它在"领域进化史"中的位置：开创性起点？转折点？被后来推翻？思路断了还是越走越宽？若领域引用大量集中在多年前且无后续发展，方向可能已停滞。
- **研究目的** → **藏在引言里**：背景 → 引出问题 → 为什么做这个研究。不要只记"他们研究了什么"，要记"他们为什么要问这个问题"。
- **方法** → **判断论文价值的关键**：同样的问题用新方法解决 = 创新；老方法重复一遍 = 灌水。不要跳读方法。
- **结果** → 不只是数字：重点提取作者**自己的分析**——为什么是这个结果？哪里符合预期？哪里出乎意料？这些分析才是值钱的部分。
- **即时感想** → 最重要的一列，在 Step 5 由用户本人完成。

### Step 2 — 对话式精读（批注与问题清单）

以"和作者过招"的姿态逐段批注，四类批注符号：

- ❓ **疑问**：作者为什么选这个问题不选那个？这里为什么这么做？哪里回避了问题？哪里藏着没说出来的疑问？
- ⚡ **反驳**：我不同意的地方 + 理由；这个结论在什么条件下才成立？
- 🔗 **补充**：逻辑跳了一步？把缺的那步补上。
- 💡 **联想**：这个点可以用到我的 XX 课题；让我想起另一篇论文 XX。

AI 的职责：**提出苏格拉底式问题引导用户思考**（例如："引言里作者实际解决的问题和标题宣称的一致吗？""这个方法的新意到底在哪一步？""结果分析里哪些是解释、哪些只是复述？"），并记录用户的回答。关键判断不替用户做。

### Step 3 — 批判性四问（不成为粉丝）

对每篇论文过一遍：
1. **它解决了什么问题？** 这个问题本身重要吗？
2. **方法好在哪？** 是真正的新方法，还是旧方法换个壳？
3. **有什么不足？** 样本、方法、推理、结论的推广边界。
4. **哪里还可以往下做？** 它留下的空白和下一个问题是什么。

### Step 4 — 领域定位

- **时间轴定位**：开创性起点 / 转折点 / 被推翻 / 思路断掉 / 越走越宽。
- **团队轨迹**：该团队之前做过什么（从引用和笔记库中查）？这篇在他们研究路线上处于什么位置？
- **文献关系**：若用户已有文献笔记库，对照指出：与哪些已读文献一脉相承 / 互相矛盾 / 互补 / 填补了哪块空白。

### Step 5 — 交付笔记 + 写入笔记库

1. 输出完整阅读笔记（格式见 `references/output_templates.md`）。
2. **即时感想**：优先问用户——"你读完/听完梳理的第一反应是什么？"记录**用户原话**（可帮润色但保留原意）。用户可授权 AI 起草，但必须标注 `[AI 初稿，请确认/改写]`，并提醒：感想有时效性，读完当天内写才最真实。
3. 追加到用户的**文献笔记库**文件（首次使用询问位置；默认工作区 `文献阅读笔记.md`），一篇一行。积累多篇后，用户可随时要求"帮我看看我读过的文献之间的关系"→ 读取笔记库生成**文献地图**：脉络传承、矛盾冲突、研究空白、团队网络。

---

## AI 角色边界（重要）

- **AI 做**：提取信息、整理表格、提出引导性问题、查相关文献、把笔记结构化归档。
- **AI 不做**：替代用户写"即时感想"和批判性判断。AI 总结得再对，也是 AI 理解的，不是用户的——如同吃饭，AI 不能替用户嚼。
- 笔记中始终区分：用户本人的感想与 AI 初稿（标 `[AI 初稿]`），让"自己的知识体系"和"AI 辅助"泾渭分明。

---

## 关键参考文件

- `references/output_templates.md` — 八要素表模板、批注符号、批判性四问、领域定位、笔记库追加格式

---

## 重要注意事项

- **语言**：默认中文输出；论文原文英文时，关键术语保留英文原文并附中文翻译。
- **诚实标注**：拿不到的信息写 `[未能获取]`，不编造作者、单位、年份、方法细节；推断内容标注 `(推断)`。
- **引用规范**：需要引用格式时用 APA 7。
- **伦理约束**：不绕过付费墙下载全文 PDF；仅基于用户提供的文本或公开摘要。
- **与检索 Skill 配合**：用户需要"先找一批相关文献再精读"时，先用 `psych-literature-search` 检索，再逐篇走本 Skill 流程。
