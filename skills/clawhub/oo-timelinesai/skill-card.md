## Description:

TimelinesAI (timelines.ai). Use this skill for ANY TimelinesAI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect TimelinesAI action schemas, read TimelinesAI workspace data, and send plain-text WhatsApp messages through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may access TimelinesAI chats, messages, workspace details, and connected WhatsApp account information during requested tasks.

Mitigation: Install and invoke the skill only for intended TimelinesAI workspace operations, and limit prompts to data the agent is allowed to inspect.

Risk: Write actions can send plain-text WhatsApp messages to an existing chat, group, or phone number.

Mitigation: Require confirmation of the exact recipient, payload, and effect before running any action tagged as write.

## Reference(s):

- [ClawHub TimelinesAI Skill](https://clawhub.ai/oomol/skills/oo-timelinesai)
- [TimelinesAI Homepage](https://timelines.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
