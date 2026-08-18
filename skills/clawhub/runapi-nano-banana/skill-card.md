## Description:

Generate and edit images with Nano Banana through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to generate, edit, or transform images with Nano Banana through RunAPI. It supports one-off CLI workflows and SDK integration workflows for applications or backends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill can make authenticated RunAPI network calls, submit paid tasks, upload request media, and download generated images.

Mitigation: Install only when RunAPI image generation or editing is intended, confirm authentication, review pricing, and avoid sensitive images unless the user accepts sending them to RunAPI.

Risk: A service task can succeed without every requested media deliverable being usable.

Mitigation: Validate the complete response, download every requested media deliverable, and require each file to be non-empty with the expected MIME type before reporting completion.

Risk: RunAPI CLI help and API reference contracts may change or disagree.

Mitigation: Inspect the current installed command help and API reference before building requests, and stop on contract mismatches instead of guessing.

## Reference(s):

- [RunAPI Nano Banana model page](https://runapi.ai/models/nano-banana)
- [RunAPI Nano Banana model documentation](https://runapi.ai/models/nano-banana.md)
- [RunAPI Google provider documentation](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Nano Banana SDK](https://github.com/runapi-ai/nano-banana-sdk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response artifacts, and optional SDK integration code.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or verify downloaded image files when a RunAPI task returns media deliverables.]

## Skill Version(s):

0.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
