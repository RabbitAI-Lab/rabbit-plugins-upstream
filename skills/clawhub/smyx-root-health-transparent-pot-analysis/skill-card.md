## Description:

Analyzes images or videos of plant roots in transparent pots, seedling boxes, plant factories, or hydroponic systems to estimate root condition, signs of rot, health score, vitality grade, and care direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users, growers, and operators of transparent-pot, seedling-box, hydroponic, or plant-factory systems use this skill to evaluate visible root health from submitted media and receive a structured report. It is intended for plant care guidance, not professional agronomy, pathology, or pesticide treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant images, videos, or media URLs to external cloud services for analysis.

Mitigation: Use only media that is appropriate to share with the external service, and avoid submitting sensitive background content or private URLs.

Risk: The skill can silently create or reuse an account identity for analysis and history retrieval.

Mitigation: Review identity handling before deployment, and document how generated or reused account identifiers are associated with reports.

Risk: The skill stores service tokens in a shared local SQLite database.

Mitigation: Restrict filesystem access to the agent workspace, rotate stored tokens when needed, and avoid sharing the database across untrusted users.

Risk: Development or private endpoint defaults may be present in bundled configuration.

Mitigation: Confirm production endpoint configuration before installation or execution, and remove or override dev/private defaults in managed deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON-formatted structured analysis report with health observations, a report link when available, and optional history-list output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include root-health score, vitality grade, visible root condition observations, care direction, and cloud report links.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
