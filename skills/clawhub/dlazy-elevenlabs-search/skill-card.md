## Description:

Search the ElevenLabs voice library by keyword, source, and category. Returns a playable preview for each matched voice so you can pick the right one before running TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search ElevenLabs' voice library with a short descriptor, filter by voice source and category, and review playable previews before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup requires a dLazy login or API key; the security review noted credential-configuration commands alongside the voice-search purpose.

Mitigation: Before installing or logging in, review the CLI and confirm the dLazy account and local credential storage fit your policies.

Risk: Search prompts and options are sent to the dLazy hosted API.

Mitigation: Avoid including sensitive information in search prompts and confirm the service's data-handling terms meet your requirements.

Risk: The security review was partial because some local references could not be resolved, and it does not establish that the skill is risk-free.

Mitigation: Review the linked CLI and package and apply your normal checks before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured JSON results with voice details and playable preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview links are returned with matching voices when available; results depend on the selected filters and API access.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
