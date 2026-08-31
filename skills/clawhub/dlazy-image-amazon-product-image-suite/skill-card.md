## Description:

A professional product image generation skill purpose-built for Amazon product-detail pages, covering main images, secondary images, product infographics, lifestyle scenes, detail shots, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, brand teams, and agents use this skill to plan and generate Amazon listing image suites that include a compliant main product image, secondary product visuals, and optional A+ content modules. It is intended for iterative image planning and generation through the dLazy CLI and hosted generation services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media files are sent to dLazy cloud services.

Mitigation: Review inputs for confidential, regulated, or customer-sensitive content before generation, and use only approved media.

Risk: Persistent global CLI installation or saved API keys can leave credentials on the local system.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for ephemeral use when appropriate, and rotate or revoke API keys from the dLazy dashboard.

Risk: Image-generation API calls may consume account credits.

Mitigation: Confirm the output scope and each generation step before running CLI commands.

Risk: Generated Amazon listing visuals can become misleading or noncompliant if product claims, comparisons, or accessories are inaccurate.

Mitigation: Review generated images against Amazon image requirements and the actual product before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, image-generation prompts, checklists, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include current phase, target deliverable, image checklist, consistency checks, next confirmation request, and todo status.]

## Skill Version(s):

1.3.11 (source: ClawHub release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
