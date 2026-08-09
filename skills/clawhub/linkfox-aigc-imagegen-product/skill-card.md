## Description:

Generates non-apparel ecommerce product images, including white-background main images, scene images, close-ups, selling-point layouts, and A+ detail images, either as single outputs or planned image sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to turn product reference images into marketplace-ready product visuals. It supports one-off image generation and planned multi-image sets for non-apparel products such as beauty, electronics, home goods, and food.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and related planning data are sent to LinkFox services during generation.

Mitigation: Use the skill only with product data that may be shared with LinkFox, and avoid submitting confidential or restricted imagery unless your policies allow it.

Risk: The bundled onboarding flow can help manage LinkFox account setup, API keys, and paid plan orders.

Mitigation: Use account, SMS-login, API-key, and payment helpers only in trusted environments and prefer manual account management when handling sensitive credentials or billing.

Risk: Some templates may infer or exclude protected traits for human-containing product scenes.

Mitigation: Review or remove trait-related prompt templates before using the skill for scenes that include people.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-product)
- [LinkFox agent portal](https://agent.linkfox.com/)
- [Runtime workflow index](references/runtime/00-index.md)
- [Runtime planning workflow](references/runtime/01-plan.md)
- [Runtime confirmation workflow](references/runtime/02-confirm.md)
- [Runtime delivery workflow](references/runtime/03-deliver.md)
- [White-background image type](references/types/white-bg.md)
- [Scene image type](references/types/scene.md)
- [Close-up image type](references/types/close-up.md)
- [Selling-point image type](references/types/selling-point.md)
- [A+ image type](references/types/aplus.md)
- [Onboarding and account guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown responses with image references, JSON parameter files, and shell commands for helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local data files, image plan files, image asset manifests, and generated image files during use.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
