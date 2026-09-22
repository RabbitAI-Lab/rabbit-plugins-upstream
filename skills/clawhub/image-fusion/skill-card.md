## Description:

Creates ecommerce outfit images by fusing up to eight product photos into a complete look on one model while preserving each item's visible details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and creative production teams use this skill to generate catalog-ready outfit images from multiple apparel and accessory product photos. It helps agents draft prompts, choose generation settings, run dry runs, save outputs, and quality-check whether all items appear correctly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and image URLs may be sent to the configured cloud image provider.

Mitigation: Use only approved assets, avoid sensitive photos or private internal URLs, and confirm the selected provider before generation.

Risk: The helper can auto-select the first configured backend, which may route data or spend to an unintended provider.

Mitigation: Set the provider explicitly when routing matters and run with dry-run first to inspect request and cost behavior.

Risk: Generated outfit images may omit or alter items despite the prompt's fidelity requirements.

Mitigation: Quality-check each output for item count, color preservation, layering, and pattern placement before publication.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0 Model Flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Skill Page](https://clawhub.ai/dlazyai/skills/image-fusion)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image files through the configured cloud image provider.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
