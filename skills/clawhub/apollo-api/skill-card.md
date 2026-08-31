## Description:

Apollo.io API integration with managed OAuth for searching and enriching people and companies and managing contacts, accounts, and sequences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operations teams, and agents use this skill to access Apollo.io through Maton OAuth for lead search, enrichment, contact and account management, and sequence-related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Apollo sales data through Maton-mediated authentication.

Mitigation: Prefer OAuth, verify the active Maton profile and Apollo connection, and use a specific connection when multiple accounts are available.

Risk: Write actions can create, update, delete, message, or enroll contacts in sequences.

Mitigation: Require explicit user confirmation before POST, PUT, PATCH, DELETE, messaging, or sequence-enrollment operations, including the target resource and intended effect.

Risk: Long-lived API keys can leak through environment variables, command arguments, logs, or files when the CLI cannot be used.

Mitigation: Use the Maton CLI with OAuth where possible; otherwise never print or persist the key, never pass it on the command line, and send it only to api.maton.ai.

Risk: External Apollo data may contain untrusted instructions or content.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and validate any follow-up endpoint, recipient, or payload choices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/apollo-api)
- [Maton homepage](https://maton.ai)
- [Apollo API Overview](https://docs.apollo.io/reference)
- [Apollo LLM Reference](https://docs.apollo.io/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or SDK examples and defaults to read/list calls before write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
