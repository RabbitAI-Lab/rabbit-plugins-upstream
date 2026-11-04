## Description:

Creates a lip-synced video from a talking-person video and a voice audio track, with an optional reference face image for selecting the target person.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a speaker's mouth movements in a video with a new voice track. They can provide a reference face image to select the target person when a video contains multiple faces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, audio, and optional face-reference media provided to the skill are uploaded to dLazy's hosted service.

Mitigation: Use only media you are comfortable uploading, and review the service terms before submission.

Risk: The CLI stores the dLazy API key in a local user configuration file.

Mitigation: Protect the local configuration and rotate or revoke the key from the dLazy organization dashboard if needed.

Risk: Generation can incur service costs.

Mitigation: Review generation costs before submitting a request.

## Reference(s):

- [dLazy CLI source code (referenced by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video asset URL with JSON task or result metadata; command-line invocation and options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated video is hosted by dLazy; local media provided as input is uploaded to its hosted media service.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
