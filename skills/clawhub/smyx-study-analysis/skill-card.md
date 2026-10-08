## Description:

Analyzes children's study videos to assess attention, posture, and learning habits and suggest improvements for families.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and educators use this skill to review children's study videos, identify potentially unhelpful learning behaviors, and obtain family education suggestions. Reports are for guidance, not professional diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's study videos or video URLs are sent to a configured cloud service for analysis.

Mitigation: Obtain appropriate consent and use a dedicated test workspace or account before submitting real footage; confirm the service's retention and deletion practices.

Risk: The skill silently associates reports with remote accounts and keeps access tokens or session data in the workspace data directory.

Mitigation: Review account-linking and token-handling controls before use, and restrict access to the workspace data directory.

## Reference(s):

- [Skill API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured report in text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional saved report file and report link; supports historical report lookup.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata; bundled frontmatter says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
