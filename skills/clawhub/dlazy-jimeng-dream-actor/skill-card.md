## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Jimeng Dream Actor service from an agent workflow, turning a static character image and prompt into generated action-video output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be uploaded to dLazy hosted endpoints for processing.

Mitigation: Use only prompts and media intended for cloud processing, and avoid private images or videos unless upload is intended.

Risk: Authentication stores or uses a dLazy API key.

Mitigation: Protect the local CLI configuration, prefer scoped keys, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A persistent global CLI install may not be appropriate in all environments.

Mitigation: Use the pinned npx invocation when a temporary install is preferred.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or save generated assets locally when requested.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
