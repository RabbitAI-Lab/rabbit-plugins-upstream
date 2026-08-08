## Description:

video-analyzer turns local or downloadable videos into structured reports with transcripts, scene and OCR analysis, multimodal alignment, timestamped summaries, editing suggestions, and subtitle or timeline exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content analysts, and editors use this skill to analyze video files or supported video URLs into transcripts, visual scene data, speaker labels, summaries, subtitles, and editing assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release suspicious because it claims offline operation while it can contact the internet, download remote videos with weakened TLS checks, and save sensitive analysis outputs.

Mitigation: Install only when local file access, subprocess execution, and network access are acceptable; for sensitive use, run only on local video files and use --no-update-check.

Risk: Remote downloads may expose the agent to untrusted content and weakened certificate checks.

Mitigation: Avoid authenticated or private platform URLs, prefer pre-downloaded local media, and treat downloaded media and derived reports as untrusted until reviewed.

Risk: Generated transcripts, subtitles, caches, and HTML reports can contain sensitive video or speech content.

Mitigation: Review output directories after each run and delete generated reports, caches, and subtitles when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/video-analyzer)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples plus generated report files such as HTML, JSON, Markdown, SRT, VTT, ASS, EDL, shell scripts, and configuration outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local analysis artifacts and may generate transcripts, subtitles, thumbnails, summaries, platform metadata, and editing timelines depending on command options.]

## Skill Version(s):

4.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
