## Description:

Crypto APIs (cryptoapis.io) enables agents to inspect schemas and run OOMOL-connected Crypto APIs market-data actions instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Crypto APIs market data through an OOMOL-connected account, including asset details, exchange rates, and supported asset lists. The skill guides agents to inspect the live connector schema before running read-only connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users or agents to execute remote oo CLI installer scripts without built-in verification.

Mitigation: Review and verify the oo CLI installation source before installation, prefer trusted signed versioned packages, and avoid automatic execution of remote installer one-liners.

## Reference(s):

- [Crypto APIs homepage](https://cryptoapis.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
