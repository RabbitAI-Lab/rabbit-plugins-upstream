## Description:

Design and generate international-brand-quality product detail pages for cross-border e-commerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsonbuilds](https://clawhub.ai/user/johnsonbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce teams, and developers use this skill to draft consumer-electronics product pages with hero copy, feature sections, lifestyle scenes, specifications, FAQ content, image prompts, and optional implementation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated product specifications or claims may be placeholders or inferred from category norms.

Mitigation: Confirm specifications, warranties, prices, and product claims with the manufacturer or user before publishing.

Risk: Image generation workflows may upload unreleased products or client images to external services.

Mitigation: Require explicit approval before WaveSpeed uploads and avoid using sensitive product imagery unless the user has authorized external processing.

Risk: Generated images for consumer electronics may contain hallucinated brand names, logos, or readable text.

Mitigation: Inspect generated images for branding or text and run the documented brand-removal workflow before integrating them into a page.

Risk: The skill includes examples using unpinned npx-based CLI execution and optional deployment actions.

Mitigation: Vet and pin CLI tooling where possible, review commands before execution, and require explicit approval before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsonbuilds/skills/product-page-designer)
- [Publisher profile](https://clawhub.ai/user/johnsonbuilds)
- [Server-resolved GitHub source](https://github.com/johnsonbuilds/awesome-hermes-skills/tree/main/creative/product-page-designer)
- [AI Brand Hallucination Reference](references/brand-hallucination-fix.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tables, image prompts, generated image URLs when used, layout guidance, and optional code or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated visual asset URLs and product specifications that require user or manufacturer verification.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
