## Description:

将已有的短剧镜头素材整理成剪辑单，完成镜序、声音、字幕与成片交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Short-drama creators and editors use this skill to select usable shots, document edit decisions, add subtitles and sound, render an episode, and check its delivery requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local renderer can overwrite files beyond an intended output boundary when an episode output tree contains symlinks.

Mitigation: Render only trusted projects; inspect or remove output-tree symlinks and consider a sandbox with limited filesystem access.

Risk: Optional Remotion rendering requires installing additional packages.

Mitigation: Use the default ffmpeg subtitle route unless Remotion is needed, and install dependencies only from a trusted package source.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-edit)
- [Editing and shot sequence](references/cut-craft.md)
- [Sound and subtitles](references/sound-and-subtitles.md)
- [Delivery and verification](references/delivery-verify.md)
- [Remotion documentation](https://www.remotion.dev/)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown editing decisions and delivery guidance with optional render commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendering also writes video and verification files to the project.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
