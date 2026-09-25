## Description:

Analyzes aquarium plant images or videos for visible leaf color changes, shape anomalies, algae attachment, and likely nutrient symptoms, then returns a structured health assessment with care-direction suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquascaping maintainers, aquarium shops, and developers use this skill to submit plant images, videos, or URLs for visible plant-health monitoring and care-direction guidance. The skill can also retrieve account-linked historical cloud reports for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium images, videos, submitted URLs, and report-history queries are sent to configured lifeemergence.com cloud services.

Mitigation: Use only with media and URLs approved for that cloud service, and disclose upload and history-query behavior before execution.

Risk: The skill automatically creates or reuses a persistent identity and stores service tokens locally.

Mitigation: Run it in an isolated workspace, review token storage and cleanup expectations, and remove local workspace data when finished.

Risk: Historical report retrieval is account-linked and may expose previous cloud-stored analysis records.

Mitigation: Confirm user intent before running history-list commands and avoid displaying or requesting internal identity values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-style report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report export link; historical report queries return cloud-backed report records.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
