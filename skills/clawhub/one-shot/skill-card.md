## Description:

Turns one existing model or mannequin product image into alternate model, background, or market-specific scene variants while keeping the garment unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and agents use this skill to create localized product marketing images from an existing model or mannequin photo. It helps vary model demographics, backgrounds, and scenes while preserving the product's visible style, color, pattern, and fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model images and prompts may be sent to dLazy or the generation provider configured in the environment.

Mitigation: Use only images and prompts approved for the chosen provider, and avoid private or internal image URLs.

Risk: A brand configuration can unintentionally force a model demographic or visual constraint across generated variants.

Mitigation: Review brand.yaml before use and remove demographic or style constraints that are not intended for the release.

Risk: Generated edits can alter garment details, misalign the garment on the new body, or produce flawed hands and lighting.

Mitigation: Use explicit product invariants, alignment and hand-quality prompts, batch generation, and human visual review before publishing outputs.

Risk: The workflow could be misused to imply endorsement by a specific person or to create inappropriate likeness substitutions.

Mitigation: Do not use the skill for unauthorized specific-person likenesses, face swaps, or misleading endorsement imagery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [One Shot source image example](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/one-shot/source-model.jpg)
- [One Shot generated output example](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/one-shot/example-output.jpg)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples, helper-script configuration, and optional locally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are saved to a local path when a save destination is supplied; JSON status output is available from the helper script.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
