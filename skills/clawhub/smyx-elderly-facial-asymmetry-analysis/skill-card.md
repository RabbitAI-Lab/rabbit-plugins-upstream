## Description:

Analyzes frontal elderly face images or short videos with facial-landmark techniques to estimate mouth-corner deviation, facial asymmetry indicators, an asymmetry index, and a non-diagnostic risk prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and health-monitoring operators use this skill to screen frontal elderly face media for geometric asymmetry indicators and historical report links. The output is an auxiliary prompt for follow-up review, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive facial and health-screening data and can associate reports with an automatically resolved identity.

Mitigation: Use it only with consent from the monitored person or guardian, and define who may initiate screening or view identity-linked reports.

Risk: The skill can use cloud history and local token storage for report retrieval.

Mitigation: Review token storage, retention, report deletion, and access-control practices before installation.

Risk: The bundled configuration includes dev or private HTTP endpoints.

Mitigation: Verify production API endpoints and prefer approved HTTPS services before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report text with JSON-style structured analysis fields and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an asymmetry index, mouth-corner deviation side, risk level, medical follow-up prompt, and historical report table.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
