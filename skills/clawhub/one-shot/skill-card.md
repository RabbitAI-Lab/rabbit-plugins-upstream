## Description:

Helps e-commerce teams replace the model, background, or both in an existing model or mannequin product photo while keeping the garment unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, creative operators, and developers use this skill to turn one existing apparel model photo into multiple audience and scene variants for catalog or advertising workflows. It helps preserve product details while changing the person, background, or mannequin presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected photos, including identifiable people, may be sent to the configured image provider.

Mitigation: Use only images you own or are authorized to edit, obtain consent from depicted models where needed, and confirm the chosen provider's data handling terms before execution.

Risk: Demographic or model replacement prompts can touch protected traits or create misleading endorsements.

Mitigation: Review brand defaults and prompts for protected-trait handling, avoid implying real-person endorsement, and do not use the skill for specific-person face swaps or forged testimonials.

Risk: Generated outputs may alter product details, produce anatomical errors, or create images unsuitable for listing.

Mitigation: Inspect each result before publication, especially garment color, logo placement, silhouette, fit, hands, lighting, and watermark or text artifacts.

Risk: Generic image-editing workflows could be misused on third-party media.

Mitigation: Do not use the tooling to remove watermarks, attribution, or other rights indicators from media you are not authorized to modify.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/one-shot)
- [dLazy CLI](https://github.com/dlazyai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples, optional JSON status output, and saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local image inputs, prompt text, provider credentials, brand configuration, batch generation, and save paths]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
