## Description:

Generate and edit images with Z-Image through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, or transform images with Z-Image through RunAPI, using the CLI for one-off tasks or SDK references for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, request data, and selected local media inputs may be sent to RunAPI.

Mitigation: Review user intent, selected inputs, RunAPI authentication, and pricing before submitting tasks.

Risk: Image-generation tasks may create billable RunAPI work or upload local media.

Mitigation: Submit only after authentication succeeds, preserve task evidence, and avoid replacement submissions without user authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-z-image)
- [RunAPI Z-Image model overview](https://runapi.ai/models/z-image)
- [RunAPI Z-Image documentation](https://runapi.ai/models/z-image.md)
- [RunAPI Alibaba provider overview](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Z-Image SDK](https://github.com/runapi-ai/z-image-sdk)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown instructions with shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce RunAPI task JSON, downloaded image files, and SDK integration guidance when requested.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
