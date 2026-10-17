## Description:

Guides Go developers in integrating the unofficial Solana Tracker Data API and Datastream client for token, wallet, market, and live subscription data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to build and test integrations for Solana Tracker token prices, trades, holders, charts, wallet analytics, and real-time data subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an unofficial Go module and granting integrations API-key access requires trust in the dependency.

Mitigation: Review the module before installation and test integrations against local fixtures where possible.

Risk: Authenticated headers and WebSocket URLs can expose the API key in logs or errors.

Mitigation: Keep the key in the environment and redact authenticated headers and WebSocket URLs from logs and user-facing errors.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-solana-tracker)
- [Go client project homepage](https://github.com/psyb0t/go-solana-tracker)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers offline tests, response handling, and authenticated REST and WebSocket integrations.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
