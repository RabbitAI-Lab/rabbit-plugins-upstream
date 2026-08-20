## Description:

Guides an agent through Qinghu AI's qhkit workflow to create men's apparel short videos by transferring motion from a reference video to a supplied model image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content-production agents use this skill to prepare, estimate, submit, and monitor a Qinghu AI men's apparel video imitation workflow using authorized reference videos and model images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-provided videos and images to Qinghu AI.

Mitigation: Confirm the user trusts the qhkit CLI and Qinghu AI service before installation or upload.

Risk: The workflow can process likenesses and commercial media, creating consent and rights risks.

Mitigation: Use only media and likenesses that the user owns or is authorized to use.

Risk: The workflow is paid and charges by reference video duration.

Mitigation: Run an estimate with the actual input video, disclose the credit cost, and wait for user confirmation before generation.

Risk: API tokens are required for qhkit access.

Mitigation: Keep the token private and use the documented qhkit configuration or environment-variable paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-mens)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, job status, log IDs, quoted or final credit usage, and user-facing error messages from the qhkit workflow.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
