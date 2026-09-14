## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images for key visuals, posters, and large-format print assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to invoke dLazy's hosted Seedream 5.0 image-generation workflow from an agent, using text prompts and optional reference images to produce high-resolution visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy API.

Mitigation: Install or invoke it only when the user trusts dLazy and the @dlazy/cli package; prefer npx/on-demand invocation when a persistent global binary is not needed.

Risk: Prompts and referenced local images are sent to dLazy's hosted service for inference and media handling.

Mitigation: Avoid submitting private prompts or images unless the user is comfortable sending that content to dLazy's service.

Risk: The workflow requires a dLazy API key for authenticated requests.

Mitigation: Use the supported login or API-key setup flow, keep the key scoped to the user's organization, and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON result with generated image URLs; optional downloaded image file when a save path is provided]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous generation ID instead of completed outputs when no-wait mode is used.]

## Skill Version(s):

1.2.13 (source: server release evidence; artifact frontmatter is 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
