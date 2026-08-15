## Description:

Generate and edit images with Qwen 2 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with Qwen 2 through RunAPI. It supports one-off CLI-based image tasks and directs application builders to use the SDK integration path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI requests may upload local media supplied by the user.

Mitigation: Review the generated request and media paths before submission, and use only files intended for upload.

Risk: Submitting a RunAPI task may create billable work.

Mitigation: Authenticate intentionally, submit only once per requested task, and require user authorization before replacing failed paid requests.

## Reference(s):

- [RunAPI Qwen 2 homepage](https://runapi.ai/models/qwen-2)
- [Qwen 2 model overview, pricing, and rate limits](https://runapi.ai/models/qwen-2.md)
- [Alibaba provider overview](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Qwen 2 SDK integration](https://github.com/runapi-ai/qwen-2-sdk)
- [Qwen 2 edit-image variant](https://runapi.ai/models/qwen-2/edit-image.md)
- [Qwen 2 text-to-image variant](https://runapi.ai/models/qwen-2/text-to-image.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request, task, result, and downloaded image files when executed by an agent.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
