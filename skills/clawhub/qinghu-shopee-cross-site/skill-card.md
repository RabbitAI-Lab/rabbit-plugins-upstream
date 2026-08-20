## Description:

Helps Shopee sellers compare brand and category demand across regional sites so they can prioritize where to expand next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers and ecommerce operators use this skill to compare brand distribution, category trends, shops, products, and site-level market data before opening additional regional stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may need access to a Qinghu API token to retrieve Shopee market data.

Mitigation: Use a scoped token where available, provide it only in trusted sessions, and rotate it if it may have been exposed.

Risk: Large market-data responses may be exported to local spreadsheet files that contain sensitive business research.

Mitigation: Review generated files before sharing them and avoid running confidential searches in shared environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-cross-site)
- [Qinghu JSON-RPC API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown recommendations with comparison tables, concise previews, and links to exported spreadsheet files when larger result sets are returned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Qinghu API responses and may export local spreadsheet files for data delivery.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
