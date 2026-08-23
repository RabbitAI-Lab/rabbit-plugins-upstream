## Description:

Generates director-level Seedance 2.5 talking-head video prompts for cross-border e-commerce products using product data, review-derived story arcs, hook variants, quality gates, reference binding guidance, and material lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, content creators, and agent operators use this skill to turn ASINs, product links, product images, or direct product descriptions into data-grounded UGC talking-head prompt variants for Seedance 2.5. The skill coordinates product and review collection, strategy cards, multiple prompt variants, quality checks, and reference asset guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product URLs, ASINs, review data, prompts, media URLs, API credentials in headers, and session metadata may be sent to LinkFox services.

Mitigation: Use the skill only for data that may be processed by LinkFox services, review configured gateway and API key environment variables before use, and avoid entering private product or credential data into prompts.

Risk: The bundled workflow can persist local caches, reports, and collected product data.

Mitigation: Run it in an appropriate workspace and periodically clear local LinkFox cache or report directories when product data is sensitive.

Risk: The file upload helper returns publicly accessible URLs.

Mitigation: Invoke file upload only for assets intended for public access and confirm file sensitivity before uploading.

Risk: Remote onboarding installs or feedback submissions may add external dependencies or transmit session information.

Mitigation: Require explicit user approval before remote onboarding installation or feedback submission flows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-ai-talking-video-script-generator)
- [Main Skill Definition](artifact/SKILL.md)
- [Seedance Prompt Structure](artifact/skills/seedance-product-oral-script/references/prompt-structure.md)
- [Seedance Product Binding](artifact/skills/seedance-product-oral-script/references/product-binding.md)
- [Seedance Camera Physics](artifact/skills/seedance-product-oral-script/references/camera-physics.md)
- [LinkFox Text Generation API](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [Amazon Product Detail API](artifact/skills/linkfox-amazon-product-detail/references/api.md)
- [Amazon Reviews API](artifact/skills/linkfox-amazon-reviews-list/references/api.md)
- [Web Data Crawler API](artifact/skills/linkfox-plugin-web-data-crawler/references/api.md)
- [File Upload API](artifact/skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured strategy cards, prompt variants, quality reports, reference binding guidance, and optional JSON or shell-command outputs from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces copy-ready Seedance 2.5 prompt text and supporting recommendations; helper skills may persist reports, cache data, or return public URLs when explicitly used.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
