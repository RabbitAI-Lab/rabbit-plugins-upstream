## Description:

Analyzes plant images or videos through a cloud service to report potential wilting, provide early warnings, and retrieve previous reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural teams use the skill to review plant imagery for possible wilting, obtain early-warning reports and recommendations, and view past analyses. Results are advisory and should be checked against field conditions and expert judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media or URLs are sent to lifeemergence.com cloud APIs for processing.

Mitigation: Use only media approved for cloud processing and obtain appropriate consent before submitting it.

Risk: The skill creates or reuses an internal user identity, queries cloud-stored history, and persists service tokens in a local workspace SQLite database.

Mitigation: Review identity linkage and history access before installation; restrict local database access and remove stored credentials when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports or Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include monitoring results, recommendations, and links to cloud-stored reports.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
