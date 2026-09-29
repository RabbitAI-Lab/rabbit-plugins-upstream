## Description:

Gives agents read-only access to Wikipedia and Wikimedia research tools for article lookup, summaries, citations, edit history, media, and current topics across multiple languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users of MCP-enabled agents can research Wikipedia topics, retrieve article details and citations, explore Wikimedia media, and inspect public edit history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may disclose search terms, article titles, coordinates, topics, and public usernames or IP addresses to Wikimedia services.

Mitigation: Send only information you are comfortable sharing with Wikimedia services.

Risk: Public contributor and IP-audit data could be used to target individuals.

Mitigation: Use contributor information for public-source research, not to target individuals.

Risk: Unpinned dependencies may change in stricter deployment environments.

Mitigation: Pin and review dependencies before deployment where reproducibility is required.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-formatted text with links to Wikipedia and Wikimedia resources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; content and availability depend on Wikimedia services.]

## Skill Version(s):

1.6.19 (source: server-resolved ClawHub release; embedded skill frontmatter states 1.1.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
