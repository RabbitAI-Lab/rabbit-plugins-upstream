---
name: prd-creator
description: Creates production-grade, internationally-standardized Product Requirements Documents (PRDs) for full-stack web/mobile projects, plus an execution-ready task breakdown so a coding agent (Claude Code, opencode CLI, etc.) can implement directly from it. Synthesizes ISO/IEC/IEEE 29148:2018, IEEE 830, Amazon's Working Backwards PR/FAQ, and Big Tech PRD conventions into one rigorous English .md deliverable. Use whenever the user asks to write/draft a PRD, product spec, SRS, feature spec, implementation plan, or "dokumen requirement/spesifikasi produk" — for any web, mobile, or full-stack system, even from a one-sentence idea. Also trigger to formalize an existing idea/backlog item into a proper requirements document, for a PRD "standar internasional"/"lengkap"/"seperti dibuat expert", or to prepare a project brief before handing off to Claude Code/opencode. Do NOT trigger for quick one-off feature descriptions the user wants kept short and informal.
---

# PRD Creator

A skill for producing rigorous, internationally-standardized Product Requirements Documents for full-stack web and mobile projects. The output must read like it was produced by a senior product/requirements engineer who has internalized ISO/IEC/IEEE 29148, not a generic template-filler.

## Why this structure

Real PRDs at mature organizations blend three traditions, and this skill deliberately merges all three rather than picking one:

1. **Formal requirements engineering** — ISO/IEC/IEEE 29148:2018 (the current international standard for requirements engineering, successor to IEEE 830-1998) gives us traceable, verifiable, uniquely-identified requirements written in unambiguous "shall" language.
2. **Narrative product framing** — Amazon's Working Backwards PR/FAQ gives us a customer-first narrative that forces clarity on *why* before *what*, and surfaces the hard questions (risks, alternatives, failure modes) early.
3. **Big Tech product-team conventions** (Google/Meta-style PRDs) give us the practical scaffolding product and engineering teams actually expect: goals/metrics, personas, scope boundaries, rollout plans, analytics.

Skipping any one of these produces a PRD that's either bureaucratically formal but disconnected from user value, or inspiring but untestable by engineers and QA. Full sourcing is listed at the bottom of this file — always keep the citation habit when the user asks where a framework comes from.

## When to go deep vs. lightweight

Not every request needs the full 20-section document. Calibrate honestly:

- **Full PRD** (default for this skill, since it was explicitly requested to be comprehensive/production-grade): use the complete structure in `references/prd-master-template.md`.
- **Feature-level addendum**: if the user is adding a feature to an *existing* product (not a new product), skip Sections 1–3 (vision/market framing) and start from Section 4 (Requirements) — but still ask whether a parent PRD exists to link to.
- Never silently downgrade to a lightweight version when the user asked for "international standard", "lengkap", "detail", or "production-grade" — that is an explicit signal to use the full template.

## Process

### Step 1 — Clarify before drafting (always)

