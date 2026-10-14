## Description:

Creates images from scene descriptions and offers prompts for targeted edits to a model, pose, or outfit using an optional reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use this skill to generate scene imagery from a description or revise a reference image's model, pose, or styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to the selected cloud image provider.

Mitigation: Avoid sensitive personal or proprietary images and confirm the provider before submitting requests.

Risk: Image generation can incur charges, especially for large or repeated batches.

Mitigation: Use dry-run to review estimated cost and generate lower-resolution drafts before final images.

Risk: Broad prompts involving children or protected attributes may produce inappropriate or misleading images.

Mitigation: Review these prompts before generation and inspect outputs before publication.

## Reference(s):

- [Creative Scene on ClawHub](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Pre-publication image check](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Prompt guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and command examples; generated images saved as files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image creation and reference-image edits; optional draft batches and dry-run cost estimates.]

## Skill Version(s):

1.0.21 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
