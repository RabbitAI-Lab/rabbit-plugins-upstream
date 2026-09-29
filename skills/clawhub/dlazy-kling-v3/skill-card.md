## Description:

Helps agents generate Kling V3 videos from text prompts or reference images using dLazy's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video or image-to-video generation and obtain a link to the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media files are sent to dLazy's cloud service.

Mitigation: Share only content approved for the service and review its terms before sending sensitive material.

Risk: Using the CLI may save a dLazy API key on the local device.

Mitigation: Use the DLAZY_API_KEY environment variable when persistent local storage is unsuitable.

Risk: The skill runs an external npm CLI.

Mitigation: Review the CLI source and pinned package before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a generated video link, saved file path, or asynchronous task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
