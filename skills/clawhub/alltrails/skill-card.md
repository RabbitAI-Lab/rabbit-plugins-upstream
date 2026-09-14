## Description:

This skill should be used when the user asks about AllTrails hiking/trail data, including trail search, trail details, hike reviews, trail conditions, saved trails, completed trails, photos, and user activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure and operate an unofficial AllTrails MCP server for read-only trail search, trail details, reviews, photos, weather, saved lists, completed trails, and activity feed lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unofficial MCP server through a signed-in browser bridge, which can expose signed-in AllTrails data to the MCP host.

Mitigation: Install only after review, prefer project-local MCP configuration, and avoid exposing unrelated files or environment variables to the MCP host.

Risk: The setup example runs the package through npx without pinning a reviewed package version.

Mitigation: Pin a reviewed alltrails-mcp package version before use and re-review before upgrading.

Risk: AllTrails has no public API, so the internal API bridge may break or create Terms of Service and reliability concerns.

Mitigation: Use the skill with a signed-in account only when acceptable under applicable terms, and expect failures from AllTrails-side changes or bot-protection behavior.

## Reference(s):

- [ClawHub alltrails skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source repository](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with MCP setup snippets, tool-use guidance, and troubleshooting notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails MCP usage; compact responses are the default, with full records available when explicitly requested.]

## Skill Version(s):

2.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
