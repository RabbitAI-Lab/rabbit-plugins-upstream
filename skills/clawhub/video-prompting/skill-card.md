## Description:

Use when crafting video or motion prompts for any generative model - dramaturgy, camera, physics-safe motion, frame anchors, and clip chaining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft, structure, and review short video-generation prompts for text-to-video, image-to-video, anchored-frame motion, clip chaining, avatar, animation, and replacement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide workflows that use paid video APIs, uploaded media, or additional skills.

Mitigation: Review the referenced tool-specific skills and avoid submitting private footage, credentials, or paid jobs until the downstream workflow is separately approved.

Risk: Generated video prompts may produce outputs with visual artifacts, motion mismatch, lip-sync issues, or replacement errors.

Mitigation: Use the included quality checklists to visually review source media, references, and generated clips before delivery or further editing.

Risk: Replacement and animation workflows may involve identifiable people, products, clothing, or source footage.

Mitigation: Confirm rights and permissions for user uploads and reference images before generating or publishing outputs.

## Reference(s):

- [Video prompt dramaturgy (`p-video`)](references/prompt-dramaturgy.md)
- [Camera and lighting vocabulary](references/camera-lighting-vocabulary.md)
- [Physics-safe motion (`p-video`)](references/physics-safe-motion.md)
- [Clip chaining (multi-scene video)](references/clip-chaining.md)
- [Audio-in-video prompting (`p-video`)](references/audio-in-video-prompting.md)
- [Scene anchor pair (visual transitions)](references/scene-anchor-pair.md)
- [Scene anchor triple (single narrated beat -> multi-scene extension)](references/scene-anchor-triple.md)
- [p-video quality checklist](references/p-video-quality-checklist.md)
- [p-video-avatar prompting](references/p-video-avatar-prompting.md)
- [p-video-avatar quality checklist](references/p-video-avatar-quality-checklist.md)
- [p-video-animate prompting](references/p-video-animate-prompting.md)
- [p-video-animate quality checklist](references/p-video-animate-quality-checklist.md)
- [p-video-replace prompting](references/p-video-replace-prompting.md)
- [p-video-replace quality checklist](references/p-video-replace-quality-checklist.md)
- [smixs/visual-skills reference material](https://github.com/smixs/visual-skills)
- [inference-sh/skills reference material](https://github.com/inference-sh/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown prose with prompt snippets, checklists, and structured prompt or payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include video prompt text, quality review criteria, shell commands, and API payload guidance for downstream tools.]

## Skill Version(s):

1.0.10 (source: evidence release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
