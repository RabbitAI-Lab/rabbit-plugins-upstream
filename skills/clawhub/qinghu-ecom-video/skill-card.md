## Description:

Guides agents through creating e-commerce promotional videos, including video generation from prompts or images and storyboard preparation with qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to guide an agent in preparing product-video prompts and storyboards, submitting video-generation jobs, and retrieving finished video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and upgrade instructions can run unreviewed commands or change the user's environment.

Mitigation: Review and approve installations and PATH changes manually; use a pinned, reviewed qhkit version and never execute upgrade commands copied from tool output.

Risk: The external package requires an API token and network access.

Mitigation: Review the external package before installation and provide the token only through an approved configuration method.

Risk: Product images or videos may be uploaded to the provider.

Mitigation: Confirm that the user authorizes sharing each asset before submitting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status, completed video URLs, and credit usage.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
