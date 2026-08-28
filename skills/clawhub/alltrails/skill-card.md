## Description:

This skill helps agents retrieve AllTrails hiking and trail data, including trail search results, details, reviews, photos, weather, GPX routes, and a signed-in user's saved lists and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to query AllTrails for trail discovery, trail details, reviews, photos, route GPX data, weather, or their own signed-in AllTrails lists and activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad trigger wording may route ordinary hiking or trail questions through AllTrails even when the user did not intend to query AllTrails.

Mitigation: Invoke the skill for explicit AllTrails or personal AllTrails-data requests, and confirm intent before using it for general hiking questions.

Risk: The skill uses an unofficial AllTrails bridge through a signed-in browser session.

Mitigation: Install and use it only when the user is comfortable with that access pattern and understands that personal AllTrails data may be queried.

Risk: All tools are read-only, but per-user tools can expose saved lists, completed trails, profile data, and activity from the signed-in session.

Mitigation: Use per-user tools only for user-authorized requests and avoid sharing returned personal data beyond the current task.

## Reference(s):

- [alltrails ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source repository](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration snippets and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trail metadata, review summaries, photo URLs, weather summaries, user-list references, activity summaries, and GPX route text when requested.]

## Skill Version(s):

2.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
