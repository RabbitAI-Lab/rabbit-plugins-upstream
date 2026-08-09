## Description:

Generates and edits images with Qwen 3 through RunAPI, using the RunAPI CLI for one-off tasks and SDKs for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to generate, edit, or transform images with Qwen 3 through RunAPI. It guides agents toward CLI usage for one-off work and SDK usage for production application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and using the third-party RunAPI CLI or Homebrew tap can execute software outside NVIDIA control.

Mitigation: Confirm the user trusts RunAPI and the Homebrew tap before installation or execution.

Risk: Prompts and images may be sent to RunAPI or Qwen 3 when the skill is used.

Mitigation: Avoid sending sensitive content unless the user accepts the service and data-handling implications.

Risk: API credentials may be stored by the CLI if login or token import is used.

Mitigation: Prefer environment-based RUNAPI_API_KEY handling unless the user intentionally wants saved CLI credentials.

Risk: RunAPI-generated file URLs are temporary and may expire within 7 days.

Mitigation: Download generated assets promptly and store them in durable user-controlled storage.

## Reference(s):

- [RunAPI Qwen 3 model page](https://runapi.ai/models/qwen-3)
- [Qwen 3 model documentation](https://runapi.ai/models/qwen-3.md)
- [Alibaba provider comparison](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Qwen 3 text-to-image variant](https://runapi.ai/models/qwen-3/text-to-image.md)
- [Qwen 3 image edit variant](https://runapi.ai/models/qwen-3/edit-image.md)
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RunAPI CLI commands, SDK integration guidance, authentication setup, and generated file storage reminders.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
