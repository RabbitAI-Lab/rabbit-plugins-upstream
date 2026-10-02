## Description:

Analyzes face images or videos for stress levels and anxiety and depression tendencies, and provides assessment reports and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and mental-health monitoring teams use the skill to assess facial media for stress and related tendencies, retrieve past reports, and share results as informational assessments rather than clinical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face media and mental-health-related inferences are sent to the Life Emergence cloud service.

Mitigation: Obtain informed consent and confirm service retention, deletion, and report-access terms before using real people's data.

Risk: Reports can be linked to a persistent identity and service tokens are stored locally.

Mitigation: Review who can access report history and whether local token storage in the workspace data database is acceptable.

Risk: Stress and tendency estimates may be mistaken for clinical diagnoses.

Mitigation: Treat results as informational only and seek qualified professional assessment for ongoing concerns.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown assessment reports and history tables; optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, stress results, and anxiety or depression tendencies.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
