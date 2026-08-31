## Description:

HeyGen Lipsync Speed is a dLazy CLI skill for fast lip-sync generation when quick turnaround is important.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy's HeyGen Lipsync Speed model from an agent workflow, supplying video and audio inputs for cloud-hosted lip-sync generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and provided media files to dLazy cloud API endpoints.

Mitigation: Only submit media you are comfortable uploading to dLazy, and review the service's data handling expectations before use.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for one-off execution when a saved local key is not desired, and rotate or revoke organization keys when needed.

Risk: The workflow depends on a pinned third-party CLI package.

Mitigation: Review the pinned @dlazy/cli package before installation in managed or sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs; asynchronous runs may return a generation ID for later polling.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
