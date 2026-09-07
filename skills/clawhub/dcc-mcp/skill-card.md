## Description:

DCC-MCP routes agent requests for 35 released creative products and 3 application UI routes through typed DCC-MCP tools first, with DCC-CUA/ui-control as the project-owned UI path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and agent operators use this skill to discover, select, and invoke DCC-MCP control routes for supported creative tools, local or remote gateway profiles, and scoped application UI automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad desktop and DCC automation can modify files, scenes, applications, or recordings when used with live tools.

Mitigation: Install and run the skill only when this level of application control is intended, and require explicit review before app launch, recording, browser UI, Office file, install, or update operations.

Risk: An untrusted or plaintext remote gateway URL can expose tool data or route control traffic outside the local trusted environment.

Mitigation: Keep the gateway on the default local endpoint or a trusted HTTPS remote, and do not set DCC_MCP_BASE_URL to an untrusted host.

Risk: Cached local application paths could otherwise lead to unintended application launches.

Mitigation: Use the documented cache behavior that stores only normalized paths and asks for explicit confirmation before starting a cached executable.

## Reference(s):

- [DCC-MCP ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP Source Skill](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [CLI Cheatsheet](references/CLI_CHEATSHEET.md)
- [Zero Instances CLI](references/ZERO_INSTANCES_CLI.md)
- [Local Application Path Cache](references/LOCAL_APP_PATH_CACHE.md)
- [Supported Products Catalog](references/PRODUCTS.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CLI commands, routing decisions, consent prompts, and verification steps for DCC-MCP or DCC-CUA workflows.]

## Skill Version(s):

0.19.100 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
