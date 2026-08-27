## Description:

Monitors home pet videos or image URLs for restricted-area entry, table climbing, and trash rummaging, then returns alerts, structured results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze household pet-monitoring media for prohibited-area entry and related behaviors, and to retrieve prior cloud-generated warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private pet-monitoring images, videos, or URLs are sent to the lifeemergence cloud service.

Mitigation: Use only with footage that is appropriate for external processing, and confirm provider retention and deletion controls before deployment.

Risk: The skill can silently create or reuse a cloud-linked account identity and store returned tokens in a local workspace database.

Mitigation: Run the skill in an isolated workspace, review token storage and cleanup controls, and remove local credentials when they are no longer needed.

Risk: History queries retrieve cloud report records associated with the resolved account identity.

Mitigation: Enable history retrieval only for authorized users and confirm that report access matches the expected account context.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON analysis report with report links; optional saved text output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4/avi/mov files up to 10 MB or public media URLs; history queries return Markdown tables.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
