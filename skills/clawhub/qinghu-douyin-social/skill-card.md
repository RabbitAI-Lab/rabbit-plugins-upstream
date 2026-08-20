## Description:

青虎AI 抖音社媒运营 helps agents use Qinghu Douyin data tools to move from trend discovery to video selling-point analysis, audience portrait matching, and executable content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce operators use this skill to plan Douyin content, evaluate trends and topics, analyze competitor videos and comments, compare fan portraits with target customers, and produce content calendars or audience-fit recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read Qinghu credentials from the environment or request them from the user.

Mitigation: Install only in workspaces where Qinghu credentials are intended to be available, and review credential handling before use with sensitive analytics data.

Risk: Paid Qinghu tools may consume credits after the user authorizes paid calls in a session.

Mitigation: Confirm the planned paid tools before first use and verify the final reported Qinghu point cost.

Risk: The skill may create local exported table files for larger result sets.

Mitigation: Review exported files for sensitive audience, account, or campaign data before sharing them outside the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown, Files]

**Output Format:** [Markdown recommendations with optional exported table files and parsed JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export tabular data when API result arrays contain 10 or more records; paid tool usage requires user authorization and point-cost reporting.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
