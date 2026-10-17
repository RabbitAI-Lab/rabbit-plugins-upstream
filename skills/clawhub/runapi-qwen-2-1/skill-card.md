## Description:

Guides agents to generate and edit images with Qwen 2.1 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to create images, transparent-background assets, and mask-based edits with Qwen 2.1 through RunAPI, or to integrate those workflows into applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI access requires authentication, potentially using an API key or saved CLI credentials.

Mitigation: Confirm the publisher is trusted and use approved credentials before submitting requests.

Risk: Local image files included in requests may be uploaded to RunAPI.

Mitigation: Review selected media for sensitive content and obtain authorization before uploading it.

## Reference(s):

- [Qwen 2.1 model overview](https://runapi.ai/models/qwen-2.1.md)
- [Qwen 2.1 model page](https://runapi.ai/models/qwen-2.1)
- [Alibaba provider overview](https://runapi.ai/providers/alibaba.md)
- [Text-to-image variant](https://runapi.ai/models/qwen-2.1/text-to-image.md)
- [Image-editing variant](https://runapi.ai/models/qwen-2.1/edit-image.md)
- [RunAPI SDK integration](https://github.com/runapi-ai/qwen-2.1-sdk)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Code, Guidance]

**Output Format:** [Image files and JSON task responses, with Markdown guidance or integration code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image deliverables are checked for non-empty content and expected MIME type.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
