## Description:

A free local checker for accounts payable aging and payment-plan tables that recalculates rows and totals, detects duplicates and blanks, and cites source lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill during monthly close, reconciliation, and cash-planning reviews to check accounts payable aging and payment-plan tables. It helps identify arithmetic inconsistencies, duplicate suppliers, blank placeholders, and missing required table fields without sending the material over the network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags the release as suspicious because its documentation and default output steer users toward a paid upgrade that uses mutable external code and a purchase flow.

Mitigation: Review SkillPay links, package installation commands, and purchase steps separately; do not let an agent run @latest installers or initiate purchases without explicit human approval.

Risk: The free edition intentionally omits several checks, including long-aging prompts, plan-versus-balance checks, and some overdue consistency checks.

Mitigation: Treat the output as covering only the listed free checks, and review the withheld and out-of-scope items before using results for payment decisions.

Risk: The checker works from pasted or JSON-wrapped table text and does not reconcile ERP exports, contracts, invoices, or payment approvals.

Mitigation: Use source-system exports in the required tabular format and perform separate source-document reconciliation when those controls are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-aging-plan-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid-upgrade information referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON containing executed checks, findings, scope, missing-input guidance, and withheld-check notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; JSON mode is available with --json; insufficient input reports missing material instead of asserting a conclusion.]

## Skill Version(s):

1.0.7 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
