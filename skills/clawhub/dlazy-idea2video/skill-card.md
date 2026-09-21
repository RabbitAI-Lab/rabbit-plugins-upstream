## Description:

Turns a user's idea into a staged video-production workflow that gathers requirements, produces a reviewable plan, expands it into canvas shapes, and uses dLazy generation and merge models to create a final video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a creative idea into a confirmed video-generation plan, canvas workflow, and dLazy CLI/API generation steps for images, shot videos, and final concatenation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use the dLazy CLI to upload prompts and local media to dLazy services.

Mitigation: Review the workflow before installation and run generation commands only after explicit user confirmation.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use per-session environment variables when practical, and rotate or revoke the key when the CLI is no longer needed.

Risk: Global CLI installation increases trust in the installed package and its pinned source.

Mitigation: Prefer the npx invocation path or verify the pinned package source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated canvas workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in canvas shapes and cloud-hosted media URLs after user confirmation; prompts and local media can be sent to dLazy services.]

## Skill Version(s):

1.3.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
