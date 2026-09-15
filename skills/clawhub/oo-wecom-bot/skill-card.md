## Description:

WeCom Bot (work.weixin.qq.com) helps agents read, create, update, and delete WeCom Bot data through the OOMOL oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and teams that use WeCom Bot can use this skill to let an agent inspect messages, schedules, meetings, todos, documents, and sheets, and to perform confirmed write or destructive actions through the OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive WeCom actions that change or remove messages, schedules, meetings, todos, documents, sheets, or records.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

Risk: First-time setup includes remote installer commands for a persistent local CLI installation.

Mitigation: Run installer commands only after independently verifying the official installer source and deciding to trust the local CLI installation.

Risk: The connected WeCom and OOMOL account determines what data the agent can access or modify.

Mitigation: Use only an account and connection that the user intends the agent to access, and review the skill before installation.

## Reference(s):

- [WeCom Bot ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wecom-bot)
- [WeCom Bot Homepage](https://work.weixin.qq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector result data and execution metadata returned by the oo CLI.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
