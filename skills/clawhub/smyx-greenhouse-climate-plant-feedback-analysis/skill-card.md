## Description:

Analyzes greenhouse plant images or videos and returns reports with suggested climate-control actions and priorities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators and developers use the skill to review plant imagery, obtain analysis reports and suggested irrigation, shading, ventilation, or heating actions, and query historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse images, videos, or supplied URLs are sent to an external cloud service.

Mitigation: Review data retention and backend access controls before submitting private camera feeds.

Risk: Account and session tokens may persist in a local workspace database.

Mitigation: Review account identity and protect access to the local workspace and stored tokens.

Risk: Suggested greenhouse actions may be mistaken for direct control instructions.

Mitigation: Treat reports as advisory and require human review before applying actions to equipment.

## Reference(s):

- [Greenhouse analysis API documentation](references/api_doc.md)
- [Published skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown table; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes suggested control actions and priorities, not actuator settings.]

## Skill Version(s):

1.0.12 (source: server-resolved release; bundled SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
