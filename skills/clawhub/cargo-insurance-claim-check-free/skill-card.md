## Description:

A free deterministic checker for cargo insurance ledgers that recalculates premiums, payable claims, claim gaps, insured ratios, duplicate policy numbers, missing fields, negative amounts, and total rows with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business, finance, logistics, freight-forwarding, and trade-operations users can use this skill during monthly insurance reconciliation or cargo-loss claim review to recalculate ledger arithmetic and identify rows that need correction or follow-up. It is a local arithmetic and consistency checker, not an insurance coverage, legal, or policy-interpretation tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The normal output path includes upsell prompts and points users toward an unpinned external paid-install flow.

Mitigation: Use --json for machine-readable local checking, and avoid running the unpinned installer or authorizing purchases unless the payment source and package version have been independently verified.

Risk: The free version omits higher-order claim determinations such as underpayment, denied-claim review, duplicate cargo insurance, underinsurance, and a claim action list.

Mitigation: Treat results as ledger arithmetic and consistency checks only; review checks_not_run and out-of-scope items before relying on the result for claim handling.

Risk: The tool does not decide whether policy terms apply, whether a loss should be covered, or whether rates, deductibles, and insured ratios are commercially reasonable.

Mitigation: Use qualified insurance, legal, or finance review for coverage and policy decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cargo-insurance-claim-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Public paid-version information](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Shell commands]

**Output Format:** [Human-readable CLI text by default, or structured JSON when run with --json.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing-field guidance and no conclusion.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
