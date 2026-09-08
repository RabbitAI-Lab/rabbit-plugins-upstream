## Description:

Uses an existing e-commerce model or mannequin photo to replace the model, the background, or both while preserving the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and agents use this skill to create multiple market, demographic, or scene variants from an existing product-on-model image while keeping garment details stable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can fetch arbitrary image URLs and pass image bytes to external AI providers.

Mitigation: Use trusted local files or known public image hosts, avoid internal and metadata-service URLs, and run the skill with outbound network restrictions when possible.

Risk: The sample brand profile may not match the user's intended model demographics or brand requirements.

Mitigation: Edit the brand profile before generation so demographic, styling, and compliance settings match the actual use case.

Risk: Model or background replacement can unintentionally change product details, hand anatomy, lighting, or pose alignment.

Mitigation: Review generated images before publication, keep product invariants explicit in the prompt, and use batch generation for selection when quality is variable.

Risk: The workflow could be misused to imply endorsement or identity transfer by a specific real person.

Mitigation: Do not use the skill for face swaps to specific real people or for fabricated endorsements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown instructions with bash command examples and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are saved when the agent executes the provided commands.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
