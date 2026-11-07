## Description:

Creates personalized birthday videos with a name song, animated photos, milestone montages, pet celebrations, or animated cards and invitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families use this skill to create a personal birthday video or song from a name, age, photos, and personal details, ready to share with friends and family.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal photos, voice samples, and details may be sent to Varg and its model providers, whose retention and deletion terms are not explained in the package.

Mitigation: Share only media and details you are authorized to send, and check the providers’ retention and deletion terms.

Risk: Video generation and retries can incur variable costs.

Mitigation: Quote each clip before generation and agree on a generation budget.

Risk: Assembly can overwrite an existing output file when its filename is reused.

Mitigation: Choose a filename that can safely be overwritten.

## Reference(s):

- [ClawHub release](https://clawhub.ai/vargai/skills/varg-birthday-video)
- [Varg birthday video guide](https://varg.ai/how-to/make-a-birthday-video)
- [Birthday formats and prompts](references/formats.md)
- [Songwriting guide](references/song.md)
- [Visual styles](references/styles.md)

## Skill Output:

**Output Type(s):** [Video files, Audio, Guidance, Shell commands]

**Output Format:** [MP4 video with generated audio; Markdown guidance and Bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized to the supplied name, age, photos, and details; export dimensions and duration depend on the selected sharing format.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
