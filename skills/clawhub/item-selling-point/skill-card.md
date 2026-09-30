## Description:

Creates Chinese e-commerce product hero images with laid-out selling points and promotional copy from a product photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn a product photo and verified Chinese selling points into a promotional main image with readable copy and a campaign badge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and campaign copy are sent to the selected cloud image provider.

Mitigation: Use a trusted provider and credentials; avoid uploading sensitive unreleased assets unless its policy permits it.

Risk: An untrusted executable selected through DLAZY_BIN could run locally.

Mitigation: Do not set DLAZY_BIN to an untrusted executable.

Risk: Generated text or product appearance may be inaccurate, and promotional claims may be misleading.

Mitigation: Check image fidelity, Chinese text, and the factual basis for product benefits and promotions before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider setup and output reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [JPEG product images, with Markdown guidance and optional JSON run status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically a square main image; review Chinese text, product fidelity, and promotion claims before publication.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
