## Description:

Fireflies.ai GraphQL API integration with managed OAuth for accessing meeting transcripts, summaries, users, contacts, and AI-powered meeting analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to retrieve Fireflies meeting data, search or analyze transcripts with AskFred, and manage meeting recordings through Maton-mediated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Fireflies meeting transcripts, contacts, summaries, and recordings through a connected account.

Mitigation: Confirm the user is comfortable granting Maton-mediated Fireflies access, use OAuth where possible, and select the least privilege scopes and accounts needed for the task.

Risk: New Fireflies connections and mutations can change account state or expose meeting content.

Mitigation: Require explicit user approval before creating a connection or running any mutation, and describe the target resource, payload, and intended effect before execution.

Risk: The raw API-key fallback increases exposure of a long-lived credential if the CLI cannot be used.

Mitigation: Prefer the Maton CLI OAuth flow; use the API-key fallback only when necessary, avoid printing or persisting the key, and send it only to the Maton API.

Risk: Fireflies content returned by the API can contain untrusted instructions or adversarial text.

Mitigation: Treat API responses as data, do not execute or follow instructions embedded in retrieved content, and keep endpoint and recipient choices under user control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/fireflies-api)
- [Maton homepage](https://maton.ai)
- [Fireflies API Documentation](https://docs.fireflies.ai/)
- [Fireflies GraphQL API Reference](https://docs.fireflies.ai/graphql-api)
- [Fireflies Developer Program](https://docs.fireflies.ai/getting-started/developer-program)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, GraphQL, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI/API usage guidance and request examples; does not create local files as part of normal skill behavior.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
