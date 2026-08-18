## Description:

Video Analyzer turns videos into structured local analysis artifacts, including transcripts, scene analysis, multimodal alignment, highlights, editing suggestions, platform analysis, subtitles, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, video creators, and analysts use this skill to process local or downloadable video into searchable transcripts, scene timelines, summaries, subtitles, and editing handoff files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release claims local/offline processing, but security evidence reports network calls and insecure remote-download settings.

Mitigation: Review before installing, prefer local video files, pass --no-update-check in sensitive or offline environments, and avoid remote URLs unless third-party network requests are acceptable.

Risk: Security evidence recommends clarifying persistence and network behavior and improving dependency safety.

Mitigation: Require publisher review of persistence and network behavior, removal of insecure TLS bypasses, and safe dependency version pinning before trusted deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/video-analyzer)
- [Artifact README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [HTML, JSON, Markdown, subtitle files, EDL/Jianying draft exports, and optional shell scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written as files in the selected output directory.]

## Skill Version(s):

4.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
