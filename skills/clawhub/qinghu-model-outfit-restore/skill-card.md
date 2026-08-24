## Description:

青虎AI 模特换装高一致性还原 helps agents submit a Qinghu AI virtual try-on job from a model image and a clothing image, preserving pose, lighting, and clothing detail for e-commerce outfit images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, e-commerce operators, and agents use this skill to run a paid Qinghu AI virtual try-on workflow that places a clothing item onto a provided model image. It is intended for authorized model and clothing assets where consistent pose, lighting, and clothing detail matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads model and clothing images to Qinghu AI.

Mitigation: Use only self-owned or authorized images, avoid sensitive personal material, and confirm that uploads are acceptable for the intended commercial use.

Risk: Generating output can consume paid Qinghu credits.

Mitigation: Run an estimate first, report the expected credit cost, and wait for explicit user confirmation before submitting a generate job.

Risk: The skill can install or upgrade local tooling such as qhkit and Node dependencies.

Mitigation: Prefer preinstalled, pinned, or platform-managed tooling; review install commands before execution in managed environments.

Risk: The workflow requires a Qinghu API token that may be stored locally.

Mitigation: Use platform-managed secrets, environment variables, or an approved config path, and avoid sharing API keys in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-restore)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON parameter files and image result URLs after Qinghu workflow completion.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
