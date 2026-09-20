## Description:

Longbridge helps agents search Longbridge market data and read brokerage account information through an OOMOL-connected Longbridge account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent query Longbridge securities, market data, company data, rankings, screeners, news, account cash, positions, orders, executions, and portfolio profit/loss information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can lead an agent to run remote installer scripts directly in a shell.

Mitigation: Install the oo CLI only through a reviewed official method, and do not allow an agent to run pipe-to-shell installers automatically.

Risk: The connector can read private brokerage and account information from the connected Longbridge account.

Mitigation: Use the skill only with accounts and data scopes the user is comfortable exposing to the agent.

Risk: Some connector actions could write, trade, or change account state if available through the live connector.

Mitigation: Require separate user confirmation for any action that could write, trade, or change account state, including the exact payload and expected effect.

## Reference(s):

- [Longbridge ClawHub skill page](https://clawhub.ai/oomol/skills/oo-longbridge)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Longbridge homepage](https://longbridge.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Longbridge icon](https://static.oomol.com/logo/third-party/longbridge.png)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
