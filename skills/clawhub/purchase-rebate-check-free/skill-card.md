## Description:

A free local checker for supplier purchase-rebate statements that recalculates expected rebates and differences, checks totals, detects duplicates and blanks, and cites source lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business operations users and agents use this skill to review tabular supplier purchase-rebate statements for arithmetic consistency, missing fields, duplicate suppliers, and line-cited discrepancies before year-end rebate follow-up. It is a local table-consistency aid and not a substitute for contract, tax, or accounting review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker can overstate rebate-bracket assurance because the free version does not verify whether the correct contractual bracket was applied.

Mitigation: Use the output as arithmetic and table-consistency support only; verify rebate brackets, tax basis, cumulative methods, and contract terms separately.

Risk: The artifact documentation includes a mutable remote install and purchase workflow for a paid upgrade.

Mitigation: Do not run the paid-upgrade npx command or follow newly installed onboarding instructions unless the package source, version, SkillPay flow, and local execution impact have been independently trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/purchase-rebate-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON containing findings, summaries, executed checks, withheld checks, and source-line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; accepts a JSON file or plain-text purchase-rebate table as input.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
