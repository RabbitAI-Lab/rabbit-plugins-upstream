## Description:

Helps agents generate cinematic videos from text or image inputs using Google Veo 3.1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating videos from prompts, reference images, or an existing video through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media supplied for generation are sent to dLazy's hosted service.

Mitigation: Share only content you are permitted to upload and trust the hosted service before using it.

Risk: Authentication may save a dLazy API key in local configuration.

Mitigation: Protect the local configuration or provide the key per invocation through DLAZY_API_KEY.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video assets]

**Output Format:** [Text guidance and JSON results containing hosted video URLs; optional downloaded media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of a completed asset.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
