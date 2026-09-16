## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Vidu Q2 image-to-video service from an agent, supplying prompts, image inputs, and generation settings to produce video assets or asynchronous task IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud service and uploads selected prompts, parameters, and media files to dLazy endpoints.

Mitigation: Pass only media and prompt content intended for upload, and review dLazy service terms before use.

Risk: Use requires storing or passing a dLazy API key.

Mitigation: Prefer the documented login or environment-variable flows, keep the key scoped to the user or organization, and rotate or revoke it from the dLazy dashboard when needed.

Risk: The skill depends on the pinned @dlazy/cli package for execution.

Mitigation: Install only if comfortable running the pinned package, and review package or source provenance when supply-chain risk matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands; command output is JSON containing hosted media URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download generated assets to a local path when the CLI is invoked with --save.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
