## Description:

Analyzes a pet face image or video by matching identity, querying linked vaccination records, and returning due or overdue reminder results without providing medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet hospital, boarding center, and pet insurance staff use this skill to check whether a registered pet appears due or overdue for vaccination from a face image or video and linked records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and linked account context may be sent to external cloud services.

Mitigation: Require explicit user or operator consent before analysis, confirm approved service endpoints, and document retention and deletion handling for uploaded media and returned reports.

Risk: The skill may silently create or reuse account identity and retrieve history reports.

Mitigation: Require explicit account selection or confirmation in real deployments and limit history lookup to authorized users and workspaces.

Risk: Authentication tokens or identity data may be stored locally with limited user-facing control.

Mitigation: Use a managed secrets store where possible, restrict workspace access, rotate credentials, and clear local token data during deprovisioning.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and history-report tables when the cloud API returns matching records.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
