## Description:

Turns a user-provided Douyin video link into Chinese transcripts and a local interactive HTML analysis report using faster-whisper and rule-based summarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers, content analysts, and creators use this skill to transcribe authorized Douyin videos, review the resulting Chinese transcript, and produce a structured content analysis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads a user-provided Douyin video and a Whisper model, then writes transcripts and an HTML report locally.

Mitigation: Install only when this network and local file behavior is acceptable, use a controlled output directory for sensitive videos, and avoid shared or monitored environments for private content.

Risk: Video links, titles, transcript previews, and optional full transcripts can appear in terminal output.

Mitigation: Keep the default preview behavior for sensitive content and use full transcript printing only in a private terminal.

Risk: The release depends on external Douyin video access and model download availability.

Mitigation: Run it only on videos the user is authorized to process and only in environments where external network access to the disclosed services is allowed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/douyin-video-parser)
- [Publisher profile](https://clawhub.ai/user/zhouq2039-lang)
- [README](README.md)
- [License](LICENSE)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Plain text transcripts, HTML report files, Markdown analysis, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes transcript and report files locally; default terminal output includes only a transcript preview unless full printing is requested.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
