## Description:

Discover public page URLs across a website using the AI Web Map skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use this skill to discover page URLs and site-wide entry points from a public website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted website URLs are sent to Dataify, and successful requests consume account credits; large result limits may increase scope and cost.

Mitigation: Use public URLs, choose an appropriate result limit, and preview requests with --dry-run. Keep the token in an environment variable and use only a trusted HTTPS gateway.

## Reference(s):

- [Map API reference](references/map-api.md)
- [AI Web Map on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-ai-web-map)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON array of discovered URL objects, or null when no URLs are found]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [URL objects may include titles and descriptions.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
