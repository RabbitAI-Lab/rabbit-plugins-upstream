## Description: <br>
佛教讲说/复讲/授课/演讲的自动评测与评分工具。上传音频或视频（不支持纯文字稿），自动转写→判定类型级别（叙事/教义/实证 × 初/中/专）→六维打分（教义准确/结构逻辑/语言表达/契机应变/感悟感染/自主发挥）→生成图表化报告。含结构大纲表、来源核验（大藏经CBETA+天台藏）、读稿检测、音频-文本对齐分析。触发词：讲经评测、讲评分析、佛教演讲评分、复讲评价、授课评估、佛学讲说打分。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and reviewers use this skill to evaluate Buddhist lectures, retellings, classes, and talks from audio or video. It transcribes the recording, classifies the talk type and level, scores six quality dimensions, checks cited Buddhist sources, and produces a chart-oriented Markdown report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive recordings may be processed outside the local machine when using IMA or Tencent Cloud transcription. <br>
Mitigation: Use the local faster-whisper path for sensitive recordings when possible, and confirm cloud processing is acceptable to the speakers and audience before using cloud transcription. <br>
Risk: Audio-timing scores can be misleading if the transcript lacks reliable timestamps. <br>
Mitigation: Use only transcription engines that provide word-level or segment-level timestamps, and stop timing-dependent analysis when timestamps are unavailable. <br>
Risk: Buddhist textual claims or quotations may be inaccurate if not checked against the stated source bases. <br>
Mitigation: Check doctrinal assertions and quotations against the L0 and L1 knowledge bases and clearly mark claims that are not found. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gouchunlei2-png/skills/sikll) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with tables, scores, source-check notes, and optional shell commands for local transcription setup] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires timestamped transcription for audio-timing features; if timestamps are unavailable, timing-dependent scoring should stop rather than be estimated.] <br>

## Skill Version(s): <br>
2.12.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
