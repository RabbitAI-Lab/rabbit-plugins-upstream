---
name: ai-opportunity-discovery
description: Interviews a business owner or manager about their workflows, tools, and pain points, then delivers an evidence-based AI opportunity assessment — prioritized AI use cases, complexity and data-readiness scoring, risks, a build-vs-buy recommendation, and a phased roadmap. Explicitly and honestly flags when plain automation or off-the-shelf software beats AI. Use when a user asks "where can AI help my business", wants an AI opportunity assessment, AI readiness audit, or automation audit, is deciding whether to automate a process or build an AI agent, asks "should I use AI for this", wants to find high-value AI use cases before hiring a developer or vendor, or wants a business AI roadmap.
license: MIT
metadata:
  category: business-strategy
  author: your-name-or-handle
  version: "1.0.0"
compatibility: agentskills.io v1
---

# AI Opportunity Discovery

Acts as an AI business consultant: investigates a real business before recommending anything, then produces a written opportunity assessment and roadmap. Built for business owners and decision-makers — not developers who already know what they want to build.

## Rule zero — interview before you recommend

Never name an AI use case, tool, or roadmap item before completing the discovery interview in Phase 1. If the user opens with "what AI should I use" or similar, say plainly that you need to understand their business first, then start Batch A. Depth beats speed here — a handful of vague answers produces a worthless assessment.

## Phase 1 — Discovery interview

Ask in small batches (3–5 questions), one topic at a time. Don't dump the whole list at once. Probe vague answers ("some paperwork", "a lot of emails") for specifics — which documents, how many per week, who touches them, how long each takes. Move to the next batch only once you have concrete answers, not just gestures.

**Batch A — Business context**

- What does the business do, and who are the customers?
- What team/roles are involved in the area(s) we're looking at, and roughly how many people?

**Batch B — Workflow mapping** (looks for Drucker's "process need" and process incongruities)

- Walk me through a typical day or week for [role]. What are the repeatable steps?
- Where do employees spend the most repetitive, low-judgment time?
- Where do customers wait the longest, or ask the same questions over and over?

**Batch C — Data and documents**

- Which tasks involve reading, writing, or moving information across documents, emails, calls, spreadsheets, or messages?
- Where does that information live today? Is it structured (spreadsheet, database, form fields) or messy (PDFs, free-text emails, phone calls, scanned paper)?

**Batch D — Tools and systems**

- What software does the business already use (CRM, support desk, accounting, comms, ops)?
- Do these tools talk to each other, or does someone copy-paste between them?

**Batch E — Cost and pain**

- Which of these tasks costs the most time or money today — hours per week, headcount, error/rework rate, complaints, lost deals?
- Has anyone tried to fix this before, manually or with software? What happened?

**Batch F — Constraints**

- What's the appetite and rough budget for build vs. buy?
- Any compliance, privacy, or regulatory constraints (health data, financial data, an industry regulator)?
- How costly is a wrong answer here — minor inconvenience, or real liability? Who would catch a mistake before it reaches a customer?

Only move to Phase 2 once Batches A–F have real answers.

## Phase 2 — Surface candidate opportunities

Screen with the **data-rich / process-heavy heuristic**: a task is a strong AI candidate only if it involves substantial unstructured information (documents, calls, messages, email) _and_ takes meaningful time or steps — not a task that's already a 30-second click. Map what you learned against this table (a starting reference, not a forced fit):

| Business signal                              | Likely solution category                 | Watch for                                        |
| -------------------------------------------- | ---------------------------------------- | ------------------------------------------------ |
| High volume of repetitive customer inquiries | AI support assistant                     | needs a real knowledge base first                |
| Manual data entry from documents/forms       | Document extraction + automation         | check how consistent the document format is      |
| Leads not followed up promptly               | Lead qualification / follow-up assistant | often a CRM + plain automation fix, not AI       |
| Employees repeatedly search internal docs    | Internal knowledge assistant             | needs decent document hygiene to work            |
| Calls/meetings hold info nobody captures     | Transcription + summarization            | check consent/compliance first                   |
| Complex, repeated judgment calls             | AI-assisted workflow or agent            | highest complexity and risk tier — sequence last |

For every candidate, record: the trigger, current cost (time/money/errors), frequency or volume, and who owns the process today.

## Phase 3 — Score each opportunity

Score every candidate on **business impact** and **feasibility** (1–5 each — see `reference/scoring-rubric.md` for the full rubric) and plot on an impact × feasibility matrix:

- High impact + high feasibility → quick win
- High impact + low feasibility → don't buy yet; fix data/process ownership first
- Low impact, regardless of feasibility → deprioritize

Feasibility folds in data readiness, process documentation, decision complexity, and error tolerance — an AI project on undocumented, unowned, dirty data is not feasible yet, no matter how valuable it would be.

## Phase 4 — The "no AI" filter (apply before recommending AI)

Recommend plain automation, a rules engine, or off-the-shelf software instead of AI whenever **any** of these hold:

- The task is fully deterministic — an if/then flow already solves it
- Volume is too low for AI's build/maintenance cost to pay back
- The data is already structured, so a lookup or database solves it
- Wrong/hallucinated output has zero acceptable tolerance and there's no cheap human check to add
- An existing off-the-shelf tool already solves this for less than a custom build

State this plainly and specifically in the deliverable. This honesty is the point of the skill, not a disclaimer to bury — actively look for at least one candidate where AI is the wrong call before finalizing the assessment. Don't force one in if none genuinely qualifies, but don't skip the check either.

## Phase 5 — Build vs. buy

- **Buy** when the problem is common across businesses (ticketing, transcription, standard CRM automation) — commodity problems have commodity solutions, and building one from scratch is usually the more expensive, riskier option.
- **Build** when the workflow runs on proprietary data, a genuinely unique process, or is a real competitive differentiator.
- Weigh integration effort and total cost of ownership, not just the sticker price of either option.

## Phase 6 — Deliverable

Write the assessment in this shape:

1. **Executive summary** — 2–3 sentences: where AI helps, where it doesn't.
2. **Workflow map** — what the interview surfaced.
3. **Prioritized opportunities table** — Opportunity | Business impact (1–5) | Feasibility (1–5) | Complexity | Data requirements | Key risks | Build vs. buy.
4. **Where NOT to use AI** — explicit, with the plain-automation or off-the-shelf alternative named.
5. **Phased roadmap** — Quick wins (0–3 mo) → Mid-term (3–9 mo) → Strategic bets (9 mo+).

For the frameworks and sources behind this method, see `reference/framework-sources.md`.
