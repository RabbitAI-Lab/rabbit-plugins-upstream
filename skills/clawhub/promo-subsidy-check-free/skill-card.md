## Description:

A free deterministic checker for promotion subsidy reconciliation sheets that recalculates payable subsidies and differences, checks totals, detects duplicates and blanks, and cites source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Retail and e-commerce operators use this skill after promotion campaigns to check subsidy reconciliation tables for arithmetic errors, duplicate activity/SKU rows, and missing required fields. It is intended for local CLI review of copied or JSON-wrapped table text, not for validating promotion policy, sales truth, tax treatment, or withheld paid-tier checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may assume the free release validates activity caps, subsidy-above-price cases, negative values, or threshold-based differences.

Mitigation: Treat outputs as arithmetic, duplicate-row, and blank-field checks only; review the withheld checks manually or with a product tier that explicitly includes them.

Risk: A passing run can be misread as approval of the activity plan, sales data, tax treatment, or settlement policy.

Mitigation: Use the cited line findings as reconciliation support and separately verify policy, sales, returns, and tax assumptions against source documents.

Risk: Incomplete or unrecognized input can produce an insufficient-input result instead of findings.

Mitigation: Provide a table with the required headers and at least one detail row, and do not treat insufficient input as a no-issues conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/promo-subsidy-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable CLI text or JSON report with findings, line numbers, summaries, and omitted-check notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided table text; sample input is included in templates/sample.json.]

## Skill Version(s):

1.0.29 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
