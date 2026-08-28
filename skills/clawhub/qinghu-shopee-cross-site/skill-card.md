## Description:

青虎AI Shopee 跨站点拓客为一店多开卖家分析品牌或同类商品在多个 Shopee 站点的分布、趋势、店铺和产品表现，并给出先开哪个站点的优先级建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers and ecommerce operators use this skill to compare cross-site demand signals before expanding one store into additional Shopee marketplaces. The agent helps rank up to three target sites, summarize brand/category density and trends, and flag sites that look weak or risky.

### Deployment Geography for Use:

Global; the skill's Shopee market analysis focuses on Taiwan, Malaysia, Indonesia, Thailand, Philippines, Singapore, Vietnam, and Brazil.

## Known Risks and Mitigations:

Risk: The skill can use a configured Qinghu API token.

Mitigation: Request the token from the user or approved environment variables only, and avoid exposing the token in responses or exported files.

Risk: The skill can make external Qinghu API requests that consume Qinghu credits after user approval.

Mitigation: Obtain approval before the first tool call, report actual Qinghu credit usage from the response envelope, and stop when authorization or parameters are missing.

Risk: The skill can create local spreadsheet exports for larger result sets.

Mitigation: Export only relevant Qinghu result data and provide concise links and previews instead of pasting large raw datasets into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-cross-site)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, files, API calls, configuration]

**Output Format:** [Markdown recommendations with comparison tables and optional local spreadsheet exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include a site priority ranking, site comparison data, localization notes, reasons to avoid weak sites, and Qinghu credit usage when paid calls are made.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
