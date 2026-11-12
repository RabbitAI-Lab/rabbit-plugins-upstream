## Description:

Generate coherent Jimeng transition videos from supplied first and last frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a prompt and beginning and ending images to generate a short Jimeng transition video, then receive a hosted result or save it locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy-hosted services, and local media paths may be uploaded.

Mitigation: Only submit prompts and images you are authorized to share with the service.

Risk: The security review is benign with medium confidence but incomplete; its guidance calls out the login step and the reviewed content not showing the video-generation operation.

Mitigation: Review the login flow and the skill's referenced behavior, and consider whether you trust the dlazy CLI and its install source before installing.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Generated media, JSON, Shell commands]

**Output Format:** [JSON task results with generated media URLs; optionally a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a prompt and first and last frame images; supports 5- or 10-second generations and asynchronous task results.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
