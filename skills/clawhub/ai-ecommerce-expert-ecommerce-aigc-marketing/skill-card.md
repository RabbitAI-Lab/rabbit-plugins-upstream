## Description:

AI电商专家｜电商 AIGC 营销内容 helps ecommerce marketing, advertising, livestream, and social content teams turn product assets and verified selling points into IMIVA MCP tasks for product images, seeding content, campaign visuals, and short-form video material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, agencies, and content marketers use this skill to prepare IMIVA MCP calls for product-image refinement, KOC seeding packages, campaign visuals, and ecommerce video generation. It guides users to confirm product facts, assets, channel requirements, budget, and task IDs before submitting or querying paid generation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper runs an unpinned external npm package for IMIVA MCP access.

Mitigation: Pin the IMIVA npm package to a reviewed version before operational use and update only after review.

Risk: The helper forwards the full local environment to the MCP subprocess.

Mitigation: Run the helper in a clean environment and pass only required variables such as MCP_TOKEN and API_URL.

Risk: Product assets and task data are sent to IMIVA under the user's token.

Mitigation: Use the skill only when the user trusts IMIVA for the relevant assets and has confirmed authorization to upload them.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-ecommerce-aigc-marketing)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool-call arguments, task-query guidance, budget-confirmation steps, and quality checks for ecommerce image or video outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
