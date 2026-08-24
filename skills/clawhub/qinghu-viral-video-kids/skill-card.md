## Description:

This skill helps an agent use Qinghu AI's kidswear viral-video imitation workflow to transfer motion from a reference video onto a child model reference image for short product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents use this skill to prepare, price, submit, and monitor Qinghu AI jobs that remake kidswear product videos with a supplied reference video and child model image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global tooling installation and persistent API credentials can expose the environment or paid account if handled casually.

Mitigation: Confirm the qhkit installation scope, prefer platform-managed secrets or scoped environment variables, and avoid sending API keys in chat or persisting them under /root unless the environment requires it.

Risk: The workflow uploads local media, including child model images, to an external paid video service.

Mitigation: Use only self-owned or authorized media, confirm guardian authorization for child-related images, and get explicit user approval after an estimate before submitting paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-kids)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON workflow parameters; qhkit command responses are one-line JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides installation, credential setup, estimate checks, paid job submission, polling, and delivery of generated video URLs from the external Qinghu workflow.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
