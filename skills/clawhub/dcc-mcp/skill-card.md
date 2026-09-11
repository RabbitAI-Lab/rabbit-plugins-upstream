## Description:

Routes agent requests for 37 released creative products and one application UI route through DCC-MCP typed tools, gateway workflows, and consent-gated setup paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and automation engineers use this skill to discover, route, and invoke DCC-MCP capabilities for supported creative applications while preserving explicit consent boundaries for setup, launch, remote gateway, and UI-control workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate DCC applications, write files, contact gateways, and guide setup actions.

Mitigation: Review each requested launch, install, marketplace change, remote gateway, or external issue action before approving, and confirm the target app, path, gateway, package ID, and source.

Risk: A stale or incorrect UI binding could affect the wrong application window.

Mitigation: Require exact provider, runtime, process ID, and native window handle attestation before UI control, refresh observations before state-dependent actions, and verify post-action state.

Risk: A remote gateway or downloaded CLI asset could point to an unexpected destination or binary.

Mitigation: Use explicit trusted gateway origins, reject non-loopback HTTP for remote gateways, and rely on the consent-gated official release manifest with SHA-256 verification for CLI installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [Source Skill Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [CLI Cheatsheet](references/CLI_CHEATSHEET.md)
- [Gateway Profiles](references/GATEWAY_PROFILES.md)
- [Zero Instances CLI](references/ZERO_INSTANCES_CLI.md)
- [Local Application Path Cache](references/LOCAL_APP_PATH_CACHE.md)
- [Failure Reporting](references/FAILURE_REPORTING.md)
- [Released Product Catalog](references/PRODUCTS.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route live application control, file writes, gateway calls, CLI setup, and UI-control workflows when the user grants the relevant permission.]

## Skill Version(s):

0.19.103 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
