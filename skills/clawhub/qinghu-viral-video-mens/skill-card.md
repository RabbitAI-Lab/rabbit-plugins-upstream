## Description:

青虎AI 爆款视频模仿（男装） helps an agent submit a Qinghu workflow that transfers action from a reference video onto a provided male model image to create menswear short-form sales videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to prepare, price, submit, and monitor a Qinghu AI menswear video imitation workflow. It is intended for generating male apparel promotional videos from authorized reference video and model-image inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install and run an unpinned third-party CLI.

Mitigation: Use a pinned, reviewed qhkit version in an isolated project or container before running workflow commands.

Risk: The workflow can upload media and consume paid Qinghu credits.

Mitigation: Confirm with the user before uploading media or submitting paid estimate and generation requests.

Risk: The skill requires a Qinghu API token for workflow execution.

Mitigation: Use a narrowly scoped token that can be rotated and avoid storing it in shared project files.

Risk: Generated output may depend on user-provided likenesses or third-party reference videos.

Mitigation: Use only self-owned or authorized materials and obtain consent for any recognizable person or likeness.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-mens)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow setup, estimate, generate, status, and delivery guidance for qhkit-based media generation.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
