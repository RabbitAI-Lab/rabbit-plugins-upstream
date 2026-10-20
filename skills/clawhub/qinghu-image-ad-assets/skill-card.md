## Description:

Creates e-commerce ad images and marketing copy, or turns a product video into social-media promotional text using Qinghu tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to draft e-commerce ad copy, generate promotional images, and adapt product videos into social-media posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup or upgrades can install remote Node tooling without a fixed version.

Mitigation: Approve installs and upgrades explicitly; prefer an already-reviewed, version-pinned qhkit installation.

Risk: Setup can change the local PATH or shell profile.

Mitigation: Review proposed environment changes before applying them.

Risk: Image generation requires a Qinghu API token that may be stored in local configuration.

Mitigation: Handle the token as a secret and review where it is stored before configuring it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-image-ad-assets)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Images, Guidance]

**Output Format:** [Markdown copy and promotional image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ad-copy variants and actual credit usage when image generation succeeds; provides prompts if generation is unavailable.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
