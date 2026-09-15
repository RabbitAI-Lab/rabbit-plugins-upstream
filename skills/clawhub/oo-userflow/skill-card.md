## Description:

Userflow lets an agent read, create, update, and delete Userflow users, groups, and events through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Userflow users, groups, and events through an OOMOL-connected account. It supports read actions, event tracking, upserts, and destructive deletes with confirmation requirements for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that may execute downloaded shell or PowerShell scripts.

Mitigation: Review the installation source and path before installing; prefer official, verifiable installation instructions or a package manager, and avoid piping remote scripts directly into a shell when possible.

Risk: Write and destructive actions can modify or delete Userflow users and groups.

Mitigation: Confirm the exact action, payload, and target with the user before running write or delete operations.

Risk: Credential or connection troubleshooting could expose sensitive account setup details if handled carelessly.

Mitigation: Use the OOMOL connection flow for credentials and avoid asking the user to paste raw Userflow tokens into the agent conversation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-userflow)
- [Userflow Homepage](https://userflow.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from the oo connector, including data and execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
