## Description:

Integrate and unbind OpenViking long-term memory with coding agents across CodeArts CLI, OpenCode, OpenClaw, Hermes, JiuwenSwarm, KimiCode, DeepSeek Harness, and Prime Agent using each agent's native memory, MCP, plugin, or configuration mechanism.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT

## Use Case:

Developers and platform engineers use this skill to connect or remove OpenViking long-term memory for supported coding agents, check integration status, verify the OpenViking MCP endpoint, and rebuild OpenClaw sandbox state when template changes need to take effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make OpenViking a persistent memory layer for supported agents, which may store or recall repository content and conversation-derived facts across sessions.

Mitigation: Install only when persistent OpenViking memory is intended, review generated AGENTS.md and prompt behavior, and use dry-run before applying changes.

Risk: Integration and unbinding change agent behavior and cleanup scope across template and live sandbox configuration.

Mitigation: Avoid --all and --yes except in controlled automation, run status and verification checks after changes, and review any partial template-only or live-only state.

Risk: Unbinding can affect existing OpenCode and Hermes sandbox configuration.

Mitigation: Back up OpenCode and Hermes sandbox config before unbinding and rely on the skill's backup and rollback guidance if verification fails.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-openviking-agent-integration)
- [Agent Configuration Reference](references/agent-configs.md)
- [Guardrails](references/guardrails.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)
- [Related Commands](references/related-commands.md)
- [IAM Policies / Access Permissions](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, markdown]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate or modify agent configuration files after explicit authorization; dry-run and status modes support review before changes.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact metadata lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
