## Description:

Use when crafting video or motion prompts for any generative model - dramaturgy, camera, physics-safe motion, frame anchors, and clip chaining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to craft and validate short video or motion prompts across generative video models, including text-to-video, image-to-video, frame-anchor, camera, motion, audio, and clip-chaining workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install examples use unpinned remote installer commands with auto-confirmation.

Mitigation: Review installer commands before use, prefer pinned versions or commit-locked sources, and avoid auto-confirmation until the installed content has been inspected.

Risk: The workflow may involve uploading user media to Pruna or related APIs.

Mitigation: Upload media only after the user has approved that data sharing.

## Reference(s):

- [Skill page](https://clawhub.ai/pruna-ai/skills/video-prompting)
- [Video prompt dramaturgy](artifact/references/prompt-dramaturgy.md)
- [Camera and lighting vocabulary](artifact/references/camera-lighting-vocabulary.md)
- [Physics-safe motion](artifact/references/physics-safe-motion.md)
- [Clip chaining](artifact/references/clip-chaining.md)
- [Audio-in-video prompting](artifact/references/audio-in-video-prompting.md)
- [Scene anchor pair](artifact/references/scene-anchor-pair.md)
- [Scene anchor triple](artifact/references/scene-anchor-triple.md)
- [p-video prompting quality checklist](artifact/references/p-video-quality-checklist.md)
- [p-video-2 prompting](artifact/references/p-video-2-prompting.md)
- [p-video-2 quality checklist](artifact/references/p-video-2-quality-checklist.md)
- [p-video-avatar prompting](artifact/references/p-video-avatar-prompting.md)
- [p-video-avatar quality checklist](artifact/references/p-video-avatar-quality-checklist.md)
- [p-video-animate prompting](artifact/references/p-video-animate-prompting.md)
- [p-video-animate quality checklist](artifact/references/p-video-animate-quality-checklist.md)
- [p-video-replace prompting](artifact/references/p-video-replace-prompting.md)
- [p-video-replace quality checklist](artifact/references/p-video-replace-quality-checklist.md)
- [p-video-edit prompting](artifact/references/p-video-edit-prompting.md)
- [p-video-edit quality checklist](artifact/references/p-video-edit-quality-checklist.md)
- [smixs visual-skills](https://github.com/smixs/visual-skills)
- [inference-sh skills](https://github.com/inference-sh/skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown prose with structured prompt blocks, checklists, and JSON-shaped planning examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model-specific prompt fields, quality checks, and media-sharing cautions.]

## Skill Version(s):

1.0.12 (source: release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
