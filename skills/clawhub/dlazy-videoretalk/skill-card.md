## Description:

Synchronizes a talking person's mouth movements to a supplied voice track, with an optional reference face to select a target in multi-person video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, media editors, and developers use this skill to synchronize a person's mouth movements to a replacement voice track, optionally selecting a face when a video contains multiple people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial: six local references were unresolved, and the login command's connection to the video task was not demonstrated.

Mitigation: Review the referenced CLI and login flow before installing, and proceed only if you are comfortable with its authentication behavior.

Risk: Local video, audio, or reference-image files supplied for processing are uploaded to dLazy media storage for hosted inference.

Mitigation: Submit only media you are authorized to share and are comfortable sending to the service.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project homepage listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video asset URL or saved video file, with JSON result or task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID; the generated asset can be saved to a local path.]

## Skill Version(s):

1.3.43 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
