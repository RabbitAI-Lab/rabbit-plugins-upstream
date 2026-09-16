## Description:

This skill lets an agent operate JustCall through the OOMOL oo CLI connector to read, create, update, and delete JustCall contacts and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage JustCall contacts and users through an OOMOL-connected JustCall account while inspecting live connector schemas before action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructs users to run remote installer scripts directly in a shell.

Mitigation: Prefer a pinned oo CLI release, trusted package manager, or verified download before installation.

Risk: Create, update, suppression-list, and delete actions can change or remove JustCall data.

Mitigation: Confirm the exact payload, target, and effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub JustCall Skill Page](https://clawhub.ai/oomol/skills/oo-justcall)
- [JustCall Homepage](https://justcall.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo connector schema and oo connector run commands; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
