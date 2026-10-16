## Description:

Creates e-commerce ad images and promotional copy, or turns a product video into social post text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers and creative teams use this skill to prepare advertising images and copy for social and shopping channels, or adapt product videos into social posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install or upgrade unpinned third-party Node tooling and change the host environment.

Mitigation: Use a preinstalled, version-pinned qhkit in a managed or disposable environment, and confirm before global installs, upgrades, or shell-profile changes.

Risk: The workflow can persist a qhkit API token on the machine.

Mitigation: Handle tokens as scoped secrets where possible; review local credential storage before configuring qhkit.

Risk: Image generation can consume credits and rendered claims or product details can be inaccurate.

Mitigation: Confirm estimated credits before generating and check image text, numerical claims, and product appearance before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Images, Text, Markdown]

**Output Format:** [Ad images with accompanying ad copy, or social post text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes copy variants and actual credit usage when available; can provide prompts if image generation fails.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
