## Description:

Apollo.io API integration with managed OAuth for searching and enriching people and companies and managing contacts and accounts through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and operations users use this skill to prospect, enrich leads, and manage Apollo contacts, accounts, sequences, and related sales data through Maton-managed authentication. Developers can also use the documented CLI and SDK patterns to make Apollo API calls through the same gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes Maton to connect to Apollo on the user's behalf and access connected Apollo data.

Mitigation: Install only when Apollo access through Maton is intended; review OAuth scopes during authorization and prefer read-only access when possible.

Risk: Connection creation or data-changing API calls can affect Apollo contacts, accounts, sequences, email data, or related sales records.

Mitigation: Require explicit user approval for connection creation and for POST, PUT, PATCH, or DELETE requests after confirming the target records, payload, and intended effect.

Risk: Multiple Maton profiles or Apollo connections can send a request to the wrong account.

Mitigation: Specify the intended connection when more than one Apollo connection exists and verify account context before writes.

Risk: Long-lived API keys or provider-issued tokens can leak if printed, logged, persisted, or passed through shell commands.

Mitigation: Prefer OAuth and the operating system credential store; never print or persist credentials, and use raw HTTP with MATON_API_KEY only when the CLI is unavailable.

## Reference(s):

- [Apollo Skill on ClawHub](https://clawhub.ai/byungkyu/skills/apollo-api)
- [Maton](https://maton.ai)
- [Apollo API Overview](https://docs.apollo.io/reference)
- [Apollo LLM Reference](https://docs.apollo.io/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Apollo connection.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
