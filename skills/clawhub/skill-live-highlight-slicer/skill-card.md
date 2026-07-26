## Description: <br>
从一段直播录屏（.webm/.mp4/.mov）中自动识别高光时刻并切割为多个短视频片段，支持音频能量、场景变化、音画混合、音画并集和 ASR 关键词五种分析方式，可输出独立片段与合并版视频。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juzanxie-dev](https://clawhub.ai/user/juzanxie-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and media operators use this skill to turn local livestream recordings into short highlight clips and an optional merged highlight reel without manually reviewing and cutting the full recording. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local media and optional transcript files that may contain private or sensitive content. <br>
Mitigation: Run it only on media you are authorized to process and keep generated clips in a controlled local directory. <br>
Risk: The skill writes clips, concat metadata, and segments.json to the selected output directory. <br>
Mitigation: Use a fresh output directory for each run and review generated files before sharing or publishing them. <br>
Risk: Reproducibility can vary when Python package versions are resolved from broad dependency ranges. <br>
Mitigation: Pin or lock dependencies when repeatable installs or production workflows matter. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/juzanxie-dev/skills/skill-live-highlight-slicer) <br>
- [README.md](README.md) <br>
- [SECURITY.md](SECURITY.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, JSON metadata] <br>
**Output Format:** [Markdown guidance with bash commands; runtime outputs MP4 clips, an optional merged MP4, and segments.json.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.9+, ffmpeg, ffprobe, and local access to the input video and output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, CHANGELOG, clawhub.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
