## Description:

Guides agents through assembling and polishing already-rendered clips with ffmpeg or composing multi-layer videos with optional Hyperframes, rather than generating video with AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to assemble finished clips, add captions, overlays and music, compose narrated showcases, and prepare exports for different platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example ffmpeg commands using -y may overwrite existing output files.

Mitigation: Check output filenames before running the commands.

Risk: Broad or unpinned installs may bring in more packages than the editing task requires.

Mitigation: Prefer pinned or reviewed versions and avoid full-suite or --full-depth installs unless needed.

## Reference(s):

- [ClawHub video-editing release](https://clawhub.ai/pruna-ai/skills/video-editing)
- [Assembly and concat](artifact/references/assembly-concat.md)
- [Captions and subtitles](artifact/references/captions.md)
- [Combination videos (Hyperframes)](artifact/references/combination-hyperframes.md)
- [Export presets](artifact/references/export-presets.md)
- [Hyperframes project](https://github.com/heygen-com/hyperframes)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with ffmpeg commands and optional HTML composition examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires pre-rendered media and local video-processing tools; does not generate video with AI.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
