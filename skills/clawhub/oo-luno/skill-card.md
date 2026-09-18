## Description:

Luno (luno.com). Use this skill for ANY Luno request — reading, creating, and updating data. Whenever a task involves Luno, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Luno account, order, balance, ticker, order book, and trade data through an OOMOL-connected account. It supports schema-first command construction and guidance for setup recovery when authentication, connection, or billing errors occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line remote installer commands.

Mitigation: Use the installer only when the oo CLI is missing and only after trusting and verifying the OOMOL installer source.

Risk: The broad Luno trigger may apply this financial connector to requests that do not need account access.

Mitigation: Use the skill only for explicit Luno account or market-data tasks.

Risk: Some actions involve orders, balances, or account state.

Mitigation: Confirm the exact action, target, and payload with the user before running commands that may affect or expose sensitive financial information.

## Reference(s):

- [Luno homepage](https://www.luno.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface JSON responses from oo connector actions, including data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
