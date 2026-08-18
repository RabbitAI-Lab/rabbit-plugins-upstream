## Description:

This skill analyzes child study-area images or video to estimate posture metrics, identify hunchback or head-tilt patterns, and return reminders plus a structured posture report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect child study-area camera inputs to cloud posture analysis, voice-reminder text, and historical posture reports. It is intended for habit feedback and reporting, not medical diagnosis or treatment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child posture videos, video URLs, and generated reports may contain sensitive minor data and are processed by a cloud service.

Mitigation: Use only with guardian consent, confirm data retention and deletion practices, and avoid submitting unnecessary identifying content.

Risk: Results may be tied to a persistent local or remote identity and authentication tokens may be stored.

Mitigation: Review identity handling, token storage, and access controls before deployment, especially for shared devices or school environments.

Risk: Visual posture metrics, including Cobb-angle estimates, may be inaccurate and are not medical diagnosis.

Mitigation: Present outputs as posture habit feedback only and direct medical concerns to qualified clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON posture analysis results with reminder text, report links, and optional history tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual posture estimates, poor-posture categories, reminder text, snapshots, session summaries, and cloud report URLs.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
