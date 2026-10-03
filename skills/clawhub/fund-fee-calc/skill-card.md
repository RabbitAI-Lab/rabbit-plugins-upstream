## Description:

A Chinese-language helper that estimates management, custody, and sales fees and net returns, and flags selected guaranteed-return claims in marketing text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theoretical text)

## Use Case:

Investors and financial-service reviewers can estimate simple fund fees and illustrative net returns and screen Chinese marketing claims for selected guarantee language. Results are preliminary and require professional review before financial or regulatory decisions.

### Deployment Geography for Use:

Global (Chinese-language content; assess local financial rules before relying on screening results)

## Known Risks and Mitigations:

Risk: Illustrative fee and return estimates may be mistaken for reliable investment projections.

Mitigation: Verify the inputs and formulas, and seek qualified financial advice before making decisions.

Risk: Keyword screening may miss misleading claims or be mistaken for a legal determination.

Mitigation: Review marketing language against current applicable rules with a qualified professional.

Risk: Remote installation commands may fetch code from a source the user has not verified.

Mitigation: Check the expected source and release tag before running remote installation commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/fund-fee-calc)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text fee estimates and claim-screening results, or structured JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports annual fee rate, estimated total fees, illustrative gross and net returns, flagged claims, and a PASS/FAIL result; exit status 0 for no flagged claims, 1 for flagged claims, 2 for usage errors.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; bundled files show other versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
