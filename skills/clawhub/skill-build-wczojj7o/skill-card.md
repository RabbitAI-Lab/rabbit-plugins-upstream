## Description:

Extracts speech text and subtitles from local video files across macOS, Windows, and Linux, using Whisper-based offline transcription with multilingual subtitle support and OCR text recognition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe local videos into editable text and timestamped subtitle files for content review, editing, and caption workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flagged recurring promotional messages and a persistent opt-out state file unrelated to transcription.

Mitigation: Review or remove promotional output before deployment and document any persistent state written by the skill.

Risk: The inspected package references transcription scripts that were not included in the artifact.

Mitigation: Verify the referenced scripts before executing installation or pipeline commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-wczojj7o)
- [Publisher profile](https://clawhub.ai/user/guipi888)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; transcription workflows produce TXT, SRT, and WAV files when the referenced scripts are present.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline local processing after dependencies and models are installed; model size and language are configurable.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
