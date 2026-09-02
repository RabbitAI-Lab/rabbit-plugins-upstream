## Description:

Generates social-commerce outfit seeding images by preserving a source outfit while changing the model, scene, pose, lighting, and camera style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and content creators use this skill to turn clear outfit photos into lifestyle social-commerce images for posts and product promotion. It guides agents to keep garment details faithful while varying the model, scene, pose, lighting, and camera language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images may contain identifiable people or third-party material without clear permission.

Mitigation: Use only images the user owns or has consent to edit, and avoid identifiable real people unless permission is clear.

Risk: Generated lifestyle images could imply a person endorsed or used a product.

Mitigation: Review outputs before publication and do not use the skill to fabricate endorsements, testimonials, or product experiences.

Risk: Remote image URLs may be fetched or sent to external generation providers.

Mitigation: Prefer local image files or trusted URLs, and avoid submitting sensitive images or images with unclear rights.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save JPEG image outputs and may use local image files or trusted image URLs as inputs.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
