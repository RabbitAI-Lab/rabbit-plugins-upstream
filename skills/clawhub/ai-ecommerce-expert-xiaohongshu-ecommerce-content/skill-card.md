## Description:

Helps Xiaohongshu ecommerce merchants and content teams use IMIVA MCP workflows to prepare product images, detail-page content, KOC seeding packages, and video materials from user-provided product facts and assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, operators, designers, ad buyers, and agency teams use this skill to turn product assets, verified selling points, audience details, channel goals, and output specs into IMIVA MCP task parameters for Xiaohongshu-oriented listings, seeding content, ads, and conversion materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper launches a mutable npm MCP package and passes the user's process environment to it, which could expose unrelated local secrets.

Mitigation: Run the skill in a clean shell or container with only MCP_TOKEN, API_URL or IMIVA_API_URL, and PATH set; review or pin the npm package before use.

Risk: Image tasks may consume credits when submitted, and repeated submissions can duplicate cost.

Mitigation: Confirm model, quantity, resolution, and budget before creation; keep task IDs and query existing tasks before retrying.

Risk: Generated ecommerce claims, prices, certifications, or product details may be inaccurate or unsupported.

Mitigation: Use only user-provided or confirmed product facts and review generated content against channel requirements before publishing.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-xiaohongshu-ecommerce-content)
- [MCP config example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MCP configuration and task-call guidance; generated media is created by the IMIVA service, not embedded in the skill response.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
