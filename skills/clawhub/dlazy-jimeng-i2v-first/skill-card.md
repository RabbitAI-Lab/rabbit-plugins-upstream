## Description:

Generate a video from a single first-frame image and a prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn a still image and text prompt into a Jimeng video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image files are sent to dLazy hosted services for generation.

Mitigation: Avoid sending sensitive or confidential prompts and images unless their use with that service is approved.

Risk: The security review was partial and noted a mismatch between the video-generation description and the shown login command.

Mitigation: Review the instructions and verify the CLI generation command and expected result before installing or running it.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Media assets, JSON]

**Output Format:** [Hosted media URLs with a JSON generation result or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may return a task ID before the media is ready.]

## Skill Version(s):

1.3.39 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
