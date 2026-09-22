## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Seedream 5.0 image generation CLI for high-resolution images from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and provided reference files are sent to dLazy's hosted service.

Mitigation: Use the skill only with content that is acceptable to share with dLazy, and review organization data-handling requirements before use.

Risk: The skill depends on a third-party npm CLI and API-key based authentication.

Mitigation: Use the pinned npx invocation when avoiding a persistent global install, and rotate or revoke the dLazy API key from the dLazy dashboard when needed.

Risk: Local files passed as reference inputs are uploaded to dLazy media storage for model access.

Mitigation: Review file paths before execution and avoid passing confidential or regulated files unless approved for this hosted workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response containing generated image URLs; optional downloaded image file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous calls may return a generateId for later polling.]

## Skill Version(s):

1.2.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
