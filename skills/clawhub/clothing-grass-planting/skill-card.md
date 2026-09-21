## Description:

Generates social-commerce lifestyle outfit images by preserving clothing details while changing the model, pose, scene, lighting, and camera framing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to turn clothing photos into social-platform seeding images while keeping garments and accessories faithful and varying scene, model, pose, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and outfit or reference images may be sent to the selected cloud image-generation provider.

Mitigation: Use the skill only with providers and API keys the user trusts, and avoid submitting private, sensitive, or unauthorized images.

Risk: Generated files are written to disk at user-selected paths.

Mitigation: Choose output paths deliberately and review generated files before reuse or publication.

Risk: The workflow changes model identity, pose, scene, and lighting, which can create misleading likeness or endorsement implications.

Mitigation: Do not use private or unauthorized likenesses, and review outputs for consent, attribution, and platform suitability before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Backend call reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; generated assets are saved as JPEG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default generation uses 1024x1536 JPEG output, medium quality, and optional batch runs that create multiple saved files.]

## Skill Version(s):

1.0.10 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
