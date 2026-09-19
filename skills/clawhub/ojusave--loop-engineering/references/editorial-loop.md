# Editorial and Anti-Slop Loop

## Contents

- [Outcome](#outcome)
- [First protect meaning](#first-protect-meaning)
- [Run the scanner](#run-the-scanner)
- [AI-slop failure classes](#ai-slop-failure-classes)
- [Simulated originality](#simulated-originality)
- [Optimization and marketing contamination](#optimization-and-marketing-contamination)
- [Em-dash rule](#em-dash-rule)
- [Cold editorial passes](#cold-editorial-passes)
- [Ending test](#ending-test)
- [Return criteria](#return-criteria)


## Outcome

Make the article sound specific, human, and intentional without changing its evidence or imitating another writer.

Inherit the parent audience, baseline, target reader effect, guardrails, and required evidence state. State the editorial defect and predicted reader-facing delta before revising.

This loop is a checker and editor, not the source of the thesis.

Editorial polish cannot create information value. When the artifact must earn attention, read the audience-value handoff before editing. If the handoff lacks a supported knowledge advantage or audience delta, return `REWORK_REQUIRED` to the parent instead of manufacturing novelty in prose.

## First protect meaning

Before editing, record:

- thesis
- load-bearing facts
- qualified claims
- author-specific observations
- intended tone
- explicit punctuation or style rules
- commodity baseline, supported knowledge advantage, and audience delta when applicable

Do not improve fluency by making claims stronger than the evidence.

## Run the scanner

When the draft is local:

```bash
python <skill-directory>/scripts/check_blog_slop.py <draft>
```

Treat findings as prompts for judgment, not automatic replacements.

## AI-slop failure classes

### Generic framing

Flag:

- broad trend openings
- `in today's world`
- `the future is here`
- `technology is evolving rapidly`
- universal audience claims
- introductions that could fit any topic

Replace with a specific observation, mechanism, scene, result, or tension.

Do not confuse specific nouns with specific value. A paragraph can mention traces, telemetry, failures, scale, or a well-known company and still make only commodity claims. Strip biography and branded nouns during a cold pass and verify that a supported takeaway remains.

### Simulated originality

Flag:

- newly coined terms with no distinct measurement, method, or evidence behind them
- proprietary-sounding frameworks invented during editing
- claims of privileged visibility without a described observation or deliverable
- biography used as a substitute for a finding
- suspense around a result the underlying work has not established
- provocative titles whose tension is absent from the body

Route these failures back to research, strategy, the audience-value loop, or the author. Do not repair them with stronger adjectives.

### Synthetic profundity

Flag:

- repeated `not X, but Y`
- `more than just`
- declarations that something changes everything without a mechanism
- abstract claims written as revelations

Ask whether the sentence changes the reader's model. Delete it when it does not.

### Canned structure

Flag:

- identical paragraph lengths
- a heading every few paragraphs
- repeated three-item lists
- excessive bullets
- predictable `problem, solution, future` scaffolding
- conclusions that simply repeat the introduction

Restructure around argument and pacing.

### Unsupported authority

Flag:

- `developers want`
- `the industry knows`
- `everyone is moving`
- invented consensus
- unsourced inevitability
- fake personal experience

Scope, source, or remove the claim.

### Vocabulary and punctuation

Flag overuse of:

- delve
- unlock
- game-changer
- seamless
- robust without a named property
- leverage as vague business language
- transformative
- paradigm shift
- navigate the landscape
- em dashes

Do not blindly ban ordinary words. Fix the sentence when the word hides missing specificity.

### Thought-leader imitation

Flag:

- borrowed catchphrases
- copied cadence
- signature rhetorical structures
- fake founder certainty
- imitation of swyx, Theo, Garry Tan, or another named writer

Restore the author's own language and evidence.

## Optimization and marketing contamination

Flag prose that appears shaped primarily for ranking, extraction, lead generation, or vendor positioning rather than reader understanding:

- paragraphs that exist only to cover a keyword or query variant
- unnatural question headings followed by generic answers
- definitions repeated with slightly different wording
- unsupported `best`, `leading`, `widely adopted`, or `industry standard` claims
- vendor claims rewritten in a neutral editorial voice
- affiliate-style comparisons without common test conditions
- citations included for authority theater rather than support
- current-year labels attached to materially old advice
- promotional calls to action disguised as conclusions
- content padded to a target length
- machine-scannable structure that harms human pacing

When SEO, AEO, or GEO is an explicit goal, preserve useful headings, crawlability, clear answers, and accurate structured information only when they also help the reader. Do not weaken the argument to satisfy speculative engine tactics.

## Em-dash rule

When the user says no em dashes, the final draft must contain zero Unicode em dash characters and zero spaced double-hyphen substitutes used as em dashes.

When no rule is stated, report the count and reduce repeated use. Prefer periods, commas, parentheses, colons, or rewritten sentences.

## Cold editorial passes

Perform separate passes:

1. Thesis and logic
2. Evidence and qualification
3. Specificity and examples
4. Structure and pacing
5. Voice and sentence rhythm
6. Punctuation and formatting
7. Ending
8. Commodity-baseline and audience-delta preservation when applicable

Do not perform all checks as one vague `polish` pass.

## Ending test

The ending should do one of:

- reveal the larger consequence
- return to the opening with changed meaning
- make the reader's next responsibility clear
- state the durable implication

It should not:

- summarize every section
- add a motivational slogan
- introduce an unsupported prediction
- end with `the choice is ours`

## Return criteria

Return `PASS` when no material slop pattern remains, style rules pass, the prose is specific, factual meaning is preserved, and any required audience delta remains legible and supported.

Editorial checks support `ARTIFACT VERIFIED`. Report `OUTCOME VALIDATED` only when representative readers demonstrate the contracted comprehension, belief, or action; otherwise preserve the validation gap.

Return `REWORK_REQUIRED` with line-level findings when argument or voice still fails, or when polished prose is carrying a commodity argument with no supported audience delta.
Return `BLOCKED` when the editor lacks the full draft or source evidence needed to protect meaning.
Return `NEEDS_HUMAN_JUDGMENT` when voice alternatives are both defensible.
