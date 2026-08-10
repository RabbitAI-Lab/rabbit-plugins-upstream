## Description:

Monitors employee on-duty status in designated areas from images or video using computer vision and human pose estimation, detects leave-post or absence conditions, supports configurable thresholds, and returns structured monitoring results and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, security, and workplace management teams use this skill to analyze workplace images or surveillance video for leave-post and absence events in monitored areas. Agents can run the bundled command-line workflow to submit media, retrieve structured results, and list cloud-hosted historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive workplace images or video and identity-linked request data may be sent to external cloud services.

Mitigation: Deploy only after confirming employee-consent, data-transfer, retention, and vendor-processing requirements for the monitored workplace.

Risk: The skill can automatically create or reuse local user records and associate reports with an internal identity.

Mitigation: Review identity handling before installation, restrict workspace access, and confirm that generated or reused identities align with internal access-control and audit policies.

Risk: Service tokens may be persisted in the workspace.

Mitigation: Use a secured runtime location, limit filesystem permissions, rotate tokens regularly, and remove persisted credentials when the skill is no longer needed.

## Reference(s):

- [Personnel Absence Monitoring API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown summaries and structured JSON returned from command-line/API workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, monitoring status, absence counts, duration statistics, recommendations, and optional saved output files.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
