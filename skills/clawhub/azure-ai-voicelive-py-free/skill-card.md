## Description: <br>
Provides basic Azure VoiceLive SDK guidance for WebSocket real-time voice conversations, API key authentication, pcm16 streaming audio input and output, and text transcription. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prototype simple Azure real-time voice assistants and validate audio-plus-transcript behavior with the Azure VoiceLive SDK. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Microphone audio and generated transcripts may be sent to Azure Cognitive Services under the user's configured Azure resource. <br>
Mitigation: Use the skill only with appropriate recording consent, avoid sensitive conversations unless permitted, and confirm the Azure resource configuration before use. <br>
Risk: Azure API keys are required for the documented authentication flow. <br>
Mitigation: Store Azure keys in environment variables, rotate compromised keys, and avoid committing credentials to version control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-ai-voicelive-py-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python and bash code blocks plus JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment variable setup, Azure VoiceLive SDK usage examples, error handling guidance, and a structured JSON result example.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
