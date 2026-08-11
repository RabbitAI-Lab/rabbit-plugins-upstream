## Description:

Analyzes fixed-camera pet rest-area video to estimate sleep and awake states, total sleep duration, rollovers or position changes, startle awakenings, and a 0-100 sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, veterinary or boarding staff, and developers use this skill to analyze pet sleep-period videos, review sleep metrics, and retrieve structured historical analysis reports. It is intended for sleep-health reference and does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet sleep videos may show homes, people, clinics, or boarding facilities and are uploaded to remote services for analysis.

Mitigation: Use only media that the user is authorized to process, avoid unnecessary private background content, and confirm that remote processing is acceptable before execution.

Risk: The skill can query cloud report history and silently associates activity with an internal or default identity.

Mitigation: Confirm the intended account context before history queries and avoid exposing internal identity values in user-facing output.

Risk: Reusable authentication tokens may be stored in a local workspace database.

Mitigation: Restrict workspace access, review local credential storage before shared deployments, and clear local data when the skill is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Sleep Quality Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the rendered report text to a file when an output path is provided; history mode returns a structured report list.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
