## Description:

Feishu (feishu.cn). Use this skill for ANY Feishu request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Feishu workspaces through an OOMOL-connected account, including Drive, Docs, Wiki, Base, Sheets, Slides, Mail, Calendar, Chat, Tasks, OKRs, approvals, Minutes, and video meetings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can involve an unverified internet installer.

Mitigation: Avoid pipe-to-shell installation; download the installer from the vendor and verify its source and integrity where possible.

Risk: The connector can read, change, and delete many Feishu resources available to the connected account.

Mitigation: Install only for trusted OOMOL and Feishu connections, and limit the connected account or scopes to the resources needed for the task.

Risk: Write and destructive actions can modify or remove workspace data.

Mitigation: Inspect the live action schema, check the exact target and payload, and require explicit approval before write or destructive operations.

## Reference(s):

- [Feishu homepage](https://www.feishu.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-feishu)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and return JSON responses from the Feishu connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
