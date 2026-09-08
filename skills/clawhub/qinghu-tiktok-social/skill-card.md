## Description:

青虎AI TikTok 社媒运营技能帮助代理监控 TikTok 行业热门话题、视频榜单、对标账号和评论舆情，并输出可执行的短视频选题与内容建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content operators use this skill to research TikTok topic opportunities, monitor industry content trends, compare peer accounts, inspect comments, and prepare content calendars or topic lists. It is intended for evidence-backed recommendations about what to publish, not for generating finished videos or visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls an external Qinghu API that requires a user-provided token and may consume Qinghu credits.

Mitigation: Require user confirmation before API calls, explain expected credit use when known, and use only the Qinghu token supplied by the user or configured environment.

Risk: Large TikTok result sets may be exported to local files.

Mitigation: Tell users when an export is created, provide the file link, and keep chat previews concise instead of exposing full raw datasets.

Risk: Trend, ranking, and comment data is time-sensitive and can lead to stale content recommendations.

Mitigation: Label recommendations with site, date range, period, and sample size so users can judge freshness and scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-social)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, text]

**Output Format:** [Markdown responses with JSON request examples, optional shell/API call guidance, and exported local files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce topic lists, trend rankings, peer-account summaries, sentiment notes, concise previews, and links to exported tabular files when result sets are large.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
