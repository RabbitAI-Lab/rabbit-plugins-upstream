## Description:

青虎AI B 站社媒运营：结合 B 站热搜榜、关键词视频搜索、视频数据与评论、UP 主信息与主页作品，完成「中长视频爆款脚本拆解 → 弹幕评论舆情把控 → 高黏性 UP 主投放匹配」的深度硬核种草方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing and social-media operators use this skill to research Bilibili topics, analyze mid-length video scripts and comment sentiment, and match high-engagement UP creators for sponsored content plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu API credentials for Bilibili analytics.

Mitigation: Install only when comfortable letting the agent use those credentials, and review the planned tools before any data calls.

Risk: Qinghu data calls may consume credits.

Mitigation: Require user confirmation before the first tool call and report actual pointCost converted to Qinghu credits.

Risk: Large result sets may be exported to local files.

Mitigation: Review exported file paths and avoid sharing sensitive datasets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-bilibili-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow API endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional exported tabular files and JSON or shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user authorization before Qinghu API calls; large record arrays may be exported to local table files.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
