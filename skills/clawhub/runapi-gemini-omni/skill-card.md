## Description:

Create Gemini Omni voice resources, character resources, and Flash Preview or multimodal text-to-video tasks through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or manage Gemini Omni voice, character, Flash Preview, and multimodal text-to-video tasks through RunAPI. It is suited for one-off media generation via the RunAPI CLI and for SDK-based integration into applications or backend workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill submits external RunAPI jobs that may involve paid task execution.

Mitigation: Review each request and obtain authorization before submitting paid tasks.

Risk: Selected local media files may be uploaded for processing.

Mitigation: Confirm that the selected files are intended for RunAPI processing before authentication and submission.

Risk: Generated media URLs may not match the requested deliverable type.

Mitigation: Download every requested media deliverable and verify each file is non-empty and has the expected MIME type before reporting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gemini-omni)
- [RunAPI Gemini Omni homepage](https://runapi.ai/models/gemini-omni)
- [RunAPI Gemini Omni documentation](https://runapi.ai/models/gemini-omni.md)
- [RunAPI Google provider overview](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Gemini Omni SDK integration](https://github.com/runapi-ai/gemini-omni-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, code, files]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce RunAPI task requests, status checks, and verified downloaded audio or video files.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
