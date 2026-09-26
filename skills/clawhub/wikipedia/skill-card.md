## Description:

Gives agents read-only access to Wikipedia and Wikimedia for article research, facts, media, current events, and multilingual lookups through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Researchers, writers, and developers use this skill to find and inspect Wikipedia articles, citations, edit history, media, and current topics in ten supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms, article titles, and optional coordinates are sent to Wikipedia or Wikimedia services.

Mitigation: Avoid submitting sensitive queries or locations; restrict outbound access to Wikimedia domains where needed.

Risk: The requests dependency is specified without an upper bound or fixed version.

Mitigation: Pin and review the requests dependency in controlled environments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown, Links, Guidance]

**Output Format:** [MCP tool responses with article text, structured facts, lists, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; no API key required; supports ten Wikipedia languages.]

## Skill Version(s):

1.6.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
