# Research Loop

## Outcome

Reduce uncertainty enough to answer the contracted question or support the named decision, while distinguishing fact, interpretation, inference, forecast, and uncertainty.

Read `source-integrity.md` for every task involving market claims, comparisons, recommendations, vendor claims, SEO, AEO, GEO, affiliate content, public relations, or marketing material.

## Design the evidence plan per task

Do not begin with a fixed list of websites or a generic research checklist.

Record:

- outcome owner, baseline uncertainty, named decision, and decision threshold
- decision or question
- audience and intended use
- scope and exclusions
- freshness requirement
- claims that would change the decision
- what a competent generalist could already conclude from common knowledge and the supplied public context
- internal, firsthand, experimental, or artifact-based evidence the author may uniquely control
- source types capable of answering each claim
- commercial or advocacy incentives likely to shape the available content
- acceptable evidence and verification paths
- source and time constraints

Do not broaden a narrow question into a generic survey.

For research that will support a talk, article, launch narrative, recommendation, or other audience-facing argument, distinguish two jobs:

1. **Verification:** determine what is true, false, qualified, or unresolved.
2. **Knowledge advantage:** determine what the author can contribute beyond the commodity baseline through original evidence, firsthand experience, reproducible work, consequential judgment, or a defensible synthesis.

External searching cannot manufacture the second job. If the needed value depends on internal telemetry, lived experience, an experiment, or an organizational decision, name the missing input and return it to the parent instead of filling the gap with general research.

## Source priority

Prefer, in order when they fit the claim:

1. Primary records: official documentation, source code, standards, filings, datasets, current policies, full talks, papers
2. Reproducible observation or direct testing
3. High-quality independent analysis with transparent method
4. Direct practitioner evidence with clear context and limitations
5. Vendor, marketing, affiliate, PR, SEO, AEO, or GEO content for discovery or for documenting the publisher's own claim
6. Secondary summaries for discovery only

The order is not absolute. A vendor's official documentation may be the strongest source for a current API, but the same vendor's case study is not independent proof of comparative superiority.

For current technical claims, verify official docs, release notes, repository state, compatibility, and dates.

For contested claims, seek credible evidence for the strongest opposing view.

## Search-result skepticism

Search ranking and answer-engine citation are not evidence of correctness.

- Open the source rather than relying on a snippet or generated summary.
- Trace repeated statistics to the original dataset or report.
- Do not count syndicated copies or pages repeating the same press release as independent confirmation.
- Inspect whether cited material actually supports the claim.
- Search for counterevidence, failures, and boundary conditions.
- Treat a recently refreshed date as weak unless the substance is also current.
- Treat confident answer-first prose, FAQs, and structured summaries as presentation, not proof.

## Claim ledger

Maintain a compact ledger:

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
Confidence:
Contradicting evidence:
Decision impact:
Status: supported | qualified | rejected | unresolved
```

Do not copy large passages into state. Record citations and concise findings.

When using a JSON claim ledger, validate field completeness with:

```bash
python <skill-directory>/scripts/validate_claim_ledger.py <ledger.json>
```

The script verifies provenance fields, not truth or source quality.

## Cycle

1. Identify the highest-impact unresolved claim.
2. Select the source type most capable of resolving it.
3. Inspect the best current source available.
4. Audit provenance, incentive, method, date, and independence.
5. Update the claim ledger.
6. Search for contradiction or boundary conditions.
7. Decide whether another pass could change the conclusion.

Avoid collecting sources after the decision is stable merely to make the bibliography longer.

## Freshness

Classify evidence as:

- current and directly applicable
- current but indirect
- historically useful
- outdated for the decision

Do not use old benchmarks, library versions, pricing, APIs, laws, policies, schedules, product capabilities, or office holders as current evidence.

When a historical source is foundational, pair it with current evidence showing whether the mechanism still applies.

## Marketing and optimization content

Do not automatically discard marketing, SEO, AEO, or GEO material. Use it for the purpose it can support.

Valid uses include:

- learning what a vendor claims
- identifying terminology and narratives
- finding a primary source to inspect
- documenting current official pricing, features, or positioning

Do not use it alone to establish:

- unbiased superiority
- broad adoption
- customer outcomes
- market consensus
- effectiveness of the author's own optimization service

If only incentive-shaped sources are available, qualify the conclusion and state the limitation.

## Synthesis

A useful synthesis should state:

- strongest supported conclusion
- mechanism or reasoning
- key evidence
- source incentive and independence concerns
- strongest counterevidence
- uncertainty
- what would change the conclusion
- what the evidence adds beyond the commodity baseline when the output must earn attention
- which findings depend on author-controlled evidence or disclosure approval

Do not flatten disagreement into false consensus or repeat marketing language as neutral fact.

## Return criteria

Return `PASS` and `DECISION READY` when the claims needed for the assignment are supported or responsibly qualified, source incentives are visible, repeated claims have been traced, additional searching is unlikely to change the decision, and the named owner can act within the stated uncertainty. When the output must earn attention, the packet must also identify a supported knowledge advantage or state explicitly that the required author-controlled evidence is unavailable.

Return `REWORK_REQUIRED` when a load-bearing claim lacks appropriate evidence or relies on uncorroborated incentive-shaped content.
Return `BLOCKED` when the necessary source or data is unavailable.
Return `NEEDS_HUMAN_JUDGMENT` when evidence supports multiple choices with different values or risk tradeoffs.
