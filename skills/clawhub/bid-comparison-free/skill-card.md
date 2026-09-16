## Description:

Compares multiple bidders' quotation line items side by side, producing an aligned comparison table, missing or extra item checks, and bidder total rankings without payment, registration, API keys, model calls, or network use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bid evaluation, and operations users can run this skill to align quotations from at least two bidders, identify missing or extra line items, and compare bidder totals before deeper review. It is a local comparison aid and does not decide contract awards, determine bid reasonableness, or make collusion findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free workflow includes upsell instructions that ask an agent to run an unpinned external installer and continue into a paid-skill flow.

Mitigation: Do not paste or execute the upgrade prompt unless the payment installer, publisher, and paid skill have been independently verified; run any purchase or installer flow in a restricted environment and require user confirmation for payment.

Risk: Bid data may be sensitive even when processed locally.

Mitigation: Run the local comparison only in an environment approved for the bid materials and avoid providing data the operator is not authorized to process.

Risk: Human-readable output includes promotional upgrade text alongside comparison results.

Mitigation: Use --json when downstream systems need structured comparison results without the human-readable upsell text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bid-comparison-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable terminal text or JSON when run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local bid-comparison results with aligned item tables, missing-item findings, totals, rankings, and explicit withheld-check scope.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
