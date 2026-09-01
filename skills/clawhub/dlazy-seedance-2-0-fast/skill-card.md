## Description:

Generates Seedance 2.0 Fast videos through the dLazy CLI with text prompts, multimodal references, first/last-frame inputs, and configurable resolution, aspect ratio, duration, and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short videos through dLazy's hosted Seedance 2.0 Fast command, optionally using text, image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media passed to the command are uploaded to dLazy cloud endpoints for processing.

Mitigation: Use only media you are authorized to send to dLazy, avoid sensitive inputs unless approved, and review dLazy service terms before use.

Risk: Authentication may save a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when local key persistence is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing the pinned global CLI adds a third-party executable to the user's environment.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 alternative for on-demand execution and review the pinned CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted file URLs; async mode returns a generateId for polling; --save can download output to a local path.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
