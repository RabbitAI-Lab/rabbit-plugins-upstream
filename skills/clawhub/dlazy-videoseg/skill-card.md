## Description:

Segments people in a video and returns a same-length black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators can submit a video for human segmentation and use the returned mask video in downstream compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video processing uploads media to dLazy and its processing providers.

Mitigation: Use videos you are comfortable uploading to dLazy and its processing providers.

Risk: Processing may consume paid credits, and login stores an API key locally.

Mitigation: Check the CLI help before processing, review the estimated cost, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [API key management](https://dlazy.com/dashboard/organization/api-key)
- [Credit balance](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands]

**Output Format:** [JSON result with an output URL; optionally a downloaded mask video file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mask video matches the input video's duration and is intended for downstream compositing or matting.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
