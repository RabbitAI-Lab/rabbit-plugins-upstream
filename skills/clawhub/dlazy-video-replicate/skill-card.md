## Description:

Analyzes a source video and returns a Seedance 2.0 replication bundle with a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to analyze a source video and prepare a Seedance 2.0 replication bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because some local references were unresolved, leaving related behavior unassessed.

Mitigation: Consider the scan's uncertainty and the CLI login step before installing or using the skill.

Risk: The documented workflow sends prompts to dLazy and uploads supplied local media to its hosted media service.

Mitigation: Use only media you are authorized to share with the service, and avoid uploading sensitive content unless its handling is acceptable to you.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image, Audio, Video]

**Output Format:** [JSON response containing generated media outputs or an asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result includes a replication bundle based on a source video's first frame, audio, and video.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
