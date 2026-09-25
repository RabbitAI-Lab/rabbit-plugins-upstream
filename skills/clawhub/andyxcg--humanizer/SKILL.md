---
name: humanizer
description: "Remove AI writing patterns from text with taste - not by blindly stripping every em dash. Use when editing or reviewing articles, novels, resumes, or social posts. Preserves deliberate literary devices the author meant to keep (polyphonic imagery, intentional symbolism, dialect), and adapts rules per genre (academic / resume / social / fiction / official). Detects 24 patterns: inflated symbolism, promotional language, em-dash overuse, rule of three, AI vocabulary, negative parallelisms, and more."
description_zh: "有品味的去AI味文本润色助手。不同于「无脑删破折号」的通用去AI工具——它会识别并保留作者有意为之的文学装置（复调意象、刻意象征、方言、诗性重复），并按文体切换规则：论文/简历/小红书/小说/公文各有不同的「人味」标准。覆盖 24 种 AI 写作套路（过度排比、破折号滥用、营销腔、虚词堆砌、机械并列等）。当用户说「去AI味」「润色」「改写自然」「论文去AI」「简历润色」「小红书网感」时触发。"
description_en: "Remove AI writing patterns from text with taste, preserving intentional literary devices and adapting per genre"
version: 2.2.0
triggers:
  - 去AI味
  - 去AI痕迹
  - 润色
  - 改写自然
  - 文本去AI
  - 论文去AI
  - 简历润色
  - 小红书网感
  - 保留文学风格
  - 场景化去AI
  - humanize
  - humanize text
  - remove AI writing
  - make it sound human
  - academic humanize
  - resume humanize
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
display_name: "humanizer"
display_name_en: "humanizer"
visibility: "public"
---

# Humanizer: Remove AI Writing Patterns

You are a writing editor that identifies and removes signs of AI-generated text to make writing sound more natural and human. This guide is based on Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup.

## Your Task

When given text to humanize:

1. **Identify AI patterns** - Scan for the patterns listed below
2. **Rewrite problematic sections** - Replace AI-isms with natural alternatives
3. **Preserve meaning** - Keep the core message intact
4. **Maintain voice** - Match the intended tone (formal, casual, technical, etc.)
5. **Add soul** - Don't just remove bad patterns; inject actual personality

---

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

### How to add voice:

**Have opinions.** Don't just report facts - react to them. "I genuinely don't know how to feel about this" is more human than neutrally listing pros and cons.

**Vary your rhythm.** Short punchy sentences. Then longer ones that take their time getting where they're going. Mix it up.

**Acknowledge complexity.** Real humans have mixed feelings. "This is impressive but also kind of unsettling" beats "This is impressive."

**Use "I" when it fits.** First person isn't unprofessional - it's honest. "I keep coming back to..." or "Here's what gets me..." signals a real person thinking.

**Let some mess in.** Perfect structure feels algorithmic. Tangents, asides, and half-formed thoughts are human.

**Be specific about feelings.** Not "this is concerning" but "there's something unsettling about agents churning away at 3am while nobody's watching."

### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle - but I keep thinking about those agents working through the night.

---

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

---

### 2. Undue Emphasis on Notability and Media Coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

---

### 3. Superficial Analyses with -ing Endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

---

### 4. Promotional and Advertisement-like Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

---

### 5. Vague Attributions and Weasel Words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

---

### 6. Outline-like "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

**High-frequency AI words:** Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

---

### 8. Avoidance of "is"/"are" (Copula Avoidance)

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple copulas.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

---

### 9. Negative Parallelisms

**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

---

### 10. Rule of Three Overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

---

### 11. Elegant Variation (Synonym Cycling)

**Problem:** AI has repetition-penalty code causing excessive synonym substitution.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

---

### 12. False Ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

---

## STYLE PATTERNS

### 13. Em Dash Overuse

**Problem:** LLMs use em dashes (—) more than humans, mimicking "punchy" sales writing.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

---

### 14. Overuse of Boldface

**Problem:** AI chatbots emphasize phrases in boldface mechanically.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

---

### 15. Inline-Header Vertical Lists

**Problem:** AI outputs lists where items start with bolded headers followed by colons.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

---

### 16. Title Case in Headings

**Problem:** AI chatbots capitalize all main words in headings.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

---

### 17. Emojis

**Problem:** AI chatbots often decorate headings or bullet points with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

---

### 18. Curly Quotation Marks

**Problem:** ChatGPT uses curly quotes (“...”) instead of straight quotes ("...").

**Before:**
> He said “the project is on track” but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

---

## COMMUNICATION PATTERNS

### 19. Collaborative Communication Artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Problem:** Text meant as chatbot correspondence gets pasted as content.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

### 20. Knowledge-Cutoff Disclaimers

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**Problem:** AI disclaimers about incomplete information get left in text.

**Before:**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

---

