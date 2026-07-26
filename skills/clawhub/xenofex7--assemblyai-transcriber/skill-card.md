## Description: <br>
Transcribes audio files or URLs with speaker diarization, timestamps, automatic language detection, and AssemblyAI-backed support for common audio formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, employees, and developers use this skill to transcribe meetings, interviews, podcasts, voice messages, or other selected audio into readable transcripts with optional speaker labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio files or audio URLs are sent to AssemblyAI under the user's API key. <br>
Mitigation: Use only audio the user is permitted to process, avoid confidential or regulated recordings unless terms have been reviewed, and confirm the file path or URL before running transcription. <br>
Risk: The skill requires an AssemblyAI API key, which could be exposed if stored carelessly. <br>
Mitigation: Store the API key in an environment variable or protected local config file and avoid placing secrets in prompts, shared files, or command history. <br>


## Reference(s): <br>
- [AssemblyAI](https://www.assemblyai.com/) <br>
- [AssemblyAI API v2 endpoint](https://api.assemblyai.com/v2) <br>
- [ClawHub skill page](https://clawhub.ai/xenofex7/skills/assemblyai-transcriber) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Text] <br>
**Output Format:** [Markdown transcript with speaker labels and timestamps, or raw JSON when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an AssemblyAI API key and sends selected audio files or audio URLs to AssemblyAI for transcription.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence release version and artifact SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
