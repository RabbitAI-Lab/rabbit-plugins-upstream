## Description:

This skill helps an agent answer AllTrails hiking and trail-data requests, including trail search, details, reviews, photos, weather, saved lists, completed trails, and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for read-only AllTrails trail discovery and account-aware hiking information through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration is unofficial, relies on a signed-in browser session, and may violate or be affected by AllTrails' Terms of Service.

Mitigation: Install only after accepting those constraints, invoke it explicitly for AllTrails-related requests, and keep use limited to appropriate trail searches or the user's own AllTrails lists and activity.

Risk: The browser bridge can fail when the AllTrails tab is not signed in, the extension is not connected, or AllTrails-side protections change.

Mitigation: Keep a signed-in alltrails.com tab open, use the documented healthcheck when tools fail, and treat failures as operational limitations rather than authoritative absence of data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/alltrails)
- [npm package](https://www.npmjs.com/package/alltrails-mcp)
- [Project source repository](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration snippets and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails responses may include trail records, reviews, photos, GPX route data, weather summaries, profile data, saved lists, completed trails, and activity feed items.]

## Skill Version(s):

2.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
