## Description:

Transcribe uploaded audio through RunAPI with an OpenAI-compatible API. Use for one-off transcription, subtitle output, multilingual hints, or application integration. Prefer the RunAPI CLI for manual requests and the target-language SDK for production integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to transcribe local audio through RunAPI's OpenAI-compatible transcription service, preserve text or subtitle responses, and integrate the same workflow into applications with the target-language SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio submitted through this workflow can be uploaded to RunAPI and OpenAI-compatible transcription services.

Mitigation: Review audio sensitivity before submission and use approved authentication and service configuration for the intended environment.

Risk: Authentication may rely on RUNAPI_API_KEY or saved RunAPI CLI configuration.

Mitigation: Prefer environment authentication or managed CLI config, avoid exposing tokens in request files or logs, and use browser login only when explicitly requested.

Risk: Unexpected returned media URLs may point to files that need validation before use.

Mitigation: Download every requested deliverable, require non-empty files, verify expected MIME type or family, and review files before opening them.

## Reference(s):

- [Model overview, pricing, and rate limits](https://runapi.ai/models/openai-transcription.md)
- [Provider overview](https://runapi.ai/providers/openai.md)
- [Full model catalog](https://runapi.ai/models.md)
- [RunAPI OpenAI Transcription homepage](https://runapi.ai/models/openai-transcription)
- [SDK integration](https://github.com/runapi-ai/openai-transcription-sdk)
- [gpt-transcribe variant](https://runapi.ai/models/openai-transcription/gpt-transcribe.md)
- [whisper-1 variant](https://runapi.ai/models/openai-transcription/whisper-1.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and SDK integration direction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce exact transcription, JSON, SRT, VTT, or downloaded media deliverables after response verification.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
