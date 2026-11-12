## Description:

Converts static images into dynamic videos with the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn still images into short videos by providing a prompt and image or frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security scan found no confirmed malicious behavior, but did not establish how CLI login and credential setup relate to image-to-video generation.

Mitigation: Review the CLI setup instructions and source, and decide whether you are comfortable installing it and providing a dLazy API credential; the scan does not establish credential theft.

Risk: Image and other local media supplied to the skill are uploaded to dLazy media storage for hosted generation.

Mitigation: Only submit media you are authorized to share with the hosted service and are comfortable uploading.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands]

**Output Format:** [Hosted video result URL and JSON task/result metadata; media can optionally be saved as a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous task IDs are returned when requested; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
