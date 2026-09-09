## Description:

青虎AI TikTok 蓝海爆品采集 helps agents find emerging TikTok Shop product opportunities, check product details, locate matching 1688 suppliers, and summarize sourcing recommendations with margin assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, sourcing teams, and commerce analysts use this skill to discover rising TikTok Shop products, compare supplier options on 1688, and decide which candidates merit follow-up sourcing work. The skill is intended for product research through supplier discovery, not marketplace listing or fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for data access.

Mitigation: Use a scoped token if available, avoid sharing credentials in chat history, and revoke or rotate the token if it is exposed.

Risk: Large product-research outputs may be written to local table files.

Mitigation: Store exports only where intended and delete them when sourcing research is no longer needed.

Risk: Qinghu API calls can consume account credits.

Mitigation: Get user authorization before calls and report actual consumption from the returned point-cost metadata.

Risk: Supplier matches and margin calculations are research estimates, not final procurement decisions.

Mitigation: State logistics and commission assumptions, verify supplier quality, and validate samples before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-bluesea-collector)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API calls, Files]

**Output Format:** [Concise Markdown summaries with exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export local table files for result arrays with 10 or more records; margin estimates should state assumptions.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
