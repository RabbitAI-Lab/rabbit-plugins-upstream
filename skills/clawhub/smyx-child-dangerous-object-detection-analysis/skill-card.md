## Description:

Analyzes submitted video of children's activity areas for contact with preset dangerous objects or electrical sockets and returns alerts and a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and childcare providers can submit video from children's activity areas to identify possible contact with preset hazardous items or electrical sockets and receive an alert report. The skill is an auxiliary warning tool; its documentation says it does not replace adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unresolved questions about what video and identity data are sent, how accounts and tokens are stored, and whether export-only options avoid analysis.

Mitigation: Avoid installation until the publisher clarifies these points. Obtain guardian consent before using children's video and protect recordings as the skill documentation advises.

Risk: The security review notes a mismatch between claims of continuous child-safety monitoring and the on-demand video-analysis workflow.

Mitigation: Treat results as auxiliary, on-demand alerts and maintain adult supervision; do not rely on the skill as continuous monitoring.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis report with alert details and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected object and action, confidence, event time, alert level, and snapshot or report links.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
