## Description:

文生图 Seedream 5.0 Lite helps agents generate images from text prompts or transform images with reference inputs using Doubao Seedream 5.0 Lite through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to generate new images from text prompts or create image-to-image variations with optional reference images through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths provided to the CLI may be uploaded to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive prompts or media unless the user accepts dLazy's hosted-service handling for that content.

Risk: Authentication can store a dLazy API key in the user's local CLI configuration.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists third-party executable code on the system.

Mitigation: Use the pinned npx invocation for one-off runs or review the referenced package and source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Image URLs, Files]

**Output Format:** [JSON responses containing generated image URLs, with optional downloaded image files when a save path is provided]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation status polling and optional local file download.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
