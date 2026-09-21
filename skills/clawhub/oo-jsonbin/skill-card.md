## Description:

JSONBin.io helps an agent read, create, update, and delete JSONBin.io bins through the OOMOL oo connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want an agent to manage JSONBin.io records through an authenticated OOMOL connection. It supports reading bins and requires confirmation before create, update, or delete operations change stored data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks the agent to run remote installer scripts without integrity checks or explicit user approval.

Mitigation: Do not let the agent run installer scripts automatically; install the oo CLI from a verified source or manually confirm the installer first.

Risk: The skill can read, replace, or delete JSONBin.io data through the connected OOMOL account.

Mitigation: Use only trusted OOMOL and JSONBin.io connections, inspect live action schemas before payload construction, and require explicit approval for write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-jsonbin)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [JSONBin.io Homepage](https://jsonbin.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
