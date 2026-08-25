## Description:

Analyzes child study-area posture video from a smart desk lamp or desk-mounted camera to estimate spinal curvature and head tilt, generate posture findings, and return reminder text when poor posture persists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to add child posture monitoring to smart lamps, home desks, or classroom study environments. It accepts local or URL-based posture video, calls the analysis workflow, and returns structured posture metrics, reminder text, report links, or historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child video, video URLs, posture reports, and report history may be sent to or retrieved from cloud services.

Mitigation: Use only with guardian consent, trusted video sources, clear retention/deletion controls, and restricted access to stored reports.

Risk: The skill may create or reuse local identity and token records without asking the end user for an identifier.

Mitigation: Deploy with explicit account separation, token protection, and review of identity storage before use with children or multiple households.

Risk: Cobb angle and posture findings are visual estimates and are not a medical diagnosis.

Mitigation: Present results as habit-correction reminders and advise clinical review for medical scoliosis or vision concerns.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON report content with posture metrics, reminder text, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted historical reports and may save report output to a file when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
