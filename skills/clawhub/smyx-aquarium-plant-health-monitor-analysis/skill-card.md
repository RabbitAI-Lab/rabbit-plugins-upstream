## Description:

Analyzes aquarium plant images or video for visible health symptoms and provides a health assessment, likely causes, and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquascapers, and aquarium shops can use the agent to review plant images or video, identify visible health concerns, and get care suggestions. It can also display cloud-hosted historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still permit uploads.

Mitigation: Wait for the export-only behavior to be corrected; before then, use only non-sensitive media in an isolated workspace.

Risk: Remote account, uploaded-media, and stored-token retention and deletion controls are unclear, and external service privacy and access controls are unverified.

Mitigation: Confirm how remote accounts, uploaded media, and stored tokens are retained and deleted, and verify external service privacy and access controls before use.

Risk: A reusable API secret may be used as identity data.

Mitigation: Avoid configuring a reusable API secret until its use as identity data is removed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Structured text report, Markdown table for historical reports, or JSON detail]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis results may include report links.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
