## Description:

ElevenLabs Instant Voice Cloning (IVC) lets an agent upload a clean voice sample to clone a custom voice for ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to create an ElevenLabs instant voice clone from an audio sample through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill wraps a sensitive voice-cloning service that uploads audio and can be misused for impersonation or deceptive content.

Mitigation: Use only audio from speakers who gave explicit permission, avoid impersonation or deceptive uses, and provide only the specific audio file needed for the task.

Risk: The skill stores and uses a dLazy API credential and can install or run a Node CLI.

Mitigation: Prefer npx or a sandbox over a privileged global install, keep the dLazy credential scoped to the task, and rotate or revoke credentials when no longer needed.

Risk: The evidence reports inconsistent command documentation.

Mitigation: Review the command help with `dlazy elevenlabs-voice-clone -h` before executing and confirm required parameters before sending audio.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
