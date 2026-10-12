## Description:

Find New York City events and activities with dates, prices, images, and booking links tailored to a person's plans and preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liangstl](https://clawhub.ai/user/liangstl)

### License/Terms of Use:

MIT-0

## Use Case:

People planning outings in New York City use this skill through an agent to find relevant events, shows, classes, and other activities, with follow-up details and booking links.

### Deployment Geography for Use:

New York City, United States

## Known Risks and Mitigations:

Risk: The third-party service receives personal preferences, location, prior activity, and potentially sensitive accessibility, health, or age details.

Mitigation: Send only details needed for the request; ask before sharing sensitive details or prior-history context.

Risk: A persistent user account token grants access to a credit-spending service.

Mitigation: Explain credit use, obtain consent before retaining the token, and avoid unnecessary searches or detail requests.

## Reference(s):

- [SyncSo skill on ClawHub](https://clawhub.ai/liangstl/skills/syncso)
- [SyncSo connection page](https://syncso.com/connect)
- [SyncSo MCP service](https://rtdb.syncso.com/partner/mcp)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Ranked Markdown event cards with images, times, prices, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Times are New York local; searches and detail requests spend the user's account credits.]

## Skill Version(s):

2.0.3 (source: server-resolved ClawHub release; bundled skill metadata says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
