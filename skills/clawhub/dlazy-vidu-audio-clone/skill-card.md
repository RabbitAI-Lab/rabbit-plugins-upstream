## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Vidu Audio Clone service from an agent workflow, providing text and optional reference audio to create cloned-voice speech output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference audio, prompts, and generated outputs are processed by dLazy's hosted service.

Mitigation: Use the skill only when the user accepts third-party processing and avoid submitting sensitive audio or text unless approved for that service.

Risk: Voice cloning can be misused without consent from the speaker.

Mitigation: Use only voices the user owns or has explicit permission to clone, and follow applicable consent and disclosure requirements.

Risk: The skill requires a dLazy API key that may be stored locally or supplied through an environment variable.

Mitigation: Store keys with restricted local permissions, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing keys in prompts, logs, or shared files.

Risk: Global installation persists the dLazy CLI on the system.

Mitigation: Use the pinned `npx @dlazy/cli@1.2.3` invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated media URLs or asynchronous task identifiers from the hosted dLazy service.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
