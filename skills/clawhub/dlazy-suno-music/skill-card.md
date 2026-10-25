## Description:

Suno music generation model. Supports inspiration mode (auto lyrics) and custom mode (manual lyrics), generating music with or without vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate Suno music from prompts, with optional custom lyrics, vocal settings, and instrumental output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media are sent to the third-party dLazy service.

Mitigation: Submit only prompts and media you are comfortable sharing with that provider.

Risk: Music generation may consume account credits.

Mitigation: Review the cost estimate and account balance before generation; use the documented dry-run option to preview a request.

Risk: The recommended login flow saves an API key in the local CLI configuration.

Mitigation: Protect access to the local account, or provide the key per invocation with the documented DLAZY_API_KEY environment variable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository (declared dependency)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [JSON result with generated audio asset URLs; optionally downloaded audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; asynchronous requests may initially return a task identifier.]

## Skill Version(s):

1.3.32 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
