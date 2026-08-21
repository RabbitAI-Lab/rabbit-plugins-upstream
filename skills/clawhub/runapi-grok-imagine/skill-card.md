## Description:

Generate and edit images and videos with Grok Imagine through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate, edit, animate, or transform images and videos with Grok Imagine via RunAPI. Developers can also use it to integrate Grok Imagine workflows into applications or backend systems with RunAPI SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media inputs may be sent to RunAPI or xAI services.

Mitigation: Use the skill only with media and prompts that are appropriate to upload to those services.

Risk: Authenticated API usage may incur billing.

Mitigation: Submit a task only after reviewing the request file and confirming the intended operation.

Risk: Generated request files may include sensitive or unintended content.

Mitigation: Review request JSON before submission and avoid including sensitive content unless explicitly approved.

## Reference(s):

- [RunAPI Grok Imagine homepage](https://runapi.ai/models/grok-imagine)
- [Grok Imagine model documentation](https://runapi.ai/models/grok-imagine.md)
- [xAI provider overview](https://runapi.ai/providers/xai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Grok Imagine SDK integration](https://github.com/runapi-ai/grok-imagine-sdk)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok-imagine)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image or video files after authenticated RunAPI execution; task responses and downloaded media should be validated before reporting completion.]

## Skill Version(s):

0.2.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
