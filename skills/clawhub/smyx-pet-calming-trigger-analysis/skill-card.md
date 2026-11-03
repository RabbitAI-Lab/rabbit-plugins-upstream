## Description:

Analyzes pet videos for behaviors associated with anxiety or prolonged isolation and returns a structured report with soothing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners can submit a supported pet-camera video to review behavioral analysis and soothing suggestions, or request prior reports. Results are guidance for care decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video analysis and report history can involve sending pet videos to a cloud service; its retention practices are not established in the evidence.

Mitigation: Require explicit approval before video submission and confirm the provider's retention practices.

Risk: The security review reports silent cloud account registration and credential retention.

Mitigation: Require explicit control over registration and store credentials in protected storage.

Risk: The advertised export-only mode may still allow network activity.

Mitigation: Verify a working export-only mode before relying on it; do not treat --export-env-only or --api-url as network controls.

Risk: History lookup may run on broad or unintended triggers.

Mitigation: Narrow history triggers and require clear user intent before retrieving reports.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior estimates and soothing suggestions for review; actual soothing effects may vary by pet.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
