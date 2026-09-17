## Description:

Helps agents operate Feishu/Lark Custom Bot through the OOMOL feishu_custom_bot connector and oo CLI to inspect action schemas and send supported bot messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send text, image, rich-text post, interactive card, and shared-chat messages through a connected Feishu/Lark custom bot while checking live connector schemas before constructing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents running an unverified remote installer script for the oo CLI.

Mitigation: Review the skill before installing and use a verified, pinned, or separately inspected oo CLI installation path.

Risk: Message-sending actions change Feishu/Lark bot state by sending content through webhooks.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-feishu-custom-bot)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feishu Custom Bot homepage](https://www.feishu.cn)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before building connector payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
