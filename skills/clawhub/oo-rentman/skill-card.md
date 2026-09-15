## Description:

Rentman (rentman.io) support for searching and reading Rentman contacts, contact persons, equipment, and projects through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Rentman records and lists through the oo CLI without handling raw Rentman credentials directly. It supports read-focused workflows for contacts, contact persons, equipment, and projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include mutable remote installer scripts executed directly in a shell.

Mitigation: Review setup commands before installation and prefer a verified package or download-then-verify process for the oo CLI.

Risk: Rentman query payloads are sent through the OOMOL service and may expose operational business data to that connected service.

Mitigation: Confirm the connected OOMOL account, Rentman scopes, requested fields, filters, and pagination before running broad list queries.

Risk: Authentication, connection, scope, credential, or billing errors may require account setup actions.

Mitigation: Run setup or billing steps only after a matching command failure and after the user confirms the account context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-rentman)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Rentman Homepage](https://rentman.io)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction and limits documented Rentman actions to read-focused get and list operations.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
