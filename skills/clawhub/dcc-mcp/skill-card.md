## Description:

Default DCC-MCP router for 35 released creative products and 3 current application routes that uses typed DCC-MCP tools first and keeps DCC-CUA/ui-control application UI work on the project-owned route without falling back to generic Computer Use providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical artists, and agent operators use this skill to route DCC and application UI requests across supported creative products through typed DCC-MCP tools, CLI workflows, and scoped DCC-CUA control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to install or update CLI tools, adapters, marketplace packages, launch GUI applications, and change DCC application state.

Mitigation: Require explicit user consent before installs, updates, launches, setup execution, adapter changes, marketplace changes, or issue-filing actions; inspect unfamiliar packages first and follow CLI-returned next steps.

Risk: Application UI control can operate real browser or desktop UI and may encounter authentication, security, purchase, or permission boundaries.

Mitigation: Use exact DCC-CUA binding, fresh observations, and post-action readback; hand CAPTCHA, authentication, purchase, and security confirmations to a human, and stop on interruption or permission failure.

Risk: Cached local application paths could be stale or could launch software unexpectedly if reused without confirmation.

Mitigation: Store only user-provided normalized paths and verification timestamps; verify the path, tell the user what was found, and ask for explicit confirmation before launching.

Risk: Remote gateway profiles and fallback REST paths can target local or remote application control surfaces.

Mitigation: Confirm the intended gateway profile and target before control actions, use gateway-required attribution when evidence is needed, and do not silently switch routes or fallback control providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [Declared homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [CLI cheatsheet](references/CLI_CHEATSHEET.md)
- [Local application path cache](references/LOCAL_APP_PATH_CACHE.md)
- [Released product catalog](references/PRODUCTS.json)
- [Zero instances CLI setup guide](references/ZERO_INSTANCES_CLI.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands and JSON-oriented CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents should prefer concise toon output for human-readable CLI results and JSON only when another program must parse the result.]

## Skill Version(s):

0.19.97 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
