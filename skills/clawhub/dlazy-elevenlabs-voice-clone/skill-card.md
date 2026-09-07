## Description:

ElevenLabs Instant Voice Cloning (IVC). Upload a clean voice sample to clone a custom voice usable with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create an ElevenLabs instant voice clone from a clean authorized voice sample, then use the custom voice with ElevenLabs text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples, prompts, and generated outputs are sent to dLazy-hosted services.

Mitigation: Upload only voice recordings you own or have explicit permission to clone, and avoid submitting sensitive audio unless the dLazy service terms and data handling are acceptable.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Keep the API key scoped to the intended organization, restrict local config access, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A persistent global CLI install expands local dependency and update exposure.

Mitigation: Use the pinned npx invocation or a restricted environment when a non-persistent install posture is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [JSON response with hosted output URLs or asynchronous task status, plus shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and an audio URL or local audio path for the source voice sample.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
