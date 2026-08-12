## Description:

Topaz helps agents upscale and enhance images and video through RunAPI, using the CLI for one-off results and SDK guidance for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent users use this skill to upscale or enhance images and video with Topaz through RunAPI while discovering request contracts, submitting tasks, and verifying media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media may be uploaded to RunAPI or the external Topaz provider.

Mitigation: Confirm the user intends to process the selected files with RunAPI before submitting a task, and avoid uploading unrelated local files.

Risk: RunAPI API usage may create paid tasks or incur provider costs.

Mitigation: Submit each paid task once, preserve task evidence, and require user authorization before retrying or replacing a task after service failure.

Risk: Authentication may expose API credentials if handled carelessly.

Mitigation: Use RUNAPI_API_KEY, saved CLI authentication, or user-approved token import; use browser login only when the user explicitly requests it.

Risk: A successful task status may not prove that requested media deliverables are complete or usable.

Mitigation: Validate the full response contract, download every requested deliverable, and check each file for non-empty content and the expected MIME type before reporting completion.

## Reference(s):

- [RunAPI Topaz model overview](https://runapi.ai/models/topaz.md)
- [RunAPI Topaz homepage](https://runapi.ai/models/topaz)
- [RunAPI Topaz provider overview](https://runapi.ai/providers/topaz.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Topaz SDK](https://github.com/runapi-ai/topaz-sdk)
- [Topaz image upscaling variant](https://runapi.ai/models/topaz/upscale-image.md)
- [Topaz video upscaling variant](https://runapi.ai/models/topaz/upscale-video.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands, JSON request guidance, and SDK integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to create request JSON, run RunAPI CLI tasks, wait for results, download media files, and verify MIME type and completeness.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
