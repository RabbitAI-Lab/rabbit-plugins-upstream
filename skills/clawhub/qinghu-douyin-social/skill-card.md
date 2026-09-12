## Description:

This skill helps agents run Douyin social media operations with Qinghu data APIs, connecting trending topics, hashtag and video analysis, creator profiles, fan portraits, and content planning into a topic-to-audience workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content operations agents use this skill to research Douyin trends, inspect comparable videos and creator audiences, evaluate audience fit, and produce actionable content plans. It is intended for Douyin social operations and does not cover product sourcing, listing, media generation, or creator deal management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require a Qinghu API token to access Douyin analytics data.

Mitigation: Use a scoped token when possible, provide it only in the intended agent environment, and rotate or revoke it when access is no longer needed.

Risk: Some Qinghu API calls may consume paid credits after user approval.

Mitigation: Confirm planned tool calls before execution and report actual Qinghu point consumption from the API response envelope when available.

Risk: The skill can export or reuse cached datasets and spreadsheets containing operational analytics.

Mitigation: Store exported files only in approved locations and review retention, sharing, and cleanup expectations before distributing them.

Risk: Douyin trend and audience conclusions are time-sensitive.

Mitigation: Label outputs with the data period, site, and sample size, and refresh the analysis before relying on it for current campaigns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-social)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow auth check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Files, API Calls]

**Output Format:** [Markdown summaries with optional exported spreadsheet files and JSON-backed API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should lead with conclusions, include data scope such as site, period, and sample size, and avoid pasting large raw datasets into chat.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
