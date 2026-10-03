## Description:

Analyzes pet race videos to flag false starts and lane crossings and provide structured results to assist referees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Race referees and event organizers use this skill to review start and finish footage, identify possible false starts or lane crossings, and consult past reports. Its findings assist rather than replace the on-site referee's decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Race footage or supplied video URLs are sent to external services for analysis.

Mitigation: Use only footage you are authorized to share; avoid sensitive footage unless you trust the service's retention and access controls.

Risk: The skill creates or reuses a local identity and stores tokens and profile data in a workspace SQLite database.

Mitigation: Review this behavior before installation and restrict access to the workspace and stored identity data.

Risk: History requests automatically retrieve cloud reports with limited user control.

Mitigation: Review access to report history before use and avoid invoking history queries when cloud retrieval is not appropriate.

Risk: Automated foul assessments may affect race decisions.

Mitigation: Treat results as referee assistance and leave final rulings to the on-site head referee.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis results, report links, and Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON result file; supports basic, standard, and JSON detail levels.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
