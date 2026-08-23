## Description:

Luno helps agents work with Luno through an OOMOL-connected account for account balances, market data, order details, and recent trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent query Luno account information and market data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Balance and order reads can expose sensitive financial data.

Mitigation: Install only when the user is comfortable letting the agent query Luno information through OOMOL, and treat returned balances and orders as sensitive.

Risk: Future connector actions that place, cancel, transfer, or otherwise change funds could have financial impact.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any action that could change funds.

Risk: Broad wording and conservative action labels may make the action impact unclear.

Mitigation: Inspect the live connector schema and explain the expected effect before executing any labeled or potentially state-changing action.

## Reference(s):

- [Luno homepage](https://www.luno.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-luno)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
