## Description:

Enables an agent to operate Slack through an OOMOL-connected account for reading Slack data and creating, updating, scheduling, or deleting Slack content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Slack conversations, channels, users, files, messages, threads, reactions, and permalinks, and to perform approved Slack write actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions can expose Slack messages, files, channels, and user metadata visible to the connected OOMOL account.

Mitigation: Install only when that account's Slack visibility is acceptable for agent access, and review read requests that may surface sensitive workspace content.

Risk: Write and destructive actions can post, update, schedule, upload, react to, or delete Slack content.

Mitigation: Review the exact payload, target conversation or file, and expected effect before approving any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-slack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Slack Homepage](https://slack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Slack connector command output and execution identifiers returned by the oo CLI.]

## Skill Version(s):

1.0.6 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
