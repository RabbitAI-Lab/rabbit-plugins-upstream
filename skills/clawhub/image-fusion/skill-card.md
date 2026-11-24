## Description:

Combines up to eight product images into a coordinated outfit image on one model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to combine product photos into a coordinated, model-worn outfit image, with optional pose or model references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags possible transmission of product images to external services without a clear privacy disclosure.

Mitigation: Tell users which configured provider receives their images and obtain consent before sending images that require confidentiality.

Risk: The security scan notes a possible mismatch between multi-image requests and the Replicate backend.

Mitigation: When using Replicate, confirm that the selected model and provider support the requested image inputs, then review the generated result.

Risk: The security analysis is incomplete: only 5 of 9 components were fully inspected, and some static checks were degraded.

Mitigation: Treat the scan as inconclusive and review the remaining components before installing or relying on the skill.

## Reference(s):

- [Provider CLI reference](artifact/references/provider-cli.md)
- [Seedream 5.0 model flags](artifact/references/model-flags.md)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/image-fusion)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; generated outfit image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 8 product images, with optional pose and model references; image size and resolution can be selected.]

## Skill Version(s):

1.0.35 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
