## Description:

Routes agent requests for supported creative applications through DCC-MCP typed tools, CLI workflows, and scoped DCC-CUA UI control boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and automation agents use this skill to discover and invoke DCC-MCP capabilities for creative tools, route local or remote gateway workflows, and apply UI-control fallback with explicit consent and verification boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gateway helper configuration can send tool payloads to arbitrary endpoints, including non-HTTPS remote endpoints.

Mitigation: Use the default local gateway or named trusted HTTPS profiles, and avoid untrusted values for DCC_MCP_BASE_URL or --base-url.

Risk: The skill can operate local DCC applications and install or update related tooling with user consent.

Mitigation: Install only from trusted DCC-MCP sources, require explicit consent before launch or mutation, and rely on the documented official-manifest and SHA-256 verification path for CLI installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP source skill](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [CLI cheatsheet](references/CLI_CHEATSHEET.md)
- [Local application path cache](references/LOCAL_APP_PATH_CACHE.md)
- [Zero instances CLI guide](references/ZERO_INSTANCES_CLI.md)
- [Released products catalog](references/PRODUCTS.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, JSON-oriented command examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve DCC-MCP routing boundaries, consent requirements, and post-action verification guidance.]

## Skill Version(s):

0.19.99 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
