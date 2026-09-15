## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition. Suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Seedream 5.0 Pro image-generation workflow from an agent. It supports prompt-based generation with optional image inputs for commercial key visuals, brand assets, and other high-detail visual outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a hosted image-generation API and uploads prompts, parameters, and referenced local media to dLazy endpoints.

Mitigation: Only provide prompts and media files that are intended for upload to dLazy, and review dLazy's service terms before using sensitive content.

Risk: Authentication requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the API key as a credential, restrict local access to the machine and config file, and rotate or revoke the key if the environment may be compromised.

Risk: Installation or execution depends on npm or npx and the third-party dLazy CLI package.

Mitigation: Review the linked dLazy CLI source or npm package before installing, avoid elevated privileges for npm commands, and prefer npx when a persistent global binary is not needed.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response containing generated image output URLs, with optional downloaded image files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return task metadata for later polling instead of immediate output URLs.]

## Skill Version(s):

1.2.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
