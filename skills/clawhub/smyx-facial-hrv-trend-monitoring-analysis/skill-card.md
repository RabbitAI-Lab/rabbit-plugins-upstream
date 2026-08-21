## Description:

Analyzes 30-60 second adult facial videos with rPPG to estimate HRV metrics such as SDNN and RMSSD, summarize trends, and provide stress or fatigue prompts for personal wellness monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit an adult still-seated facial video or video URL for HRV trend analysis, structured metrics, report links, and historical report summaries. The results are wellness trend references and are not a substitute for medical diagnosis or clinical cardiovascular assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video and HRV-related results are sent to a configured backend for analysis.

Mitigation: Use only with informed consent and an approved production HTTPS backend for sensitive biometric and wellness data.

Risk: Report history is tied to an automatically managed identity.

Mitigation: Review account creation, retention, deletion, and history-query behavior before installing or deploying the skill.

Risk: Local SQLite records may include service tokens.

Mitigation: Run the skill in a controlled environment, restrict filesystem access, and remove local records when they are no longer needed.

Risk: The security evidence reports private development backend endpoints for sensitive face-video analysis.

Mitigation: Switch to documented production HTTPS endpoints before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis)
- [Adult facial HRV API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown and JSON analysis reports with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HRV metrics, signal-quality assessment, trend summaries, stress or fatigue prompts, historical report tables, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
