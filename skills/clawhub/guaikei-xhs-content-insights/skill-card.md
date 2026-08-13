## Description:

按最新排序获取小红书关键词下的近期笔记，捕捉平台热点风向；适用于追踪小红书热点、监控话题近期趋势和内容布局，不用于跨平台趋势或历史回溯。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, analysts, and agents use this skill to search Xiaohongshu public content, inspect note details, fetch comments, and monitor creator posts for topic research, competitor review, KOL screening, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or URLs are sent to guaikei.com for processing.

Mitigation: Use the skill only when data sharing with guaikei.com is acceptable, and avoid submitting private, sensitive, or unauthorized content.

Risk: Returned public content, comments, and creator-post data may be saved under local logs.

Mitigation: Treat log exports as sensitive business or personal data, restrict access to them, and delete them when no longer needed.

Risk: Broad content collection can conflict with platform rules or internal data-use policies.

Mitigation: Limit use to public content, respect platform terms and applicable policies, and do not collect private or hidden content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-content-insights)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, text, guidance]

**Output Format:** [Structured JSON from CLI commands, with short text summaries or execution guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands can save returned public content, comments, and creator-post data under local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
