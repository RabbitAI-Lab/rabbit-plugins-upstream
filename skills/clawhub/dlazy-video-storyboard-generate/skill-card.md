## Description:

Converts storyboard context into a video-generation pipeline that can be added to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to read storyboard details, compute video dimensions, build a JSON video pipeline, and add that pipeline to a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or run the dLazy npm CLI and store a dLazy API key locally.

Mitigation: Install only trusted dLazy CLI versions, review local credential storage, prefer scoped environment variables where appropriate, and rotate or revoke API keys when access is no longer needed.

Risk: The skill may send prompts and referenced media files to dLazy cloud services for generation.

Mitigation: Do not provide sensitive prompts or media unless cloud processing is acceptable, and confirm each generation command before execution.

Risk: The security verdict flags broad cloud CLI generation behavior that is less clearly scoped than the storyboard description.

Mitigation: Review the generated commands and required network endpoints before use, and limit execution to storyboard workflows the user explicitly approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON pipeline examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas-ready JSON pipeline definitions and dLazy CLI command guidance.]

## Skill Version(s):

1.2.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
