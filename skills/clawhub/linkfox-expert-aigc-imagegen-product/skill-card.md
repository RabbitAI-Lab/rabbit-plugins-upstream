## Description:

Generates non-apparel ecommerce product images, including white-background main images, scene images, close-ups, selling-point layouts, and A+ detail images, with direct single-image generation or coordinated set planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and product-content teams use this skill to generate product marketing images from supplied product references. It supports single image requests and planned image sets for common ecommerce formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to LinkFox services.

Mitigation: Review product-image and prompt sensitivity before use, and avoid submitting private, regulated, or unreleased materials unless approved.

Risk: Local files can be uploaded to public URLs.

Mitigation: Confirm that any uploaded file is intended for public access before invoking upload-dependent workflows.

Risk: Generated assets, raw responses, and session data may be stored locally.

Mitigation: Run in a controlled workspace and clean up generated artifacts according to the user's data-retention requirements.

Risk: The package includes credential and payment onboarding helpers.

Mitigation: Use only trusted environments for credential configuration and keep billing or account setup separate from routine generation runs.

Risk: Security evidence flags broad local script execution and dynamic script-path behavior.

Mitigation: Review scripts and resolved paths before production use, and run the skill with least-privilege filesystem access.

Risk: Security evidence flags biased human-depiction prompt rules.

Mitigation: Fix or disable biased depiction rules before production use and review generated prompts for fairness-sensitive content.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Runtime index](artifact/references/runtime/00-index.md)
- [Plan phase](artifact/references/runtime/01-plan.md)
- [Confirm and dispatch](artifact/references/runtime/02-confirm.md)
- [Image delivery protocol](artifact/references/runtime/03-deliver.md)
- [White-background image type](artifact/references/types/white-bg.md)
- [Scene image type](artifact/references/types/scene.md)
- [Close-up image type](artifact/references/types/close-up.md)
- [Selling-point image type](artifact/references/types/selling-point.md)
- [A+ image type](artifact/references/types/aplus.md)
- [AI image generation API reference](artifact/skills/linkfox-aigc-imagegen/references/api.md)
- [AI text generation API reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [File upload API reference](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses with image links, JSON parameter and state files, shell commands, and generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores generated assets, task state, raw responses, and manifests in the session workspace.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
