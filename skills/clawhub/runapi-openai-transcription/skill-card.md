## Description:

Transcribe uploaded audio through RunAPI with an OpenAI-compatible API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to transcribe local audio files through RunAPI for one-off transcription, subtitle output, multilingual hints, and application integration. It guides production integrations toward target-language SDKs while reserving the RunAPI CLI for manual requests and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files and transcription requests may be sent to RunAPI or OpenAI-compatible transcription services.

Mitigation: Confirm that this data flow is acceptable before use and avoid sensitive recordings unless the service handling is approved for the use case.

Risk: API keys or saved CLI authentication state may be present on the user's machine.

Mitigation: Prefer environment-based authentication or managed CLI configuration, and avoid exposing RUNAPI_API_KEY in shared logs, shell history, or committed files.

Risk: Using the CLI as a production runtime layer can create brittle integrations.

Mitigation: Use the target-language SDK integration path for application, backend, worker, or library code and reserve the CLI for manual testing and one-off transcription.

## Reference(s):

- [RunAPI OpenAI Transcription homepage](https://runapi.ai/models/openai-transcription)
- [Model overview](https://runapi.ai/models/openai-transcription.md)
- [OpenAI provider page](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [whisper-1 model reference](https://runapi.ai/models/openai-transcription/whisper-1.md)
- [gpt-transcribe model reference](https://runapi.ai/models/openai-transcription/gpt-transcribe.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CLI commands, SDK package names, multipart request guidance, and transcription response-format guidance.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
