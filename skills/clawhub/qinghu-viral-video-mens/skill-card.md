## Description:

青虎AI 爆款视频模仿（男装） helps an agent use qhkit to upload a reference video and model image, estimate cost, submit the Qinghu menswear video-imitation workflow, poll status, and deliver the generated video output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents use this skill to produce menswear short-form sales videos by transferring motion from an authorized reference video onto a supplied model image. The skill guides setup, quote review, paid submission, polling, and final media delivery through Qinghu's qhkit workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request API key handling during setup.

Mitigation: Use a local environment variable, configuration file, or managed secret store; do not paste API keys into chat.

Risk: The skill may install or upgrade qhkit and Node tooling on the local system.

Mitigation: Review installation commands before execution and prefer an isolated environment when local toolchain changes are not acceptable.

Risk: Generating a video is a paid, submit-and-poll workflow that consumes Qinghu credits.

Mitigation: Run estimate first, present the expected credit cost and key parameters, and wait for explicit user approval before calling generate.

Risk: Commercial use of reference videos, model images, or likenesses can create rights and consent issues.

Mitigation: Use only self-owned or properly authorized materials and confirm permission for any person's likeness before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-mens)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON parameters and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces instructions and command invocations for qhkit; completed workflow outputs are media URLs returned by the Qinghu service.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
