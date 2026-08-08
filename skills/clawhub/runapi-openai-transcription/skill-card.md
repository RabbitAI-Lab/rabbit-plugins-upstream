## Description:

Transcribe uploaded audio through RunAPI with an OpenAI-compatible API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add or verify audio transcription workflows through RunAPI, including one-off CLI transcription, subtitle output, multilingual hints, and SDK-based application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio submitted for transcription is sent to RunAPI/OpenAI-compatible services and may use an API key or saved CLI authentication.

Mitigation: Use the skill only with audio the user is allowed to share with that provider, and prefer environment authentication or saved CLI configuration for credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-openai-transcription)
- [RunAPI OpenAI transcription homepage](https://runapi.ai/models/openai-transcription)
- [RunAPI OpenAI transcription documentation](https://runapi.ai/models/openai-transcription.md)
- [RunAPI OpenAI provider page](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [whisper-1 transcription model](https://runapi.ai/models/openai-transcription/whisper-1.md)
- [gpt-transcribe model](https://runapi.ai/models/openai-transcription/gpt-transcribe.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and SDK guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes CLI setup guidance, SDK package selection, multipart file input guidance, and transcription response-format handling.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
