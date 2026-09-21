## Description:

Reconciles BaconCo vendor documents and Sports Inc invoices against Odoo purchase orders, corrects supported price variances, files documents for matched or human review, and posts vendor bills only when totals match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and finance operators use this skill to reconcile payable documents, update Odoo purchase order pricing when vendor evidence is clear, and create or post vendor bills only when invoice totals pass the configured match check. Ambiguous, unreadable, mismatched, or unsupported cases are routed for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live accounts-payable records, including PO prices, document filing, vendor bills, and matched bill posting.

Mitigation: Install only where the Odoo token is intentionally allowed to perform those actions, confirm the intended posting mode, and begin with dry-run or draft-only operation until the workflow is validated on real tenant data.

Risk: A mismatched or unsupported invoice could be posted if operators bypass the documented match checks.

Mitigation: Post only when the bill total matches the vendor invoice within tolerance; leave mismatches in draft and route them to a human reviewer.

Risk: The Odoo MCP token and optional Sports Inc credential-sharing setup grant access to sensitive financial workflows.

Mitigation: Treat credentials as secrets, scope installation to trusted environments, and review the optional credential-sharing setup before enabling it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-payable-matching)
- [Odoo](https://www.odoo.com)
- [Payable matching procedure](references/matching_procedure.md)
- [Sports Inc payables](references/sportsinc_payables.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status reports with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update Odoo purchase orders, document folders, internal log notes, draft vendor bills, and matched posted bills through configured tools.]

## Skill Version(s):

0.9.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
