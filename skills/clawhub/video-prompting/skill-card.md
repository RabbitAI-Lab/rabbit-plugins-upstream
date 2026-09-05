## Description:

Use when crafting video or motion prompts for any generative model — dramaturgy, camera, physics-safe motion, frame anchors, and clip chaining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to write and review short video or motion prompts for text-to-video, image-to-video, avatar, animation, replacement, and instruction-based video-edit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install commands in the skill are not pinned to an immutable package version.

Mitigation: Install from a trusted source and pin the installer or package version when reproducibility matters.

Risk: Companion Pruna API workflows may involve uploading user media to an external service.

Mitigation: Upload only media the user is allowed to share, and review companion API guidance before granting credentials or running jobs.

Risk: Prompting guidance can produce misleading or low-quality video edits if applied without review.

Mitigation: Use the matching quality checklist and review generated prompts and media outputs before deployment.

## Reference(s):

- [Video prompt dramaturgy](references/prompt-dramaturgy.md)
- [Camera and lighting vocabulary](references/camera-lighting-vocabulary.md)
- [Physics-safe motion](references/physics-safe-motion.md)
- [Audio-in-video prompting](references/audio-in-video-prompting.md)
- [Clip chaining](references/clip-chaining.md)
- [Scene anchor pair](references/scene-anchor-pair.md)
- [Scene anchor triple](references/scene-anchor-triple.md)
- [p-video prompting quality checklist](references/p-video-quality-checklist.md)
- [p-video-avatar prompting](references/p-video-avatar-prompting.md)
- [p-video-avatar quality checklist](references/p-video-avatar-quality-checklist.md)
- [p-video-animate prompting](references/p-video-animate-prompting.md)
- [p-video-animate quality checklist](references/p-video-animate-quality-checklist.md)
- [p-video-replace prompting](references/p-video-replace-prompting.md)
- [p-video-replace quality checklist](references/p-video-replace-quality-checklist.md)
- [p-video-edit prompting](references/p-video-edit-prompting.md)
- [p-video-edit quality checklist](references/p-video-edit-quality-checklist.md)
- [smixs visual-skills](https://github.com/smixs/visual-skills)
- [inference-sh skills](https://github.com/inference-sh/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured prompt text and optional JSON or shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model-specific prompt fields, quality checklists, and media-handling cautions.]

## Skill Version(s):

1.0.11 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
