## Description:

Compares multiple bidders' quotation line items side by side, identifies missing or extra items, and ranks bidder totals for bid review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, bid evaluation, and bid-clearing reviewers use this skill to align multiple bidders' quotation items, compare quantities, unit prices and amounts, identify missing or extra items, and review total rankings before human evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid quotation files may contain confidential procurement or pricing data.

Mitigation: Run the skill only in a trusted local agent environment and verify that unrelated shell commands and outbound network access are controlled before processing sensitive files.

Risk: The skill provides mechanical bid comparisons and does not decide winners, assess collusion, or cover checks outside the free-version scope.

Mitigation: Use the output as review support only; have qualified evaluators verify findings and perform any required legal, compliance, arithmetic, or collusion analysis separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bid-comparison-free)

## Skill Output:

**Output Type(s):** [text, json, analysis]

**Output Format:** [Plain text or JSON comparison report with findings, item-level comparisons, and bidder totals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on user-provided bid quotation data and may return insufficient-input status instead of conclusions when fewer than two bidders or too few line items are provided.]

## Skill Version(s):

1.0.46 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
