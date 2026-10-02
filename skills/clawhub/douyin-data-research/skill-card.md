## Description:

Helps creators and marketers retrieve public Douyin search results, trending topics, creator posts, and video comments for content and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this skill to gather public Douyin videos, trending topics, creator posts, and comments as structured data for content planning, competitor research, and audience analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Douyin links, and the API token are sent to a third-party service.

Mitigation: Use the skill only if that data transfer is acceptable; protect the token and avoid sensitive queries or links.

Risk: Returned comments and creator data, including locally saved results, may contain user information.

Mitigation: Limit access to saved logs, retain only necessary data, and comply with applicable privacy rules and Douyin terms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-data-research)
- [API service and token setup](https://www.guaikei.com)
- [Command options](references/options.md)

## Skill Output:

**Output Type(s):** [Text, JSON data, Shell commands]

**Output Format:** [CLI commands and structured JSON results for searches, trends, posts, and comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, and comment results may be saved to local logs.]

## Skill Version(s):

1.3.0 (source: SKILL.md frontmatter, package.json, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
