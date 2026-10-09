## Description:

Helps Douyin creators and commerce teams prepare and generate short promotional videos using qhkit video tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Douyin creators and e-commerce teams use this skill to plan and generate short product-promotion videos from prompts and selected media, with user approval before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node and npm packages on the host.

Mitigation: Review tooling changes first; preinstall qhkit yourself if preferred.

Risk: Configuring qhkit may persist an API key locally.

Mitigation: Use a scoped or revocable key and avoid persistent shell profile changes unless wanted.

Risk: Selected images and videos may be uploaded to qhkit for processing.

Mitigation: Upload only media you are comfortable sharing with the service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-douyin-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation consumes credits and requires user confirmation before submission.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
