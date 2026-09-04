## Description:

Transcribes uploaded audio through RunAPI using an OpenAI-compatible API for one-off transcription, subtitle output, multilingual hints, and application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to transcribe local audio through RunAPI, preserve returned transcript or subtitle formats, and integrate OpenAI transcription requests through the appropriate SDK for application code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio submitted through this skill is uploaded to a third-party transcription service.

Mitigation: Install and use the skill only when third-party processing is acceptable for the audio; avoid sending sensitive audio unless the user has approved that handling.

Risk: RunAPI authentication may rely on local CLI credentials or an API key.

Mitigation: Prefer environment authentication or saved CLI configuration, import user-provided tokens only when needed, and use browser login only when explicitly requested.

Risk: Generated download URLs and output paths can expose or overwrite transcription deliverables if handled carelessly.

Mitigation: Review generated download URLs and output paths before fetching results, then verify each downloaded file is non-empty and has the expected MIME type.

## Reference(s):

- [RunAPI OpenAI Transcription product page](https://runapi.ai/models/openai-transcription)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/openai-transcription.md)
- [Provider overview](https://runapi.ai/providers/openai.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/openai-transcription-sdk)
- [gpt-transcribe variant](https://runapi.ai/models/openai-transcription/gpt-transcribe.md)
- [whisper-1 variant](https://runapi.ai/models/openai-transcription/whisper-1.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to preserve complete RunAPI responses and validate any downloaded deliverables before reporting completion.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
