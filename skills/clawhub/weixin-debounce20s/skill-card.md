## Description:

Enables and verifies 20-second burst debouncing for the OpenClaw WeChat channel by installing the ClawBot fork plugin when needed, updating inbound message debounce settings, restarting the gateway, and checking behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yechang1450](https://clawhub.ai/user/yechang1450)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw operators use this setup skill to enable or repair 20-second message burst merging for WeChat, then verify the behavior with logs and a live burst test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can replace the OpenClaw WeChat channel plugin with the named ClawBot fork and restart the gateway.

Mitigation: Run it only when the user explicitly wants WeChat debouncing enabled, checked, or repaired, and require approval before installing the plugin package.

Risk: The skill writes debounce settings into openclaw.json, which can change inbound message handling.

Mitigation: Keep the changes limited to messages.inbound debounce settings, validate the OpenClaw configuration, and verify the 20000 ms window through logs and a live burst test.

## Reference(s):

- [README](artifact/README.md)
- [README-zh](artifact/README-zh.md)
- [Skill instructions](artifact/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/yechang1450/skills/weixin-debounce20s)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill changes local OpenClaw plugin state and openclaw.json only when run by an agent with user approval where required.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
