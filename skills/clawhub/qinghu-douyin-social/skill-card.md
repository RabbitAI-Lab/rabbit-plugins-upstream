## Description:

Qinghu AI Douyin social operations skill for finding trends, analyzing topics and videos, reviewing creator profiles and fan portraits, and turning those signals into content plans and audience-fit recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators and marketing teams use this skill to research Douyin trends, benchmark videos and creators, compare fan portraits with target customers, and produce actionable topic lists, sales-message material, audience conclusions, and content plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls external Qinghu data tools that may use configured tokens and consume Qinghu credits.

Mitigation: Review the planned Qinghu tool calls before approving execution and confirm expected credit usage when available.

Risk: The skill may create local exported result files for larger data sets.

Mitigation: Review exported files before sharing them and avoid exposing sensitive campaign, creator, or customer-analysis data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow API check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Markdown responses with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export table files for larger returned record sets and should keep final responses concise with links and brief previews.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
