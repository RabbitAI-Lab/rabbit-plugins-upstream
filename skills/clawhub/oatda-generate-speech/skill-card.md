## Description: <br>
Generate speech or audio from text using OATDA's unified audio API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devcsde](https://clawhub.ai/user/devcsde) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert supplied text into narrated speech, voiceovers, accessibility audio, or other generated audio through OATDA's unified audio API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for speech generation is sent to OATDA and may be processed by selected text-to-speech providers. <br>
Mitigation: Avoid sending private or regulated text unless OATDA's data handling terms fit the intended use. <br>
Risk: The skill requires an OATDA API key through the environment or a local credentials file. <br>
Mitigation: Store the key in the documented environment variable or credentials file and avoid printing the full key in logs or responses. <br>
Risk: Available audio models, voices, formats, and optional parameters can change over time. <br>
Mitigation: Query the OATDA audio models endpoint before using optional parameters and handle unsupported-model errors by refreshing model choices. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/devcsde/skills/oatda-generate-speech) <br>
- [OATDA Homepage](https://oatda.com) <br>
- [OATDA Audio Models Endpoint](https://oatda.com/api/v1/llm/models?type=audio) <br>
- [OATDA Speech Endpoint](https://oatda.com/api/v1/llm/speech) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash commands and generated audio file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save binary speech audio such as MP3 or WAV to a local file; requires OATDA_API_KEY, curl, and jq.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
