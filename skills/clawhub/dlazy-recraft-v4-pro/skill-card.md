## Description:

Generates 4MP high-resolution raster images through the dLazy Recraft V4 Pro CLI for print-ready assets and large-format use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to generate high-resolution raster images from prompts through the dLazy hosted Recraft V4 Pro service. It is suitable for print-ready assets and large-format creative workflows where an agent can call the CLI and return generated image metadata or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI receives the user's dLazy API key and any prompts or local files explicitly passed for generation.

Mitigation: Use a scoped dLazy API key where possible, pass only intended prompts and files, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Installing a global npm CLI can persist third-party code on the local system.

Mitigation: Use the pinned npx invocation or a controlled local install when global installation is undesirable, and review the referenced CLI source or package before use in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON response containing generated image metadata and URLs; optional downloaded image file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Asynchronous runs may return a generation ID for later polling.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
