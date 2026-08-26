## Description:

青虎AI Shopee 爆款截流跟卖 helps an agent analyze Shopee product rankings, item details, trend snapshots, price-band crowding, and 1688 image-search sourcing so it can assess whether to follow, differentiate, or drop candidate products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers and ecommerce operators use this skill to find Shopee hot or rising products by site and category, validate product trends, compare price bands, locate 1688 sourcing options, and receive follow-sell or differentiation guidance. It is also useful for agents preparing concise market-analysis deliverables with exported detail files when result sets are large.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API token for Shopee and 1688 data requests and may consume Qinghu points after user confirmation.

Mitigation: Install and run it only when token use and Qinghu point consumption are acceptable; keep the token scoped to the intended Qinghu account and review the requested tool set before approving calls.

Risk: Large result sets may be exported to local spreadsheet files.

Mitigation: Avoid using sensitive business data unless local storage is acceptable, and review exported files before sharing them outside the workspace.

Risk: Shopee follow-sell decisions can involve brand authorization, patent, import, or local marketplace compliance obligations.

Mitigation: Treat strategy labels as market-analysis guidance and verify product, brand, patent, and site-specific compliance requirements before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-hot-intercept)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance, API Calls]

**Output Format:** [Concise Markdown recommendations with optional spreadsheet-style file exports for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include candidate product lists, strategy labels, sourcing and margin estimates, and concise previews with site, accounting period, cycle, and sample-size context.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
