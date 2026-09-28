## Description:

Provides read-only Wikipedia and Wikimedia lookups for articles, citations, media, history, and readership across multiple languages through MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Researchers, writers, and developers use this skill to find and examine Wikipedia articles, sources, media, historical events, and readership trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live lookups require HTTPS access to Wikipedia and Wikimedia services.

Mitigation: Install only where outbound access to those services is acceptable.

Risk: Search terms, coordinates, or usernames may contain sensitive information.

Mitigation: Avoid submitting private queries, precise sensitive locations, or sensitive usernames.

Risk: Unpinned dependencies can change between installations.

Mitigation: Pin and review dependencies for controlled deployments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text and Markdown with article links, lists, and occasional tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; supports ten Wikipedia language editions for most tools.]

## Skill Version(s):

1.6.18 (source: ClawHub release metadata; bundled skill frontmatter says 1.1.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
