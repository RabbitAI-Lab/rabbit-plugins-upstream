## Description:

This skill helps agents work with AllTrails trail data, including trail search, details, reviews, photos, weather, and signed-in user lists and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent answer hiking and trail questions from AllTrails data and review their own saved trails, completed trails, and activity through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an unofficial AllTrails browser bridge into a signed-in account.

Mitigation: Install it only when that access pattern is acceptable, be deliberate with requests involving personal trails or activity, and remove or disable the MCP entry when it is no longer needed.

Risk: AllTrails has no public API, so the integration may break or conflict with service terms.

Mitigation: Review the applicable AllTrails terms before use and expect failures such as 403 responses or bridge errors when the signed-in browser session, extension, or upstream behavior changes.

## Reference(s):

- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source repository listed by the skill](https://github.com/chrischall/alltrails-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides read-only AllTrails MCP usage; tool results may include trail details, reviews, photos, weather, GPX data, profile data, lists, and activity.]

## Skill Version(s):

2.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
