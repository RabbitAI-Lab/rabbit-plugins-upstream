## Description: <br>
Transcribe audio files using OpenAI's gpt-4o-mini-transcribe model with vocabulary hints and text replacements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darinkishore](https://clawhub.ai/user/darinkishore) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can use this skill to transcribe supported audio files, especially voice memos, and then respond based on the transcript. It supports vocabulary hints and replacement rules for recurring transcription corrections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process private or third-party voice recordings through OpenAI. <br>
Mitigation: Use it only with recordings you are authorized to transcribe, avoid sensitive content unless appropriate safeguards are in place, and confirm consent requirements before use. <br>
Risk: The artifact references an unbundled hard-coded local transcribe command. <br>
Mitigation: Inspect and trust the local transcribe command before installation or execution. <br>
Risk: The skill requires an OpenAI API key and may cache transcripts or audio-derived data. <br>
Mitigation: Use a dedicated API key and verify where cached data is stored and how to delete it. <br>


## Reference(s): <br>
- [Voice Transcribe on ClawHub](https://clawhub.ai/darinkishore/skills/voice-transcribe) <br>
- [uv documentation](https://docs.astral.sh/uv/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration] <br>
**Output Format:** [Plain text transcript with Markdown usage guidance and configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses vocabulary hints and replacement rules; artifact notes English-only behavior and SHA-256 audio caching.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
