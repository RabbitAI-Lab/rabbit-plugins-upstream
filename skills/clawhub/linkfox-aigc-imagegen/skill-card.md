## Description:

Generates images from prompts and reference image URLs using LinkFox AIGC models, with controls for resolution, aspect ratio, quality, and output count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create or edit images from a prompt and at least one reference image URL through LinkFox image generation services. It can return one or more generated images while preserving response metadata for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and reference image URLs to LinkFox services and stores generated images and response metadata locally.

Mitigation: Review prompts, reference URLs, and saved output paths before use with sensitive or restricted content.

Risk: The package includes account, API-key, plan selection, and payment-order workflows beyond image generation.

Mitigation: Review the onboarding flow before installation or execution, and only proceed with account or payment actions after explicit user intent.

Risk: API keys may be exposed through shared terminals, logs, or copied configuration commands.

Mitigation: Keep LinkFox API keys out of logs and shared terminals, and rotate credentials if they are exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen)
- [AI 生图 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, image files, JSON, shell commands, configuration, guidance]

**Output Format:** [Stdout text containing saved local file paths, plus generated image files and JSON response metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally under the session media directory; raw API responses are saved under the session data directory.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
