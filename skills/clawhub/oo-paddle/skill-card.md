## Description:

Paddle (paddle.com) supports reading, creating, and updating Paddle data through this skill instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Paddle catalog and customer workflows through an OOMOL-connected account. It supports product, price, and customer read and write actions while requiring live schema inspection before connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Install only from trusted OOMOL sources, prefer an official package manager when available, and review or verify installer contents before execution.

Risk: Write actions can change Paddle customer, product, and price data.

Mitigation: Review the live action schema, confirm the exact payload and expected effect with the user, and reserve destructive actions for explicitly approved targets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-paddle)
- [Paddle Homepage](https://www.paddle.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
