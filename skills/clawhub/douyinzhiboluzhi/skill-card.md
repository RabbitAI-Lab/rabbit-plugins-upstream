## Description: <br>
从一段直播录屏（.webm/.mp4/.mov）中自动识别高光时刻并切割为多个短视频片段，支持音频能量、场景变化、音画混合、音画并集和 ASR 关键词五种分析方式，可输出独立片段与合并版视频。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juzanxie-dev](https://clawhub.ai/user/juzanxie-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, operators, and developers use this skill to analyze local livestream recordings and produce short highlight clips, metadata, and an optional merged highlight compilation for review or redistribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs ffmpeg/ffprobe on local media and writes generated clips plus metadata to an output directory. <br>
Mitigation: Use a dedicated output folder, avoid processing untrusted media in sensitive environments, and review generated files before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juzanxie-dev/skills/douyinzhiboluzhi) <br>
- [Publisher profile](https://clawhub.ai/user/juzanxie-dev) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON metadata, Guidance] <br>
**Output Format:** [MP4 video clips, segments.json metadata, and optional merged MP4 output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local absolute input video paths, ffmpeg/ffprobe, Python analysis dependencies, and an optional ASR transcript for keyword-based slicing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
