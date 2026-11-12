## Description:

Generates a lip-synced video by matching a talking-person clip to supplied speech audio, with an optional reference face image for choosing a person in multi-face clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize a talking-person video with new speech, optionally selecting the target person with a reference face image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted that the documented login operation does not match the skill's stated lip-sync purpose, and some references could not be resolved during scanning.

Mitigation: Check that this skill and its pinned @dlazy/cli package are the intended ones before installing, and verify any unresolved references.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Video files]

**Output Format:** [JSON result metadata with a generated video URL or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated media is hosted by dLazy and can optionally be saved to a local path.]

## Skill Version(s):

1.3.39 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
