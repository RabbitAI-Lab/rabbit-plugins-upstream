## Description:

AI电商专家｜批量 SKU 内容生产 helps ecommerce teams prepare IMIVA MCP visual-migration requests for batch SKU content generation, task submission, and result tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, brand teams, supply-chain teams, and operators use this skill to turn product assets, channel goals, specifications, and budget constraints into executable IMIVA MCP visual-migration workflows for batch SKU image and video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned npm package for IMIVA MCP access.

Mitigation: Install only if the IMIVA package is trusted, and prefer pinning the npm package version before deployment.

Risk: The MCP helper forwards the local environment while using MCP_TOKEN and API_URL.

Mitigation: Run it in a clean environment containing only MCP_TOKEN, API_URL, required PATH entries, and the product assets needed for the task.

Risk: Visual-generation tasks may consume credits when submitted.

Mitigation: Confirm model, output count, specifications, and budget before creating credit-consuming tasks.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-batch-sku-content-production)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MCP setup guidance, task arguments, task-query commands, and quality-check criteria; generated media is produced by the IMIVA service.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
