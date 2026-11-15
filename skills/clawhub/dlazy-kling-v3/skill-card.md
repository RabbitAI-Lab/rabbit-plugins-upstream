## Description:

Generate videos with Kling v3 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from text prompts or reference images, with options for aspect ratio, duration, quality mode, and sound.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy-hosted services for generation.

Mitigation: Avoid submitting confidential or personal media unless you are authorized to share it and it is appropriate under the service terms.

Risk: The security review had medium confidence and incomplete evidence around the referenced CLI login flow.

Mitigation: Review the install and login steps and the CLI package before providing credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [Generated media asset with a JSON result containing hosted output URLs; media can optionally be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return asynchronously; results can include video or other media assets.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
