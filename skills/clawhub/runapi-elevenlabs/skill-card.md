## Description:

Generate speech, dialogue, sound effects, and audio transcription with ElevenLabs through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create ElevenLabs speech, dialogue, sound effects, transcription, and audio isolation outputs through RunAPI. It supports one-off generation through the RunAPI CLI and application integration through RunAPI SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can require RunAPI CLI authentication or an optional RunAPI API key for agent or headless execution.

Mitigation: Confirm RunAPI account and credential handling before installation, prefer environment or saved CLI auth, and avoid exposing RUNAPI_API_KEY in logs or shell history.

Risk: Generated audio file URLs returned by RunAPI are temporary.

Mitigation: Download generated files promptly and move them to durable storage when the output must be retained.

Risk: Using the CLI as a production runtime integration layer can create brittle application behavior.

Mitigation: Use the RunAPI SDK path for application, backend, worker, webhook, or production integration work.

## Reference(s):

- [RunAPI ElevenLabs model page](https://runapi.ai/models/elevenlabs)
- [RunAPI ElevenLabs model documentation](https://runapi.ai/models/elevenlabs.md)
- [RunAPI ElevenLabs provider comparison](https://runapi.ai/providers/elevenlabs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-elevenlabs)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, SDK package names, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce or retrieve audio files through RunAPI; returned generated-file URLs are temporary.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
