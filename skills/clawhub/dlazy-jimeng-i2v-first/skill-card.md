## Description:

Generate dynamic videos from a single first-frame image and a prompt using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a supplied still image and prompt into a short Jimeng video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image files are sent to dLazy's hosted service for generation.

Mitigation: Submit only images and prompts you are comfortable sending to dLazy.

Risk: Video generation can consume account credits.

Mitigation: Review the cost estimate and available credits before submitting a generation request.

Risk: CLI login stores an organization API key in the local user configuration.

Mitigation: Protect access to the local account, or use the supported environment variable for per-invocation authentication; rotate or revoke the key when needed.

Risk: Installing the CLI introduces third-party package code into the environment.

Mitigation: Review the pinned CLI package before installation and consult command help when examples conflict.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Video assets, JSON task and result metadata, Shell commands, Usage guidance]

**Output Format:** [Generated video URL with JSON task/result metadata; Markdown usage guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one first-frame image and a prompt; supports 5- or 10-second videos and asynchronous task IDs.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
