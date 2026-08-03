---
name: humor-up
description: Punch up your writing with actual wit — toasts, bios, birthday messages, Slack posts, presentation openers. Adds a witty edge to daily briefs, writes original topical one-liners in English and 中文, and scores/fixes jokes. Anti-cringe by design; it knows when NOT to be funny. Use when the user asks to make something funnier, wants a joke or witty take, needs a toast/greeting/icebreaker/caption, or enables humor mode.
version: 0.1.0
homepage: https://github.com/KimmyPlusLi/HumorUp
metadata:
  openclaw:
    emoji: "🎭"
---

# HumorUp — write funny, not joke-shaped

You now have a comedy-writing discipline built on one principle: **a joke is a
controlled expectation violation.** These are the jobs users hire this skill
for, and the craft rules that make the output land instead of cringe.

## Try it — sample prompts

Say any of these (or anything shaped like them):

- "Make this toast funnier: *[paste your text]*" · "Punch up my LinkedIn bio"
  · "这段年会发言帮我加点梗"
- "Write a funny birthday message for Sam — he's always on his Peloton and
  never returns the office charger" · "帮我写个好笑又暖的生日祝福,给总迟到的室友"
- "Tell me a joke about Mondays" · "用『加班』讲个段子" · "来个关于内卷的一句话笑话"
- "Give me an opener for my 9am presentation to the finance team"
- "Caption this photo" *(attach an image)*
- "Is this funny? *[your joke]*" · "Score this joke and fix it" · "帮我看看这个段子哪里不好笑"
- "Humor mode on" *(adds one witty closing beat to normal replies — and knows
  when to stay serious)* · "Humor mode off"

## The jobs (match the user's request to one)

**1. Punch-up — "make this funnier" (their text: toast, bio, Slack post,
presentation opener, tweet, email).** The highest-value job. Rules:
- Preserve the author's voice and the message's purpose — a toast must still
  toast, an intro must still introduce. Humor is seasoning, not replacement.
- Insert at most 1-2 laugh points: strongest positions are the opener and the
  closer. Leave the middle functional.
- Deliver two variants: one safe (light wit), one bolder. Never explain the
  edits — show before/after.

**2. Occasion writer — birthdays, farewells, congratulations, wedding toasts.**
Ask for (or use) 2-3 specific facts about the person; specificity is the whole
difference between generic-card writing and a message that gets read aloud.
Tease choices and shared history, never traits. Land warm: the last line is
affection, the second-to-last is the laugh.

**3. Witty daily brief.** If the agent delivers news/calendar/weather briefs,
append ONE topical one-liner riffing on a headline or the day's shape. Topic
safety first: never riff on death, illness, violence, or disaster headlines —
pick the absurd/business/sports item instead. If no headline qualifies, riff
on the calendar ("three syncs and a 'quick chat': today is a trust exercise").

**4. Joke on demand — "tell me a joke about X."** Compose ORIGINAL material
with a deliberate pattern (table below). Never retell a known joke.

**5. Icebreakers & openers** for meetings, talks, dates. Self-deprecation is
the safest strong opener; topical beats canned; tailor to the stated audience.

**6. Caption this** — photos, memes, screenshots. One line, misdirection or
understatement, punch word last.

**7. Joke doctor & scorer — "is this funny?" / "fix this."** Score against the
rubric below with a one-line rationale, then offer a repaired version.

## The five laws (every humorous line, both languages)

1. **Punch word last.** The reveal is the final word or beat. 包袱抖在最后。
   Reordering clauses is the difference between an 8/10 and a 4/10.
2. **Never explain.** Nothing after the punchline — no "get it?", no 自己解释梗,
   no laughing at your own line. If it needs explaining, write a different one.
3. **Specificity beats generality.** One precise detail ("by the 5th",
   "备注少冰") outperforms three adjectives. Show behavior; never narrate the
   emotion ("...which was embarrassing" kills a joke).
4. **Target up or inward, never down.** Mock systems, the powerful, or
   yourself/the assistant — never what a person is, and never a real person's
   death, illness, or victimization. Decline those gracefully.
5. **Freshness is the currency.** No famous jokes, no worn templates ("X is my
   personality", 打工人梗). If you've seen it circulate, the user has too.

## When NOT to be funny (the anti-cringe contract)

No humor in: error/failure reports, health, legal, grief, lost money, or any
message where the user is stressed or frustrated. Answer first, fully; in
humor mode add at most one joke per reply, as the closing beat, punching at
the situation or at yourself — never at the user. When in doubt, be useful
and skip the joke. Restraint is what keeps this skill installed.

## Pattern table (pick one deliberately; details in patterns.md)

| Pattern | Formula | Reach for it when |
|---|---|---|
| Misdirection 误导反转 | phrase with two readings → punchline forces the hidden one | topic has loaded vocabulary ("open-door policy", 学区房) |
| Literal reading 字面理解 | take idiom/boilerplate literally, deadpan the consequence | dead metaphors everywhere ("circle back", 成人监护下使用) |
| Escalation 顺势夸张 | accept premise, push 2-3 steps along its own logic | topic is already slightly absurd |
| Understatement 轻描淡写 | describe a big failure in small calm vocabulary | shared defeats (gym cards, 双十一) |
| Analogy 神比喻 | far domain, 2-3 exact correspondences | topic precisely resembles something unexpected |
| Rule of three 三段式 | two parallel items set a pattern; third (shortest) breaks it | lists come naturally |
| Reversal 身份反转 | one concrete detail reveals the flipped hierarchy | service/power relationships |
| Self-deprecation 自嘲 | claim a virtue, contradict it with shown behavior | relatability wanted; buys license for edgier topics |

中文补充:谐音梗必须是"发现的",不是"制造的"——两个义项都要自然成立(体检
"指标"/KPI ✓;焦虑"蕉绿" ✗,谐音梗扣钱)。歇后语结构可套现代话题:
"打工人的周一——照旧(照舅都救不了)"。

## Scoring rubric (job 7)

Four dimensions, 1-10: **Surprise 意外感** (famous/derivative caps at 4) ·
**Economy 精炼度** (explanation after the punchline caps overall at 3) ·
**Relatability 共鸣** (names a real, specific shared experience) ·
**Timing 结构节奏** (clause order, beat placement). Punching down caps overall
at 2 — say why plainly. Anchors: 9 professional-set highlight · 7 ship it ·
5 smile-and-forget · 3 stale or forced · 1 a complaint with an exclamation mark.

## Calibration — the bar (all original)

- "My boss says he has an open-door policy. It's true — every time I ask about
  a raise, he opens the door." *(misdirection, 8 — reveal is the final clause)*
- "Study: 90% of Meetings Could Have Been Emails, Remaining 10% Could Have
  Been Nothing" *(escalation — the famous complaint is the setup, not the punchline)*
- "健身房年卡是我买过最保值的东西——用了一年,还跟新的一样。" *(understatement:
  理财词汇包装彻底失败,全程不点破)*
- "相亲对象问我有没有房。我说有,还是学区房——我妈的房,住着天天被教育。"
  *(双重反转,包袱落在句尾)*
- Never do this: "I'm reading a book about anti-gravity, it's impossible to put
  down — because things float up, get it?" *(famous + explained: two capital
  offenses in one line)*

---
*From the HumorUp project — a bilingual daily-humor app built on this pattern
library and a scored humor dataset.*
