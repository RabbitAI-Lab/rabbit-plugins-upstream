## Description:

Generate coherent transition videos from supplied first and last frames using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create transition videos by providing a prompt and first and last frame images to Jimeng through dLazy's hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service; local media paths may be uploaded for processing.

Mitigation: Send only prompts and media you are comfortable having processed by dLazy, and review its service terms.

Risk: The CLI stores an API key in local user configuration when using its login or auth commands.

Mitigation: Protect the local configuration and key, use the environment variable for per-invocation credentials when appropriate, and rotate or revoke exposed keys.

Risk: Video generation uses account credits, and the skill's examples contain inconsistencies.

Mitigation: Check the installed CLI's help and use its dry-run cost estimate before submitting a paid generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy service](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits settings](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URL or saved video file, with JSON result or asynchronous task metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 5- or 10-second generation; asynchronous jobs can return a task ID for later status checks.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
