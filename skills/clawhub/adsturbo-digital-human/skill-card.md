## Description:

Helps agents create talking-avatar videos using a platform avatar, a custom photo-and-voice persona, or one-off portrait lip sync, with text-to-speech and avatar management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to turn scripts, authorized portraits, and voice recordings into narrated avatar videos or lip-synced clips through AdsTurbo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face and voice cloning can enable unauthorized impersonation or deceptive synthetic media.

Mitigation: Use only faces, voices, and recordings with documented permission; avoid impersonation and misleading content.

Risk: Uploading portraits and recordings sends sensitive media to AdsTurbo and can yield publicly accessible asset URLs.

Mitigation: Confirm the user accepts third-party processing and potential public asset URLs before uploading; avoid sharing sensitive media unnecessarily.

Risk: Deleting a custom persona may be irreversible.

Mitigation: Confirm the exact persona and obtain explicit approval before deletion; assume recovery is unavailable unless AdsTurbo documents it.

Risk: Resubmitting an in-progress media task after a timeout can incur duplicate charges.

Mitigation: Check the existing task status instead of resubmitting after a timeout.

## Reference(s):

- [AdsTurbo Digital Human skill](https://clawhub.ai/adsturbo/skills/adsturbo-digital-human)
- [AdsTurbo API key setup](https://adsturbo.ai/iris/api)
- [Digital human usage guide](references/digital_human.md)
- [Asset upload guide](references/upload.md)
- [Task status guide](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Text or Markdown with generated media links and task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation is asynchronous; results are returned as links.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
