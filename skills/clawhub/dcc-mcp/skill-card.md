## Description:

Default DCC-MCP router for 35 released creative products and 3 current application routes; it directs agents to typed DCC-MCP tools first and uses the project-owned DCC-CUA route for supported application UI tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to discover, route, and call DCC-MCP capabilities for supported creative tools and application UI workflows while preserving explicit boundaries for setup, gateway use, and UI control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route an agent to control supported creative tools and application UIs, which can change local or external state.

Mitigation: Approve CLI installation, app launches, marketplace install/update/uninstall actions, remote gateway changes, and GitHub feedback filing only after reviewing the exact command or requested action.

Risk: UI automation can encounter authentication, CAPTCHA, purchase, security, or native confirmation boundaries.

Mitigation: Keep those boundaries as human handoff points and stop on interruption, permission failure, stale binding data, or missing post-action readback.

Risk: A zero live-instance result can be mistaken for proof that a product is unsupported or uninstalled.

Mitigation: Use the zero-instance guide to keep catalog support, package installation, project bootstrap, live registration, readiness, and real-host effect evidence separate before any mutation.

## Reference(s):

- [DCC-MCP ClawHub page](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP source skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [CLI cheatsheet](references/CLI_CHEATSHEET.md)
- [Zero instances CLI guide](references/ZERO_INSTANCES_CLI.md)
- [Local application path cache](references/LOCAL_APP_PATH_CACHE.md)
- [Released products catalog](references/PRODUCTS.json)
- [DCC discovery decision schema](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/contracts/dcc-discovery-decision-v1.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to execute CLI commands, inspect tool schemas, preserve operation identifiers, and request user consent before state-changing actions.]

## Skill Version(s):

0.19.98 (source: server release metadata, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
