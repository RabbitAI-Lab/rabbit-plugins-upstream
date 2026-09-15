## Description:

Generates and edits ecommerce main-image candidates from approved product photos, covering white-background baselines, visible-difference images, content-commerce scenes, color SKU sets, and single-variable A/B test variants while emphasizing product fidelity and channel-rule checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent users use this skill to draft main-image prompts and dLazy CLI commands for marketplace listing images and controlled A/B image tests. It is intended for workflows that already have approved product photos and require product-faithful visual variants rather than unsupported claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images are uploaded to dLazy-hosted services for generation.

Mitigation: Use only approved product images and review every path passed with --images before running the command.

Risk: The workflow depends on an npm-distributed dLazy CLI and an external hosted service.

Mitigation: Use the pinned CLI version from the evidence, consider npx or an isolated environment, and install only if the external service is acceptable for the use case.

Risk: API keys may grant organization-level access to dLazy resources.

Mitigation: Use a dedicated revocable dLazy API key and rotate or revoke it when no longer needed.

Risk: Generated ecommerce images can misrepresent product structure, accessories, claims, pricing, or platform compliance if inputs and prompts are not constrained.

Mitigation: Keep product structure, color, logo, quantity, and claims grounded in approved product photos; run the skill's pre-publication checklist against current platform rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts, CLI command patterns, validation checklists, and operational guidance; image generation results are returned by the external dLazy service.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
