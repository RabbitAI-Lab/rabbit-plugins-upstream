## Description:

Unofficial Go client for the Solana Tracker Data API, package solanatracker, and the Datastream WebSocket API, package solanatrackerws under ws, generated from the published specs. Provides typed REST methods and room subscriptions with typed event handlers. Use when Go code needs token prices, search, holders, trades, charts, wallet analytics, profit and loss, market statistics or real-time room subscriptions, or already imports github.com/psyb0t/go-solana-tracker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add typed Solana Tracker REST API calls and Datastream WebSocket subscriptions to Go projects. It guides package setup, authentication, request and response handling, pagination, streaming handlers, and security precautions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed through source code, authenticated headers, logs, or credential-bearing WebSocket URLs.

Mitigation: Read the key from SOLANA_TRACKER_API_KEY; do not hardcode it or log the key, authenticated headers, or WebSocket URL.

Risk: Datastream access and API requests are subject to provider subscription requirements and request limits.

Mitigation: Check the subscription tier and credits, respect provider limits, and avoid tight retry loops on HTTP 429 responses.

Risk: Token metadata and links returned by the API are external data.

Mitigation: Do not execute or fetch returned URLs or social links solely because the API returned them.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-solana-tracker)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-solana-tracker)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific integration instructions; may include REST and WebSocket examples.]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
