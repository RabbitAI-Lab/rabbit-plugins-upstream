## Description:

Automatically detects personnel in target areas based on computer vision, supports real-time video stream detection, and produces structured human-detection reports for access monitoring in parks, offices, and restricted areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Security, operations, and facilities teams use this skill to analyze monitoring videos or video URLs for people, counts, frequency, and intrusion signals in defined areas. Agents can also query cloud-hosted historical human-detection reports when users ask for prior results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring footage or video URLs may be sent to lifeemergence.com services.

Mitigation: Use only footage that is approved for third-party processing and confirm consent, retention, and data-handling terms before deployment.

Risk: The skill may silently create or reuse a cloud-linked identity.

Mitigation: Install only where automatic identity handling is acceptable, and document who owns the linked account and reports.

Risk: Returned account tokens may be stored in a workspace SQLite database.

Mitigation: Restrict workspace access, avoid shared workspaces for sensitive deployments, and rotate or remove stored tokens when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-formatted text reports, with optional saved result files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; historical report queries are returned as Markdown tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
