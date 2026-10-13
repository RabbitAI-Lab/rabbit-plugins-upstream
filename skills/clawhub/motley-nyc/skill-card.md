## Description:

Helps families explore New York City neighborhoods, schools, admissions, safety, and local resources using Motley's hosted information service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitbrujo](https://clawhub.ai/user/bitbrujo)

### License/Terms of Use:

MIT-0

## Use Case:

Families and their advisers use this skill to compare NYC neighborhoods and schools, understand admissions methods, and find family resources using Motley data.

### Deployment Geography for Use:

Global (information covers New York City)

## Known Risks and Mitigations:

Risk: NYC-related queries, including a supplied home address, may be sent to Motley's hosted service.

Mitigation: Share only information needed for the query and consider the service's data handling before providing sensitive details.

Risk: The skill recommends automatically approving access to a remote service.

Mitigation: Keep normal MCP permission controls unless the service is independently trusted.

Risk: Admissions competitiveness and neighborhood scores may be mistaken for individual admission odds or current official ratings.

Mitigation: Do not estimate a family's admission odds; distinguish Motley assessments from official data and note score dates when relevant.

## Reference(s):

- [Motley MCP overview](https://motley.nyc/mcp)
- [Motley skill on ClawHub](https://clawhub.ai/bitbrujo/skills/motley-nyc)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to source pages and dates for neighborhood scores.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
