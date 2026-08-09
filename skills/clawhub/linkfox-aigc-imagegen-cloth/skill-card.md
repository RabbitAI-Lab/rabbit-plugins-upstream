## Description:

Generates e-commerce clothing visuals from uploaded model or garment images, including white-background, model, lifestyle, selling-point, A+ content, size-chart, and planned multi-image sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn clothing reference images into single e-commerce assets or coordinated image sets for product listings and marketing content. It routes each requested image type through documented planning, prompt-building, and image-generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes account signup, API key creation, balance checks, and payment-order flows in addition to clothing image generation.

Mitigation: Prefer official LinkFox web pages for signup, billing, and key management; run onboarding commands only after reviewing where credentials and payment artifacts are shown or stored.

Risk: Authentication workflows can expose sensitive account or API key material in command output.

Mitigation: Store the LinkFox API key in the documented environment variable, avoid sharing terminal output containing credentials, and restart the session after configuration changes.

Risk: Billing workflows can create payment orders for selected plans and payment methods.

Mitigation: Confirm plan and payment method choices before order creation, and use the query command only for user-requested payment status checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-cloth)
- [Runtime workflow index](references/runtime/00-index.md)
- [Collection confirmation and dispatch workflow](references/runtime/02-confirm.md)
- [Delivery workflow](references/runtime/03-deliver.md)
- [Model image reference](references/types/model-image.md)
- [Scene image reference](references/types/scene.md)
- [Selling-point image reference](references/types/selling-point.md)
- [A+ image reference](references/types/aplus.md)
- [Size image reference](references/types/size.md)
- [White-background image reference](references/types/white-bg.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with inline image references, JSON parameter files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local media files and JSON state for single-image or multi-image collection workflows.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
