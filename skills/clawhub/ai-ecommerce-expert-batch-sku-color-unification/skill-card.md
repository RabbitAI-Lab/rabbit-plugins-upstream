## Description:

AI电商专家｜多图统一商品颜色 helps ecommerce design, photography, operations, brand visual, and advertising teams submit IMIVA MCP tasks that unify multiple product images to one target color while preserving SKU consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce content teams use this skill to prepare and submit IMIVA color-change tasks for batch SKU color unification across product images. It guides users through material checks, model and resolution choices, budget confirmation, task submission, and result lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external IMIVA MCP package with a user account token and may create paid ecommerce content tasks.

Mitigation: Install only if the publisher and IMIVA package are trusted, use a least-privilege token, confirm credits and task settings before creation, and avoid exposing unrelated secrets in the runtime environment.

Risk: The MCP package is referenced with a latest-version install pattern, so behavior can change as the upstream package changes.

Mitigation: Consider pinning the npm package version in production or reviewing the package before deployment.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-batch-sku-color-unification)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an IMIVA MCP token and may create paid ecommerce content tasks when invoked.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
