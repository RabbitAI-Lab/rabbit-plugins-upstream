## Description:

Combines qhkit-powered local commands and service calls to help agents process videos and images, including watermark or subtitle removal, video super-resolution, background cleanup, image editing, compression, and watermarking for ecommerce media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to route ecommerce video and image asset cleanup or enhancement requests through qhkit while preserving confirmation before billable generation tasks. It is especially suited for media optimization and second-use creation workflows such as removing subtitles, improving video resolution, changing image backgrounds, compressing images, or adding watermarks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local or hosted media files may be sent to the qhkit-linked service for processing.

Mitigation: Use the skill only with media the user is comfortable submitting to that service, and confirm the selected files or URLs before generation.

Risk: Billable qhkit generation actions can consume credits.

Mitigation: Run estimates when supported and require explicit user confirmation of model, media, size, duration, and expected credits before submitting generate actions.

Risk: Removing watermarks from content the user does not own or have permission to reuse can create rights issues.

Mitigation: Ask the user to confirm they have reuse rights before performing watermark removal, especially for commercial use.

Risk: The skill requires a qhkit API token for authenticated use.

Mitigation: Handle API tokens as credentials, prefer environment variables or qhkit configuration, and do not expose the token in public outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-media-tools)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu account and API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, status polling instructions, processed media URLs, and credit usage summaries.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
