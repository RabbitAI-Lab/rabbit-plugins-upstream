## Description:

AI电商专家｜竞品构图参考重制 helps ecommerce design, brand marketing, advertising, agency, and content teams use IMIVA MCP to rebuild competitive product-media compositions by learning public reference structure and information hierarchy without copying trademarks, identities, or protected expression.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce content, brand marketing, advertising, and agency teams use this skill to prepare IMIVA visual migration tasks for product images and videos. It helps users confirm product facts, reference-material roles, output specs, budget, task creation, and result review for competitive-composition rebuild workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned external IMIVA MCP package with a user token.

Mitigation: Install only if the IMIVA npm package is trusted, use a scoped and revocable token, and avoid storing the token in skill files, screenshots, chats, or repositories.

Risk: IMIVA task creation can consume account credits.

Mitigation: Check credits and confirm model, quantity, resolution, and maximum cost before submitting generation tasks; save task IDs and query existing tasks instead of resubmitting blindly.

Risk: Reference media and generated ecommerce claims can create IP, identity, or misleading-product risks.

Mitigation: Use only authorized reference media, copy only general composition and information hierarchy, and verify all product facts, logos, pricing, certifications, claims, and channel requirements before publication.

Risk: A generic API_URL value could point the MCP client to an unintended endpoint.

Mitigation: Use the documented IMIVA endpoint unless there is an approved reason to change it, and review environment variables before running the MCP client.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-competitor-composition-rebuild)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an IMIVA MCP token and may create paid IMIVA generation tasks when invoked.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
