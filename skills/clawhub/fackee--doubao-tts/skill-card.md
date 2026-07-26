## Description: <br>
Call the Volcano Engine Doubao Large Model Speech Synthesis V3 API to perform text-to-speech and voice cloning, including public or cloned voice synthesis with configurable speech rate, volume, emotion, and language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fackee](https://clawhub.ai/user/fackee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure and run Doubao speech synthesis workflows, including converting text into audio files and training cloned voices from authorized audio samples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text prompts and voice samples are sent to an external Volcano Engine/ByteDance speech service. <br>
Mitigation: Avoid confidential or regulated content unless the service's retention, billing, and acceptable-use terms have been reviewed for the deployment. <br>
Risk: Voice cloning can be misused when source audio is submitted without consent. <br>
Mitigation: Use only voices the user owns or has explicit permission to clone, and keep consent and usage records for cloned voices. <br>
Risk: Doubao credentials are required for API access. <br>
Mitigation: Keep DOUBAO credentials scoped and protected, do not embed them in shared files or prompts, and rotate them if exposed. <br>


## Reference(s): <br>
- [Doubao TTS API Parameter Reference](references/api-params.md) <br>
- [Volcano Engine Speech Console](https://console.volcengine.com/speech/new) <br>
- [Volcano Engine Public Voice Documentation](https://www.volcengine.com/docs/6561/1257544) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead to local audio files when users run the included synthesis script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
