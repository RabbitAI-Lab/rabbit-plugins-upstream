## Description:

Converts storyboard details into a video-generation canvas pipeline and can guide dLazy CLI-based media generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn storyboard names, dialogue, prompts, aspect ratios, and resolution into a structured audio, image, and video pipeline for a canvas workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a dLazy API key locally for authenticated CLI use.

Mitigation: Use the documented environment variable option for session-scoped credentials when possible, restrict local config access, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Prompts and selected image, video, or audio files may be sent to dLazy services and hosted through dLazy file storage.

Mitigation: Review prompts and media for sensitive content before execution and use the skill only when third-party processing by dLazy is acceptable.

Risk: The security verdict is suspicious because the instructions expand beyond a passive storyboard-to-canvas workflow into terminal-based generation and third-party uploads.

Mitigation: Review the skill before installing, confirm that dLazy CLI execution is intended, and execute one terminal generation command at a time with user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON pipeline snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas pipeline JSON, dLazy CLI commands, and generated media URLs from dLazy services.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
