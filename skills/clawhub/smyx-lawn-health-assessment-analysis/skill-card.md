## Description:

Uses cloud analysis of lawn images or videos to provide turf health metrics, care guidance, and access to past reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Lawn managers and groundskeepers use overhead images or videos to assess yellowing, weed cover, and overall turf health, and to review past assessments when planning maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lawn images, videos, or their URLs are sent to the lifeemergence.com cloud service.

Mitigation: Only submit media or URLs you are comfortable sharing with that service.

Risk: Report history is associated with a silently created or reused local identity, and tokens persist locally.

Mitigation: Review or clear the workspace data database and tokens if you do not want identity reuse across runs.

Risk: Code and documentation differ in several places.

Mitigation: Review actual script behavior before relying on documented parameters or results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text reports or Markdown tables with report links; optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include health metrics and maintenance suggestions; history is retrieved from the cloud service.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
