## Description:

Converts Douyin video links into Chinese transcripts and a single-file interactive HTML analysis report using local Whisper transcription and rule-based extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn Douyin videos into readable Chinese transcripts, structured summaries, quote candidates, and HTML reports for content review or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes network requests to Douyin/CDN services, may download a Whisper model from HuggingFace, and may launch a temporary headless browser fallback.

Mitigation: Install and run it only in environments where those network and browser behaviors are acceptable, and review execution before processing a link.

Risk: Transcript text, video titles, and HTML reports are stored locally and can expose private video content on shared or monitored machines.

Mitigation: Avoid processing sensitive videos on shared systems; use --out-dir to control where generated transcript and report files are written.

Risk: The optional cookies.txt fallback can contain account session material.

Mitigation: Use cookies only when required for fallback access, keep the file private, and remove it after use when practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/douyin-video-parser)
- [ClawHub publisher profile](https://clawhub.ai/user/zhouq2039-lang)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with bash commands and local file paths; generated artifacts are UTF-8 text transcripts and a single-file HTML report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write timestamped transcript files and an HTML report to work/ or --out-dir; default terminal output is a 500-character transcript preview.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
