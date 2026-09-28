## Description:

Generates short videos from text prompts and optional image, video, audio, or first- and last-frame references through dLazy's Seedance 2.0 Fast integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from prompts, multimedia references, or first and last frames using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI executes code outside the skill itself.

Mitigation: Review the pinned @dlazy/cli package before installing or running it.

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Only submit content approved for sharing with dLazy.

Risk: The CLI stores or uses a dLazy API key.

Mitigation: Protect the key and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Video asset links, Video files]

**Output Format:** [JSON response with hosted asset URLs; optional downloaded video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before the video is ready.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
