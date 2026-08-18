## Description:

Integrate and unbind OpenViking long-term memory with coding agents running in bwrap sandboxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to connect OpenViking long-term memory to supported coding agents, check integration status, verify the MCP endpoint, and unbind the integration when it is no longer needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenViking persistence can cause agents to recall, save durable facts, and index repository or project context across sessions.

Mitigation: Install only when persistent memory is intended, confirm retention, deletion, and access controls, and unbind the integration when durable memory is no longer acceptable.

Risk: Sensitive code, secrets, or user context may be captured by persistent memory or exposed through credential handling mistakes.

Mitigation: Avoid use in sensitive workspaces unless approved, never place API keys in chat or logs, and do not use troubleshooting patterns that print or reuse another process's model API token.

Risk: Template-level changes can survive sandbox restarts and affect multiple supported agents.

Mitigation: Use dry-run first, require explicit confirmation for mutations, target a single agent unless all agents are intended, then verify with status and MCP checks.

## Reference(s):

- [Agent Configuration Reference](references/agent-configs.md)
- [Guardrails](references/guardrails.md)
- [IAM Policies / Access Permissions](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-openviking-agent-integration)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, JSON]

**Output Format:** [Markdown guidance with shell commands and optional JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration and unbinding scripts create timestamped backups and support dry-run mode.]

## Skill Version(s):

1.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
