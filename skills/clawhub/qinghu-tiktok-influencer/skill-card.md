## Description:

青虎AI TikTok 达人带货建联：从达人库按站点和类目筛达人，批量查达人详情、达人视频列表与带货商品列表，反向从商品和店铺找关联带货达人，精准匹配高 ROI 达人，避免盲目寄样。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and ecommerce teams use this skill to research TikTok Shop creators, compare forward category search with reverse competitor-product or seller discovery, and produce prioritized outreach lists for product seeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Qinghu API token for creator research.

Mitigation: Confirm whether the agent will use a user-provided token or an environment token before any API call.

Risk: Qinghu tool calls may consume credits.

Mitigation: Confirm the tools to be called and expected credit usage before execution, then report actual credit usage from returned call metadata.

Risk: Large result sets may be exported to spreadsheet or cached files.

Mitigation: Confirm where exported spreadsheets and cached result files will be stored and share only concise previews in chat.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-influencer)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Markdown summaries with optional exported spreadsheet files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked creator lists, concise previews, cited data scope, and Qinghu credit usage when paid tools are called]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
