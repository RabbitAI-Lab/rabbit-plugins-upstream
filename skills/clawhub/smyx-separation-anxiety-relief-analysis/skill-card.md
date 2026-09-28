## Description:

Analyzes pet footage for signs of separation anxiety and provides behavior reports and comfort recommendations, without directly controlling smart devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and boarding staff use the skill to analyze footage of pets left alone, review possible anxiety behaviors and historical reports, and consider suggested comfort measures. Reports are observational, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet and home camera media or media URLs are sent to the lifeemergence cloud service.

Mitigation: Review the service's data practices and share only footage or URLs you are comfortable sending to it.

Risk: Service identity tokens persist in a local workspace database.

Mitigation: Restrict workspace access and review local data retention before installing.

Risk: The skill description suggests automatic speaker, feeder, or toy control, but the inspected implementation produces reports and recommendations rather than device automation.

Mitigation: Treat comfort actions as suggestions; verify and configure any device integrations separately.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links; analysis output can optionally be saved to a file.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; bundled frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
