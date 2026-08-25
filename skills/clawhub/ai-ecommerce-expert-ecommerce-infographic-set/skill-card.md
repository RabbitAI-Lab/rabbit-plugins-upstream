## Description:

AI电商专家｜电商信息图套装 helps ecommerce creative, operations, brand and advertising teams prepare IMIVA MCP workflows for generating product detail-page infographic sets, including size, material, structure, comparison and usage-step visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and developers use this skill to organize product materials, verified selling points, channel requirements and IMIVA MCP calls for Chinese ecommerce infographic and detail-page production. It supports task creation, task lookup and result handoff while reminding users to confirm budgets, credits and product facts before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a live external MCP package with broad environment access.

Mitigation: Run it only in a minimal environment containing MCP_TOKEN, API_URL and required PATH values, and install it only when the IMIVA package is trusted.

Risk: The MCP package is configured with an unpinned @latest package reference, so behavior may change between runs.

Mitigation: Pin a validated package version before production use and re-review the skill after package updates.

Risk: Image-generation task submission can consume credits and may create misleading ecommerce claims if inputs are not verified.

Mitigation: Check credits first, confirm generation counts and specifications with the user, and use only user-provided or confirmed product facts.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-ecommerce-infographic-set)
- [MCP config example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with JSON MCP arguments and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses token-backed external IMIVA MCP calls and may return task IDs for later result lookup.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
