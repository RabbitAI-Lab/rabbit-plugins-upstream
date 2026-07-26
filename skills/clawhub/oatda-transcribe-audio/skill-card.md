## Description: <br>
Transcribe audio to text using OATDA's unified audio API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devcsde](https://clawhub.ai/user/devcsde) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to transcribe meetings, podcasts, voice notes, subtitle source audio, and other speech recordings through OATDA. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio selected for transcription is sent to OATDA and may be processed by its configured transcription provider. <br>
Mitigation: Avoid confidential, regulated, or third-party recordings unless external processing is acceptable and any required consent has been obtained. <br>
Risk: The skill requires an OATDA API key for authenticated requests. <br>
Mitigation: Keep the OATDA API key private and avoid printing or sharing the full key. <br>
Risk: Model availability and supported transcription parameters can change over time. <br>
Mitigation: Query the OATDA audio models endpoint before use when a requested model or option fails. <br>


## Reference(s): <br>
- [OATDA](https://oatda.com) <br>
- [OATDA Audio Models API](https://oatda.com/api/v1/llm/models?type=audio) <br>
- [OATDA Transcriptions API](https://oatda.com/api/v1/llm/transcriptions) <br>
- [ClawHub skill page](https://clawhub.ai/devcsde/skills/oatda-transcribe-audio) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and API JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include transcript text, subtitles, segments, word timestamps, language, duration, and cost fields when returned by OATDA.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
