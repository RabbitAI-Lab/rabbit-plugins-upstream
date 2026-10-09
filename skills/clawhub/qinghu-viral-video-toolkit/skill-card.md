## Description:

Helps sellers analyze short videos, adapt their scripts into new marketing videos, and extract audio from video links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and content creators use the skill to analyze a reference short video, adapt its script for their own product, create a new marketing video, or extract its audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external video-generation toolchain may change the local environment.

Mitigation: Pin qhkit in an isolated environment and review PATH or shell profile changes before applying them.

Risk: A qhkit account token grants access to an external service.

Mitigation: Treat QHKIT_TOKEN as a sensitive credential and avoid exposing it in shared outputs.

Risk: Reusing video scripts or extracted background music may infringe others' rights.

Mitigation: Adapt the source structure rather than copying content, and confirm rights before using audio commercially.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-viral-video-toolkit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include script text, video or audio links, task status, and credit usage.]

## Skill Version(s):

0.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
