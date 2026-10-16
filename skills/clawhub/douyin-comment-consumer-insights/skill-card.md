## Description:

Analyzes public Douyin comments and related content to surface consumer questions, purchase concerns, feedback, and trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, creators, and marketing analysts use this skill to search public Douyin content, review creator posts and video comments, track trending topics, and summarize consumer feedback for content and product planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords, links, or IDs and the API token are sent to a third-party service.

Mitigation: Use only approved queries and links, and confirm the data-sharing scope before running the skill.

Risk: Search, creator-post, and comment results are saved in local logs by default.

Mitigation: Restrict access to local logs and remove retained results when they are no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-comment-consumer-insights)
- [Command options](references/options.md)
- [Release history](references/changelog.md)
- [Data API provider](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Analysis, Shell commands]

**Output Format:** [Markdown summaries and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public Douyin data; search, creator-post, and comment results are saved locally by default.]

## Skill Version(s):

1.3.0 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
