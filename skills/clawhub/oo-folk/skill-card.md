## Description:

folk (folk.app) connector for reading, creating, updating, and deleting Folk people, companies, groups, custom fields, and workspace users through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Folk CRM data through an OOMOL-connected account, including people, companies, groups, custom fields, and workspace users. The skill supports read, create, update, and delete workflows while requiring confirmation for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup references unverified remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installing, prefer a trusted versioned source with checksum or signature verification, and avoid automatic installer execution.

Risk: The skill can create, update, and delete Folk CRM records.

Mitigation: Confirm exact payloads for write actions and require explicit approval before destructive delete actions.

Risk: The connector operates on the Folk account connected through OOMOL.

Mitigation: Connect only the Folk account intended for agent-managed workflows and review connection scope or expiration errors before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-folk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [folk homepage](https://folk.app)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue oo CLI commands that return JSON responses from Folk connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
