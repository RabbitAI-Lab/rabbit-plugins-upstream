## Description:

Enables agents to send text, markdown, link, actionCard, and feedCard messages through a user's OOMOL-connected DingTalk custom bot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent inspect the DingTalk Bot connector schema and send approved DingTalk custom bot messages through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send DingTalk bot messages through an OOMOL-connected account.

Mitigation: Confirm the exact message payload and intended effect with the user before running any send action.

Risk: Setup guidance includes remote shell installer commands for the oo CLI.

Mitigation: Prefer a verified, versioned, or manually inspected installation method before running installer commands.

Risk: The routing description is broader than the documented send-message actions.

Mitigation: Limit use to the documented DingTalk Bot send actions and inspect the live connector schema before constructing payloads.

## Reference(s):

- [ClawHub DingTalk Bot skill page](https://clawhub.ai/oomol/skills/oo-dingtalk-bot)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [DingTalk Bot homepage](https://www.dingtalk.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action execution and user confirmation for write actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
