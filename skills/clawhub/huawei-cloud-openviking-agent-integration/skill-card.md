## Description:

Integrates and unbinds OpenViking long-term memory for eight coding agents through MCP, HTTP memory providers, TypeScript extension hooks, or settings.json configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to connect OpenViking long-term memory to supported coding agents, remove that integration, check integration state, verify the MCP endpoint, and rebuild the OpenClaw sandbox when template changes must be applied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the skill can fetch and cache plugin code before the promised confirmation step.

Mitigation: Review or fix the confirmation order so package downloads, npm installs, plugin cache writes, and runtime provisioning happen only after explicit confirmation.

Risk: The skill modifies multiple agent templates and runtime sandboxes while enabling long-term memory tools.

Mitigation: Use dry-run and status checks before applying changes, require explicit authorization for integration or unbinding, and keep the generated backups for rollback.

Risk: OpenViking may index or store project context through the enabled memory integration.

Mitigation: Install only in environments where storing project context in OpenViking is acceptable, and avoid passing an API key unless the server requires authenticated access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-openviking-agent-integration)
- [Agent configuration reference](references/agent-configs.md)
- [Guardrails](references/guardrails.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification and acceptance criteria](references/verification.md)
- [Related commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify agent templates, sandbox configuration, and local runtime caches after authorization.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter and changelog show 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
