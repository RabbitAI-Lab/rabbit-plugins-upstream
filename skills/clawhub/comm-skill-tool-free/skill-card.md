## Description:

Helps an agent draft context-aware, empathetic communication using conversation history, emotional cues, relationship context, and channel-specific templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft empathetic messages, customer replies, and difficult-conversation scripts while adjusting tone for relationship, context, and channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags command execution and file, API, and command automation as broader than expected for a communication-drafting skill.

Mitigation: Manually review and approve any command execution, file write, callback URL, credential use, or external API action before allowing the agent to proceed.

Risk: Generated communication may be inaccurate, misread emotional context, or be inappropriate for sensitive interpersonal or customer situations.

Mitigation: Require human review before sending messages, especially for difficult conversations, customer complaints, or high-impact decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/comm-skill-tool-free)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown or JSON-like structured text with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include draft messages, tone guidance, configuration examples, execution status, and operation logs.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
