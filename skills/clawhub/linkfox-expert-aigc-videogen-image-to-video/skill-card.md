## Description:

Routes image-to-video requests to LinkFox video generation skills for reference-image and first/last-frame workflows across supported models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn one or more hosted images into short videos while selecting between reference-image and first/last-frame generation modes. It validates model-specific parameters, routes to the appropriate LinkFox video skill, and returns local generated-video paths or concise failure guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox's external video service and can send image URLs, prompts, task data, and generated media to that provider.

Mitigation: Use it only for media and prompts that are appropriate to share with LinkFox, and avoid sensitive, private, unlicensed, celebrity, or rights-restricted images.

Risk: Bundled onboarding helpers can handle phone numbers, SMS codes, API keys, plan choices, and payment-order workflows.

Mitigation: Provide credentials, phone verification data, billing choices, or payment actions only when the user explicitly requested that auth or billing flow.

Risk: Endpoint environment variables can redirect requests away from the default LinkFox services.

Mitigation: Do not override LinkFox endpoint variables unless the destination is explicitly trusted and intended for the session.

Risk: Image review or rights-related failures may occur during video generation.

Mitigation: Treat review failures as terminal for that input; ask for compliant replacement media instead of retrying the same image, changing models, or routing around the failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-videogen-image-to-video)
- [图转视频编排参考](artifact/references/api.md)
- [AI 生视频 API 参考（首尾帧/单图模式）](artifact/skills/linkfox-aigc-videogen/references/api.md)
- [多参考图生视频 API 参考](artifact/skills/linkfox-aigc-videogen-multi/references/api.md)
- [解决认证和积分问题](artifact/skills/linkfox-aigc-videogen/references/onboarding.md)
- [编排用例](artifact/examples/test-cases.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown text with local generated-video file paths, command guidance, and concise JSON-derived error or status summaries when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs surface local media paths only; raw video bytes, base64 content, and temporary source URLs are not user-facing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
