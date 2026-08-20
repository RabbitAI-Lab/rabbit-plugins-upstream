## Description:

Supports identifying high-risk behaviors and health risks through video/images, including elderly falls, precursors to heart attacks and strokes, and abnormal behaviors, issuing timely warning alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit videos, images, URLs, or streams for remote high-risk behavior and health-risk analysis, including fall detection, abnormal behavior detection, and visual warning reports. It can also retrieve cloud-hosted report history associated with the skill's local identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted videos, images, URLs, and streams may be uploaded to Life Emergence/Smyx cloud services for analysis.

Mitigation: Use only media that is intended for that remote processing, and avoid private camera streams, signed URLs, or sensitive medical and safety footage unless the sharing is approved.

Risk: The skill can automatically create or reuse a local identity and store cloud authentication tokens for report history.

Mitigation: Run it in an isolated workspace, review and protect the workspace data directory, and remove stored identity or token data when access should be reset.

Risk: Risk-analysis results are advisory and may affect safety or health decisions if treated as authoritative.

Mitigation: Use outputs as decision support only, and require human review or professional emergency, medical, or security procedures for high-risk findings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-risk-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Risk Categories and Alert Levels](artifact/references/risk_categories.md)
- [API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON analysis results, report summaries, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report history and export links returned by the remote service.]

## Skill Version(s):

999.999.1004 (source: ClawHub release metadata; source skill frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
