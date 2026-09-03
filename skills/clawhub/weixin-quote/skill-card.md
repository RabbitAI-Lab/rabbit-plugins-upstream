## Description:

Enables and verifies WeChat quote-as-context behavior in OpenClaw by configuring the ClawBot fork of the WeChat channel plugin so quoted bot replies are available as model context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yechang1450](https://clawhub.ai/user/yechang1450)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw developers and operators use this setup skill to install or verify WeChat quote-followup support, replacing the stock WeChat channel plugin when needed and checking logs for successful quote injection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can replace the OpenClaw WeChat channel plugin and restart the gateway, which may affect compatibility or current service behavior.

Mitigation: Confirm the intended plugin change before execution, expect a gateway restart, and keep the official @tencent-weixin/openclaw-weixin plugin available for rollback.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown instructions with inline shell commands and verification criteria]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Idempotent setup flow; asks for user approval before installing the ClawHub plugin package.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
