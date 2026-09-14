## Description:

Converts flat-lay garment photos into ghost-mannequin style 3D product images with realistic volume while preserving color, material, pattern placement, and garment proportions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creatives, marketplace sellers, and developers use this skill to transform single flat-lay clothing images into dimensional product shots without hiring models or using visible mannequins. It is intended for clothing catalog images where preserving the garment's fabric, color, labels, and proportions is important.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images and prompts may be sent to the selected cloud image provider.

Mitigation: Use the skill only with images and prompt text that are acceptable to share with the selected provider, and review provider configuration before execution.

Risk: The bundled generator can fetch remote image URLs.

Mitigation: Prefer trusted local image files over remote URLs and avoid running the skill from environments that can reach sensitive internal web services.

Risk: The shared generator supports tasks beyond this to-3d workflow.

Mitigation: Limit agent invocation to the documented to-3d task and review dry-run output before allowing broader generator use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter List](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [Input Example Image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/to-3d/garment-flatlay.jpg)
- [Output Example Image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/to-3d/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell command examples; generated runs save image files such as JPEG outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run mode can emit request previews and estimated credits before sending images to a provider.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
