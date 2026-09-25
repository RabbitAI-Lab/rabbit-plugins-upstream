## Description:

Builds real-time Python voice AI applications with Azure AI Voice Live SDK for bidirectional audio streaming, Server VAD, conversation turns, function calling, MCP tools, avatar integration, and transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thegovind](https://clawhub.ai/user/thegovind)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to build Python applications that connect to Azure AI Voice Live for real-time voice assistants, voice-enabled chatbots, speech-to-speech translation, transcription, avatar integration, and WebSocket-based audio streaming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Azure credentials or API keys can be exposed if example authentication patterns are copied without secret handling.

Mitigation: Use a virtual environment, prefer managed credentials where appropriate, store Azure keys securely, and avoid hard-coding real secrets.

Risk: Microphone or audio-file content may be sent to Azure for processing, and generated audio may be saved locally.

Mitigation: Make applications clearly inform users when audio is captured, transmitted, processed, or stored, and align consent and retention with deployment policy.

Risk: Unpinned dependencies can drift from the versions reviewed during development.

Mitigation: Pin and review dependencies before installation or deployment.

## Reference(s):

- [Azure AI Voice Live SDK - API Reference](references/api-reference.md)
- [Azure AI Voice Live SDK - Examples](references/examples.md)
- [Azure AI Voice Live SDK - Models Reference](references/models.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no files are generated unless an agent applies the examples.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
