## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-resolution images from text prompts and optional reference images for key visuals, posters, and large-format print assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party dLazy npm CLI and hosted API, which receive prompts, selected reference files, generated outputs, and API credentials.

Mitigation: Install or invoke the pinned CLI only after deciding to trust dLazy with that data; use per-invocation credentials where practical and rotate or revoke the dLazy API key when it is no longer needed.

Risk: The CLI may persist the dLazy API key in the local user configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for temporary credentials when persistence is not desired, and protect or remove the local configuration file according to local credential-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions]

**Output Format:** [CLI commands and JSON responses with generated image URLs or saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation, reference images, selectable 2K/3K/4K resolution, common aspect ratios, and optional local save paths.]

## Skill Version(s):

1.2.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
