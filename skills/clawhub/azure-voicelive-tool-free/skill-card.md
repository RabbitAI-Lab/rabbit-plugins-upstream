## Description: <br>
Azure语音交互免费版 helps developers build basic real-time Azure VoiceLive applications with WebSocket speech interaction, text and audio responses, session configuration, API key authentication, and PCM16 audio streaming. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to generate guidance, Python examples, shell commands, and configuration steps for Azure VoiceLive prototypes such as voice assistants, text-to-speech dialogs, and simple speech transcription workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad local agent powers and may operate in workspaces that contain sensitive code or secrets. <br>
Mitigation: Review proposed commands and file changes before execution, and use the skill only in workspaces where read, write, and exec access are appropriate. <br>
Risk: The skill handles Azure API keys and configuration values. <br>
Mitigation: Store keys in secure environment variables or a secret manager, and avoid committing credentials to files or logs. <br>
Risk: Voice data or business conversations may be sent to Azure VoiceLive services. <br>
Mitigation: Do not send private speech, customer data, or confidential business data unless Azure use is approved for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-voicelive-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command snippets; examples may include JSON response shapes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs focus on Azure VoiceLive setup, session configuration, audio streaming, error handling, and credential handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
