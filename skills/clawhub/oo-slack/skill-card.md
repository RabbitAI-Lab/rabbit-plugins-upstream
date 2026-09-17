## Description:

Slack lets agents read, create, update, delete, search, and manage Slack content through the OOMOL-connected oo CLI and Slack connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and employees use this skill to operate Slack from an agent through an OOMOL-connected account, including reading conversations, posting messages, managing reactions, uploading files, and updating or deleting content after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include running an internet installer for the oo CLI.

Mitigation: Use a verified oo CLI installation path before installing instead of piping a remote script directly into a shell.

Risk: The skill can post, upload, update, delete, or remove Slack content through the connected account.

Mitigation: Confirm exact payloads, targets, and effects with the user before any write or destructive Slack action.

Risk: Slack workspace access depends on permissions granted to OOMOL and the connected identity.

Mitigation: Review the Slack permissions granted to OOMOL and use an account with only the access needed for the task.

## Reference(s):

- [ClawHub Slack Skill](https://clawhub.ai/oomol/skills/oo-slack)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Slack](https://slack.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON payloads, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write and destructive Slack operations require confirmation.]

## Skill Version(s):

1.0.9 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
