## Description:

Slack Bot enables agents to read, create, update, and delete Slack data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external teams use this skill to operate Slack Bot through an OOMOL-connected account. It supports schema-first Slack read actions and confirmed write or destructive actions for messages, files, reactions, and conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup advises running remote installer scripts directly in a shell.

Mitigation: Review the OOMOL CLI installation path carefully and prefer a verified package or signed, pinned release before installing.

Risk: Slack write or destructive actions can change or remove workspace data.

Mitigation: Confirm the exact payload, target, and effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-slackbot)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Slack](https://slack.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes schema-first command examples and confirmation guidance for write and destructive Slack actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
