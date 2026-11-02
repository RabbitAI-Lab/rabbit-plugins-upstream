## Description:

Researches publicly available Douyin videos, creator posts, comments, and trending topics to support content and competitor analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, brand researchers, and creators use this skill to explore public Douyin search results, trending topics, creator posts, and comments for content planning, competitor research, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and associated charges involve a third-party provider.

Mitigation: Use the service only when authorized and when its data sharing and charges are acceptable.

Risk: The API token could be exposed.

Mitigation: Protect GUAIKEI_API_TOKEN and do not include it in shared output or logs.

Risk: Submitted links or IDs and results may be retained locally, and logs may contain sensitive research context.

Mitigation: Use clean public links or IDs, keep logs private, and delete stored logs when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-content-research-v1)
- [Guaikei service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON data, Analysis, Text, Markdown]

**Output Format:** [Structured JSON research results with concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers public search, trending topics, creator posts, and comments; requires Node.js and a GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
