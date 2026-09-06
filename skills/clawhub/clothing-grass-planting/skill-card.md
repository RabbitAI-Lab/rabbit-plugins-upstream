## Description:

Creates social-commerce lifestyle outfit images by preserving an input outfit while changing the model, scene, pose, lighting, and framing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and developers use this skill to generate lifestyle social-commerce outfit images from source outfit photos, optionally using a reference image for model, pose, scene, and lighting. It helps prepare content variants while preserving garment colors, materials, fit, and accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may copy a reference model's identity or imply an endorsement in generated lifestyle images.

Mitigation: Use only reference photos where rights and consent are clear, and avoid fake endorsements, identity imitation, or fabricated use experiences.

Risk: Uploaded outfit or model images and prompts may be processed by the selected cloud provider.

Mitigation: Do not upload sensitive images unless the selected provider's data handling terms are acceptable for the intended use.

Risk: The security evidence notes tension between the skill's no-face-swap claim and instructions to reproduce a reference model identity.

Mitigation: Review generated outputs before publication, especially when reference images depict real people.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash examples and generated JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default generation target is 1024x1536 JPEG at medium quality; batch output may save multiple numbered files.]

## Skill Version(s):

1.0.5 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
