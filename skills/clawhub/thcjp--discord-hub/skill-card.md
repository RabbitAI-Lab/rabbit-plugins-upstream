## Description:

Discord中心 helps agents work with Discord Bot API workflows for interactions, commands, message handling, and operations automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to let an agent send Discord messages, respond to interactions, run Discord command workflows, and review delivery or execution results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local file and shell command authority.

Mitigation: Run it in a constrained workspace and require explicit approval before file writes or shell commands.

Risk: Discord automation can send messages, perform bulk operations, or retrieve archives.

Mitigation: Confirm the target channel, recipient, action scope, and message content before any Discord operation is executed.

Risk: Discord credentials and other sensitive tokens may be exposed if broad workspace or credential access is granted.

Mitigation: Provide only the minimum required credentials through environment variables and avoid granting access to unrelated secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-hub)
- [SkillHub skill catalog](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Discord message IDs, delivery receipts, interaction status, execution logs, and error information.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
