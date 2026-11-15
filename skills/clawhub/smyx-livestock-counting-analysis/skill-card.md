## Description:

Automatically detects and counts livestock or poultry in barn or passage camera images and videos, returning a headcount and confidence for inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock farm operators can use this skill to count animals from barn or passage images and videos, review structured headcounts and confidence, and query historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags persistent account and token handling.

Mitigation: Review credential handling and access before use, and avoid supplying credentials unless the service requires them and is trusted.

Risk: Images or videos and identity data may be sent to a remote service.

Mitigation: Use only media authorized for external processing, and confirm the service's privacy and retention terms before submitting it.

Risk: The security review notes that the export-only option may still analyze media.

Mitigation: Treat export-only as media processing unless its behavior is confirmed; avoid it for sensitive media when that behavior is unclear.

Risk: The security scan is partial because a referenced local path was missing.

Mitigation: Review the missing reference and scan the complete package before deployment.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured counting report with headcounts and confidence; historical reports can be listed in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-area counts, report links, and uncertainty notes for occluded or densely grouped animals]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
