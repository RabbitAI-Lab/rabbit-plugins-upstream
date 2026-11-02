## Description:

Generates videos with Kling v3 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can generate videos from text prompts or reference images using Kling v3 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy for generation, and API use may incur charges.

Mitigation: Use only prompts and media you are comfortable sharing with dLazy; review the request and estimated cost with --dry-run before generating.

Risk: Logging in saves an API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option if preferred, and revoke the key when it is no longer needed.

## Reference(s):

- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video assets, JSON]

**Output Format:** [JSON results with generated media URLs or task status; optionally a downloaded video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-video and image-to-video generation with configurable aspect ratio, duration, mode, and sound.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
