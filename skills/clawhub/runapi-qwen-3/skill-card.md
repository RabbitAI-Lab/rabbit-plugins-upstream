## Description:

Generate, edit, and transform images with Qwen 3 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide agents through Qwen 3 image generation and image editing on RunAPI, including contract discovery, request construction, execution, result verification, and bounded recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images used for editing or transformation may be uploaded to RunAPI and may incur API billing.

Mitigation: Avoid confidential media unless the user accepts that remote-service data flow and potential billing before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-qwen-3)
- [Qwen 3 RunAPI homepage](https://runapi.ai/models/qwen-3)
- [Qwen 3 model overview, pricing, and rate limits](https://runapi.ai/models/qwen-3.md)
- [Alibaba provider overview](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Qwen 3 SDK integration](https://github.com/runapi-ai/qwen-3-sdk)
- [Qwen 3 edit image variant](https://runapi.ai/models/qwen-3/edit-image.md)
- [Qwen 3 pro edit image variant](https://runapi.ai/models/qwen-3/pro-edit-image.md)
- [Qwen 3 pro text to image variant](https://runapi.ai/models/qwen-3/pro-text-to-image.md)
- [Qwen 3 text to image variant](https://runapi.ai/models/qwen-3/text-to-image.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, and downloaded image files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the runapi CLI and optional RUNAPI_API_KEY authentication; downloaded media must be non-empty and match the expected image MIME type.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
