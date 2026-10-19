## Description:

Guides an agent to synchronize a speaker's mouth in a video with a supplied voice track using dLazy's hosted VideoRetalk service, with an optional reference face for multi-person footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate a talking-person video whose mouth movements match a new speech recording; a reference image can select the subject when multiple faces appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video, audio, or reference images supplied to the command are uploaded to dLazy.

Mitigation: Use only media you are comfortable sending to the hosted service.

Risk: Logging in can store an API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication if you do not want a saved key.

Risk: The workflow installs a third-party CLI package.

Mitigation: Review the pinned @dlazy/cli package before installation when supply-chain controls are required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions with shell commands and example JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results can include a generated-media URL or an asynchronous task ID.]

## Skill Version(s):

1.3.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
