## Description:

Call third-party APIs through the Maton gateway, which injects the credential for an app the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route concrete, user-approved actions to connected third-party apps through Maton, including reading business data, updating records, sending messages, and managing event automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect live connected app accounts through writes, deletions, message sends, campaign scheduling, permission changes, triggers, webhook destinations, hosted functions, and local --exec handlers.

Mitigation: Default to read and list calls, require specific user confirmation before sensitive actions, and periodically remove old connections, functions, triggers, and destinations.

Risk: Actions may run against the wrong connected account when multiple connections exist for the same app.

Mitigation: List available connections and pin the intended connection before making calls that depend on account identity.

Risk: Credentials or event payload data could be exposed through API keys, webhook headers, body templates, or local handlers.

Mitigation: Prefer OAuth and the operating system credential store, avoid long-lived MATON_API_KEY exposure, never embed Maton or provider credentials in destinations, and route data only to user-approved destinations.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-connected app credentials.]

## Skill Version(s):

1.2.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
