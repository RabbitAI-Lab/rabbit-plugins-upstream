## Description:

Analyzes fixed-camera footage at a home entrance or balcony to estimate a child's outdoor time from entry and exit events and produce daily activity reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers can use this skill to estimate a child's daily outdoor time from doorway footage. Developers can integrate its event counts, duration summaries, and reminders into family or school applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote analysis and report retrieval involve sensitive household video and identity or token handling.

Mitigation: Use only footage with appropriate guardian consent, send it only to a trusted service, protect credentials, and restrict access to video and exported reports.

Risk: Doorway events estimate time outside and may not represent actual outdoor activity; similar-looking children may be confused.

Mitigation: Present results as estimates, check event attribution and summaries, and use caregiver observation for context.

## Reference(s):

- [API interface notes](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured activity report; Markdown table for history lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entry and return events, estimated session and daily durations, reminders, and report links]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
