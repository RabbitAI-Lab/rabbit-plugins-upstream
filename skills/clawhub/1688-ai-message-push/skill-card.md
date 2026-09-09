## Description:

This skill lets an agent send WeChat or app system notifications to the current 1688 AI user through a Python CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to send explicit notification text to the user's own WeChat or 1688 app notification channel. It also provides configuration guidance for the ALI_1688_AK credential required by those notification calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports suspicious credential handling, including a mismatched credential namespace and possible use of an environment-selected gateway URL.

Mitigation: Install only in a trusted OpenClaw environment, confirm the intended gateway and credential namespace before configuring ALI_1688_AK, and rotate the key if configuration behavior is unclear.

Risk: The skill can send live WeChat or app notifications.

Mitigation: Send only user-provided notification text, ask for missing text before execution, and do not rewrite or expand the message without explicit approval.

Risk: Security evidence notes misleading DingTalk setup references in a skill that is presented as a 1688 message-push tool.

Mitigation: Review setup prompts and capability guides before use so user-facing configuration guidance matches the intended 1688 notification workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/1688aiinfra/skills/1688-ai-message-push)
- [App Push Capability Guide](references/capabilities/app_push.md)
- [Configure Capability Guide](references/capabilities/configure.md)
- [WeChat Push Capability Guide](references/capabilities/wx_push.md)
- [Skill Usage Tracking Notes](references/skill埋点说明.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON command output with a user-facing markdown status field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and an ALI_1688_AK credential; notification content is plain text.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
