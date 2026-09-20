# Source Integrity and Incentive Audit

## Purpose

Prevent research, strategy, and writing from treating highly ranked, highly quotable, or commercially optimized content as neutral evidence.

Inherit the parent decision, baseline uncertainty, claim threshold, guardrails, and required evidence state. The purpose is to reduce decision-relevant uncertainty, not to maximize the number of sources.

SEO, AEO, GEO, public relations, affiliate publishing, demand generation, and vendor thought leadership can all shape what is easy to find. Optimization does not make a source false, but it changes the questions that must be asked before relying on it.

## Terms

Use these meanings unless the task defines them differently:

- **SEO:** optimization for discovery and ranking in conventional search systems
- **AEO:** optimization for direct-answer and answer-engine visibility
- **GEO:** generative engine optimization, usually meaning visibility or citation in AI-generated answers

These practices and labels change quickly. Verify current guidance rather than relying on remembered tactics.

## Core rule

Search visibility is evidence of discoverability, not truth.

Citation by an answer engine is evidence that a system selected a source, not that the source is independent, current, or correct.

Do not let answer-shaped prose, structured FAQs, confident language, citations, or a recent date substitute for source verification.

## Classify source purpose

For every load-bearing source, classify its likely purpose:

- primary record or authoritative specification
- independent reporting or analysis
- academic research
- practitioner experience
- first-party operational evidence, internal telemetry, experiments, or artifacts
- vendor documentation
- vendor marketing or thought leadership
- public relations or sponsored content
- affiliate or comparison content
- community discussion or user-generated content
- SEO, AEO, or GEO guidance selling services or tools
- synthetic or unattributed summary

A source may belong to more than one class.

## Audit the incentive

Record, when material:

- author and publisher
- publication and update date
- ownership or commercial relationship
- sponsor, affiliate, referral, or lead-generation incentives
- product or service being sold
- intended audience and desired conversion
- whether the source reports original evidence
- methodology and sample
- citations and whether they support the claim
- corrections, version history, or disclosure
- independence from other sources used
- signs of date refreshing without substantive updates

Do not infer hidden motives. Record observable incentives and their effect on evidentiary weight.

## Valid uses of marketing content

Marketing content can be primary evidence for:

- what a company claims
- how a product is positioned
- current documented features, pricing, support, or policy when published officially
- the language a market uses
- the existence of a campaign or narrative

It is weak evidence for:

- comparative superiority
- adoption or market consensus
- product reliability
- customer outcomes
- unbiased recommendations
- the effectiveness of the author's own SEO, AEO, GEO, or marketing method

Corroborate these claims independently or qualify them as vendor claims.

## First-party operational evidence

First-party operational evidence can be the strongest source for what the author or organization directly observed. Treat it as privileged but incentive-shaped evidence: record collection method, scope, sample, missing populations, aggregation, disclosure limits, and whether an outside reader could reproduce or independently inspect any part of it. Do not discard it merely because it is not independent, and do not generalize it beyond the population it can support.

## Optimization-shaped content risks

Treat these as prompts for closer review, not automatic rejection:

- broad `best` or comparison pages tied to affiliate revenue
- exact-match headings repeated across many sites
- answer-first paragraphs that make unsupported certainty easy to quote
- large FAQ sections created for coverage rather than reader need
- statistics repeated without the original dataset
- citations that point to another summary instead of the primary source
- authoritative language without method or domain expertise
- new publication dates on materially old content
- claims about secret ranking or answer-engine factors
- special files, markup, or hacks presented as mandatory without official support
- benchmark charts produced by the vendor being evaluated
- earned-media claims that trace back to the same press release

## Evidence plan

Before searching, define which source types could actually answer the question.

Examples:

- framework capability: current official docs, source repository, release notes, reproducible test
- product reliability: status history, incident record, independent measurement, direct test
- market size: primary dataset, filing, audited report, transparent methodology
- user behavior: direct research, disclosed survey method, telemetry, or carefully scoped qualitative evidence
- policy or law: official authority and current text
- comparative claim: common test conditions, independent benchmark, or reproducible evaluation
- marketing trend: campaign evidence plus independent data on actual behavior

Do not let the search results page choose the evidence standard for you.

## Claim ledger additions

For each load-bearing claim, include:

```text
Claim:
Type: fact | interpretation | inference | forecast
Evidence:
Source date:
Source class:
Commercial or advocacy incentive:
Independence from other evidence:
Optimization risk: low | medium | high
Verification path:
Contradicting evidence:
Confidence:
Status: supported | qualified | rejected | unresolved
```

## Triangulation rules

- Trace repeated statistics to the earliest available source.
- Do not count syndicated copies or sources repeating the same press release as independent confirmation.
- For high-impact claims, seek evidence with different incentives or collection methods.
- Compare a vendor claim with documentation, observed behavior, customer evidence, or independent analysis.
- Open and inspect cited sources. Do not rely on snippets, AI summaries, or citation presence alone.
- Search for counterevidence and failure cases, not only confirmation.
- If all available sources share the same incentive, say so and lower confidence.

## SEO, AEO, and GEO as an output goal

When the user explicitly wants discoverability optimization:

1. Finish the people-first argument or utility first.
2. Preserve factual meaning, reader value, voice, and accessibility.
3. Apply current technical discovery practices only after verifying official guidance.
4. Keep optimization suggestions separate from claims about content quality.
5. Reject keyword stuffing, fake questions, redundant definitions, inflated length, hidden text, citation decoration, and date manipulation.
6. Do not promise rankings, inclusion, citations, or answer-engine visibility.
7. Label experimental or engine-specific tactics as uncertain.

For Google Search AI features, current official guidance says normal SEO fundamentals and people-first content remain relevant, with no special AI markup or additional technical requirements. Recheck the current official guidance at execution time because this may change.

## Research return criteria

A source packet is not ready when it only contains popular or optimized pages.

Return `PASS` only when load-bearing claims are supported by appropriately current evidence, commercial incentives are visible, repeated claims have been traced, and meaningful counterevidence has been considered.

Report `DECISION READY` only when this evidence is sufficient for the named owner and next decision. Otherwise report the strongest supported evidence state and the unresolved claim or source gap.
