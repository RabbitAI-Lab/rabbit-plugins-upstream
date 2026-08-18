## Description:

AIGC图像生成 uses LinkFox services to generate or edit images from prompts and reference image URLs, with controls for model, resolution, aspect ratio, quality, and output count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request AI-generated or edited images from reference image URLs, poll asynchronous LinkFox generation jobs, and retrieve saved image files and response JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help create or retrieve account credentials and create payment orders for credits.

Mitigation: Install and use it only when you trust LinkFox and have reviewed the authentication, API-token, and payment-order flows.

Risk: Prompts and reference image URLs are sent to LinkFox services for generation.

Mitigation: Avoid submitting sensitive prompts, private images, or confidential reference URLs unless that data sharing is acceptable.

Risk: Endpoint environment variables can redirect service calls.

Mitigation: Do not override LinkFox endpoint environment variables unless intentionally testing with non-production credentials and trusted endpoints.

Risk: Generated files and API response JSON are stored locally in session directories.

Mitigation: Review local storage locations and handle generated media, response JSON, and API keys according to the user's data-handling requirements.

## Reference(s):

- [AI 生图 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or plain text guidance with shell commands and local file paths; generated images and JSON API responses are saved as files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation runs asynchronously, polls for up to 10 minutes, and can save up to 10 generated images per request.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
