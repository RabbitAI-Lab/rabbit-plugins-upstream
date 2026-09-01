## Description:

Uses visual AI to analyze care images or videos for wet clothing or abnormal excretion and return caregiver-facing alerts, care suggestions, and report links for elderly, bedridden, or infant care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and care-system operators use this skill to submit care images, videos, or media URLs for incontinence-status analysis, alert review, and historical report lookup. It is intended as a care-assistance workflow and does not replace professional medical judgment or human checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send sensitive care images, videos, or media URLs to remote services.

Mitigation: Use only with patient or guardian consent and confirm the backend endpoint, privacy policy, retention policy, deletion process, and caregiver notification access before deployment.

Risk: The skill silently creates or reuses internal identities and can query cloud report history.

Mitigation: Restrict use to authorized caregivers, verify report-access controls, and audit who can view historical reports.

Risk: Backend tokens may be stored locally in the workspace data directory.

Mitigation: Protect the workspace, avoid shared machines for real care data, rotate credentials when needed, and remove local tokens after testing or decommissioning.

Risk: Care-analysis results can be wrong or incomplete and should not drive care decisions alone.

Mitigation: Require human confirmation for alerts and continue to follow professional care or medical judgment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Incontinence alert analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON care-analysis reports, Markdown history tables, shell command examples, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alert levels, wet-clothing or excretion indicators, care warnings, care suggestions, history records, and export URLs.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
