## Description:

Analyzes camera images or video from home and childcare settings to detect children contacting dangerous objects or electrical sockets, returning structured alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, childcare operators, and developers use this skill to analyze child activity-zone camera footage for dangerous-object contact, socket-contact behavior, and related warning events. It can also retrieve historical cloud reports for the same monitoring scenario.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child video files or video URLs may be uploaded to a remote service for analysis.

Mitigation: Use only with guardian or administrator consent, and confirm the configured endpoint and data handling expectations before deployment.

Risk: The skill creates or reuses a local identity and stores authentication tokens in a workspace SQLite database.

Mitigation: Install only in trusted workspaces, restrict filesystem access, and review token storage and cleanup procedures before use.

Risk: Historical cloud report queries may expose sensitive child safety reports.

Mitigation: Limit report-list access to authorized users and verify that cloud report retention and visibility match the deployment policy.

## Reference(s):

- [Child Dangerous Object Detection API Reference](artifact/references/api_doc.md)
- [SMYX Analysis API Reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs structured detection results, alert text, historical report lists, and export links from the configured remote service.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
