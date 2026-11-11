## Description:

Converts static character images into action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a static character image into an animated action video by supplying a prompt and media to Jimeng Dream Actor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending confidential or sensitive media unless its use with the service is approved.

Risk: The security review was partial and did not clearly connect a reported login action to the skill's video-generation purpose.

Mitigation: Review the CLI package and login flow before installing it or authorizing an account.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated media URL or saved media file, with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and up to one image or video input; asynchronous tasks can return a task ID before completion.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
