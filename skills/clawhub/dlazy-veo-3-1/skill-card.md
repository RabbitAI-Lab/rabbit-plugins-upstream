## Description:

Generates cinematic videos with Google Veo 3.1 from text prompts and image or video references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos with Veo 3.1 from prompts, frames, reference images, or an existing video, then retrieve or save the generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt and reference media are sent to dLazy, and local media paths are uploaded for processing.

Mitigation: Submit only media you are comfortable uploading to dLazy.

Risk: Video generation may consume account credits.

Mitigation: Check generation costs with --dry-run before submitting a request.

Risk: The CLI uses an API key stored in the local user configuration or supplied through an environment variable.

Mitigation: Protect the locally saved API key and rotate or revoke it if exposed.

Risk: Installing the skill's separate npm CLI requires trusting that package.

Mitigation: Review the CLI package and its declared source before installing; use the pinned CLI version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated media URLs or saved media files, with JSON status and task details; usage and setup guidance is provided as Markdown with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may run asynchronously; output media is hosted by dLazy unless saved locally.]

## Skill Version(s):

1.3.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
