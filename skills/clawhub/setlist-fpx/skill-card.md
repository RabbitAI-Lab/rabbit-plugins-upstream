## Description:

Guides agents in reading setlist.fm concert data through its REST API and changing attendance through an authenticated browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and concertgoers use this skill to find setlists, artists, venues, cities, and users, and to mark or unmark their attendance at shows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local tool and browser extension can access setlist.fm login cookies, which can be reused to perform account actions.

Mitigation: Grant access only if comfortable with that exposure; treat captured cookies like passwords, avoid sharing logs or screenshots containing them, and remove or unpair the bridge profile when finished.

Risk: An attendance toggle can reverse the intended state if sent without checking the current state.

Mitigation: Check the current state, dry-run before changing it, and recheck the page afterward.

## Reference(s):

- [setlist-fpx ClawHub release](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm API access](https://www.setlist.fm/settings/api)
- [REST API read endpoints](references/rest-api.md)
- [Attendance change walkthrough](references/attendance-write.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The free API key is for non-commercial use; displayed data requires setlist.fm attribution and must not be persistently cached.]

## Skill Version(s):

1.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
