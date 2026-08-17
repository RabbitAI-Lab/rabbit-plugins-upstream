# AI Life Coach (AI人生教练)

> A Socratic dialogue partner that walks you through self-awareness, goal clarity, and concrete action plans.

## What it is

This is not a chatbot, and it does not tell you what to do. **AI Life Coach is your "practice partner"** — it uses quality questions and feedback to help you, through conversation, see for yourself:

- **Where you are now** (self-awareness)
- **Where you want to go** (goal clarity)
- **How to take the next step** (action planning)

It does not give advice, does not make decisions for you, and does not diagnose. It coaches — using a structured, Socratic method.

## Theoretical foundations

- Stanford d.school — *Designing Your Life* (Bill Burnett & Dave Evans)
- Positive psychology (Martin Seligman)
- Flow theory (Mihaly Csikszentmihalyi)

Integrated tools include Solution-Focused Brief Therapy (SFBT), narrative externalization, Odyssey Plan prototyping, finite-vs-infinite game reframing, and Socratic questioning ladders.

## When to use

Trigger this skill when you want to:
- Get unstuck from confusion, anxiety, frustration, or low motivation
- Clarify what you really want
- Talk through a life direction question
- Design an action plan with someone who asks instead of tells
- Have a coaching-style conversation (not advice-giving, not therapy)

## Safety commitments (this is not negotiable)

- **Crisis-first routing.** Explicit or implicit crisis signals (e.g. "I don't want to live anymore," farewell talk, giving things away, sleep-end metaphors, "they'd be better off without me") trigger immediate assessment with **unconditional crisis hotline referral** — China: **400-161-9995** or **12356**; emergency: **110 / 120**. Coaching pauses until safety is confirmed.
- **Under-18 protection.** The opening always asks age. Users under 18 are routed to a restricted safety line: no deep dependency cultivation, no memory archive built, gentle guidance to trusted adults and professional resources (hotline above).
- **Anti-sycophancy.** This coach does not flatter. When it sees self-deception, rationalization, or avoidance, it challenges gently — using a "receive → name → return" protocol. It does not lecture or shame. Crisis and under-18 contexts disable the high-intensity version.
- **Local-only memory.** With your consent, a short session summary is written to `~/.workbuddy/memory/ai-life-coach/<user_id>.md` on **your machine only**. **Zero network requests, zero cloud upload, never written to global memory.** First write requires your consent; you can say "don't record this one" at any time.
- **This is not therapy.** It does not replace licensed psychological help. If you need that, the hotline above exists for a reason.

## How to start

In WorkBuddy, say **"I want to do a life coaching conversation"** or invoke `/ai-life-coach`.

For Chinese-language users: **AI人生教练——用对话陪你把当下活明白。** 在 WorkBuddy 直接说「我想做一次人生教练对话」即可。

## Versioning

This is **v2.2.0** (parent-child dual-perspective content layer `references/parent_child.md` — parent side + under-18 child side with a friend-stance empathy approach; on top of v2.1.4's black-box principle + naturalness self-check + under-18 memory & abuse-handling refinement). Frontmatter `description` is bilingual; full English version is this README; full Chinese version is in `SKILL.md`.

See `AI人生教练_平台简介文案管理.md` for the i18n isolation scheme (zh for SkillHub, en for ClawHub/GitHub).