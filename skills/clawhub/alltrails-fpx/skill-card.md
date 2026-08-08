## Description:

Query alltrails.com for trail search, trail detail, reviews, photos, weather, and signed-in account data from shell commands with @fetchproxy/cli through an active browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to make read-only AllTrails lookup requests from shell workflows when the MCP server is unavailable or unsuitable. It is useful for trail research, route details, weather, photos, reviews, and signed-in saved or completed trail data when the user intends to expose that browser session data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access signed-in AllTrails account data through the user's active browser session.

Mitigation: Use a signed-out or separate browser profile for public trail lookup, and request saved lists, completed trails, or activity feeds only when that account data should be exposed to the agent.

Risk: AllTrails calls can return challenge pages, non-JSON bodies, or stale app-key errors instead of usable data.

Mitigation: Refresh the AllTrails tab, recapture the x-at-key value, and verify that returned bodies are valid JSON before relying on the result.

## Reference(s):

- [AllTrails endpoints for fpx](artifact/references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails API calls executed through an active browser session; responses are expected to be JSON but should be checked for challenge pages or upstream errors.]

## Skill Version(s):

2.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
