## Description:

Zixflow (zixflow.com). Use this skill for ANY Zixflow request: reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zixflow workspaces from an agent, including listing, querying, creating, updating, and deleting collections, lists, records, entries, and workspace members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code.

Mitigation: Use an official signed or package-manager install path where available, or review the installer before running it.

Risk: The skill can create, update, and delete Zixflow data.

Mitigation: Confirm the exact payload and target before write actions, and require explicit approval before destructive actions.

Risk: Zixflow access is mediated through OOMOL rather than direct API calls.

Mitigation: Install only when the user accepts OOMOL as the intermediary for Zixflow access.

## Reference(s):

- [ClawHub Zixflow Skill](https://clawhub.ai/oomol/skills/oo-zixflow)
- [Zixflow Homepage](https://zixflow.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
