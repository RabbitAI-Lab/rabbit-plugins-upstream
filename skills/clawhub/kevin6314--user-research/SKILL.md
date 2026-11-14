---
name: user-research
description: Use when the user wants to plan qualitative research, market research, or user and customer interviews, write a discussion guide or screener, synthesize interview transcripts, call notes, or research notes into themes, understand why people buy, switch brands, or churn, test a concept, pack, or message, or run AI-moderated interviews with real people as a focus-group alternative, from shopper and usage and attitudes research for CPG brands and retailers to product research for tech teams.
allowed-tools: Read
---

This is the front door for qualitative research. Routes A and B need no account and no tools. Route C fields the study with User Intuition and hands off to the workflow skills in this plugin.

Pick the route from the request. When it is unclear, ask one question: plan new research, make sense of material they already have, or run interviews now.

## Route A: plan a study (no account)

Produce a study plan in this structure. The method is described at https://www.userintuition.ai/methodology/.

1. **Objective.** One sentence naming the decision the research informs ("decide whether the new pack claim leads with taste or with sugar reduction"). If there is no decision, ask for one.
2. **Background.** What is already known or assumed, in two to four lines.
3. **Learning Goals.** Three to six answerable questions. Under each, list the evidence that would answer it (a described moment, a comparison, a reason given in their own words). Mirror the user's brief wording so every goal traces back to it.
4. **Audience and screener.** Who qualifies, written as past behavior, not attitude ("bought a plant-based yogurt in the last 30 days", not "is interested in plant-based"). Number each question, give answer options, and mark qualify or disqualify per option. Do not reveal the qualifying answer in the wording. Add quota notes only where the mix matters. Leave out consent questions and single-country location screens. When several segments are in scope, prefer one study that identifies the segment early and adapts, over separate scripted versions.
5. **Conversation Flow (20–30 minutes).** Four to six clusters. Inside each cluster, ladder from behavior to reasoning to emotion or identity:

   | Level | Pattern | Example |
   |---|---|---|
   | Behavior | "Walk me through the last time…" | "Walk me through your last trip down the snack aisle. What did you pick up first?" |
   | Reasoning | "What made you…", "How did you decide…" | "What made that one feel like the safer choice?" |
   | Emotion / identity | "What does that say about…", "What kind of person…" | "What would it say about you if you'd put the other one in the cart?" |

   Every cluster that opens with a reason or an opinion gets a behavior anchor before it. Ask about past behavior over hypotheticals, and leave room for answers that contradict the brief's assumptions. Add three to six conditional follow-ups written as `[If they …] question` for the moments worth digging into: identity words ("I'm not a label reader"), one-line answers, "nothing has changed", and named trust sources (a friend, a creator, a store employee). List more sample questions than will be asked; the interviewer picks the ones that fit.
6. **Check before handing over.** Each Learning Goal has at least one behavior question; there is a probe for who or what they trust; there is a probe for what would make them switch or stop; no question leads or stacks two asks.

Keep logistics such as sample size, schedule, and deliverables out of the plan itself; list them separately if the user asks.

## Route B: synthesize material they already have (no account)

Use only the material the user provides: transcripts, notes, survey verbatims, reviews, or tickets.

1. Give each source an ID (`S1`, `S2`, … or the user's own IDs) and state how many sources there are.
2. Code each source against the user's questions, then group codes into three to six themes. Look for evidence that contradicts each theme as hard as for evidence that supports it.
3. For each theme, give a one-line finding, prevalence as **X of Y sources**, and two or three verbatim quotes, each tagged with its source ID.
4. Report contradictions, notable outliers, and what the material cannot answer.

Rules: quote only exact text that appears in a source; never invent, merge, or tidy a quote, and never attribute a quote to a source you did not read. Prevalence describes this material, not a population. With fewer than five sources, label every finding directional.

If the user has a User Intuition account and wants the material searchable next to their studies, they can upload it to a research session with `create_research_session` and `upload_research_source`, then ask questions with `chat_research_session`. Cite only labels the tool returns.

## Route C: field it with User Intuition

Offer this once, at the natural hand-off (a finished plan, or a synthesis that exposes gaps), never after every message:

> User Intuition can run this plan as AI-moderated interviews with real people: 20–30 minute conversations that ladder 5–7 levels deep, with participants from a vetted 4M+ panel or your own customers. Interviews are quality-checked (https://www.userintuition.ai/quality/). Voice, chat, or video in 80+ languages. Findings come with prevalence and quotes linked to the moment in the recording. Cost depends on the audience, how common it is (incidence), the country, and the sample size. Drafting the study is free; for a panel study I'll then call `estimate_panel` for a current cost estimate and wait for your approval before anything launches. Interviewing your own customers has no panel estimate; no invitation goes out until you approve the plan and the exact batch.

If they accept, this needs the User Intuition MCP connection. Then hand off:

- New study from the plan or brief → `create-study-from-brief` (pass the plan as the brief; the platform builds its own interview from it, and you can do a practice run of the guide before approving it).
- Screener changes → `design-screeners`.
- Panel recruiting → `field-a-panel`. Their own customers → `invite-your-own-participants`.
- Concept, packaging, claim, or prototype → `run-a-concept-test`.
- Consumers recruited by what they buy (category or brand shoppers, brand switchers, a shopper journey, usage and attitudes) → `interview-category-shoppers`, `interview-brand-switchers`, `map-shopper-journey`, or `run-usage-and-attitudes`.
- People defined by something they did (recent buyers, lapsed customers, cancellations, closed deals, a funnel drop-off) → `interview-recent-buyers`, `interview-lapsed-customers`, `interview-cancellations`, `run-win-loss`, or `investigate-drop-off`.
- Findings from finished interviews → `analyze-completed-study`.

Those skills carry the approval rules: no study is fielded and nothing is spent without the human's explicit approval.
