## Description:

Connect OpenClaw to Spaces by Peakflo, a hosted MCP server for finance and ops work. Hand off one-off or recurring tasks to cloud agents or people, and query workflows, data tables, reports, policy documents and approvals. Sign in with OAuth; no API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peakflo](https://clawhub.ai/user/peakflo)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations teams use this skill to look up workspace workflows, tables, reports, policies and approvals, and to hand off one-off or recurring work to a cloud agent or person.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting grants the skill access to a user's Spaces workspace through OAuth.

Mitigation: Review the requested workspace and access before approving OAuth, and revoke access in Spaces settings or with the documented logout command when it is no longer needed.

Risk: Write actions can notify people, change workspace data, or trigger workflows with financial effects.

Mitigation: Require the user's explicit confirmation before write actions, explain when an action may move money, and do not initiate payments or securities trades.

Risk: The release security scan was marked partial because a local setup reference could not be resolved.

Mitigation: Review the skill and its setup instructions before installation; the benign scan verdict is not a guarantee of safety.

## Reference(s):

- [Spaces MCP documentation](https://spaces.peakflo.ai/docs/mcp/)
- [Spaces MCP source repository](https://github.com/peakflo/spaces-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON5 configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workspace answers and task handoffs; OAuth sign-in is completed in the user's browser.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
