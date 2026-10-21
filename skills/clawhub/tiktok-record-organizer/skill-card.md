## Description:

Retrieves public TikTok search results, creator posts, and video comments as structured data for content and audience analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketers, creators, agencies, and analysts use this skill to find public TikTok posts, compare creator performance, and review video comments for research and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the API token are sent to the GUAIKEI service.

Mitigation: Use the skill only if sending TikTok keywords, profile URLs, video IDs, and the token to www.guaikei.com is acceptable.

Risk: Returned comments and creator details may contain personal data.

Mitigation: Review applicable platform rules and legal requirements before collecting, retaining, or sharing results.

Risk: Saved local logs may retain query results.

Mitigation: Delete temporary logs when they are no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-record-organizer)
- [Usage and parameter reference](artifact/references/options.md)
- [GUAIKEI service and API token information](https://www.guaikei.com)
- [Release notes](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Human-readable summaries and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public posts and comments only; a GUAIKEI API token is required.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
