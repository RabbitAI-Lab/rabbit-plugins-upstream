## Description:

Provides agents with Wikipedia and Wikimedia search, article summaries, history, media, and research tools through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can research Wikipedia articles, discover related topics and media, and inspect sources, revisions, and readership across supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, article titles, coordinates, dates, and public editor usernames or IPs are sent to Wikipedia/Wikimedia APIs.

Mitigation: Avoid sensitive internal terms in queries and review outbound data before use in controlled environments.

Risk: The requests dependency has no upper version bound.

Mitigation: Pin and review the requests version before deployment in controlled environments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown-formatted text with links to Wikipedia and Wikimedia sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses vary by tool and may include article extracts, citations, media links, dates, and statistics.]

## Skill Version(s):

1.6.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
