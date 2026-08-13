## Description:

Generate speech, dialogue, and sound with ElevenLabs through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and external users use this skill to generate speech, dialogue, sound effects, and transcripts through RunAPI while following authentication, contract discovery, result verification, and bounded recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompt or media inputs to RunAPI and ElevenLabs.

Mitigation: Review requests before submission, especially when audio content or prompts are sensitive.

Risk: RunAPI or ElevenLabs usage may incur API costs.

Mitigation: Confirm the selected operation and request payload before submitting paid tasks.

Risk: Interactive browser login may expose account-level access beyond a single request.

Mitigation: Prefer environment authentication, saved CLI configuration, or an imported token over interactive login unless the user explicitly requests it.

## Reference(s):

- [RunAPI ElevenLabs homepage](https://runapi.ai/models/elevenlabs)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/elevenlabs.md)
- [Provider overview](https://runapi.ai/providers/elevenlabs.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/elevenlabs-sdk)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-elevenlabs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response handling, and optional code integration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce or verify audio files, JSON, text, SRT, or VTT outputs returned by RunAPI.]

## Skill Version(s):

0.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
