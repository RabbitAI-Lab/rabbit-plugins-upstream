## Description:

Zoho Books provides AgentPMT-hosted remote tool guidance for OAuth-based access to list organizations and manage accounting resources such as contacts, invoices, bills, expenses, payments, projects, time entries, and bank reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to invoke AgentPMT-hosted Zoho Books actions for organization-scoped accounting workflows such as creating invoices, syncing contacts, recording expenses, and matching bank transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete accounting data when the connected Zoho Books account has add, edit, or delete permissions.

Mitigation: Prefer read-only access unless write actions are required, and require human approval before creating, updating, or deleting records.

Risk: The skill can change invoice status, email invoices, and match or unmatch bank transactions.

Mitigation: Require human approval before changing invoice status, emailing invoices, or matching bank transactions.

Risk: Setup examples include unpinned npx commands.

Mitigation: Avoid the unpinned npx setup path unless the current upstream package source is trusted.

## Reference(s):

- [Zoho Books Schema](artifact/schema.md)
- [AgentPMT Marketplace Page](https://www.agentpmt.com/marketplace/zoho-books)
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/zoho-books)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes action schemas, permission requirements, and organization-scoped tool call examples.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
