## Description:

Uses computer vision to analyze workplace images or video for employee phone-use behavior and return structured monitoring reports, warnings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise workplace monitoring or facilities teams use this skill to submit office images, videos, or media URLs for phone-usage detection and to retrieve historical monitoring reports. It is intended as internal management support and should not be used as the sole basis for employee discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-based analysis of employee images or videos can expose sensitive workplace and personal data.

Mitigation: Verify the backend configuration before use, obtain appropriate employee and legal approvals, and define retention and access-control policies before deployment.

Risk: The skill silently creates or reuses persistent backend identity tokens for report access.

Mitigation: Use only in workspaces with controlled access, protect local workspace data, and rotate or remove stored identity data when access changes.

Risk: Monitoring reports may be incomplete or misleading if used without human and policy review.

Mitigation: Treat results as advisory internal management support and review them against workplace policy, legal requirements, and source media before taking action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Phone usage monitoring API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports or JSON responses, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection counts, duration summaries, compliance scores, warnings, recommendations, historical report tables, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
