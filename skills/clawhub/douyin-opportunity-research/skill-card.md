## Description:

研究抖音搜索结果、作品结构、达人数据和用户反馈，筛选值得继续验证的机会。当用户询问抖音选题、抖音增长或用户痛点时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to retrieve public Douyin search results, hot-list items, creator posts, and comments for topic discovery, competitor monitoring, audience research, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, profile links, video links, and API token are sent to the third-party service at www.guaikei.com.

Mitigation: Install and run only when that data sharing is acceptable for the user or organization, and keep GUAIKEI_API_TOKEN scoped and protected.

Risk: Returned public-data results may be written to local log files and can include comments, user identifiers, links, and research outputs.

Mitigation: Review and remove local logs when outputs should not persist on disk or should not be shared further.

Risk: The skill is intended for public Douyin data only and does not support private, login-only, or write actions.

Mitigation: Use it only for public-data research workflows and do not attempt to route private-data or account-action requests through this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-opportunity-research)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Guaikei API and token page](https://www.guaikei.com)
- [Changelog](artifact/references/changelog.md)
- [Options reference](artifact/references/options.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Structured JSON command output with concise human-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command output uses stdout JSON with diagnostic logs on stderr.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
