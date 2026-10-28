## Description:

Orchestrates the gtrk CLI to find B-roll and other media, then arrange candidate tracks in video projects, including workflows with local materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and agents use this skill to search for B-roll, music, and images, then arrange candidate media tracks in a video project. It supports cloud searches, local-material workflows, and editable plans for reviewing and refining selections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local-material mode still sends extracted video frames and planning data for cloud processing; selected original images may also upload.

Mitigation: Treat local mode as cloud-connected. Use --no-image-broll to exclude image candidates, noting that video-frame uploads can still occur, and avoid processing media that must remain on-device.

Risk: Cloud processing may incur costs, and forced replacement can overwrite edited tracks.

Mitigation: Agree on costs before using --yes and back up the project before approving forced replacement of edited tracks.

## Reference(s):

- [gtrk-matrix on ClawHub](https://clawhub.ai/gitruck/skills/gtrk-matrix)
- [Gitruck CLI](https://github.com/Gitruck/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON plans, Video project edits, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON plan examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May arrange candidate media tracks in a video project; cloud processing and costs may apply.]

## Skill Version(s):

1.3.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
