## Description:

Provides an MCP interface for searching and reading Wikipedia and Wikimedia articles, media, activity, and public edit histories across multiple languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Researchers, writers, and developers use this skill to find and summarize encyclopedia content, discover media and related articles, and inspect public article history and sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms, article titles, optional coordinates, and queried usernames or IP addresses are sent to public Wikipedia/Wikimedia services.

Mitigation: Avoid submitting sensitive queries or precise locations unless external disclosure is acceptable.

Risk: Public editor and IP contribution histories can be used to profile individuals.

Mitigation: Use editor-audit tools only for appropriate public-data research; do not treat activity patterns as proof of identity or intent.

Risk: Unpinned dependencies can change across installations.

Mitigation: Pin and review dependencies when reproducible deployments are required.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text and Markdown with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include public editor names, IP addresses, and article activity data.]

## Skill Version(s):

1.6.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
