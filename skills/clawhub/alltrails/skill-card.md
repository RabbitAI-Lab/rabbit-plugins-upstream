## Description:

This skill helps an agent answer AllTrails hiking and trail-data requests, including trail search, trail details, reviews, photos, weather, saved lists, completed trails, and account activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to read-only AllTrails trail discovery, trail-detail, review, photo, weather, and signed-in account activity workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an unofficial AllTrails integration through a signed-in browser session.

Mitigation: Use it only for explicit AllTrails tasks and only with an account/session the user is comfortable exposing to the agent.

Risk: Broad hiking requests may cause access to account-linked AllTrails activity data.

Mitigation: Ask for confirmation before invoking account-specific tools such as profile, saved lists, completed trails, or activity feed.

Risk: The integration may break or behave inconsistently because it depends on AllTrails internal behavior and bot-protection flow.

Mitigation: Run the healthcheck when tool calls fail and treat returned data as advisory until confirmed against AllTrails directly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm Package](https://www.npmjs.com/package/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON configuration and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return compact or full trail, review, photo, weather, GPX, list, profile, and activity data depending on the invoked AllTrails tool and view setting.]

## Skill Version(s):

3.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
