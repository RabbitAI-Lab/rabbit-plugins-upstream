## Description:

Assesses top-down lawn images or videos for yellowing, weeds, bare soil and overall turf health, then provides a report and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Groundskeepers, landscape managers and property owners use overhead lawn imagery to estimate yellowing and weed coverage, review a turf health score and plan maintenance. They can also request prior cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private lawn images or videos are uploaded to configured lifeemergence.com cloud services.

Mitigation: Confirm the service and permitted data before submitting private site imagery; restrict network endpoints if needed.

Risk: A persistent workspace identity and service tokens are stored locally.

Mitigation: Review and restrict access to the workspace data directory, especially in shared environments.

Risk: Report-history requests can automatically retrieve cloud records.

Mitigation: Review history-query triggers and confirm the intended account and access before retrieving reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured lawn assessment and report links; JSON or Markdown report listings when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include yellowing and weed coverage, a health score, care suggestions and links to current or historical reports.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
