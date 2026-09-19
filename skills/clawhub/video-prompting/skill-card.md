## Description:

Use when crafting video or motion prompts for any generative model - dramaturgy, camera, physics-safe motion, frame anchors, and clip chaining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to craft short-video and motion-generation prompts, including text-to-video, image-to-video, start/end frame anchors, narrated beats, camera and lighting cues, physics-safe motion, and clip chaining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional install examples use mutable npx package references.

Mitigation: Install from a trusted PrunaAI source and prefer version-pinned commands or reviewed release artifacts.

Risk: Using the video workflows may upload prompts, images, audio, or video assets to Pruna APIs.

Mitigation: Review media and prompt contents before use, avoid uploading sensitive assets unless approved, and follow the applicable API data-handling policy.

Risk: Generated video outputs can be visually incorrect, misleading, truncated, or misaligned with audio.

Mitigation: Apply the matching quality checklist from the skill references and visually review outputs before publication or downstream use.

## Reference(s):

- [Prompt Dramaturgy](references/prompt-dramaturgy.md)
- [Camera and Lighting Vocabulary](references/camera-lighting-vocabulary.md)
- [Physics-Safe Motion](references/physics-safe-motion.md)
- [Audio-in-Video Prompting](references/audio-in-video-prompting.md)
- [Clip Chaining](references/clip-chaining.md)
- [Scene Anchor Pair](references/scene-anchor-pair.md)
- [Scene Anchor Triple](references/scene-anchor-triple.md)
- [p-video-2-pro Prompting](references/p-video-2-pro-prompting.md)
- [p-video-2-pro Quality Checklist](references/p-video-2-pro-quality-checklist.md)
- [p-video-2 Prompting](references/p-video-2-prompting.md)
- [p-video-2 Quality Checklist](references/p-video-2-quality-checklist.md)
- [p-video Prompting Quality Checklist](references/p-video-quality-checklist.md)
- [p-video-avatar Prompting](references/p-video-avatar-prompting.md)
- [p-video-avatar Quality Checklist](references/p-video-avatar-quality-checklist.md)
- [p-video-animate Prompting](references/p-video-animate-prompting.md)
- [p-video-animate Quality Checklist](references/p-video-animate-quality-checklist.md)
- [p-video-replace Prompting](references/p-video-replace-prompting.md)
- [p-video-replace Quality Checklist](references/p-video-replace-quality-checklist.md)
- [p-video-edit Prompting](references/p-video-edit-prompting.md)
- [p-video-edit Quality Checklist](references/p-video-edit-quality-checklist.md)
- [smixs/visual-skills](https://github.com/smixs/visual-skills)
- [inference-sh/skills](https://github.com/inference-sh/skills)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, quality checklists, and structured video request fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model-selection guidance, prompt payload structure, review checklists, and concise shell install examples.]

## Skill Version(s):

1.0.13 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
