## Description:

青虎AI 短视频数据引擎 helps agents submit Douyin, Xiaohongshu, and Bilibili video links to QinghuAI/QHKit, retrieve play, like, share, favorite, and comment metrics, and export the results as an Excel workbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketing analysts, and agents use this skill to batch request short-video engagement exports for owned or competitor videos, compare performance, and hand off the resulting XLSX file for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting a workflow can consume Qinghu credits.

Mitigation: Run the estimate action first, present the estimated credits and key parameters, and submit only after explicit user approval.

Risk: The Qinghu API key is sensitive and may be stored locally by the CLI.

Mitigation: Treat the key like a password, avoid sharing it in transcripts, and prefer secure environment or local CLI configuration.

Risk: Short or unsupported video links may fail to retrieve metrics.

Mitigation: Use full Douyin, Xiaohongshu, or Bilibili video URLs and refresh field definitions with the options action when unsure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shortvideo-data-engine)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and XLSX file links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single exported Excel workbook per completed workflow run; task submission consumes Qinghu credits after user confirmation.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
