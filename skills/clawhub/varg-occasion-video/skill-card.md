## Description:

Guides an agent in turning photos and occasion details into invitation, holiday, anniversary, and tribute videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this workflow to help people create invitation, holiday, anniversary, and memorial videos from photos and event details. It covers planning the message and style, generating scenes, and assembling a shareable video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Photos and event details are sent to Varg's hosted services, and their retention or sharing policies are not established by this package.

Mitigation: Get permission to use submitted photos and keep private invitation details local when possible.

Risk: Video generation can incur service costs.

Mitigation: Estimate and confirm the cost before generation.

Risk: The assembly script overwrites an existing output file with the same name.

Mitigation: Choose a new output filename before assembly.

## Reference(s):

- [Invitation and occasion video guide](https://varg.ai/how-to/make-birthday-and-occasion-videos)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/varg-occasion-video)
- [Holiday and festival greetings](artifact/references/holidays.md)
- [Invitations and save-the-dates](artifact/references/invitations.md)
- [Old photos, anniversaries and tributes](artifact/references/old-photos.md)
- [Video styles](artifact/references/styles.md)
- [Kling guide to animating old photos](https://kling.ai/blog/animate-old-photos)

## Skill Output:

**Output Type(s):** [Video files, Guidance, API calls, Shell commands]

**Output Format:** [MP4 video with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated using hosted services; review the result before sharing.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
