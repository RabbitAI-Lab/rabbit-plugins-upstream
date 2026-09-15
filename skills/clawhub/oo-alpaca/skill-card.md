## Description:

Alpaca lets an agent operate Alpaca account, trading, and market-data workflows through an OOMOL-connected oo CLI account without handling raw API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Alpaca account data, assets, positions, orders, watchlists, news, market calendars, and stock or crypto market data. The agent should confirm exact payloads and effects before any state-changing Alpaca action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Install only after trusting OOMOL and prefer a verified or manually reviewed oo CLI installation path instead of allowing an agent to run installer one-liners automatically.

Risk: The skill can route Alpaca account access through the OOMOL connector.

Mitigation: Use only when comfortable with that account-access path and confirm any Alpaca action that could change account state before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-alpaca)
- [Alpaca homepage](https://alpaca.markets/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include Alpaca connector results as JSON when actions are run with the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
