## Description:

Plans what Amazon product main images and secondary images should communicate based on product-detail fields and customer-review comprehension gaps; it does not generate image files, run ads, or publish listing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, catalog operators, and product-content teams use this skill to plan Amazon listing image content from product fields and review-derived buyer questions. The workflow checks available data, quotes any paid ARI operation, and only runs after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key for ari.funewa.com and may spend ARI credits after quoted paid operations.

Mitigation: Install only if sharing an ARI API key with ari.funewa.com is acceptable, review the quote, and run paid operations only after explicit user confirmation.

Risk: Security evidence flags that the bundled CLI can run broader product-operation workflows than the image-planning scope promises.

Mitigation: Use the documented listing/images workflow and avoid workflow or focus overrides unless the publisher narrows or clearly documents the broader operation surface.

## Reference(s):

- [Amazon Product Image Planning Workflow](references/operation-workflow.md)
- [Amazon Product Image Planning API Reference](references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/image-planner)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with concise findings, evidence notes, and optional bash commands for the ARI CLI workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit confirmation before paid ARI credit usage.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, scripts/ari.py, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
