## Description:

Xero helps agents read, create, and update Xero accounting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Xero action schemas, read organisations, accounts, contacts, invoices, bank transactions, and financial reports, and perform confirmed write actions such as creating contacts or draft invoices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup commands execute remote installer scripts directly.

Mitigation: Prefer official, versioned, verifiable installer instructions and review installer contents before running setup commands.

Risk: Write actions can change Xero accounting data.

Mitigation: Inspect the live action schema and confirm each write action's exact payload and expected effect with the user before execution.

Risk: Connector-based access can expose or modify data in connected Xero tenants.

Mitigation: Install only when the publisher is trusted, connect only the intended Xero account, and verify the target tenant before running actions.

## Reference(s):

- [ClawHub Xero Skill](https://clawhub.ai/oomol/skills/oo-xero)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Xero Homepage](https://www.xero.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance may include oo CLI schema inspection and connector run commands; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
