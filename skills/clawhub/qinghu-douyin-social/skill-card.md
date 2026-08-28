## Description:

Helps Douyin social media operators use Qinghu AI data to connect trending topics, hashtag details, video search, creator profiles, and fan portraits into topic selection, selling-point analysis, audience matching, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators, marketers, and agent users use this skill to research Douyin topics, analyze high-performing videos and comments, compare creator fan portraits with target audiences, and produce actionable content plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Qinghu API token and may authorize paid Qinghu API calls.

Mitigation: Confirm user authorization before API use, prefer environment variables for tokens, and report Qinghu pointCost-based consumption using the skill's stated conversion.

Risk: Larger Douyin analytics results may be exported as local files.

Mitigation: Provide file links deliberately, keep chat previews concise, and avoid pasting large raw datasets into the conversation.

Risk: Generic content-planning requests can be misrouted if the platform is not clear.

Mitigation: Clarify that the requested analysis is Douyin-specific before using this skill's Qinghu/Douyin workflow.

Risk: Douyin trends and performance data are time-sensitive and can become stale.

Mitigation: Label site, period, cycle, and sample size in conclusions, and refresh data before relying on it for campaign decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-social)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu login and registration](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with optional JSON or shell examples and exported tabular files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs prioritize conclusions, recommendations, data-cycle labels, sample-size context, concise previews, and links to exported files when large Qinghu/Douyin datasets are produced.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
