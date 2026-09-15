## Description:

DingTalk Bot (dingtalk.com). Use this skill for DingTalk Bot requests that send supported custom bot webhook messages through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to send text, markdown, link, action card, and feed card messages through a connected DingTalk custom bot webhook. It is intended for agent workflows that need schema-checked bot message payloads and user confirmation before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote installer code for the oo CLI.

Mitigation: Review the installer before use and prefer a pinned or otherwise verifiable oo CLI installation method when available.

Risk: All listed actions send messages through a connected DingTalk bot.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect before executing any send action.

## Reference(s):

- [DingTalk Bot homepage](https://www.dingtalk.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dingtalk-bot)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces schema inspection and connector execution guidance; write actions require confirmation of the exact message payload before sending.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
