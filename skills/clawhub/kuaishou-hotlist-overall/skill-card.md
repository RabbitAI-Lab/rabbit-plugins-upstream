## Description:

快手(Kuaishou)关键词搜索获取快手实时搜索数据｜当用户需要做快手内容研究、快手选题、热点观察、竞品内容对比、趋势判断或素材整理时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use this skill to search public Kuaishou videos, review creator posts and video comments, and gather material for topic research, trend monitoring, competitor comparisons, and audience research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and video or creator links are sent to www.guaikei.com.

Mitigation: Avoid sending sensitive information; use search terms and links that are appropriate to share with that service.

Risk: The scan only fully inspected 20 of 32 components.

Mitigation: Consider the incomplete inspection when deciding whether to install, and review the partially inspected components if you need greater assurance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/kuaishou-hotlist-overall)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [GuaiKei service and API access](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON envelope containing public video search results, creator posts or profile metrics, or video comments, depending on the command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by endpoint and requested limit. Search, creator, and comment requests have separate account-plan limits; the agent can use the returned data for follow-up summaries or analysis.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
