## Description: <br>
Translate foreign-language audio into English text using OATDA's unified audio API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devcsde](https://clawhub.ai/user/devcsde) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to translate uploaded or local foreign-language audio into English text through OATDA. It guides API-key setup, model selection, upload format, and common error handling for audio translation requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio files selected for translation are uploaded to OATDA using the user's OATDA API key. <br>
Mitigation: Avoid translating sensitive recordings unless the user is comfortable with OATDA processing that content. <br>
Risk: API keys could be exposed if commands or logs print credential values. <br>
Mitigation: Verify only that the API key exists, and never print the full key. <br>
Risk: Model identifiers and supported audio parameters can change over time. <br>
Mitigation: Query the OATDA audio model list before retrying failed model or parameter requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devcsde/skills/oatda-translate-audio) <br>
- [OATDA](https://oatda.com) <br>
- [OATDA audio model discovery endpoint](https://oatda.com/api/v1/llm/models?type=audio) <br>
- [OATDA translations endpoint](https://oatda.com/api/v1/llm/translations) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash command snippets and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces English translation text from audio files; responses may include language, duration, and cost metadata when OATDA returns JSON.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
