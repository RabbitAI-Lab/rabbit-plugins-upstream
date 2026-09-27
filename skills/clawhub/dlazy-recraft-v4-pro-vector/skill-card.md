## Description:

High-fidelity text-to-vector generation for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to invoke the dLazy Recraft V4 Pro Vector service from the CLI and generate vector-style assets from prompts. It supports synchronous generation, asynchronous polling, dry-run payload checks, and optional local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided local media files are sent to dLazy hosted endpoints for generation.

Mitigation: Avoid submitting sensitive content unless that use is approved for dLazy's hosted service, and review the service terms before production use.

Risk: The dLazy API key can be saved in the local CLI configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI guidance and JSON responses with generated asset URLs; optional downloaded asset files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Prompts and explicitly provided local media files are sent to dLazy hosted endpoints; asynchronous runs return a generateId for polling.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
