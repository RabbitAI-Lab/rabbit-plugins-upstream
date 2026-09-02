## Description:

Turns a user's video idea into a gated production workflow covering story, characters, portraits, scenes, shots, keyframes, shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a creative prompt into a reviewable video-generation plan, expand it into canvas shapes, and optionally run a dLazy CLI-backed generation workflow after confirmation gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy CLI with cloud processing of prompts and uploaded media.

Mitigation: Review each generation step, prefer the documented canvas workflow, and avoid attaching sensitive local files.

Risk: The workflow can use a locally saved dLazy API key.

Mitigation: Store keys only as needed and rotate or revoke the dLazy API key when access is no longer required.

Risk: The security verdict recommends review before installation because the skill combines a canvas plan workflow with direct terminal execution.

Mitigation: Confirm commands before execution and install only after accepting dLazy CLI use and the associated cloud workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured plan summaries and inline JSON or bash snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses confirmation gates before plan expansion and generation; generated media workflows depend on dLazy CLI and cloud services.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
