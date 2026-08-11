## Description:

Video Replicate helps an agent submit source videos to dLazy, extract the first frame and audio, generate a video-understanding prompt, and return a Seedance 2.0 replicate bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external agents use this skill to invoke dLazy's hosted video-replication workflow from a CLI, using selected source videos and generation parameters to produce media outputs or asynchronous task handles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos, audio, images, prompts, and parameters are sent to dLazy's hosted service.

Mitigation: Confirm the user is comfortable sending the selected media and parameters to dLazy before running the command.

Risk: The dLazy API key is stored locally or supplied to the CLI for authentication.

Mitigation: Prefer the pinned npx invocation when avoiding a global install, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or asynchronous task metadata; requires a dLazy API key and uploads selected media to dLazy's hosted service.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
