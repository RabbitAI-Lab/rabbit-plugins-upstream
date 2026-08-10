## Description:

Enhances image clarity and detail for low-resolution assets and returns an upscaled image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to upscale low-resolution images through the dLazy hosted service and retrieve enhanced image URLs for restoration or further production work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to dLazy's hosted service for processing.

Mitigation: Use this skill only with images and prompts that are appropriate to send to the dLazy API and media storage endpoints.

Risk: The dLazy API key is stored locally when using the documented login or auth setup.

Mitigation: Protect the local CLI configuration file, use per-invocation DLAZY_API_KEY where preferable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists tooling on the host environment.

Mitigation: Use the documented npx @dlazy/cli@1.2.3 invocation path when a non-persistent CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON response containing hosted image output URLs, with markdown and shell guidance in the skill documentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service may return an asynchronous task identifier when no-wait mode is used; polling is required to retrieve final output URLs.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
