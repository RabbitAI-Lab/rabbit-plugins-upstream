## Description:

Retrieves public Douyin data for keyword search, creator posts, video comments, and real-time hot-list queries so agents can support content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect structured public Douyin search results, creator posts, comments, and hot-list entries for short-video research, content planning, competitor monitoring, and operations analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, profile or video identifiers, request limits, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Install and run the skill only when that data sharing is acceptable, keep the token confidential, and rotate it if exposure is suspected.

Risk: Retrieved public posts and comments may be saved locally in the skill logs directory.

Mitigation: Use the smallest practical limits, delete logs when they are no longer needed, and verify collection and analysis comply with applicable rules and privacy expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/douyin-search-keyword)
- [抖音数据获取技能官网](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON from CLI tools, with Markdown guidance and shell command examples for agents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; API responses may be logged as local JSON files.]

## Skill Version(s):

1.2.1 (source: server release evidence, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
