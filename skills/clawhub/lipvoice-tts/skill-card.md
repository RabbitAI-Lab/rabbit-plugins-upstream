## Description: <br>
LipVoice TTS helps agents use the LipVoice enterprise API to create voice-clone models from reference audio, list or delete models, and synthesize text into downloadable WAV audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cxhcccvvvsder](https://clawhub.ai/user/cxhcccvvvsder) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to automate LipVoice voice-cloning and text-to-speech workflows, including uploading reference audio, managing custom voice models, and returning generated WAV files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference audio, synthesis text, and voice model metadata are sent to LipVoice using the user's API key. <br>
Mitigation: Use only authorized voice samples and non-confidential text or recordings unless the user has approval to share them with LipVoice. <br>
Risk: The LipVoice API key grants access to voice model operations. <br>
Mitigation: Prefer the LIPVOICE_API_KEY environment variable or secure secret handling, avoid exposing keys in prompts or logs, and rotate keys if they are disclosed. <br>
Risk: The delete command can remove a selected voice model by audio-id. <br>
Mitigation: Confirm the target audio-id before running deletion commands. <br>
Risk: Generated audio is written to a caller-selected output path. <br>
Mitigation: Verify output paths before execution to avoid overwriting unintended files. <br>


## Reference(s): <br>
- [LipVoice API endpoint](https://openapi.lipvoice.cn/api/third) <br>
- [ClawHub skill page](https://clawhub.ai/cxhcccvvvsder/skills/lipvoice-tts) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Files, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated WAV file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return a local WAV file path and the original generated audio URL after a successful synthesis task.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
