## Description:

Analyzes outdoor sports footage for potential injuries and health risks, returning safety reports and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event organizers and safety staff use this skill to assess participant videos for falls, injuries, and signs of distress, then review risk reports or query prior reports. Its findings are safety aids, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos, video URLs, identity fields, and report-history queries are sent to configured cloud services without clear privacy or retention disclosure.

Mitigation: Review service privacy and retention terms and obtain informed approval before sending participant media or querying reports.

Risk: A reused local default identity may associate reports from different users in shared workspaces.

Mitigation: Require a trusted per-user identity for every invocation; do not enable history lookup without authenticated user identity.

Risk: Video-based health and injury assessments may be mistaken for medical diagnoses.

Mitigation: Have qualified event medical personnel review warnings; seek urgent medical care for suspected emergencies.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured safety reports, Markdown report lists, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk warnings, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: ClawHub release; artifact frontmatter lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