Never start writing a full PRD from a one-line idea. Ask clarifying questions first — this is non-negotiable for this skill, independent of any other instruction. Prioritize (ask only what's not already inferable from context):

1. **Product type & platform target** — web only, mobile only (iOS/Android/both), or full-stack (web + mobile sharing a backend)?
2. **Stage** — greenfield (new product, needs vision/market framing) or feature addition to an existing system (needs less narrative, more precise scoping against existing architecture)?
3. **Primary users/personas** — who exactly will use this, and what's the core job-to-be-done?
4. **Constraints** — team size, timeline, tech stack already decided (or should this skill assume the user's known stack: Next.js App Router / Laravel 12 / TypeScript / Prisma-PostgreSQL for web, Flutter/Riverpod for mobile — ask, don't assume silently), budget/hosting limits (e.g. self-hosted, resource-constrained hardware), and any compliance requirements (data privacy, accessibility, industry regulation).
5. **Success definition** — what metric or outcome defines this as shipped-and-working, not just shipped?
6. **Downstream use** — will this PRD be handed to a coding agent (Claude Code, opencode CLI, etc.) right after? If so, default to also producing the execution-ready task breakdown (Step 5) in the same pass, since that's this skill's primary use case — don't make the user ask for it separately unless they say they only want the PRD itself.

Use `ask_user_input_v0`-style short questions (or the plain equivalent if that tool isn't available in this environment) rather than a giant intake form. Batch 2–3 questions at a time. If the user has clearly already answered some of this in their prompt or in prior conversation/memory, do not re-ask — state the assumption instead and move on.

### Step 2 — Pick the scope and load the template

Read `references/prd-master-template.md`. It contains the full section-by-section structure with guidance on what goes in each section, tailored with explicit web AND mobile sub-sections (browser/OS support matrices, offline behavior, push notifications, app store compliance, responsive breakpoints, API contracts). Use only the sub-sections relevant to the platform target confirmed in Step 1 (e.g. omit "App Store Compliance" entirely for a web-only product — don't leave it as an empty stub).

### Step 3 — Write requirements the correct way

Read `references/requirement-writing-standards.md` before writing the Functional/Non-Functional Requirements sections. This governs:
- Unique requirement IDs (REQ-F-001, REQ-NF-001, etc.) for traceability, per ISO/IEC/IEEE 29148.
- RFC 2119 keyword discipline (MUST/SHOULD/MAY) so priority is unambiguous in the sentence itself, not just in a separate priority column.
- EARS syntax (Easy Approach to Requirements Syntax) for conditional/triggered requirements.
- Acceptance criteria in Given–When–Then form for every user-facing requirement.
- MoSCoW and RICE for prioritization; INVEST for any user-story-shaped requirements.

Do not skip straight to prose feature descriptions — every functional requirement in the final document must be independently testable and traceable to a requirement ID.

### Step 4 — Draft, section by section

For documents this long, don't try to generate the whole thing in one pass:
1. Draft the Executive Summary / PR-FAQ narrative first and confirm it captures the user's intent — this is the cheapest place to catch a wrong direction.
2. Then draft Goals & Success Metrics, Personas, and Scope (in/out) — confirm scope boundaries explicitly, since scope creep is the single most common PRD failure mode.
3. Then draft the full Requirements section (functional + non-functional) using the standards from Step 3.
4. Then fill in the remaining sections (architecture overview, data model, platform-specific requirements, rollout, risks, testing, appendix).
5. Run the Definition-of-Ready checklist in `references/requirement-writing-standards.md` before presenting the final document — a PRD with unresolved "Open Questions" left silently unaddressed is not done.

### Step 5 — Task breakdown (default: on, unless the user only wants the PRD)

Read `references/task-breakdown-guide.md`. This turns the PRD's `REQ-F-###` / `REQ-NF-###` requirements into a sequenced, dependency-aware task list that a coding agent can execute directly — this is the actual handoff artifact into Claude Code / opencode CLI, so treat it as a first-class output, not an afterthought.

Key points (full detail in the guide):
- Every task links back to the REQ-ID(s) and AC-ID(s) it implements — a coding agent should never have to re-derive intent from scratch.
- Tasks are grouped into phases (e.g. Foundation/Schema → Core Features → Non-Functional Hardening → Polish) and ordered so dependencies resolve before dependents.
- Each task states its scope tightly enough to be a single agent turn/session (roughly: one feature slice, not "build the backend").
- This file is deliberately tool-agnostic — it works the same whether the user runs it through Claude Code, opencode CLI, or does it manually. Don't invent Alya/HEARTBEAT-specific IDs (HB-###) unless the user explicitly says this project uses that convention; default to a plain `TASK-###` scheme.

### Step 6 — Output

- **Output location**: save both files inside `.project/prd/` at the project root (create the folder if it doesn't exist). This keeps PRD/task artifacts out of the way of source code and out of version control by default — remind the user once (not every time) to add `.project/` to `.gitignore` if it isn't already there, since these documents may contain product/business context not meant for a public repo history.
- **PRD file**: `.project/prd/PRD-[product-or-feature-slug]-v[version].md`, **written entirely in English**, regardless of the language used in conversation.
- **Task breakdown file** (when produced): `.project/prd/TASKS-[product-or-feature-slug]-v[version].md`, in English, cross-referencing the PRD above by filename in its header.
- Include a Document Control table at the top of the PRD (version, author, date, status, reviewers) — version starts at `0.1 (Draft)`.
- Use real Markdown structure (H1/H2/H3, tables for requirements, checkboxes for tasks/acceptance criteria) — these are documents meant to be read in GitHub/Notion/an editor or fed to a CLI agent, not just pasted into chat.
- Save both files and present them as downloadable artifacts rather than pasting the whole content inline in chat, once the user has confirmed the drafted outline/summary is on the right track.

## Sources for the frameworks synthesized in this skill

- ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes — Requirements engineering* — https://standards.ieee.org/standard/29148-2018.html
- IEEE 830-1998, *IEEE Recommended Practice for Software Requirements Specifications* (superseded by, but still widely referenced alongside, ISO/IEC/IEEE 29148) — https://ieeexplore.ieee.org/document/720574
- Amazon Working Backwards / PR-FAQ process — https://workingbackwards.com/resources/working-backwards-pr-faq/
- RFC 2119, *Key words for use in RFCs to Indicate Requirement Levels* — https://www.rfc-editor.org/rfc/rfc2119
- EARS (Easy Approach to Requirements Syntax), Rolls-Royce/Alistair Mavin et al., IEEE RE Conference 2009 — commonly summarized at https://alistairmavin.com/ears/
- INVEST criteria for user stories, Bill Wake — https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/
- MoSCoW prioritization, DSDM Consortium — https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html

When drafting, cite these (or equivalent authoritative sources found via web search, if these links go stale) if the user asks why the PRD is structured the way it is.
