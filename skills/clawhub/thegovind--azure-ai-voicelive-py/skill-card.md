## Description: <br>
Azure Ai Voicelive Py helps developers build Python applications for real-time bidirectional audio with Azure AI Voice Live, including voice assistants, chatbots, speech translation, transcription, function calling, MCP tools, and avatar integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create Python voice AI applications that connect to Azure AI Voice Live over WebSockets. It provides guidance, code examples, and configuration patterns for authentication, sessions, audio streaming, event handling, turn detection, function calling, MCP tools, transcription, and avatar integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Azure credentials or API keys can be exposed if copied into source code or shared logs. <br>
Mitigation: Use least-privilege Azure credentials, prefer DefaultAzureCredential for production, store secrets outside code, and avoid committing or logging API keys. <br>
Risk: Microphone audio, generated audio, and transcripts may contain sensitive personal or business information. <br>
Mitigation: Obtain consent before recording or streaming speech, minimize retained audio and transcript data, and protect any generated audio files. <br>
Risk: Function calls or MCP tools selected by the model may perform unintended actions if connected to real systems. <br>
Mitigation: Review tool definitions before use, restrict tool permissions, and require approval for actions that affect external services or user data. <br>
Risk: Real-time speech is streamed to an Azure-hosted service endpoint. <br>
Mitigation: Use approved Azure endpoints and configurations that match the organization's privacy, residency, and compliance requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thegovind/skills/azure-ai-voicelive-py) <br>
- [API Reference](references/api-reference.md) <br>
- [Examples](references/examples.md) <br>
- [Models Reference](references/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and shell code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides installation, authentication, session configuration, audio streaming, event handling, function calling, MCP, transcription, and avatar integration guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
