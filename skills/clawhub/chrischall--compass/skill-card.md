## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Compass real-estate listing searches, property records, photos, price history, address resolution, comparisons, mortgage calculations, and diagnostics through a configured MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-backed Compass lookups use a local MCP server connected to a signed-in browser tab through fetchproxy.

Mitigation: Install only when that browser-mediated access is acceptable, review the fetchproxy pairing prompt, and approve only the expected compass.com scope.

Risk: The setup depends on external npm and GitHub code that may change over time.

Mitigation: Review the installed package and extension source at the version being deployed before enabling the skill in a trusted environment.

Risk: Compass may present sign-in requirements, WAF challenges, or unsupported saved-home and saved-search flows.

Mitigation: Use the documented healthcheck and session tools, resolve browser challenges in the signed-in tab, and treat unsupported flows as unavailable rather than relying on fallback behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Compass listing fields, property details, photo URLs, price history, comparison tables, mortgage calculations, setup steps, and per-target error messages.]

## Skill Version(s):

0.12.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
