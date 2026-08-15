## Description:

Generates e-commerce apparel images such as white-background, model, lifestyle, selling-point, A+ content, and size-chart images from clothing or model reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and agent workflows use this skill to create single apparel images or coordinated apparel image sets from uploaded product/model references, including marketplace-ready detail, promotional, and sizing visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags high-impact account, credential, billing, upload, and persistence behavior.

Mitigation: Review before installing in shared or sensitive environments; use trusted LinkFox endpoints, avoid overriding service base-url environment variables, and provide phone numbers or payment choices only when intentionally using the onboarding or billing flow.

Risk: API keys and generated session artifacts may expose credentials, clothing/model images, image URLs, brand data, or generated plans.

Mitigation: Prefer session-scoped or secret-store API keys, avoid writing keys into shell startup files, and clean up local session artifacts when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-cloth)
- [Runtime workflow index](artifact/references/runtime/00-index.md)
- [Type reference: white background](artifact/references/types/white-bg.md)
- [Type reference: model image](artifact/references/types/model-image.md)
- [Type reference: scene](artifact/references/types/scene.md)
- [Type reference: selling point](artifact/references/types/selling-point.md)
- [Type reference: A+ content](artifact/references/types/aplus.md)
- [Type reference: size chart](artifact/references/types/size.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration files for downstream text and image generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local session artifacts such as prompt parameters, image plans, task results, manifests, and generated image references.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
