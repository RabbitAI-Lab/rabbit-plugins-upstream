## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative production users invoke this skill to generate high-resolution images from prompts and optional reference images through the dLazy hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to a hosted third-party service.

Mitigation: Confirm trust in dLazy before use and avoid sending sensitive prompts or images unless permitted by the user's data policy.

Risk: The skill relies on a local dLazy API key stored in configuration or supplied through DLAZY_API_KEY.

Mitigation: Use OS-restricted config permissions, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation credentials for temporary environments.

Risk: Global CLI installation persists the dLazy CLI on the host.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses containing generated image URLs, with optional downloaded image files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and reference images are sent to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
