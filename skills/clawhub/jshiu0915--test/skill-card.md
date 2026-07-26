## Description: <br>
Transcribes audio files to text with Baidu Intelligent Cloud speech recognition and writes local transcript, JSON result, and processing report files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jshiu0915](https://clawhub.ai/user/jshiu0915) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Claude Code users use this skill to batch transcribe supported audio files, including Mandarin, English, Cantonese, and Sichuanese recordings, into local text and JSON outputs through Baidu Cloud speech recognition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio files are sent to Baidu Cloud for transcription, which may expose confidential or regulated recordings to an external service. <br>
Mitigation: Use only recordings approved for Baidu Cloud processing and store transcript and JSON outputs in a private directory. <br>
Risk: Baidu API keys and secret keys are required for operation. <br>
Mitigation: Prefer environment variables or a secrets manager and avoid committing credentials in config files or command histories. <br>
Risk: The skill depends on the requests package and external network calls. <br>
Mitigation: Pin or audit dependencies and confirm outbound network access is acceptable before enterprise use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jshiu0915/skills/test) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration] <br>
**Output Format:** [Plain text transcripts, JSON API results, JSON processing reports, and Markdown usage examples with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Baidu API credentials; selected audio files are sent to Baidu Cloud for transcription.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
