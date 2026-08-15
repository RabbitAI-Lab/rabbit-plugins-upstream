## Description:

将一个或多个本地视频转写为带每段开始和结束时间的整理版 TXT，并汇总批量处理结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[156554395](https://clawhub.ai/user/156554395)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to convert local video files into timestamped TXT transcripts. It is suited for Chinese-by-default transcription, batch processing, and concise reporting of output paths, segment counts, media duration, and processing time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local video files named by the user and writes transcript TXT files next to those videos or to a selected output path.

Mitigation: Use it only on videos intended for transcription, review output paths before execution, and allow overwrite only when replacing an existing TXT is intended.

Risk: Incorrect language selection can reduce transcription quality, especially because Chinese is the default when no language is specified.

Mitigation: Specify the language explicitly for non-Chinese content and review transcripts before relying on technical terms, numbers, names, or doses.

Risk: The skill invokes local ffprobe and Whisper through uv and stores Whisper models under ~/.cache/whisper.

Mitigation: Install it only in environments where these local tools, model downloads, and cache writes are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/156554395/skills/video-transcript-txt)
- [Publisher profile](https://clawhub.ai/user/156554395)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text TXT transcript files with timestamped segments, plus concise Markdown status summaries and script SUMMARY_JSON lines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One TXT is produced per video; intermediate Whisper files are written to a temporary directory and cleaned up.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
