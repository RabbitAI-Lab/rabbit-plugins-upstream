## Description:

ERPClaw is an AI-native ERP skill for local accounting, invoicing, inventory, purchasing, tax, billing, HR, payroll, advanced accounting, and financial reporting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailnike](https://clawhub.ai/user/mailnike)

### License/Terms of Use:

GPL-3.0

## Use Case:

Business operators, finance teams, and developers use this skill to run local-first ERP workflows through an agent, including company setup, customer and supplier records, invoices, payments, inventory, payroll, and financial reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate real financial, payroll, banking, credential, backup, and local ERP code state.

Mitigation: Use it only in an intended ERP environment, enable and test RBAC, and restrict mutating workflows to authorized operators.

Risk: Module installation and update actions can fetch and execute local code.

Mitigation: Review module provenance before installing add-ons and treat GitHub-backed module actions as local code execution.

Risk: CSV imports from arbitrary server paths can introduce unwanted or incorrect business data.

Mitigation: Limit import paths to approved locations and review imported data before relying on it for business decisions.

## Reference(s):

- [ClawHub ERPClaw skill page](https://clawhub.ai/mailnike/skills/erpclaw)
- [ERPClaw documentation](https://www.erpclaw.ai/docs)
- [ERPClaw website](https://www.erpclaw.ai)
- [OpenClaw](https://openclaw.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON-like action results, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or change local ERP records and files when the user invokes mutating workflows.]

## Skill Version(s):

4.15.0 (source: SKILL.md frontmatter, CHANGELOG, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
