## Description:

抖音公开数据全在 4 个命令里：搜（关键词，视频/图文/用户）、扒（博主作品）、读（视频评论）、看（实时热榜）。每维筛选有默认值，不传参也能跑；退出码 0/1/3 区分成功/错误/令牌无效。触发词覆盖抖音数据调研全场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to retrieve public Douyin search results, hot rankings, creator posts, and comments for content research, competitor monitoring, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the configured API token and requested Douyin keywords or public links to guaikei.com.

Mitigation: Use only after approving guaikei.com as a third-party service and avoid submitting inputs that should not leave the local environment.

Risk: Some commands store fetched results locally in the skill directory logs.

Mitigation: Avoid processing data that should not be retained locally and clear generated logs according to the user's retention requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-feed-processing-pipeline)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API Website](https://www.guaikei.com)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [JSON command output with local JSON log files for some commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; stdout is intended to be machine-readable JSON while logs and status messages are written separately.]

## Skill Version(s):

1.0.0 (source: release metadata, skill frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
