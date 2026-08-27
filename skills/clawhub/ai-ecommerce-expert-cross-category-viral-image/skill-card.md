## Description:

AI电商专家｜跨品类爆款图改造 helps ecommerce design, brand, advertising, agency, and content teams use IMIVA MCP to migrate reusable viral visual structures across product categories for ecommerce images, product pages, social commerce, and video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce design, brand marketing, advertising, agency, and content teams use this skill to prepare and submit IMIVA visual migration tasks for cross-category product creative. It helps agents collect product facts, authorized media, channel requirements, budget constraints, and output specifications before creating or querying generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP tokens can grant access to the user's IMIVA account.

Mitigation: Keep MCP_TOKEN in local environment variables or client secret storage, and do not place it in chats, screenshots, or repositories.

Risk: User-selected local media or HTTPS URLs may be uploaded to IMIVA generation tasks.

Mitigation: Submit only media the user intends to upload and has authority to use, especially when referencing third-party creative.

Risk: Image or video task creation can consume credits.

Mitigation: Confirm model, quantity, resolution, estimated credits, and budget limits before creating tasks, and query existing task IDs instead of recreating tasks.

Risk: The MCP runtime fetches the IMIVA npm package at execution time.

Mitigation: Install only if the user trusts IMIVA and the package source; consider pinning the package version or running with a minimal environment for tighter control.

## Reference(s):

- [IMIVA AI Ecommerce Expert homepage](https://imiva.ecpro.com/)
- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-cross-category-viral-image)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with JSON MCP arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MCP_TOKEN and user-provided local files or HTTPS media; creates and queries IMIVA visual migration tasks.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
