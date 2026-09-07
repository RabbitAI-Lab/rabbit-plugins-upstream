## Description:

Enables OpenClaw's WeChat channel to treat quoted bot replies as context by installing or verifying the ClawBot fork plugin and validating quote-hit behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yechang1450](https://clawhub.ai/user/yechang1450)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw operators use this skill to enable and verify quote-as-context behavior for WeChat conversations, so follow-up questions that quote a fresh bot reply can be grounded in the quoted text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to replace the official WeChat plugin with an unpinned third-party fork that handles message context.

Mitigation: Confirm the publisher and source, prefer a pinned and reviewed package version, get user approval before installation, and keep a rollback path to the official plugin.

Risk: Quoted message text is processed for context injection.

Mitigation: Use the skill only in environments where processing quoted chat text by the configured WeChat plugin is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yechang1450/skills/weixin-quote)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and verification checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing setup and validation instructions for local OpenClaw CLI execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
