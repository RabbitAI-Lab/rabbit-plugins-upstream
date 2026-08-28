## Description:

Flyelep Generate Kits helps agents use Flyelep API documentation to create ecommerce posters, product images, videos, image edits, translations, background removal, upscaling, and file uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill package to collect required Flyelep API inputs, construct HTTP requests, poll asynchronous tasks, and return generated media URLs for ecommerce creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media files, and the Flyelep API key are sent to Flyelep during use.

Mitigation: Use the skill only when that external transfer is acceptable, provide the API key at runtime, and avoid storing real keys in skill files, examples, or persistent configuration.

Risk: Local media uploads can create public, non-expiring links.

Mitigation: Require explicit confirmation before uploading local files and avoid confidential, personal, regulated, or unreleased media unless the user accepts the exposure.

Risk: Generated images, videos, and transformed media may be unsuitable or incorrect for a product listing without review.

Mitigation: Review returned media URLs and generated assets before publishing or using them in customer-facing ecommerce workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-generate-kits)
- [Flyelep platform](https://www.flyelep.cn)
- [Artifact README](artifact/README.md)
- [Main skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and curl commands; successful API calls return Flyelep media URLs or task IDs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Flyelep secretKey and public media URLs or uploaded media files.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
