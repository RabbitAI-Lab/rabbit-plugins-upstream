## Description:

Using fixed cameras in enterprise office areas with employee consent and anonymization, this skill monitors facial-expression and posture signals against per-person baselines and produces HR-facing emotion-fluctuation alerts for supportive follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR leaders and authorized managers use this skill to analyze consented workplace camera video, compare anonymous employee behavior and expression metrics against historical baselines, and review structured care suggestions or historical reports. It is intended for supportive HR intervention, not diagnosis, performance review, promotion, or termination decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive employee emotion and behavior data from workplace camera footage.

Mitigation: Install only after confirming explicit employee consent, legal approval, opt-out handling, HR access controls, retention limits, and clear limits on use.

Risk: Reports could be misused for employment decisions or treated as mental-health diagnoses.

Mitigation: Use outputs only for voluntary supportive check-ins; prohibit use for performance, promotion, termination, or medical diagnosis.

Risk: The skill uploads or queries reports through a backend service and creates persistent local account or token state.

Mitigation: Approve the backend service and local token storage before deployment, and treat generated reports and account state as sensitive HR data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [Employee Emotion HR Report API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown and JSON structured HR reports, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include anonymous subject IDs, workstation IDs, baseline comparisons, alert levels, HR care suggestions, EAP references, historical report records, and report export URLs.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
