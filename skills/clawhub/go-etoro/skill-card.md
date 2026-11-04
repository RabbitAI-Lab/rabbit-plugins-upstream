## Description:

Provides unofficial, typed Go REST and WebSocket clients for eToro’s public API, with examples for market data, account information, and live streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Go integrations with eToro's public REST API and WebSocket streams, including market data and account information. It also helps developers understand credential handling and when an operation can affect funds or public content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: eToro API credentials could be exposed through source code, logs, or requests sent to an unintended host.

Mitigation: Read keys from environment variables, keep them out of source and logs, and attach them only to requests sent to the documented eToro API hosts.

Risk: Some API operations can transfer money or publish, edit, or delete content in a real account.

Mitigation: Use read-only access by default and make a sensitive account change only when the user has requested that exact action; review the requested transfer or content change first.

Risk: The unofficial external SDK and its dependencies were not audited.

Mitigation: Review and pin the dependency version before using real-account credentials.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [go-etoro source repository](https://github.com/psyb0t/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for REST and WebSocket client usage; no files are produced by the library itself.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
