## Description:

Image matting separates the foreground from a background and returns a transparent image URL for product photos, portraits, and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can use this skill to remove backgrounds from product photos or portraits and obtain transparent images for compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the image matting purpose and the login/authentication behavior shown, with incomplete scanner coverage.

Mitigation: Review the CLI setup and credential flow before installing, and use the documented key rotation or revocation controls when needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image, JSON]

**Output Format:** [JSON response containing a transparent image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image can optionally be saved to a local path.]

## Skill Version(s):

1.3.42 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
