## Description:

Guides developers using an unofficial Go client to call the Latitude LLM API with typed operations, authentication, and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that reads or manages Latitude LLM projects, traces, issues, and related organization resources through the unofficial client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, OAuth tokens, and trace or export contents may contain sensitive information.

Mitigation: Keep credentials and trace data out of logs, send credentials only to a trusted API URL, and confirm export recipients and scope.

Risk: Write, revoke, delete, invite, and export operations can change organization state or disclose data.

Mitigation: Use these operations only when explicitly requested and with the appropriate authorization.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-latitude-llm)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers authenticated requests and checking HTTP responses; it does not automatically execute API operations.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
