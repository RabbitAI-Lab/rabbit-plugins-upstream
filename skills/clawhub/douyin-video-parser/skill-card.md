## Description:

Turns a Douyin video link into local Chinese transcript files and a structured content analysis using faster-whisper, without API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers, content operators, and creators use this skill to convert Douyin videos into transcripts, summaries, structural breakdowns, quote candidates, and content-quality judgments for review or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads user-provided Douyin video content and may process private or sensitive media.

Mitigation: Use it only with explicit Douyin links that the user intends to process, and review whether the video content is appropriate before storing or sharing transcripts.

Risk: The skill writes transcript files locally and may fetch a faster-whisper model on first use.

Mitigation: Review the output directory before execution and install or fetch dependencies only in an environment approved for local file writes and model downloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/douyin-video-parser)
- [README](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text transcript files plus Markdown-style analysis and terminal output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes timestamped and plain transcript files named with the video ID; optionally includes model, language, output directory, tag, and MP4 retention settings.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
