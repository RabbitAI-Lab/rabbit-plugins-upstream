## Description:

Guides an agent through creating a personalized AI birthday video from a person's details and photos, including a custom song, generated scenes, and a finished export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating a birthday surprise for a friend, family member, or pet use this skill to plan a personalized video, generate its images and music through Varg, and assemble an export suited to its destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal photos and details are sent to Varg and its model providers for online generation.

Mitigation: Use only material you are authorized to share, and review the providers' retention and sharing terms, especially for family photos.

Risk: Video and music generation can incur usage costs, and assembly can overwrite an existing output file.

Mitigation: Confirm the quoted generation cost before each run and choose an output filename that is safe to overwrite.

## Reference(s):

- [Varg birthday video guide](https://varg.ai/how-to/make-a-birthday-video)
- [formats.md](artifact/references/formats.md)
- [song.md](artifact/references/song.md)
- [styles.md](artifact/references/styles.md)
- [assemble.sh](artifact/scripts/assemble.sh)

## Skill Output:

**Output Type(s):** [Video files, Guidance, Shell commands]

**Output Format:** [Exported MP4 video with supporting prompts and assembly guidance]

**Output Parameters:** [One personalized video; duration, aspect ratio, and size depend on the destination]

**Other Properties Related to Output:** [May include generated stills, clips, and an original song.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
