## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving the spoken script text exactly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and production teams use this skill to turn structured short-video copy into shot-by-shot storyboard scripts with scene, camera, lighting, and spoken-script guidance. It is also useful for agents that need a consistent Markdown storyboard format before downstream video planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags the release as suspicious because a text storyboard helper also includes a cloud media-generation CLI workflow.

Mitigation: Install it only when the dlazy cloud workflow is intended; for text-only storyboard generation, review whether the CLI workflow is necessary before installing.

Risk: The security evidence notes that use may require a dlazy API key, local credential storage, prompt submission to dlazy services, media-file uploads, and confirmed CLI command execution.

Mitigation: Use an appropriate dlazy account, avoid sending sensitive prompts or media unless permitted, and rotate or revoke API keys through the dlazy control panel when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown storyboard script with global video parameters and repeated per-shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves user-provided spoken script text word for word and defaults missing video parameters to 9:16 and 720p.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
