## Description:

Query FreshBooks invoices, clients, estimates, payments, expenses, projects, and time tracking from a shell with curl and a rotating OAuth token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to authenticate to FreshBooks, resolve account and business identifiers, and run shell-based FreshBooks API queries or accounting actions without installing the FreshBooks MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable live FreshBooks accounting write actions.

Mitigation: Require explicit user approval before POST, PUT, PATCH, DELETE, email, payment, invoice, estimate, client, or time-entry operations.

Risk: OAuth credentials and token state can expose FreshBooks account access if mishandled.

Mitigation: Keep credentials out of logs, protect the token state file, and install only when FreshBooks OAuth access is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer app registration](https://my.freshbooks.com/#/developer)
- [recipes.md](references/recipes.md)
- [fb-token.sh](references/fb-token.sh)
- [fb-bootstrap.mjs](references/fb-bootstrap.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper code, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses FreshBooks OAuth credentials and may produce live API calls that read or modify accounting data.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
