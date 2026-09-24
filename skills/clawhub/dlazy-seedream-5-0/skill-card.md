## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-resolution images through the dLazy hosted Seedream 5.0 workflow from text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files may be sent to a third-party hosted API and media storage service.

Mitigation: Avoid sending sensitive data unless approved for the dLazy service and review organization data-handling requirements before use.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation environment credentials or pinned npx execution when appropriate, and rotate or revoke API keys from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses containing generated image URLs, with optional downloaded image files when a save path is supplied.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K image generation, optional reference images, asynchronous task IDs, and remote file-hosted outputs.]

## Skill Version(s):

1.2.16 (source: server release evidence; artifact frontmatter shows 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
