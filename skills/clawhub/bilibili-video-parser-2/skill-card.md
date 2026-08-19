## Description:

Converts Bilibili video links into Chinese transcript text and interactive HTML analysis reports, using CC subtitles when available and faster-whisper local transcription when subtitles are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and analysts use this skill to turn user-provided Bilibili links or BV IDs into local transcript files and structured HTML reports for review, summarization, and content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads Bilibili audio or subtitles and may download a Whisper model on first transcription.

Mitigation: Run it only when network access to Bilibili and HuggingFace model downloads are acceptable for the environment.

Risk: Video links, titles, transcript text, and HTML reports can be written to local files or terminal history.

Mitigation: Avoid private or sensitive videos on shared machines, use a controlled output directory, and keep full transcript printing disabled unless needed.

Risk: The generated local HTML report contains content derived from the source video.

Mitigation: Open reports only from trusted runs and keep the artifact behavior that HTML-escapes video-derived text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/bilibili-video-parser-2)
- [Publisher profile](https://clawhub.ai/user/zhouq2039-lang)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Plain text transcript files, single-file HTML reports, optional JSON analysis input, and Markdown guidance with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes transcript and report files locally; terminal output is limited to a transcript preview unless full printing is requested.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
