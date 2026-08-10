## Description:

Analyzes adult still-face video from everyday cameras with rPPG to estimate HRV metrics such as SDNN and RMSSD, summarize trends, and return structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and health-program operators use this skill to submit adult 30-60 second still-face video or a video URL for rPPG-based HRV trend monitoring. It returns HRV metrics, trend status, suggestions, and report links for personal wellness, fatigue, stress, and long-term trend review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video or video URLs may be sent to a remote Life Emergence service for biometric HRV processing.

Mitigation: Use the skill only with the subject's consent and only for videos intended for HRV trend analysis.

Risk: The skill may create or reuse an account-linked identity, store local tokens in the workspace data directory, and retrieve cloud-stored report history.

Mitigation: Install only in workspaces where account-linked report history and local token storage are acceptable, and review workspace data handling before shared use.

Risk: HRV trend output may be mistaken for medical diagnosis or clinical cardiovascular assessment.

Mitigation: Treat results as wellness trend indicators and seek qualified clinical review for medical concerns.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HRV metrics, signal-quality rating, trend status, stress or fatigue prompts, and cloud report export links.]

## Skill Version(s):

1.0.7 (source: server release metadata; SKILL.md frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
