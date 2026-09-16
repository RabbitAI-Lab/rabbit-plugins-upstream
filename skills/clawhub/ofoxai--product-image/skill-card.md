## Description:

Produces a set of product images in different styles, backgrounds, or treatments for a product listing, store page, or ad, quoting the full set cost before generation and routing real product photos through edits while using text generation for fictional or prototype products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multiple product-image options for commerce listings, store pages, and ads. It helps decide whether to edit a real product photo for consistency or generate plausible prototype imagery when no product photo exists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to Ofox for generation.

Mitigation: Use the skill only with product imagery and prompts that are acceptable to send to Ofox, and avoid sensitive credentials or confidential product assets unless approved.

Risk: Fallback installation guidance may install unpinned skills broadly across agents.

Mitigation: Install only the required ofox-image-core dependency from a trusted, pinned source and inspect it before using this skill.

Risk: Generated prototype product images may not match a real SKU, and edited images may still need label or product-detail review.

Mitigation: Confirm source photos before editing, disclose text-generation consistency limits for fictional products, and review each output image before using it in commerce.

## Reference(s):

- [ClawHub product-image skill page](https://clawhub.ai/ofoxai/skills/product-image)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Source homepage from metadata](https://github.com/ofoxai/skills/tree/main/skills/product-image)
- [Ofox API key portal](https://app.ofox.ai)
- [Ofox models endpoint](https://api.ofox.ai/v1/models)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and itemized cost/route recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that call the Ofox image workflow after confirming prerequisites, source-image suitability, route, quality, and total set cost.]

## Skill Version(s):

1.0.0 (source: server release evidence, artifact frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
