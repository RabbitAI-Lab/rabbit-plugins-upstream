## Description:

Podcast Downloader downloads Xiaoyuzhou podcast audio and show notes, converts episodes to MP3, and supports single or batch downloads with configurable audio quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zymclaw](https://clawhub.ai/user/zymclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to save Xiaoyuzhou podcast episodes and show notes for offline listening or personal archival workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast metadata can control output paths and may overwrite files outside the intended folder.

Mitigation: Review before installing, use a non-synced output directory, keep backups, and avoid untrusted episode URLs until file-name sanitization and output-directory containment are added.

## Reference(s):

- [Podcast Downloader Reference](artifact/reference.md)
- [Xiaoyuzhou](https://www.xiaoyuzhoufm.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; script execution produces MP3 audio files and Markdown show notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, and ffmpeg; behavior can be configured with PODCAST_DIR, AUDIO_QUALITY, and KEEP_M4A.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
