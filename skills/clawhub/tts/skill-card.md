## Description: <br>
Convert text to speech using Hume AI or OpenAI when a user asks for an audio message, a voice reply, or spoken output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amstko](https://clawhub.ai/user/amstko) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can use this skill to turn requested text into MP3 speech output through Hume AI by default or OpenAI as a legacy option. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text provided to the skill is sent to Hume AI or OpenAI for speech generation. <br>
Mitigation: Do not use secrets, regulated data, or private content unless the selected provider is approved for the user's use case. <br>
Risk: Dependency versions may change if dependencies are installed from the package manifest instead of the lockfile. <br>
Mitigation: Prefer locked installs and review dependency updates before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/amstko/skills/tts) <br>
- [Hume AI TTS API endpoint](https://api.hume.ai/v0/tts) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [MP3 audio file with shell command guidance and a MEDIA path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires provider API credentials and writes the generated audio to the requested output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
