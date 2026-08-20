## Description:

青虎AI Shopee 爆款截流跟卖 helps agents pull Shopee ranking data by site and category, inspect product details and trend snapshots, compare price and sales structure, choose follow-selling or differentiated interception strategies, and find matching 1688 sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, marketplace researchers, and ecommerce operators use this skill to identify hot or rising Shopee products across supported regional sites, validate trend quality, estimate sourcing margin from 1688 matches, and decide whether to follow-sell, differentiate, observe, or reject candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu API credentials and paid data tools for Shopee market research.

Mitigation: Confirm the intended Qinghu token, check tool authorization prompts before paid calls, and disclose Qinghu point consumption when paid calls are made.

Risk: Large result sets may be exported as local files that can contain sensitive marketplace research data.

Mitigation: Store exports only where the user expects them, share file links instead of pasting large datasets into chat, and clean up local exports when the data should not persist.

Risk: Follow-selling recommendations may overlook brand authorization, patent, import, or marketplace compliance requirements.

Mitigation: Present compliance checks as user-owned prerequisites before acting on a sourcing or follow-selling recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-hot-intercept)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown summaries with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should lead with conclusions, include site/date/period/sample-size context for metrics, and keep large record sets in exported files rather than long chat tables.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
