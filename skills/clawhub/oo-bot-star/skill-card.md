## Description:

BotStar helps agents read, create, update, publish, and delete BotStar bots, CMS entities, bot attributes, and audience user attributes through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and BotStar operators use this skill to manage BotStar bots, CMS entities, bot attributes, and audience user attributes from an agent. It supports read workflows and state-changing workflows where payloads and effects should be confirmed before writes, publishing, or deletes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer instructions execute remotely downloaded code directly.

Mitigation: Review installer instructions before installation and prefer a verified package or documented manual installation path for the oo CLI.

Risk: Write, publish, and delete actions can change or remove BotStar resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write, publish, or destructive actions.

Risk: Connector payloads can be invalid if based on stale assumptions.

Mitigation: Inspect the live action schema before constructing BotStar connector payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bot-star)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [BotStar homepage](https://botstar.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include BotStar connector action names, live schema inspection commands, JSON payloads, and cautions for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
