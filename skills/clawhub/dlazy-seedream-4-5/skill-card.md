## Description:

Generate images from text prompts or reference images using Doubao Seedream 4.5 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text or adapt reference images with Seedream 4.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to the dLazy service.

Mitigation: Send only content you are comfortable sharing with that service.

Risk: An API key may be stored locally for authentication.

Mitigation: Protect the local configuration and rotate the key from the dLazy dashboard if needed.

Risk: Installing the third-party CLI globally leaves a persistent executable on the system.

Mitigation: Review and trust the CLI before installation; use the pinned npx option to avoid a global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance with CLI commands and generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include a generated-image URL, optional saved file path, or asynchronous task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
