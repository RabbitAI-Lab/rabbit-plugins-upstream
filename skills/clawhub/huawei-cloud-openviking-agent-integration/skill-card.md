## Description:

Integrates and unbinds OpenViking long-term memory for coding agents using each agent's native MCP, HTTP memory provider, TypeScript hook, or settings configuration mechanism.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to connect, verify, monitor, and remove OpenViking long-term memory integrations across supported coding agents. It is intended for environments where agent startup templates and sandbox configuration can be modified with explicit user authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently modify agent startup templates and sandbox configuration.

Mitigation: Use dry-run first, require explicit authorization for integration or unbinding, verify status after changes, and rely on generated backup files for rollback.

Risk: Remote plugin sources may change between installations.

Mitigation: Review or pin plugin sources before use and rely on the skill's byte-verification and cache workflow where available.

Risk: OpenViking endpoint or API-key handling can expose sensitive access paths if used carelessly.

Mitigation: Prefer local or trusted HTTPS endpoints, avoid passing root API keys on the command line, and do not echo credentials in logs or chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-openviking-agent-integration)
- [Agent configuration reference](references/agent-configs.md)
- [Guardrails](references/guardrails.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification and acceptance criteria](references/verification.md)
- [Related commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include status checks, dry-run guidance, integration or unbinding commands, and configuration review steps.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter and changelog report 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
