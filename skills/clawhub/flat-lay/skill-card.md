## Description:

Turns a garment flat-lay and a pose reference into an on-model e-commerce image while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and merchants use the skill to create on-model clothing images from garment photos and pose references, including coordinated outfits and consistent model looks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model reference images and prompts are sent to cloud image-generation providers.

Mitigation: Use only images you are authorized to upload and confirm the chosen provider's data handling before generation.

Risk: The bundled generator includes image and video tasks beyond the advertised virtual try-on workflow.

Mitigation: Restrict use to the flat-lay task and review or remove unrelated tasks before deployment.

## Reference(s):

- [ClawHub flat-lay release](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Model flags](references/model-flags.md)
- [Provider CLI guidance](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG images with optional JSON task results and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated images for garment color, texture, logos, anatomy, and resemblance before publication.]

## Skill Version(s):

1.0.24 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
