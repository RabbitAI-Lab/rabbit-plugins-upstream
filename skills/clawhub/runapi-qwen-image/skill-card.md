## Description:

Generate and edit images with Qwen Image through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with Qwen Image through RunAPI, using the CLI for one-off artifacts and SDK guidance for application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media inputs may be uploaded to RunAPI while generating or editing images.

Mitigation: Confirm trust in RunAPI before use, avoid private media unless upload is acceptable, and use a scoped API key where possible.

Risk: A paid async image task could be duplicated if failures are handled by resubmitting instead of waiting on the original task.

Mitigation: Submit once, persist the task id, wait on that task, and retry only when evidence confirms that no task was created and no billing occurred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-qwen-image)
- [RunAPI Qwen Image model overview](https://runapi.ai/models/qwen-image.md)
- [RunAPI Qwen Image homepage](https://runapi.ai/models/qwen-image)
- [Alibaba provider overview](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Qwen Image SDK](https://github.com/runapi-ai/qwen-image-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, SDK integration code, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses RUNAPI_API_KEY or saved RunAPI CLI authentication when available; validates generated media files before reporting completion.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
