## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Jimeng Dream Actor workflow, turning a static character image and prompt into an action video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires storing or passing a dLazy API key.

Mitigation: Use the documented dLazy login or auth flow, keep the key scoped to the user's organization, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Selected image, video, or audio files may be uploaded to dLazy's hosted media service for processing.

Mitigation: Confirm the media is appropriate for upload before invocation, especially when broad image-to-video requests could select private files.

Risk: Global installation of the dLazy CLI persists tooling on the local system.

Mitigation: Use the documented npx/on-demand command path when a persistent global CLI is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; runtime CLI responses are JSON with hosted media URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and upload of selected media files to dLazy's hosted service.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
