## Description:

Fireberry lets agents read, create, update, delete, list, and query Fireberry account and contact records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with Fireberry CRM records, including reading, listing, querying, creating, updating, and deleting account and contact data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path documents remote shell and PowerShell installer pipelines.

Mitigation: Install the oo CLI through a verified method you trust, and do not let an agent run curl-to-shell or PowerShell download-to-execute commands automatically.

Risk: Write and destructive actions can change or delete Fireberry account and contact records.

Mitigation: Require explicit user confirmation of the exact payload, target record, and intended effect before running write or delete actions.

Risk: Fireberry record queries and responses may expose business or contact data.

Mitigation: Limit queries to the records needed for the task and avoid sharing returned data beyond the user's requested workflow.

## Reference(s):

- [Fireberry homepage](https://www.fireberry.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Fireberry skill](https://clawhub.ai/oomol/skills/oo-fireberry)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; write and destructive operations require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
