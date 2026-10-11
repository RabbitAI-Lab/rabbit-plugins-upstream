## Description:

Helps agents look up concert setlists and live-music history through setlist.fm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music fans and researchers use this skill to find songs performed at concerts and explore shows by artist, venue, city, date, or tour. It also offers tools to mark or unmark concerts as attended on a user's account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite read-only wording, attendance tools can change the user's setlist.fm account without a built-in confirmation step.

Mitigation: Require explicit user approval before marking or unmarking any concert as attended.

Risk: The integration requires access to a user's setlist.fm API key.

Mitigation: Provide the key only to a trusted server and do not expose or share it in responses.

Risk: A free setlist.fm API key is limited to non-commercial use, even though this release has a commercial usage posture.

Mitigation: Obtain setlist.fm permission before commercial API use and include source links when presenting results.

## Reference(s):

- [setlist-mcp package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key setup](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with links to setlist.fm results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may include song lists, show details, and links to the source results.]

## Skill Version(s):

1.1.8 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
