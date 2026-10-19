## Description:

Helps agents generate videos from prompts and reference media using Kling v3 Omni through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text prompts, images, or reference video and receive links to the generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI requires trusting the package publisher.

Mitigation: Review the package before use, and prefer the on-demand npx option if a persistent global install is unnecessary.

Risk: Media supplied for generation is uploaded to dLazy's service.

Mitigation: Only submit files and prompts you are comfortable sharing with the service.

Risk: Signing in saves an API key in local user configuration.

Mitigation: Protect local access to the key and rotate or revoke it if compromised.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance and shell commands; invocation results include JSON with generated-media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can be saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
