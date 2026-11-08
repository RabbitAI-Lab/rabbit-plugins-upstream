## Description:

Analyzes a submitted infant crib video for blanket coverage and kicking-related events and returns a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and baby-monitoring developers can request on-demand analysis of crib footage for blanket coverage and kicking-related events, then review structured reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant recordings may be uploaded even when analysis is explicitly disabled; the supplied security guidance also calls for credential logging to be fixed.

Mitigation: Wait for those behaviors to be fixed before using sensitive recordings. Explicitly authorize footage uploads and confirm the service's retention, deletion, account-linking, and pricing terms.

Risk: Continuous monitoring and dependable alerts are not established by the supplied artifacts.

Mitigation: Treat this as on-demand clip analysis and keep an adult responsible for monitoring and checking the infant directly.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Report links]

**Output Format:** [Structured JSON analysis presented with a Markdown heading and report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an analysis report or a list of historical reports.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
