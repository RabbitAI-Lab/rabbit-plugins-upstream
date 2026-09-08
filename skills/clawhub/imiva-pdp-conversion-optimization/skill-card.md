## Description:

商品页转化率优化 helps brand merchants, ecommerce operators, designers, and content teams use the IMIVA MCP to reorganize above-the-fold content, selling points, detail sections, parameters, and calls to action into a verifiable product detail page content plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and brand content teams use this skill to turn product materials, verified selling points, target channels, specifications, and budget constraints into IMIVA MCP tasks for product detail page conversion optimization and content delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm MCP CLI that is not pinned to a fixed package version and can inherit a broad local environment.

Mitigation: Prefer a pinned CLI version and run it with a minimal environment containing only MCP_TOKEN, API_URL or IMIVA_API_URL, and PATH.

Risk: The skill requires an IMIVA MCP token and may handle product materials provided by the user.

Mitigation: Keep tokens in local environment variables or client secret storage, avoid storing them in skill files, screenshots, chat logs, or repositories, and share only materials intended for the IMIVA workflow.

Risk: Creating IMIVA image, video, or detail page tasks can consume credits.

Mitigation: Check available credits and require explicit confirmation of model, quantity, specification, and budget before submitting paid tasks.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)
- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/imiva-pdp-conversion-optimization)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA task setup, budget confirmation steps, task IDs, status checks, and result delivery guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
