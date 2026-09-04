## Description:

Provides a warm companion workflow for OpenClaw that uses Zhipu AI to generate short supportive replies and can share configured static images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xioadign](https://clawhub.ai/user/xioadign)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users can use this skill to add companion-style replies for tired, waiting, greeting, encouragement, and casual-chat moments. When configured with a channel, it can send generated text and selected static media through OpenClaw-supported messaging destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Companion-chat text is sent to Zhipu AI for response generation.

Mitigation: Avoid using the skill for sensitive conversations unless the provider's privacy expectations are acceptable.

Risk: Configured OpenClaw channels can receive generated messages or static media.

Mitigation: Review destination channels and message content before enabling automated delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xioadign/skills/skill)
- [Publisher profile](https://clawhub.ai/user/xioadign)
- [Server-resolved GitHub provenance](https://github.com/xioadign/skill)
- [Zhipu AI platform](https://open.bigmodel.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZHIPU_API_KEY for generated companion responses and an OpenClaw channel for message or media delivery.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
