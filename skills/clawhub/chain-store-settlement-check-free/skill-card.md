## Description:

Performs a local free-edition check of chain franchise store settlement tables, including row recalculation, total reconciliation, duplicate detection, missing-field detection, and source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashier staff use this during monthly settlement, reconciliation, or inventory close to check chain-store franchise settlement tables before payment review. It helps identify arithmetic, total-row, duplicate-row, blank-field, and negative-amount issues while preserving source references for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a prompt for paid installation and purchase steps that are outside the free offline checker workflow.

Mitigation: Do not copy or execute the purchase prompt unless the user intentionally wants a paid install flow; require separate confirmation for external installs, purchases, wallet authorization, or newly installed skill instructions.

Risk: The free edition omits several settlement checks that are listed as paid-edition capabilities.

Mitigation: Review the executed-check scope and checks-not-run list before relying on results, and use a broader review process when omitted checks matter.

Risk: The checker evaluates table arithmetic and reconciliation, not contract compliance, legal, tax, POS import, or revenue-recognition questions.

Mitigation: Use the findings as source-cited calculation support and route contract, tax, legal, POS, and accounting-policy decisions to the appropriate human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/chain-store-settlement-check-free)
- [SkillPay storefront](https://skillpay.alipay.com/public/tokendidi)
- [Purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON produced by a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, message, executed-check scope, checks not run, and insufficiency messages when required table fields are missing.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
