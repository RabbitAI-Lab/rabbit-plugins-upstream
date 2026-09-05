## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict plan-first, render-later flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, creative teams, and agent users use this skill to turn a creative brief into cinematic or narrative storyboard plans, character references, generated image prompts, and final storyboard assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires installing or running @dlazy/cli and authenticating with a dLazy API key that may be stored locally or passed through the environment.

Mitigation: Confirm the package and command before installation, protect the local CLI config or environment variable, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Prompts and referenced media files may be sent to dLazy cloud endpoints for generation and result hosting.

Mitigation: Use the skill only with content that is approved for upload to dLazy services, and avoid sensitive prompts or local media unless the user has accepted that data flow.

Risk: Generated shell commands can be sensitive to quoting, local paths, or platform-specific command behavior.

Mitigation: Review each command before execution, avoid shell-sensitive prompt characters where possible, and run generation commands one at a time as the skill workflow requires.

Risk: The artifact contains a version mismatch between server release metadata and skill frontmatter.

Mitigation: Use the server release version for the public card and confirm future artifacts keep release metadata and skill frontmatter aligned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and storyboard prompt structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces staged planning text, confirmation gates, dLazy CLI commands, generated image URLs, and final storyboard assembly guidance.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
