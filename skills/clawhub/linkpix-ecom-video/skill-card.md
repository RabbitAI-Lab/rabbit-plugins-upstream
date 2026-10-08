## Description:

Guides agents through creating product, promotional, and talking-head videos with LinkPix, including script planning and turning product images into videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate e-commerce product videos, advertisements, and social-media clips from prompts or product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing external tooling changes the local environment.

Mitigation: Review the qhkit package and use a vetted, pinned CLI version in managed environments; avoid persistent shell-path changes unless intended.

Risk: The provider receives an API token and selected product images or videos.

Mitigation: Confirm the provider and only configure a token and upload media that you are authorized to share.

Risk: Video generation consumes credits and submitted tasks cannot be cancelled.

Mitigation: Confirm parameters and estimated credits before submission where estimates are available.

## Reference(s):

- [LinkPix skill on ClawHub](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video links]

**Output Format:** [Markdown with CLI examples and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation is asynchronous; results and charges depend on the selected model and duration.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
