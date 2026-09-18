## Description:

Checks Chinese royalty and licensing settlement tables by recalculating line items, totals, duplicates, blanks, and negative values, with each finding tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Publishing, IP, content, finance, and business operations teams use this Chinese-language local checker during royalty or licensing settlement review to verify table arithmetic and identify missing or duplicate entries before issuing statements or audit samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers users toward a paid upgrade flow that includes mutable remote package execution.

Mitigation: Do not allow an agent to run payment or install commands unless the package source, permissions, and purchase terms have been independently verified.

Risk: The free checker omits some royalty-settlement checks that may matter for contract, advance, rate-tier, and duplicate-settlement review.

Mitigation: Treat results as limited to the stated free checks and route contract, tax, accounting, and withheld-check issues to qualified reviewers or separately verified tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/royalty-settlement-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; reports insufficient input instead of issuing unsupported conclusions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
