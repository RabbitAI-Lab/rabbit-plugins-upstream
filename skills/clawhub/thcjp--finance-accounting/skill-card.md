## Description:

Provides finance and accounting document workflows for bookkeeping, reconciliation, tax calculations, and generating balance sheets, income statements, cash flow statements, invoices, and audit-style reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft or process accounting records, reconcile financial data, calculate taxes, and produce finance reports for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive financial and tax workflows while requesting command and file-write authority.

Mitigation: Install only in environments where the agent is allowed to read, write, and run commands on financial data; restrict permissions and review all generated files before use.

Risk: Generated tax forms, invoices, accounting entries, audit reports, or financial statements may be incorrect or incomplete.

Mitigation: Treat outputs as drafts and require review by a qualified finance, accounting, or tax professional before filing, sending, or relying on them.

Risk: The artifact makes security, encryption, access-control, logging, and compliance claims that evidence.security says should not be assumed to be enforced.

Mitigation: Do not rely on the skill for compliance controls; verify encryption, access control, audit logging, retention, and regulatory obligations in the deployment environment.

## Reference(s):

- [ClawHub skill page: finance-accounting](https://clawhub.ai/thcjp/skills/finance-accounting)
- [Publisher profile: thcjp](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial, accounting, and tax outputs are drafts that require qualified human review.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
