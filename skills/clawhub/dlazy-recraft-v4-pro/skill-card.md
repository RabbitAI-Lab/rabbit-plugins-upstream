## Description:

Generates 4MP high-resolution raster images through the dLazy Recraft V4 Pro CLI wrapper for print-ready and large-format assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to request high-resolution image generation from prompts through dLazy's hosted Recraft V4 Pro service and receive generated image URLs or saved PNG files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs third-party npm code through the dLazy CLI.

Mitigation: Prefer the pinned on-demand npx invocation when a persistent global install is unnecessary, and review the dLazy CLI source before installing.

Risk: Prompts, selected media files, and generation requests are sent to dLazy's hosted API and file service.

Mitigation: Submit only prompts and files intended for upload to the third-party service.

Risk: Use requires a dLazy API key stored in local CLI configuration or passed through an environment variable.

Mitigation: Use the documented login or auth flow, restrict access to the local config, and rotate or revoke the API key when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [JSON response with hosted image URLs and optional downloaded PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports async task IDs, polling, aspect-ratio selection, dry-run cost estimates, and local save paths.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
