## Description:

Generates ecommerce advertising images, promotional visuals, and video-derived social commerce copy through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and commerce operators use this skill to create image ads, promotional graphics, and social commerce post copy from product images or short-form videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may trigger global npm or Node installation steps in the execution environment.

Mitigation: Review before installing and prefer preinstalling Node and qhkit through the organization’s normal package-management process.

Risk: The skill may reuse a root-level OpenClaw credential file for qhkit API access.

Mitigation: Use only trusted publisher and account scopes, and prefer explicit scoped credentials through qhkit configuration or QHKIT_TOKEN.

Risk: The skill can consume qhkit API credits while generating media assets.

Mitigation: Run the documented estimate step before generation when credits matter, and report insufficient balance before submitting jobs.

## Reference(s):

- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs, long-running task IDs, credit estimates, and final credit usage.]

## Skill Version(s):

0.1.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
