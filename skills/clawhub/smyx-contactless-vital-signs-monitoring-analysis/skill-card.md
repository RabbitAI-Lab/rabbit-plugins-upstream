## Description:

Analyzes camera footage to estimate heart rate, respiration, blood oxygen, and heart rate variability without wearable sensors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People or care teams can submit a short face video to request an informational vital-signs report or retrieve prior reports. Results are for health reference and do not replace professional measurement or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos may be uploaded for remote analysis even when export-only mode is requested.

Mitigation: Wait for corrected export-only behavior before sending sensitive footage, and confirm the provider's upload, retention, and deletion terms.

Risk: Shared deployments may mix users' report accounts.

Mitigation: Wait for reliable per-user account separation and protect the local credential database and debug logs.

Risk: The review did not verify the remote service's privacy controls or measurement accuracy.

Mitigation: Review the provider's privacy terms and treat results as health reference rather than a substitute for professional measurement or diagnosis.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured vital-signs report; historical report listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include estimates, risk notes, recommendations, and report links; results are informational and are not a substitute for medical measurement or diagnosis.]

## Skill Version(s):

1.0.21 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
