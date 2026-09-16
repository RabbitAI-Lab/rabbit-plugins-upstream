## Description:

Operate named supported apps through DCC-MCP, discover typed tools, and support marketplace skill workflows for explicit DCC-MCP or DCC-CUA requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative technical users use this skill to route agent work to supported digital content creation, UI control, and Office applications through DCC-MCP. It supports live instance discovery, typed tool execution, marketplace maintenance, setup guidance, and verified post-action readback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad control over supported creative, Office, browser, and other application UI surfaces.

Mitigation: Install only when this automation is desired, keep actions within the user's requested scope, prefer typed DCC-MCP tools, and verify state with post-action readback.

Risk: Gateway workflows can contact local or explicitly approved remote endpoints and may transmit project data needed for an operation.

Mitigation: Use the default loopback gateway unless the user approves an exact remote HTTPS origin, validate gateway URLs, and avoid sending credentials in payloads.

Risk: CLI, component, adapter, and marketplace install or update actions can change local state.

Mitigation: Require user consent before install, update, launch, marketplace, or broad UI-control actions, and use the documented verified release manifest and SHA-256 checks where provided.

Risk: Cached application paths can become stale or point to unintended local software.

Mitigation: Cache only user-provided absolute paths, store no credentials or launch arguments, re-check the path, and ask for explicit confirmation before launching.

## Reference(s):

- [DCC-MCP Skill source](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [DCC-MCP ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [CLI cheatsheet](references/CLI_CHEATSHEET.md)
- [Tool execution](references/TOOL_EXECUTION.md)
- [Gateway profiles](references/GATEWAY_PROFILES.md)
- [Application UI workflows](references/UI_WORKFLOWS.md)
- [Marketplace maintenance](references/MARKETPLACE_MAINTENANCE.md)
- [Local application path cache](references/LOCAL_APP_PATH_CACHE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured JSON payloads, and file or configuration changes when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include local or gateway command plans, typed tool-call arguments, setup prompts, failure reports, and post-action verification summaries.]

## Skill Version(s):

0.19.106 (source: SKILL.md metadata, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
