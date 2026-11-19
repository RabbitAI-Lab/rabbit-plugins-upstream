## Description:

在使用者的本地工作区制作 Vlog、原声纯享版、照片段落和封面。实际阅片、确认故事后，按章节同步交付分镜脚本和可播放的 HTML 选材页，并按题材剪辑与交付。适用于本地影像制作和修订。

This skill is ready for commercial/non-commercial use.

## Publisher:

[milanor1970](https://clawhub.ai/user/milanor1970)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use this skill to review local footage, confirm a story, and produce Vlog edits with a synchronized storyboard and playable selection preview. It also supports local media refinement, captions, covers, and sound checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan classifies the release as suspicious with medium confidence and had incomplete path coverage.

Mitigation: Review the skill's required access before use and run it only with trusted workspaces and executable settings.

Risk: The scan flags availability and executable trust risks, and calls out resolved Pillow and NumPy versions for review without establishing that they are vulnerable.

Mitigation: Check the resolved Pillow and NumPy versions and assess any concerns from their actual versions; do not treat the scan as proof of a vulnerability.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/milanor1970/skills/local-vlog-production)
- [First run and local workspace setup](references/first-run.md)
- [Storyboard and selection review](references/storyboard-review.md)
- [Visual presets](references/visual-presets.md)
- [Optional editing patterns](references/optional-edits.md)
- [Validation workflow](references/validation.md)
- [FFmpeg downloads](https://ffmpeg.org/download.html)
- [Smiley Sans font source](https://github.com/atelier-anchor/smiley-sans)
- [Ma Shan Zheng font source](https://github.com/google/fonts/tree/main/ofl/mashanzheng)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON configuration, Video files, Image files, Editing guidance]

**Output Format:** [Markdown storyboards and notes, playable HTML selection previews, JSON timelines, and rendered media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local project deliverables; storyboard and selection preview are kept in sync across revisions.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
