## Description:

Reviews environmental protection tax filing worksheets by recalculating pollution-equivalent counts, tax amounts, post-reduction tax, totals, duplicate rows, and missing or negative fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and tax staff use this skill before environmental protection tax filing to check copied worksheet rows for arithmetic errors, missing required values, duplicate pollutant rows, and total-line mismatches. It uses values supplied by the worksheet and does not select tax rates, pollution-equivalent values, or exemption policy positions for the user.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The free checker repeatedly promotes a paid upgrade path that includes unpinned remote code execution and purchase/install instructions.

Mitigation: Use the free local checker without starting the upgrade flow unless the source, package version, and payment details have been separately verified at that moment.

Risk: The skill recalculates worksheet arithmetic but does not choose local tax rates, pollution-equivalent values, exemption positions, or verify the truth of emissions data.

Mitigation: Treat results as worksheet checks only and have a qualified tax or compliance reviewer confirm policy choices and source data before filing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/environmental-tax-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade public entry](https://skillpay.alipay.com/public/tokendidi)
- [Paid upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Human-readable Markdown or JSON containing worksheet findings, summaries, omitted checks, and source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are based on user-provided worksheet text or JSON; materials that lack recognizable table headers return an insufficient-input response instead of a tax conclusion.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
