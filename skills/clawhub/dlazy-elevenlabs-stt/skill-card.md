## Description: <br>
ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization for subtitles, transcription, and meeting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to submit audio URLs or local audio files to dLazy's hosted ElevenLabs speech-to-text wrapper and receive transcription-oriented JSON results. It supports common transcription workflows such as subtitles, meeting notes, language detection, and optional speaker diarization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio files, audio URLs, prompts, and parameters are processed through dLazy cloud infrastructure. <br>
Mitigation: Use the skill only with audio that is appropriate for dLazy processing and review the service terms before submitting sensitive content. <br>
Risk: The dLazy API key may be stored in the local CLI configuration when the user logs in. <br>
Mitigation: Use npx for non-persistent CLI execution when preferred, pass DLAZY_API_KEY per invocation when suitable, and rotate or revoke keys that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Async runs may return a generateId for polling with dlazy status.] <br>

## Skill Version(s): <br>
1.3.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
