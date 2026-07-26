## Description: <br>
Transcribe audio files using Google's Gemini API or Vertex AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[araa47](https://clawhub.ai/user/araa47) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to convert selected audio files, such as voice messages or recordings, into text through Google Gemini or Vertex AI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio is sent to Google Gemini or Vertex AI for transcription. <br>
Mitigation: Use the skill only with recordings your policy allows to be processed by those cloud services. <br>
Risk: Confidential, regulated, or third-party recordings may require additional approval before cloud processing. <br>
Mitigation: Avoid those recordings unless your organization has approved the data handling path and credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/araa47/skills/gemini-stt) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/araa47) <br>
- [Gemini API models](https://ai.google.dev/gemini-api/docs/models) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text transcription with command-line usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an audio file and either GEMINI_API_KEY or Google Cloud Application Default Credentials.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
