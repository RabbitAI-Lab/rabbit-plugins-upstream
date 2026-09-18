## Description:

Token Metrics lets an agent search and read Token Metrics market data through the OOMOL Token Metrics connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query Token Metrics market data through an OOMOL-connected account, including prices, OHLCV records, token lists, market-cap rankings, and trading signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running an unverified remote installer directly in a shell.

Mitigation: Review the installer path before installing, prefer verified official documentation or pinned packages with checksums or signatures, and require explicit user approval before an agent runs installer, login, or account-connection steps.

Risk: The skill depends on account connection state and may fail when authentication, Token Metrics connection, scope, or billing status is missing or expired.

Mitigation: Run normal read actions first, and only perform setup, login, reconnection, or billing-related steps after a matching error and explicit user approval.

## Reference(s):

- [Token Metrics homepage](https://www.tokenmetrics.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-token-metrics)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Token Metrics connector actions return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
