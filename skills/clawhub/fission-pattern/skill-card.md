## Description:

Generates a coordinated set of product images from one product photo and its selling points, varying camera angles and scenes for e-commerce use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce creators provide a product photo and selling points to generate a coordinated set of product views, lifestyle scenes, and detail images for a listing or product page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input photos and prompts may be sent to the selected cloud provider for image generation.

Mitigation: Choose the provider explicitly and upload only materials you are permitted to share with that provider.

Risk: A CLI login may retain an API key locally, and an unintended provider, destination, or spend may be selected.

Mitigation: Use a vetted CLI version, protect local credentials, and run a dry-run to review the provider, output destination, image count, and estimated cost.

Risk: Generated images may not preserve every product detail accurately.

Mitigation: Compare the generated set with the source product photo and verify product attributes before publishing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Model flags and parameters](artifact/references/model-flags.md)
- [Provider and data-flow guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Product image files, typically JPEG; the documented default is 1024x1536 at medium quality, with available formats and dimensions depending on provider.]

**Output Parameters:** [Multiple images per set, with varied angles, scenes, and compositions.]

**Other Properties Related to Output:** [Generated using the selected cloud image provider; review product details and visual fidelity before publishing.]

## Skill Version(s):

1.0.25 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
