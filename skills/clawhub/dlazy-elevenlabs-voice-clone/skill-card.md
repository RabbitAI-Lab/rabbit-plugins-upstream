## Description:

Uploads a clean voice sample through the dLazy CLI to create an ElevenLabs Instant Voice Cloning voice for use with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit a voice sample and create a custom ElevenLabs-compatible cloned voice through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to dLazy-hosted services for processing.

Mitigation: Confirm the user is comfortable using the external service and submit only audio the user has the right and consent to clone.

Risk: A global CLI installation and saved API key can persist credentials on the local machine.

Mitigation: Use npx or a per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Voice cloning can be misused to impersonate people or create unauthorized synthetic speech.

Mitigation: Restrict use to authorized voice samples and review generated voice use against consent, identity, and applicable policy requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may return hosted output URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.6 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
