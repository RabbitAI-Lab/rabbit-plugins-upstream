## Description:

Finds personalized live events, activities, and places to go in New York City, with times, prices, images, and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liangstl](https://clawhub.ai/user/liangstl)

### License/Terms of Use:

MIT-0

## Use Case:

People planning outings in New York City use this skill through an assistant to discover relevant events and activities and find schedules, prices, and booking links.

### Deployment Geography for Use:

New York City, United States

## Known Risks and Mitigations:

Risk: Requests may disclose remembered preferences and sensitive personal details to SyncSo without clear consent.

Mitigation: Disclose the SyncSo query, omit prior-conversation memory unless the user requests personalization, and confirm before sharing sensitive details.

Risk: Sharing exact coordinates may expose a person's precise location.

Mitigation: Use a neighborhood or other coarse location instead of coordinates unless precise location is needed and approved.

Risk: Searches and detail lookups use the person's account credits.

Mitigation: Explain the account-linked allowance and request only as many results or details as the person needs.

## Reference(s):

- [SyncSo on ClawHub](https://clawhub.ai/liangstl/skills/syncso)
- [SyncSo account connection](https://syncso.com/connect)
- [SyncSo MCP endpoint](https://rtdb.syncso.com/partner/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown recommendations with images and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked New York City suggestions with dates, times, venues, and prices.]

## Skill Version(s):

2.0.2 (source: ClawHub release; supplied SKILL.md lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
