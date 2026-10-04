## Description:

Helps agents find concert setlists, artists, venues, and live-music history through setlist.fm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music fans and assistants use this skill to look up songs played at concerts, explore artists and venues, and resolve concerts by date and location. Attendance tools can also change a user's setlist.fm account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attendance marking and unmarking change a user's setlist.fm account despite read-only wording.

Mitigation: Require explicit user intent before using either attendance tool; do not treat the skill as read-only.

Risk: The integration requires a setlist.fm API key.

Mitigation: Provide the key only if comfortable granting the integration access, and do not expose it in responses.

## Reference(s):

- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [ClawHub setlist skill](https://clawhub.ai/chrischall/skills/setlist)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include setlist.fm attribution links and representative tour setlists clearly distinguished from the requested show.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
