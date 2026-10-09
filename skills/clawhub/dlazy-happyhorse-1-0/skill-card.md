## Description:

Helps agents create or edit videos with Happy Horse 1.0 using text prompts, first frames, reference images, or existing videos through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide text-to-video, first-frame-to-video, reference-to-video, and video-editing requests through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image, video, or audio files are sent to dLazy; generated outputs are hosted there.

Mitigation: Share only content suitable for the dLazy cloud service and review its terms before submitting sensitive media.

Risk: The CLI may save a dLazy API key on the local device.

Mitigation: Protect local credentials, or supply the key per invocation with DLAZY_API_KEY instead of saving it in the CLI config.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text instructions and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include hosted media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
