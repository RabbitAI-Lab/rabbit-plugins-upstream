## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to generate or transform images through the dLazy Seedream 5.0 Lite CLI using prompts, optional reference images, size, resolution, and async controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a hosted SaaS CLI that requires a dLazy API key and can store that credential locally.

Mitigation: Treat the API key as a credential, prefer per-invocation environment variables or protected local config, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Prompts, parameters, and local media paths supplied to image inputs are sent to dLazy API and media storage for generation.

Mitigation: Only submit prompts and media files that are appropriate to upload to dLazy, especially in sensitive environments.

Risk: Installing or running npm packages can execute third-party code in the local environment.

Mitigation: Review the dLazy CLI source or package before installation, prefer npx for one-off use, and avoid elevated privileges.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as dLazy-hosted file URLs; async calls can return a generateId for polling.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
