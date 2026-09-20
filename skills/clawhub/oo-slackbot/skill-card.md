## Description:

Enables an agent to handle Slack Bot requests for reading, creating, updating, and deleting Slack data through the OOMOL Slack connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Slack Bot through an OOMOL-connected Slack account for reading workspace data and performing approved message, file, reaction, and conversation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes immediate execution of a downloaded installer script.

Mitigation: Use a verified or pinned oo CLI installation path instead of directly piping downloaded scripts into a shell.

Risk: The skill can post, update, upload, or delete Slack content through the connected account.

Mitigation: Confirm exact Slack targets, payloads, and intended effects before write or destructive actions.

Risk: Connector use may involve OOMOL processing Slack workspace data.

Mitigation: Connect only Slack workspaces where that processing is acceptable for the user or organization.

## Reference(s):

- [Slack Bot ClawHub Page](https://clawhub.ai/oomol/skills/oo-slackbot)
- [Slack](https://slack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector commands and JSON payloads; write and destructive Slack actions require target and payload confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
