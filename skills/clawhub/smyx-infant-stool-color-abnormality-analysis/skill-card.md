## Description:

Analyzes infant diaper or stool images for color patterns and returns a structured screening report with risk reminders and follow-up suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, pediatric clinics, and postpartum care staff can use this skill to review infant stool images for color patterns and receive screening reminders and suggested follow-up. The results are visual screening guidance, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: In shared workspaces, infant health reports may be associated with the wrong user.

Mitigation: Require reliable per-user account separation before use in a shared workspace.

Risk: The configuration-only option may still trigger image processing, and the provider's media and report retention practices are unverified.

Mitigation: Confirm configuration-only behavior and provider retention and deletion practices before sending infant images or reports.

Risk: Visual screening accuracy has not been verified, and infant images and reports are sensitive information.

Mitigation: Treat results as screening guidance, obtain guardian consent, protect stored tokens and reports, and seek clinical assessment for concerning results.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured screening report with a stool color category, risk reminders, suggested actions, and report links; JSON by default and Markdown for report lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual screening guidance only; image quality and lighting can affect color classification.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
