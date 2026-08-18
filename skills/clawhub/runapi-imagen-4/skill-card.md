## Description:

Generate and edit images with Imagen 4 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, or transform images with Imagen 4 through RunAPI. It supports one-off CLI execution and SDK-based application integration while preserving task evidence and validating image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit paid RunAPI image-generation requests.

Mitigation: Authenticate explicitly, submit only once by default, preserve task evidence, and require user authorization before any replacement paid request.

Risk: The skill requires installing and invoking the RunAPI CLI and may use an API key.

Mitigation: Confirm the user is comfortable installing the CLI and using or providing a RunAPI API key before installation or execution.

Risk: Image URLs or task success statuses can be incomplete or misleading without deliverable checks.

Mitigation: Download every requested image deliverable and verify each file is non-empty with the expected image MIME type before reporting completion.

## Reference(s):

- [RunAPI Imagen 4 model page](https://runapi.ai/models/imagen-4)
- [Imagen 4 model overview, pricing, and rate limits](https://runapi.ai/models/imagen-4.md)
- [RunAPI Google provider overview](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Imagen 4 SDK integration](https://github.com/runapi-ai/imagen-4-sdk)
- [imagen-4 variant](https://runapi.ai/models/imagen-4/imagen-4.md)
- [imagen-4-fast variant](https://runapi.ai/models/imagen-4/fast.md)
- [imagen-4-pro-remix-image variant](https://runapi.ai/models/imagen-4/pro-remix-image.md)
- [imagen-4-ultra variant](https://runapi.ai/models/imagen-4/ultra.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to preserve task and result JSON, download every requested image deliverable, and verify non-empty image files with expected MIME types.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
