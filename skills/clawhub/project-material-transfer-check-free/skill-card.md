## Description:

Checks project material transfer and issue tables for row arithmetic, totals, duplicate or blank entries, and negative values, with findings tied back to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, construction operations, and audit users can run the skill during monthly close, reconciliation, or inventory checks to verify project material transfer and issue tables. It focuses on deterministic table checks and reports missing input instead of inventing conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers users and agents toward an unpinned third-party npm install and a paid SkillPay purchase flow.

Mitigation: Review the exact package source, version, permissions, and payment details before allowing an agent to run the install command or initiate purchase steps.

Risk: The free checker intentionally omits several checks that are advertised as part of a paid tier.

Mitigation: Treat results as limited to the listed free checks and review the omitted checks before relying on the output for operational or audit decisions.

Risk: The checker only validates table arithmetic and internal consistency, not whether materials physically arrived or whether approvals and pricing policies are correct.

Mitigation: Pair the output with source-document review, approval controls, contract or budget checks, and physical inventory procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-material-transfer-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or structured JSON containing scope, findings, summary, omitted checks, and disclaimers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; sample execution reports no network use and lists checks not run in the free tier.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
