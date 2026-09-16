## Description:

Query alltrails.com for trail search, trail details, reviews, photos, weather, saved lists, completed trails, and activity feed data from a shell with @fetchproxy/cli fpx through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch AllTrails trail and user-session data from shell workflows without running the alltrails-mcp server. It is useful for scripts or environments where MCP is unavailable, while still requiring appropriate browser session access for private account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes AllTrails requests through a signed-in browser session and can return profile, list, completion, and activity data.

Mitigation: Use it only with accounts and sessions appropriate for the task, treat returned data as private, and avoid logging or sharing captured headers or API responses.

Risk: The documented setup uses an unpinned global CLI install and a temporary file path for captured session data.

Mitigation: Prefer a pinned or local @fetchproxy/cli installation, use a secure temporary file instead of /tmp/at.json, and delete captured session data after use.

## Reference(s):

- [AllTrails endpoint examples](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails GET and read POST workflows; outputs may include private profile, list, completion, and activity data from the signed-in browser session.]

## Skill Version(s):

2.3.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
