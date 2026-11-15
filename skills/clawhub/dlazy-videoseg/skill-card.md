## Description:

Segments people in a video and returns a same-duration black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use this skill to create a human-segmentation mask video for downstream compositing or matting. It requires a dLazy API key and sends input media to the hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan was partial and did not verify that the reported CLI commands perform the advertised video-segmentation task.

Mitigation: Check the CLI command and expected mask output against trusted documentation before relying on a result.

Risk: Input video may be uploaded to dLazy media storage and processed through its hosted API.

Mitigation: Avoid sending sensitive or identifying video unless you have authorization and have reviewed the service's data-handling terms.

Risk: The external CLI requires a dLazy API key for authenticated requests.

Mitigation: Keep the key private, use the documented user-scoped configuration, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy service homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Files, API Calls]

**Output Format:** [JSON result containing a hosted mask media URL and, for asynchronous runs, task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mask video can be downloaded to a local path; local input media is uploaded to the hosted service.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
