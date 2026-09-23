## Description:

ElevenLabs text-to-sound model that generates 1-22 second sound effects from a text description for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to generate short sound effects through the dLazy hosted API and ElevenLabs SFX model. It is suited for foley, ambience, alerts, and game audio assets when users can provide a dLazy API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and file inputs may be sent to the dLazy hosted API and media storage.

Mitigation: Use the skill only with prompts and files that are acceptable to share with dLazy, and review dLazy service terms before use.

Risk: Authentication can persist a dLazy API key in the user's local CLI config.

Mitigation: Prefer scoped keys, restrict local config access to the OS user, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The documented output example shows image fields even though the skill is for sound-effect generation.

Mitigation: Review actual CLI output before integrating downstream automation and update the artifact example to show audio output.

Risk: The skill depends on a third-party CLI and hosted service.

Mitigation: Confirm trust in the pinned dLazy CLI package and service before installing or invoking the skill.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a pinned dLazy CLI command and may return hosted output URLs or save generated audio assets locally when requested.]

## Skill Version(s):

1.3.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
