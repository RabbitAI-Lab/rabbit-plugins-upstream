## Description:

Generates 1MP raster images through the dLazy Recraft V4 CLI for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call dLazy's hosted Recraft V4 image generation service from the CLI, tune prompt and aspect-ratio options, and retrieve generated image URLs or saved PNG assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and eligible local media paths are sent to dLazy hosted API and media storage endpoints.

Mitigation: Avoid passing sensitive local files or confidential prompts unless that SaaS data flow is acceptable for the task.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation API key configuration when less persistence is desired, and rotate or revoke the key when the service is no longer used.

Risk: The skill depends on an external npm CLI package for execution.

Mitigation: Review the referenced CLI source or npm package before installation when supply-chain exposure matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses containing image asset URLs, with optional downloaded PNG files via --save]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation with a task identifier when --no-wait is used; local media paths supplied to relevant fields may be uploaded to dLazy media storage.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
