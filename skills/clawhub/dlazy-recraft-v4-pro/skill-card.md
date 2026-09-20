## Description:

Generates 4MP high-resolution raster images for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and external users use this skill to have an agent call the dLazy Recraft V4 Pro CLI for high-resolution image generation and optional local PNG downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local files may be sent to the dLazy hosted service for image generation.

Mitigation: Confirm the data is appropriate for a third-party cloud service before use and avoid passing sensitive files or prompts unless approved.

Risk: The dLazy API key can be stored in local CLI configuration.

Mitigation: Use per-invocation environment variables when preferred, protect the local config file, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A persistent global CLI install may remain on the system.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred, and review the dLazy CLI source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions]

**Output Format:** [JSON response with generated image metadata and hosted file URLs; optional PNG file download when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports aspect-ratio options, dry-run cost estimates, asynchronous task IDs, polling, and optional local save paths.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
