## Description:

Generate and edit images with Recraft through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide agents through Recraft image generation and editing with RunAPI, including request setup, task submission, result retrieval, and deliverable verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI that may handle RunAPI authentication, upload selected media, create billable tasks, and save request or result files.

Mitigation: Install and use it only for intended RunAPI/Recraft work, prefer environment or saved CLI authentication, and review requests before task submission.

Risk: A missing service, stale operation contract, or contract mismatch can lead to invalid requests or unintended task behavior.

Mitigation: Inspect installed CLI help and current RunAPI operation documentation before execution, and stop instead of guessing when the contract is unavailable or inconsistent.

Risk: A successful task status may still omit a requested deliverable or return an unexpected media type.

Mitigation: Verify the complete response, download every requested media deliverable, and require non-empty files with the expected MIME type before reporting completion.

## Reference(s):

- [RunAPI Recraft homepage](https://runapi.ai/models/recraft)
- [RunAPI Recraft model documentation](https://runapi.ai/models/recraft.md)
- [RunAPI Recraft provider documentation](https://runapi.ai/providers/recraft.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Recraft SDK integration](https://github.com/runapi-ai/recraft-sdk)
- [Recraft crisp upscale variant](https://runapi.ai/models/recraft/crisp-upscale.md)
- [Recraft remove background variant](https://runapi.ai/models/recraft/remove-background.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON file conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request, task, result, and downloaded media files in the working directory.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
