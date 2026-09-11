## Description:

Enforce Persian output for all Telegram group, channel, and DM interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when producing Telegram group, channel, or direct-message content that must be written in Persian while preserving code, commands, technical terms, and URLs in their original language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telegram-facing output may be unintentionally forced to Persian when the skill is combined with another skill or used outside the intended Telegram context.

Mitigation: Confirm the output destination before applying the skill, and do not apply it to terminal output or file generation unless the user explicitly requests that combination.

Risk: Users may expect incoming non-Persian messages to be translated, but the skill only enforces the language of outgoing responses.

Mitigation: Treat translation of incoming content as a separate task and make only the final Telegram-facing response Persian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ehsanghaffar/skills/telegram-persian-enforcer)
- [Publisher profile](https://clawhub.ai/user/ehsanghaffar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Persian-language plain text or Markdown for Telegram-facing messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves code blocks, commands, technical terms, and URLs in their original language when appropriate.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
