## Description:

Converts garment flat-lay and pose reference images into on-model ecommerce product photos while preserving garment style, color, weave, and fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to generate catalog-style on-model clothing images from flat-lay garment photos, pose references, and optional fixed model-face references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, reference images, model-face images, prompts, and product context may be sent to dLazy or another configured cloud provider.

Mitigation: Use only approved assets and providers, avoid private biometric images or proprietary unreleased catalog assets unless policy and provider terms allow them, and review provider data-handling terms before use.

Risk: Generated virtual try-on images may alter garment color, texture, print placement, fit, anatomy, or background details.

Mitigation: Perform manual quality control before publishing outputs, and rerun with the documented color, material, anatomy, or precise-selection prompt constraints when defects appear.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Skill page](https://clawhub.ai/dlazyai/skills/flat-lay)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands plus generated JPEG image files or JSON provider responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default workflow uses cloud image-generation providers, accepts local paths or image URLs, and can save outputs to local files.]

## Skill Version(s):

1.0.13 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
