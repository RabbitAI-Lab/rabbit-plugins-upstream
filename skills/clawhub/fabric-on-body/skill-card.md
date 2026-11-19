## Description:

Creates visual garment previews by replacing the material in a garment reference image with the fabric shown in a swatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers, apparel merchandisers, and e-commerce teams use the skill to preview a garment pattern in different materials before physical sampling. It turns a garment style image and fabric swatch into one or more visual previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious, citing external image processing without a privacy warning; only 5 of 9 components were fully analyzed.

Mitigation: Before proceeding, confirm which provider receives the images and review its data handling terms. Avoid confidential garment or fabric images until those details are clear.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Prompt text, Shell commands, Usage guidance]

**Output Format:** [Garment preview images (JPEG by default) with Markdown prompt and command examples]

**Output Parameters:** [Two image inputs (garment style reference and fabric swatch) produce one or more fabric preview images]

**Other Properties Related to Output:** [Visual preview only; it does not represent real fabric hand feel or weight.]

## Skill Version(s):

1.0.34 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
