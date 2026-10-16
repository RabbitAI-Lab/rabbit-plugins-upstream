## Description:

Fetch upcoming events from Luma (lu.ma) for any city when the user asks about tech events, startup meetups, networking events, conferences, or local happenings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[regalstreak](https://clawhub.ai/user/regalstreak)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to find upcoming public Luma events for selected cities, including technology meetups, startup events, conferences, and networking opportunities. The skill can return human-readable event summaries or JSON for follow-up filtering and comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches public event data but also instructs agents to automatically save event searches and inferred interests in local memory without a clear opt-out.

Mitigation: Use the skill only for explicit event-discovery requests, review local retention expectations with the user, and clear or disable ~/clawd/memory/luma-events.json when persistence is not desired.

## Reference(s):

- [ClawHub Luma Events skill page](https://clawhub.ai/regalstreak/skills/luma)
- [regalstreak publisher profile](https://clawhub.ai/user/regalstreak)
- [Luma public event pages](https://lu.ma)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable event summaries or JSON emitted by the Python fetch script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inputs are city slugs with optional day-range and result-limit filters. The artifact instructs agents to retain fetched event summaries in a local memory file.]

## Skill Version(s):

1.0.0 (source: server release evidence, SKILL.md frontmatter, package.json, README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
