## Description:

Finds and ranks New York City activities and events with reasons, times, prices, images, and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liangstl](https://clawhub.ai/user/liangstl)

### License/Terms of Use:

MIT-0

## Use Case:

People and their assistants use SyncSo to find and compare live events, dining, classes, and other activities in New York City based on dates, location, budget, and preferences.

### Deployment Geography for Use:

New York City, United States

## Known Risks and Mitigations:

Risk: Routine planning requests may send sensitive preferences and location details to SyncSo.

Mitigation: Tell users what is shared and send only the personal details needed for the request.

Risk: Account codes and refresh tokens may remain usable for a long time and charge requests to the user's allowance.

Mitigation: Use a dedicated revocable token, protect it as a secret, and review the service's token storage and replacement options before relying on it.

## Reference(s):

- [SyncSo skill listing](https://clawhub.ai/liangstl/skills/syncso)
- [SyncSo account connection](https://syncso.com/connect)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown activity recommendations with images and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked results include reasons, local times, venues, and prices.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
