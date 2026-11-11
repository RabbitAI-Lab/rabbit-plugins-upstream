## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate short videos from text prompts or image inputs, or extend an existing video, with Google Veo 3.1 Fast through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags a login operation that does not clearly match the video-generation description; the scan does not establish how authentication is handled.

Mitigation: Review the pinned CLI installation details and confirm that the separate login and API-key flow fits your needs before installing or authenticating.

Risk: Prompts and local image, video, or audio inputs are sent to dLazy services, and generated media is hosted there.

Mitigation: Avoid submitting sensitive prompts or media unless your use of the service and its terms allow it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Files, JSON, Media URLs]

**Output Format:** [JSON result with generated media URLs and task status; optionally a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier when run without waiting; generated media can be saved locally.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
