## Description:

Searches public Kuaishou videos by keyword and retrieves creator posts or video comments for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use this skill to identify popular Kuaishou videos, review creator posts, and analyze comments for research and campaign planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, profile and video identifiers, and the API token are sent to guaikei.com.

Mitigation: Use only with approval to share those inputs with the provider; protect the token and avoid sensitive queries.

Risk: Fetched results, including comments, persist in local logs.

Mitigation: Protect or delete the logs directory when research results should not persist.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-video-search)
- [API token and support](https://www.guaikei.com)
- [Usage options](references/options.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured JSON results with an optional brief Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a success, empty, or error status; fetched results are also saved locally in logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
