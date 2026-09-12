## Description:

DCC-MCP Creator guides developers and agents through creating or modernizing DCC-MCP adapters and standalone internal MCP services for DCC and studio systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, scaffold, modernize, test, and release DCC-MCP adapters or private standalone MCP services. It helps choose runtime boundaries, host dispatch patterns, gateway behavior, packaging, and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned npm debugging command can resolve a different package version over time.

Mitigation: Pin or preinstall the MCP Inspector package in higher-assurance environments before using the debugging workflow.

Risk: Adapter and service testing can interact with local DCC runtimes, internal services, or credentials.

Mitigation: Run testing in a development environment without production credentials, keep development on loopback by default, and require operator-owned TLS, authentication, firewall policy, secret storage, and audit controls before intranet exposure.

## Reference(s):

- [DCC-MCP Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [Clawdis homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [ADAPTER_WORKFLOW.md](references/ADAPTER_WORKFLOW.md)
- [INTERNAL_SERVICE_WORKFLOW.md](references/INTERNAL_SERVICE_WORKFLOW.md)
- [HOST_PATTERN_MATRIX.md](references/HOST_PATTERN_MATRIX.md)
- [ASYNC_RECOVERY.md](references/ASYNC_RECOVERY.md)
- [CORE_ESCALATION_CHECKLIST.md](references/CORE_ESCALATION_CHECKLIST.md)
- [TESTING_AND_RELEASE.md](references/TESTING_AND_RELEASE.md)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Core protocol router ADR](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/docs/adr/033-mcp-http-protocol-router.md)
- [Protocol type ownership ADR](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/docs/adr/027-protocol-type-ownership.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with code snippets, shell commands, checklists, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include adapter scaffolding recommendations, validation steps, release guidance, and risk notes.]

## Skill Version(s):

0.19.103 (source: release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
