## Description:

B站评论分析工具。输入B站视频链接或BV号即可获取一级评论数据，支持分页浏览、评论情感分析（积极/负面/需求/竞品），生成精美 HTML 报告。当用户需要查看B站视频评论、分析评论舆情、了解用户反馈时使用。触发词：B站评论、B站视频评论、评论查询、评论分析、评论舆情、看评论、bilibili评论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessdy](https://clawhub.ai/user/jessdy)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, UP owners, brand operators, content planners, and product managers use this skill to retrieve first-level Bilibili comments, page through results, analyze comment sentiment across positive, negative, demand, and competitor dimensions, and optionally create an HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends Bilibili video IDs to yige.zone using the user's YIGE_API_KEY.

Mitigation: Use the skill only when that third-party API use is acceptable, keep the key in environment configuration, and avoid exposing it in prompts, logs, or generated files.

Risk: The skill can create local HTML reports under ~/Downloads/QoderReports and may open them after user confirmation.

Mitigation: Review generated report paths and content before sharing, and open local reports only when expected.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/jessdy/yige-skills/tree/main/skills/bilibili-comment)
- [ClawHub skill page](https://clawhub.ai/jessdy/skills/bilibili-comment-2)
- [Core workflow](references/core_workflow.md)
- [Yige API key settings](https://yige.zone/settings/api-keys?source=github)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with tables and optional local HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Bilibili BV ID or video URL and YIGE_API_KEY; retrieves one page of first-level comments per request.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
