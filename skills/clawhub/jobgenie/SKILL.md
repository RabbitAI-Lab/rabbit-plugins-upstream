---
name: "jobgenie"
description: "Researches employers, discovers where your skills align with their needs, and writes bespoke résumés and cover letters. No AI slop."
metadata:
  version: "1.0.1"
  openclaw:
    homepage: "https://github.com/RedRookAI/openclaw-skills/tree/main/skills/jobgenie"
---

# JobGenie: Tailored Job Applications at Scale

Your strongest qualification might be something you left off your résumé. JobGenie helps you uncover overlooked capabilities, builds a reusable skills matrix, and researches what each employer needs. It then writes a tailored résumé and cover letter showing how you can do the work, supported by your most relevant experience. Your answers and preferences carry forward, so every application draws on the full picture of what you bring.

A single OpenClaw owns all five rounds by default. Treat writing, review and correction as distinct rounds. When available, the user may choose a separate reviewer subagent, second OpenClaw or another model family for round 4; a second bot or provider is not required.

The letter shows: I see your work and am interested; I understand what you need; here is how I can help; here is brief closely relevant experience; I welcome an interview. Research the role, pay, daily work, current projects and needs with existing public tools. Match individual accomplishments to the actual work instead of telling whole job histories.

The applicant's supplied career facts are authoritative. Present their legitimate work confidently and impressively. Explicitly reject hedging, minimization, defensive credit disclaimers, gap apologies and career-transition narration. If something cannot be stated factually and confidently, leave that statement out and present the relevant facts positively without hedging. Preserve the underlying accomplishments; do not turn this into another claim check. No claim approval, compulsory supporting-example project/employer/metric, fixed example count or omission ledger. Respect the applicant's supplied disclosure preferences. Use relevant publications with the applicant's preferred standard identifiers and links, without automatically adding publication-status qualifiers. Do not automatically insert career length/article volume. Do not treat ordinary user-accepted paraphrases as defects. Describe implemented work; do not automatically carry product-development status qualifiers from private notes into employer-facing accomplishments.

Read and apply [the complete current method](references/five-round-workflow.md), [saved writing research](references/writing-methods.md), [current career sources](references/sources.md) and [existing runtime/document tools](references/runtime.md). The complete current method supersedes historical templates and broad capability-first selection. Preserve current holds and unrelated work.

Résumé-only current owner preferences: read [recent experience, relevant older work, publications and credentials](references/resume-preferences.md). The approved cover-letter method is unchanged.

Apply [core experience, automation and complementary résumé selection](references/resume-preferences.md) in rounds 2–5. Substantive current independent work is core experience. For applicants with automation capability, every application shows useful employer-specific automation in both documents; the résumé selects relevant proof per role and complements the letter without copying its prose.

## Build and maintain the user's career reference

Before a first application, or when the user wants to expand an incomplete record, read and follow [guided skills-matrix discovery](references/skills-matrix.md). Guide the conversation: ask useful questions, suggest related skills, software and team contributions, let the user accept/correct/reject them, and save the answers for reuse. Continue those rounds as useful; do not substitute a résumé import for that conversation or delay an application until every possible question is exhausted.

## Find suitable jobs

When the user wants opportunities, follow [job discovery](references/job-discovery.md): read their résumé, career reference, skills matrix and feedback; ask about missing search preferences; search current postings across relevant role families; and return a sourced shortlist explaining what they could do for each employer and the relevant supporting experience. Judge the actual day-to-day work rather than filtering on matching titles, degrees or keywords. Save findings and preferences for reuse. This precedes choosing an application and does not add a sixth writing round. A supplied job can go directly to the existing five rounds. One Claw handles discovery by default; optional named role assignments can include a scout.

## Optional role assignment

One Claw is the complete default. No setup question, second account or provider configuration is needed to use the skill. If the user wants to involve existing additional bots, accept an ordinary instruction such as "This bot writes; that bot reviews" and save those names in the user's preferences. Writer owns rounds 1, 2, 3 and 5; reviewer owns round 4. The user may also assign individual rounds. Use existing reachable agents/connections; do not require IDs, a new gateway or edits to server configuration. If the named reviewer is unavailable, explain that and offer to perform the review locally rather than silently claiming independent review. See [runtime guidance](references/runtime.md).

At the start of selection, drafting, review and correction, read the user's current career reference and feedback record. Supply their actual relevant contents to isolated workers. The [source and feedback guidance](references/sources.md) explains storage and updates.

## Execute the approved rounds

Read the [five-round method](references/five-round-workflow.md). When composing isolated task requests, use the corresponding [approved stage prompts](references/stage-prompts.md) and supply the required source contents. Round 3 receives the saved [writing research](references/writing-methods.md) and [formatting guide](references/formatting.md); round 4 also receives the full [Remove AI Slop guide](references/remove-ai-slop.md). The user's current presentation preferences and explicit rejection of hedging/minimization govern generic style advice. Apply that guide as editorial reference: its standalone output instructions and input marker do not replace JobGenie's consolidated review. Keep review and corrections separate.

Use [runtime and document guidance](references/runtime.md) for one-agent operation, optional separate review, available web tools, native file production and delivery. Use the user's configured models and existing tools. This skill does not configure providers, create automations or submit applications. Honor current task scope and any existing submission authorization or hold.

See [Sources](SOURCES.md) for the bundled research, its primary-source links and how it informs the application rounds.
