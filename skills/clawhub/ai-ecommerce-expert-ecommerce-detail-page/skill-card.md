## Description:

AI电商专家｜电商商品详情页 helps ecommerce design, photography, operations, brand visual, and advertising teams use IMIVA MCP to generate structured ecommerce product detail page image groups from 1 to 5 product images and verified selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, brand operators, agencies, and developers use this skill to prepare IMIVA MCP requests for product detail page generation, including material checks, budget confirmation, task creation, task lookup, and result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a mutable external npm MCP package.

Mitigation: Pin @infimind/ecom-content-cli to a reviewed version before deployment and review changes before upgrading.

Risk: The MCP process may inherit environment secrets.

Mitigation: Run it in a clean environment with only the required MCP token and without unrelated cloud, repository, or production secrets.

Risk: Product media paths provided to the MCP may be uploaded to IMIVA.

Mitigation: Provide only product media intended for IMIVA processing and use a dedicated low-scope MCP token.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-ecommerce-detail-page)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP task parameters, task IDs, budget checks, and review guidance for generated ecommerce assets.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
