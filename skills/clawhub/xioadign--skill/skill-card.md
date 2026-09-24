## Description:

Provides warm companion-style chat responses using Zhipu AI and optional static image sharing through OpenClaw.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xioadign](https://clawhub.ai/user/xioadign)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users can use this skill to add brief companion-style responses for fatigue, greetings, encouragement, waiting periods, and optional static-image sharing in configured chat channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ordinary greetings or fatigue-related messages may trigger companion responses unexpectedly.

Mitigation: Use explicit opt-in invocation or confirmation before the skill responds on behalf of the agent.

Risk: User messages may be sent to Zhipu AI for response generation.

Mitigation: Avoid sending secrets, regulated data, or sensitive personal information through this skill.

Risk: The skill can post messages or static media through configured OpenClaw channels.

Mitigation: Confirm target channels before sending and keep OpenClaw CLI installation pinned or locally isolated.

## Reference(s):

- [Zhipu AI Open Platform](https://open.bigmodel.cn)
- [Source repository](https://github.com/xioadign/skill)
- [Publisher profile](https://clawhub.ai/user/xioadign)
- [ClawHub skill page](https://clawhub.ai/xioadign/skills/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce short companion replies and optional OpenClaw message-send commands using configured channels.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
