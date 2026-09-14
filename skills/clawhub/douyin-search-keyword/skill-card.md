## Description:

A read-only Douyin public-data toolbox for keyword search, creator post retrieval, video or image-post comment collection, and real-time hot-list tracking, returning structured JSON for content research, competitor analysis, sentiment monitoring, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, marketers, and developers use this skill to retrieve public Douyin search results, creator posts, comments, and hot-list data for topic research, competitor monitoring, public-opinion analysis, trend tracking, and report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords, Douyin links, target accounts, and collected comments may be sensitive and are sent to www.guaikei.com for processing.

Mitigation: Review the query and authorization context before execution, configure GUAIKEI_API_TOKEN only in trusted environments, and avoid sending confidential campaign or account data.

Risk: Search, post, and comment results are automatically saved to a local logs directory, which can retain large public-data datasets.

Mitigation: Run the skill in an appropriate workspace and delete or protect logs when retention, backup, or shared-machine exposure is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/douyin-search-keyword)
- [抖音关键词搜索技能官网](https://www.guaikei.com)
- [完整选项参数说明](references/options.md)
- [更新日志](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes from Node.js CLI commands, usually summarized in Markdown for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, and comment results may be saved locally under logs.]

## Skill Version(s):

1.3.0 (source: SKILL.md metadata, package.json, changelog, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
