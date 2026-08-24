## Description:

Helps agents research TikTok Shop blue-ocean product opportunities by using Qinghu TikTok rankings and search data, checking product details and video signals, finding matching 1688 suppliers, and estimating gross margin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, sourcing teams, and product-research agents use this skill to identify emerging TikTok Shop products, compare demand signals, locate same-style 1688 supply, and produce prioritized product recommendations with margin assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Qinghu API token and may make paid TikTok/1688 data calls.

Mitigation: Install only when Qinghu data access is intended, review the listed tools before approving calls, and monitor the reported Qinghu credit consumption after each run.

Risk: Supplier matches and gross-margin calculations may not reflect final product quality, platform fees, or logistics costs.

Mitigation: Treat margin figures as assumption-based estimates, verify costs before acting, and validate 1688 matches through supplier checks or samples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-bluesea-collector)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Concise Markdown recommendations with optional exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports assumptions for margin estimates and summarizes Qinghu credit consumption when paid data calls are made.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
