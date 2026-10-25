## Description:

Image generation skill. Automatically selects the best dlazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate images from text prompts and, when useful, reference images. It selects a suitable dLazy image model and returns the generated image result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files may be sent to dLazy-hosted services for generation.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy.

Risk: Generation uses organization credits, and video or speech pipelines can create additional tasks.

Mitigation: Consider credit costs and limit execution to the media type requested.

Risk: The stored organization API key is sensitive, and the pinned CLI is an external dependency whose distributed contents were not independently verified.

Mitigation: Protect the stored API key and review the pinned CLI package before installing or running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy website](https://dlazy.com)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, URLs]

**Output Format:** [Generated image assets with hosted result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt-based generation and optional reference images; available controls and output quality depend on the selected model.]

## Skill Version(s):

1.3.34 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
