## Description:

Turns product footage into short-form ecommerce ads by recutting hooks, removing pauses, adding captions and calls to action, and exporting platform-ready variants with FFmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and ecommerce teams can use the skill to turn existing product, creator, or unboxing footage into short-form ads for TikTok, Reels, and Meta, including hook variants and alternate aspect ratios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-shell fallback sends selected footage to a hosted varg service, and its retention and access practices are not established by the supplied files.

Mitigation: Keep private footage local; use the hosted fallback only after explicitly approving the upload and checking the applicable data practices.

Risk: The scripts can overwrite files when output paths collide with existing files.

Mitigation: Choose separate output paths for each run and check that the targets do not contain files you need to keep.

## Reference(s):

- [Project homepage listed in skill metadata](https://github.com/vargHQ/skills/tree/main/ecommerce-video-edit)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/ecommerce-video-edit)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Editing guidance]

**Output Format:** [MP4 video variants (9:16 and 4:5), a JPEG cover frame, and Markdown guidance with inline Bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected workflow; variants can include one MP4 per hook.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
