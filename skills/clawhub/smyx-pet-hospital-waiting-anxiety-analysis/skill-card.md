## Description:

Analyzes pet waiting-area videos for visible stress behaviors and reports a 1–5 anxiety level to support veterinary triage, not diagnosis or treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary clinic staff and pet care professionals use video-based behavior assessments to identify pets that may need earlier attention or calming while waiting. Results are observational and do not diagnose disease or recommend treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet clinic media and supplied URLs are sent to an external analysis service.

Mitigation: Review the service and obtain appropriate permission before sending clinic media or URLs.

Risk: The skill may silently create or reuse an internal identity and store service tokens locally.

Mitigation: Use an approved workspace, restrict access to its data directory, and review identity and token handling before installation.

Risk: Historical cloud reports can be retrieved automatically without separate confirmation.

Mitigation: Limit use to authorized report viewers and confirm that automatic history access fits clinic policy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [Text or Markdown report; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 1–5 anxiety level and observed behavior signals; can list linked historical reports or save results to a file.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
