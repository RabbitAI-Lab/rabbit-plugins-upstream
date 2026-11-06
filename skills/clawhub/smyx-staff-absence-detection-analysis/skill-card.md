## Description:

Analyzes supplied images or videos to report personnel presence and possible absence from monitored work areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Managers and workplace operations or safety teams can submit an image or video for an on-demand review of personnel presence in a monitored area and receive a structured report. The skill can also query previously generated reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied footage may be sent for cloud analysis even when an option says analysis is disabled.

Mitigation: Avoid sensitive footage until export-only behavior is fixed; confirm the cloud destination and retention terms before sending media.

Risk: Credential handling and separation from identity data need review.

Mitigation: Defer use with real credentials until credential and identity separation are fixed; confirm account-enrollment controls and protection of stored tokens.

Risk: Continuous alerting is unverified; the evidence supports on-demand cloud analysis.

Mitigation: Treat results as on-demand analysis and do not rely on the skill for continuous alerts.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results in JSON and Markdown report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include detected status, absence counts or durations, recommendations, and report links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
