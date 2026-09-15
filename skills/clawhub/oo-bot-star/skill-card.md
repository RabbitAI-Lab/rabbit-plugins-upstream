## Description:

BotStar operates BotStar bots, CMS entities, CMS items, bot attributes, and audience user attributes through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect BotStar connector schemas and run BotStar read, create, update, publish, and delete actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include direct execution of remote installer scripts.

Mitigation: Install the oo CLI through a documented, verifiable method, review any installer before execution, and do not let an agent run the installer automatically.

Risk: Write, publish, update, and delete actions can change BotStar bots, CMS content, bot attributes, or audience user attributes.

Mitigation: Inspect the live action schema, confirm the exact target, payload, and expected effect, and require explicit approval before running state-changing actions.

## Reference(s):

- [ClawHub BotStar Skill](https://clawhub.ai/oomol/skills/oo-bot-star)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [BotStar](https://botstar.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected BotStar provider; write, publish, update, and delete actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
