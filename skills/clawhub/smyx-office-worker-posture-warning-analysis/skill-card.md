## Description:

Analyzes office workstation images or videos to estimate continuous sitting duration, forward head posture, back curvature, shoulder asymmetry, and screen distance, then produces sitting and posture warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, workplace health teams, and developers use this skill to analyze office workstation media and generate posture or prolonged-sitting alerts. It supports ergonomic behavior reminders and historical workplace health report lookup, but does not provide medical diagnosis or rehabilitation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace posture videos, video URLs, report queries, and account-linked identifiers may be sent to external services.

Mitigation: Deploy only with employee notice and consent, confirm provider retention and deletion terms, and restrict media submissions to approved workplace health workflows.

Risk: The skill silently creates or reuses identities and stores tokens locally.

Mitigation: Limit access to the runtime environment, rotate or revoke tokens when needed, and verify local token storage protections before enterprise use.

Risk: Historical report lookup may expose account-linked workplace health records.

Mitigation: Restrict who can query historical reports and verify access-control, encryption, and audit requirements with the provider.

Risk: Posture warnings may be mistaken for medical advice.

Mitigation: Present outputs as visual posture and activity reminders only and direct users with neck or back symptoms to qualified medical professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)
- [Office Posture Warning API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports and tables with optional JSON detail from API-backed analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include posture metrics, warning classifications, reminder text, summary statistics, and report links.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