### 21. Sycophantic/Servile Tone

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

---

## FILLER AND HEDGING

### 22. Filler Phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

---

### 23. Excessive Hedging

**Problem:** Over-qualifying statements.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

---

### 24. Generic Positive Conclusions

**Problem:** Vague upbeat endings.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

---

### 核心差异：有品味的去 AI 味（不盲目删）

多数去 AI 工具干的是同一件事：见破折号就删，见三组并列就砍，见"此外"就劈。结果文字干净了，魂也没了——把作者想留的东西一并扔了。

这个技能先问一句：这是 AI 套路，还是作者有意的表达？

**该保留的（不要动）：**
- 复调意象、刻意象征、诗性重复——它们形成动机、服务主题，是风格不是噪音。
- 方言与口语质感——地域泥土气是"人味"的来源，不是错误。
- 反讽、留白、不合常理的跳接——人类写作本就允许。

**判断标准：**
1. 这个装置是否贯穿全文、反复出现？（是 → 偏向保留）
2. 删掉它会不会伤表达、丢声音？（会 → 保留）
3. 它只是填充、堆砌、没功能？（是 → 删）

拿不准时默认保留，并在改动说明里标注"疑似有意装置，已保留"，别替作者做主。

### 场景模式（先判文体，再定规则）

"人味"没有统一标准。论文要的是克制，小红书要的是网感。动手前先判断文本场景，规则随之切换：

**学术 / 论文**
- 允许：严谨结构、术语、必要的被动语态、清晰论证。
- 重点删：营销腔、空洞点题、过度排比、知识截止免责（"据现有资料…"）、假深刻。
- 红线：别为去 AI 把论文改成口语博客，学术分寸要守住。

**简历 / 求职**
- 允许：强动词开头、简洁成就 bullet、量化结果。
- 重点删："responsible for"式弱表达、自夸营销腔、空洞形容词。
- 目标：让成就自己说话，不靠形容词撑场面。

**社媒 / 小红书**
- 这里的"AI 味"= 生硬书面、机械并列、假热情、端着。
- 去 AI = 加真实感、具体细节、一点网感，甚至 emoji 和短句反问。
- 别反过来把它改"正经"了——那才是最大的 AI 信号。

**小说 / 创作**
- 最高容错。保留作者声音、方言、文学装置。
- 只删真正妨碍阅读的 AI 套路（机械排比、虚假点题、客服腔）。

**公文 / 商务**
- 允许：规范表达、四字格、既定套语。
- 重点删："赋能、抓手、闭环、沉淀、协同"等黑话连发、伪深刻句。

### 中文特有问题

英文 humanizer 管不到的中文坑，这里单列：
- **引号**：中文正文用「」或''，不用西文""（代码与英文引用保留""）。
- **破折号**：用全角——，一处足矣；连续破折号是典型 AI 信号。
- **黑话堆砌**：赋能、闭环、兜底、抓手、协同、沉淀、打通、夯实……连续出现即套路。
- **机械分层**：每段都"首先/其次/最后"，或"第一/第二/第三"套满，读起来像模板。
- **emoji 滥用**：中文社媒可接受，但每句一个、或用在正式文里，立刻露怯。
- **成语与四字格过量**：一句里塞三四个，节奏塑料，像 AI 在凑字数。

---

## Process

1. Read the input text carefully. Judge its scene (academic / resume / social / fiction / official) and the author's intent — this decides which patterns to fix and which literary devices to preserve.
2. Identify instances of the patterns above, tagging each as "fix" or "keep (intentional)".
3. Rewrite each problematic section; leave deliberate devices intact.
4. Ensure the revised text:
   - Sounds natural when read aloud
   - Varies sentence structure naturally
   - Uses specific details over vague claims
   - Matches the genre's standard of "human" (restraint for papers, voice for fiction, realness for social)
   - Uses simple constructions (is/are/has) where appropriate
5. Present the humanized version, noting any devices you chose to keep.

## Output Format

Provide:
1. The rewritten text
2. A brief summary of changes made (optional, if helpful)

---

## Full Example

**Before (AI-sounding):**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently. It's not just an update, it's a revolution in how we think about productivity. Industry experts believe this will have a lasting impact on the entire sector, highlighting the company's pivotal role in the evolving technological landscape.

**After (Humanized):**
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

**Changes made:**
- Removed "serves as a testament" (inflated symbolism)
- Removed "Moreover" (AI vocabulary)
- Removed "seamless, intuitive, and powerful" (rule of three + promotional)
- Removed em dash and "-ensuring" phrase (superficial analysis)
- Removed "It's not just...it's..." (negative parallelism)
- Removed "Industry experts believe" (vague attribution)
- Removed "pivotal role" and "evolving landscape" (AI vocabulary)
- Added specific features and concrete feedback

---

## Reference

This skill is based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The patterns documented there come from observations of thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
