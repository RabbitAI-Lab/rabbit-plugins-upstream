## Description:

Provides read-only Wikipedia and Wikimedia research tools for article search, summaries, citations, media, history, and discovery across multiple languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users can research Wikipedia articles, assess sources and editing activity, discover related topics, and gather public information for content creation or general knowledge queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, article titles, coordinates, usernames, or IP addresses may be sent to Wikimedia public APIs.

Mitigation: Do not submit secrets, sensitive personal data, or private investigation terms; establish an outbound-domain and privacy policy before deployment.

Risk: The requests dependency has no upper bound or exact version pin.

Mitigation: Pin and review the requests dependency before deployment in stricter environments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured tool responses with article text, metadata, and source links; agent-facing prose or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; supports ten Wikipedia languages for most tools.]

## Skill Version(s):

1.6.28 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
