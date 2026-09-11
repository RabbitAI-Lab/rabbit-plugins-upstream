## Description:

Fireflies.ai GraphQL API integration with managed OAuth for retrieving meeting transcripts, summaries, users, contacts, recordings, and AskFred meeting analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to connect an agent to Fireflies.ai through Maton, query meeting transcripts and summaries, inspect users and contacts, and perform approved meeting-recording actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive meeting transcripts, summaries, users, contacts, and recordings from a connected Fireflies account.

Mitigation: Install only for intended Fireflies use, prefer OAuth, use least-privilege scopes where available, and confirm the target Fireflies connection before access.

Risk: Mutation calls can modify or delete meeting-related resources or create live meeting actions.

Mitigation: Default to read and list calls, then require explicit approval after checking the target resource, payload, and intended effect before any mutation.

Risk: The workflow depends on external Maton CLI or SDK packages.

Mitigation: Pin or verify Maton CLI and SDK packages before installing them in controlled environments.

## Reference(s):

- [Fireflies API Documentation](https://docs.fireflies.ai/)
- [Fireflies GraphQL API Reference](https://docs.fireflies.ai/graphql-api)
- [Fireflies Developer Program](https://docs.fireflies.ai/getting-started/developer-program)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with shell, GraphQL, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Fireflies connection; Fireflies and Maton rate limits apply.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
