## Description:

Provides read-only AllTrails trail search, trail details, reviews, photos, weather, GPX export, and signed-in user hiking data through an unofficial MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when answering hiking and trail questions with AllTrails-backed search, trail details, reviews, weather, photos, GPX data, and signed-in user lists or activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in AllTrails browser session for broad hiking requests and account data without a clear per-use consent boundary.

Mitigation: Install only when read-only access through the signed-in AllTrails tab is acceptable; keep the tab open only when needed and review source/package contents before use.

Risk: The unofficial MCP server relies on AllTrails internal endpoints and browser-mediated access that may break or conflict with AllTrails terms.

Mitigation: Use it only when AllTrails-backed results are explicitly desired, expect service changes, and review AllTrails terms and package behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [npm package: alltrails-mcp](https://www.npmjs.com/package/alltrails-mcp)
- [Source: chrischall/alltrails-mcp](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API calls, Markdown]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool call descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails data access; signed-in session behavior depends on the user's AllTrails browser tab and fetchproxy bridge.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
