## Description:

This skill helps ecommerce teams prepare IMIVA-powered Instagram product images, product detail content, KOC-style social posts, and video generation tasks from product assets, channel goals, specifications, and budget constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce merchants, operators, designers, advertisers, and agency teams use this skill to turn verified product facts and assets into IMIVA MCP task parameters for Instagram Shop, Reels, Stories, Meta Ads, and related ecommerce content workflows. It is intended for product listing, social commerce seeding, paid creative, detail-page, and product video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper runs an unpinned npm package.

Mitigation: Pin a reviewed @infimind package version before production use.

Risk: The helper passes the local environment to the MCP process, which can expose unrelated secrets.

Mitigation: Run it from a clean environment that exposes only MCP_TOKEN, API_URL or IMIVA_API_URL, PATH, and required runtime variables.

Risk: Image and video task creation can consume platform credits.

Mitigation: Confirm product assets, model choices, output quantity, and credit limits before creating tasks.

## Reference(s):

- [IMIVA AI Ecommerce Expert Homepage](https://imiva.ecpro.com/)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-instagram-ecommerce-content)
- [MCP Configuration Example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with JSON parameters and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces IMIVA MCP task setup, submission, and task-query guidance; generated media results are produced by the connected IMIVA service.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
