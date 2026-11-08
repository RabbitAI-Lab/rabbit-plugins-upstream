## Description:

Connect OpenClaw to Spaces by Peakflo, a hosted MCP server for finance and ops work. Hand off one-off or recurring tasks to cloud agents or people, and query workflows, data tables, reports, policy documents and approvals. Sign in with OAuth; no API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dimavedenyapin](https://clawhub.ai/user/dimavedenyapin)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and operations teams use this skill to connect an agent to their Spaces workspace, delegate one-off or recurring work, and retrieve workspace information such as workflow status, reports, policy documents, and approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the skill grants an agent access to the selected Spaces workspace, and some workspace actions may affect payment-related workflows.

Mitigation: Connect only to the intended workspace; confirm before writes, workflow execution, or approval completion, and do not initiate payments.

Risk: The security scan reported incomplete coverage because a local path-like reference in SKILL.md could not be resolved.

Mitigation: Review the unresolved reference and complete a fresh security scan before deployment.

## Reference(s):

- [Spaces MCP documentation](https://spaces.peakflo.ai/docs/mcp/)
- [Spaces MCP project repository (linked in skill documentation)](https://github.com/peakflo/spaces-mcp)

## Skill Output:

**Output Type(s):** [Text, API Calls]

**Output Format:** [Natural language workspace answers and task handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task creation and other write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
