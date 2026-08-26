## Description:

当用户需要公开数据支撑抖音相关决策时，使用本技能：关键词搜索排序、博主作品批量抓取、评论抓取分析、实时热榜查询。适用于营销选品、内容策划、流量研究，即使用户没说出"抖音数据分析"这类术语。不适用于需要登录权限的私域数据（如后台播放量）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect public Douyin keyword search results, author posts, video comments, and hot-list data as structured JSON for content planning, competitor monitoring, sentiment review, and trend research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends GUAIKEI_API_TOKEN and requested Douyin search terms or URLs to guaikei.com.

Mitigation: Install only after confirming the provider and data-sharing posture are acceptable for the intended use.

Risk: Results are saved locally in logs and may include queried public Douyin content or user-supplied URLs.

Mitigation: Run the skill in an approved workspace and manage generated logs according to the user's data handling policy.

Risk: Runtime token or authorization errors may show provider website or WeChat contact text despite documentation claiming neutral error output.

Mitigation: Review authentication error behavior before deployment and avoid exposing stderr or logs to end users until the messages are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-video-comments-to-sentiment-data)
- [抖音关键词搜索完整选项参数说明](references/options.md)
- [抖音关键词搜索更新日志](references/changelog.md)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands; runtime stdout is structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. Runtime logs and results may be saved locally under logs/, while status and error messages are written to stderr.]

## Skill Version(s):

1.0.0 (source: release evidence, SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
