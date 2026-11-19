## Description:

Converts static character images into action videos using Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a character image into an action video from a text prompt. It sends prompts and selected media to the dLazy hosted service and returns generated media or a task result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and selected local image, video, or audio files to dLazy hosted services.

Mitigation: Only submit prompts and media that are appropriate to share with that service.

Risk: ClawScan reports that the CLI login flow's connection to the stated image-to-video purpose is unclear.

Mitigation: Review the CLI login flow and service information before authenticating or storing an API key.

## Reference(s):

- [Project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Generated media, JSON, Files]

**Output Format:** [JSON result with generated media URLs; optionally a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous mode can return a task ID; the skill documents at most one reference image and one reference video.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
