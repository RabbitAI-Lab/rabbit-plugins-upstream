## Description:

Based on facial video, identifies abnormal rhythms such as premature beats, atrial fibrillation, tachycardia/bradycardia, assists in early detection of heart health risks. | 心律失常早期预警技能，基于面部视频识别早搏、房颤、心动过速/心动过缓等异常节律，辅助心脏健康风险早发现

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit a facial video or video URL for cloud-assisted early warning analysis of arrhythmia-related health risks and to retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face videos or video URLs may be sent to LifeEmergence cloud APIs.

Mitigation: Use only intentionally selected video files or URLs and avoid private, sensitive, or tokenized URLs.

Risk: Prior health reports may be queried automatically, and a workspace identity/default account plus tokens may be created and stored locally.

Mitigation: Review account, token, and report-handling behavior before deployment in environments with sensitive health data.

Risk: The output concerns potential cardiac health risks and may be mistaken for diagnosis.

Mitigation: Treat results as screening information only and direct users to professional ECG testing or cardiology care for diagnosis.

## Reference(s):

- [API 接口文档](artifact/references/api_doc.md)
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON structured report, with optional output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk results, recommendations, report links, and historical report lists returned from cloud APIs.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
