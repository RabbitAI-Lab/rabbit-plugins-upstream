## Description:

Creates shareable AI videos for occasion invitations, holiday greetings, anniversary stories, old family photos, and memorial or tribute films using photos and event details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to make occasion invitations, holiday greetings, anniversary films, and family tributes from photos and event details, then prepare a shareable video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Family photos and event details are processed by Varg and its generation providers, which may expose sensitive personal information.

Mitigation: Get agreement from the people shown, review provider retention practices, and add private invitation details locally where practical.

Risk: Video and music generation can incur costs, and generated names, dates, or places may be inaccurate.

Mitigation: Estimate and quote costs before generation, then check every name, date, and place in the finished video before sharing it.

Risk: The assembly script writes to the requested output path and can overwrite an existing video.

Mitigation: Choose a fresh output filename before assembling the video.

## Reference(s):

- [Varg occasion video guide](https://varg.ai/how-to/make-birthday-and-occasion-videos)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/varg-occasion-video)
- [Invitations and save-the-dates](references/invitations.md)
- [Holiday and festival greetings](references/holidays.md)
- [Old photos, anniversaries and tributes](references/old-photos.md)
- [Styles for occasion videos](references/styles.md)

## Skill Output:

**Output Type(s):** [Video files, Guidance, Shell commands]

**Output Format:** [MP4 video with H.264/AAC, plus text guidance and Bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines one or more clips with music; the assembly script defaults to vertical 9:16 and supports 16:9 output.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
