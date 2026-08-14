## Description:

Generate and edit images with GPT-4o Image through RunAPI. Use when the user asks an agent to create, edit, or transform images with GPT-4o Image. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate, edit, or transform image assets with GPT-4o Image through RunAPI. It supports one-off CLI execution and SDK-based integration while requiring contract discovery, request validation, and deliverable verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image prompts and input media may be sent to RunAPI/OpenAI-backed services.

Mitigation: Use deliberate RunAPI authentication and review request.json before submission when handling private prompts or media.

Risk: Authenticated task submission may trigger paid service usage.

Mitigation: Submit exactly once, preserve task evidence, and avoid replacement submissions without user authorization.

Risk: Generated deliverables may be missing, empty, or not match the expected image media type.

Mitigation: Download every requested media result and verify each file is non-empty with an expected image MIME type before reporting completion.

## Reference(s):

- [RunAPI GPT-4o Image model overview](https://runapi.ai/models/gpt-4o-image.md)
- [RunAPI GPT-4o Image homepage](https://runapi.ai/models/gpt-4o-image)
- [RunAPI OpenAI provider overview](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI GPT-4o Image SDK](https://github.com/runapi-ai/gpt-4o-image-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI CLI authentication and verifies downloaded image deliverables for non-empty content and expected MIME type.]

## Skill Version(s):

0.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
