## Description:

Guides agents to create e-commerce video ads from prompts or product images and prepare scripts and storyboards using LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate short product, promotional, and narrated videos for e-commerce campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running a third-party CLI may expose the environment to untrusted tooling.

Mitigation: Install only if the qhkit/LinkPix service is trusted; avoid unpinned npx/latest installs in sensitive environments.

Risk: An API token is required to access the video-generation service.

Mitigation: Use a scoped key where possible and supply it through a managed secret or QHKIT_TOKEN rather than a command-line argument.

Risk: Video generation can consume credits and submitted jobs cannot be canceled.

Mitigation: Check supported estimates before submission, confirm duration and cost, and retain the returned task ID.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with CLI examples and video delivery links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are delivered through task-status URLs; generation consumes credits.]

## Skill Version(s):

0.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
