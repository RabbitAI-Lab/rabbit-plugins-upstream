## Description:

Generates 4MP raster images through the dLazy Recraft V4 Pro CLI wrapper for print-ready assets and large-format creative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can invoke this skill to generate high-resolution raster images from prompts, including print-ready or large-format assets. It is useful when an agent should call a pinned CLI command and return generated image result metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly provided local media files are sent to dLazy cloud endpoints for generation.

Mitigation: Confirm the user trusts dLazy with the prompt and files before use, and avoid sending sensitive content unless permitted.

Risk: The CLI stores a dLazy API key in a local user configuration file or accepts it from the DLAZY_API_KEY environment variable.

Mitigation: Use OS user permissions for the config file, prefer per-invocation secrets where appropriate, and rotate or revoke the key from the dLazy dashboard when access is no longer needed.

Risk: Installing a global CLI persists executable code on the host.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 path when a non-global install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result metadata with generated image URLs and markdown guidance for command usage or errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when --no-wait is used; completed image outputs are hosted as URLs.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
