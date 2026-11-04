## Description:

Analyzes child activity images or videos for contact with preset dangerous objects or electrical outlets and returns detection results and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families and childcare providers can submit child activity footage to identify possible contact with hazardous household items or electrical outlets, then review the resulting detection report and available history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account handling may expose private child reports across users.

Mitigation: Defer use with private child footage until sender isolation and export-only behavior are fixed; evaluate only non-sensitive samples in a separate single-user workspace.

Risk: Remote account creation, charges, and footage retention or deletion practices are not confirmed.

Mitigation: Confirm account creation, possible charges, and footage retention and deletion practices before use.

Risk: The supplied workflow does not establish continuous safety alerts, and cloud authorization and detection quality remain unverified.

Mitigation: Do not rely on the package for continuous or emergency alerts; treat it only as a supplemental aid.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown, Report links]

**Output Format:** [Structured detection results and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected object and action, confidence, event time, alert level, snapshot, and report links when returned by the service.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
