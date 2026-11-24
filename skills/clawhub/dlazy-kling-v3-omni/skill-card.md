## Description:

Versatile video generation with Kling v3 Omni. Supports multi-modal inputs to generate stunning dynamic videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate videos from prompts, with optional image or video references, using Kling v3 Omni through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, but evidence is incomplete and the reported CLI login action is not clearly connected to video generation.

Mitigation: Review the CLI installation and authentication flow before use, and use only the account credentials needed for the service.

Risk: Prompts and supplied local media are sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive prompts or media unless their transfer and hosting are acceptable for your use case.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Hosted video asset URLs with JSON result and task status metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video duration and aspect ratio depend on the selected generation options; generated assets are hosted by dLazy.]

## Skill Version(s):

1.3.42 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
