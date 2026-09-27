## Description:

Helps HR review employee emotion trends from office video against historical baselines and produces fluctuation alerts and supportive follow-up suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized HR staff use the skill to review consented office video, compare anonymized employee behavior trends with historical baselines, and receive alerts, care suggestions, or historical report listings for supportive follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Office video and employee emotion reports expose sensitive HR information, and anonymized identifiers may still allow employees to be identified.

Mitigation: Use only in an approved HR environment with employee notice and consent, opt-out, legal review, restricted administrator access, and audited report access; verify actual data retention and anonymization before deployment.

Risk: Identity and access tokens persist locally while analysis and historical reports use vendor services.

Mitigation: Review vendor endpoints, local SQLite token storage, workspace data/smyx-api-key.txt behavior, and historical report permissions before providing real employee data.

Risk: Inferred emotion alerts can be misleading or misused in employment decisions.

Mitigation: Require human review and contextual follow-up; do not treat alerts as medical diagnoses or use them for performance, promotion, or termination decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [HR report API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured JSON analysis or Markdown report listings and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes emotion-trend alerts, suggested HR follow-up, and report links when available.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; bundled frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
