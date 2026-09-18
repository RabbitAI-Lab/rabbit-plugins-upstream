## Description:

A free local skill for checking segmented monthly tax tables across VAT input/output and tax burden, VAT surtaxes, and prepaid corporate income tax, with source-backed findings that can be recomputed offline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during monthly close, reconciliation, or filing preparation to check pasted segmented tax tables for arithmetic consistency, totals, missing fields, and duplicate periods. The free edition covers three check categories and reports when input is insufficient instead of fabricating a conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation and normal output steer users toward a paid complete edition through an agent-led install and purchase flow that includes mutable remote package execution.

Mitigation: Use the free checker locally, and require independent verification of the package, merchant, product, payment flow, and any install command before purchase or installation.

Risk: Users may treat the free edition as a complete tax review even though it executes only three check categories and withholds other listed checks.

Mitigation: Review the executed and withheld check lists before relying on results, and use qualified review for filing decisions or any checks outside the free edition scope.

Risk: Tax tables can contain sensitive business data even when the local checker itself is offline.

Mitigation: Keep pasted materials in approved local files and avoid moving tax data into remote services unless the data handling has been separately approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-monthly-selfcheck-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Complete edition purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON check results from a local Node.js runner, with Markdown usage instructions in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline deterministic execution; insufficient input returns missing-material guidance rather than a tax conclusion]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
