## Description:

Guides Go developers in using an unofficial typed client for Solana Tracker's Data API and Datastream WebSocket API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate token and wallet data queries, typed REST responses, and real-time Datastream subscriptions into their applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Solana Tracker API key could be exposed through logs, source code, or a Datastream URL.

Mitigation: Read SOLANA_TRACKER_API_KEY from the environment and avoid logging the key, authenticated headers, or WebSocket URL.

Risk: Adding the unofficial Go client introduces an external dependency and live API requests may consume subscription credits.

Mitigation: Use it only in intended Go projects, review the dependency, and respect API limits and HTTP 429 responses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-solana-tracker)
- [Setup and reference](references/setup.md)
- [Go client source and examples](https://github.com/psyb0t/go-solana-tracker)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-solana-tracker)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration guidance covers authentication, response handling, pagination, and WebSocket subscriptions.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
