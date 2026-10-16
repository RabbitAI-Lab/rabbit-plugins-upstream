## Description:

Retrieves public Douyin search results, trending topics, creator posts, and comments as structured data for content and audience analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use this skill to examine public Douyin posts, trends, and comments for topic research, competitor monitoring, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords, Douyin URLs, and the API token are sent to the GUAIKEI service.

Mitigation: Confirm the data-sharing scope before use and keep the API token confidential.

Risk: Saved results may retain comments, author fields, and profile metadata locally.

Mitigation: Use only public data you are authorized to process and manage or delete local logs when retention is not needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-record-organizer)
- [GUAIKEI service and help](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Release notes](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON data, Analysis, Guidance]

**Output Format:** [Structured JSON results with optional plain-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, post, and comment results can be saved in local logs; trending topics are returned directly.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
