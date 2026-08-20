## Description:

LinkPix helps agents process ecommerce videos and images through qhkit and local tools, including watermark or subtitle removal, video upscaling, background changes, cleanup, text edits, watermarking, and compression.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to route image and video cleanup or enhancement requests to LinkPix/qhkit workflows. It supports media optimization and secondary creative production for product listings and related commercial content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill may send local images or videos to the LinkPix/qhkit service.

Mitigation: Use it only for media the user is comfortable sending to that service, and avoid uploading sensitive or restricted assets.

Risk: The security review says qhkit may reuse an existing OpenClaw Qinghu token if present.

Mitigation: Confirm token use is expected before running workflows that require authenticated service access.

Risk: The security review says the skill may install or upgrade global Node/npm tooling.

Mitigation: Review installation commands before execution and prefer a controlled environment when persistent system changes are not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-media-tools)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return media task IDs, status guidance, credit estimates, and generated media URLs from qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
