## Description:

青虎AI 电商选品上货总入口，帮助 agents use Qinghu data APIs for product sourcing, competitor analysis, market evaluation, supplier collection, and listing workflows across Amazon, TikTok Shop, Shopee, Ozon, Douyin, Xiaohongshu, Bilibili, and 1688.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to route sourcing, research, analysis, data collection, and listing tasks to Qinghu API-backed workflows. It is intended for marketplace decision support and operational handoff, with user approval before Qinghu API calls that may consume points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token or environment-provided credential for data calls.

Mitigation: Provide the token only in trusted environments and rotate it if it may have been exposed.

Risk: Qinghu API calls may consume points, including calls whose tool descriptions appear free.

Mitigation: Ask for user approval before the first API call, report actual Qinghu point consumption from the response envelope, and avoid repeated trial-and-error calls.

Risk: Listing or upload workflows can affect storefront operations.

Mitigation: Review requested listing or upload actions before approving them and report success, failure details, and follow-up actions clearly.

Risk: Marketplace and social platform data may differ from seller back-office records or platform-native reporting.

Mitigation: Use Qinghu data for research and decision support, and confirm important business decisions against the relevant platform backend.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ecom-sourcing)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workbench login](https://www.iqinghu.com/workbench/login?urlCode=agentch)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON-RPC request examples, concise conclusions, and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include marketplace metrics, ranked candidate lists, risk notes, authorization status, processing counts, failure reasons, and Qinghu point consumption when API calls are made.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
