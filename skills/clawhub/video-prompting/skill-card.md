## Description: <br>
Use when crafting video or motion prompts for any generative model -- dramaturgy, camera, physics-safe motion, frame anchors, and clip chaining. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to draft and review short video-generation prompts for text-to-video, image-to-video, avatar, animation, replacement, audio-led, and multi-clip workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video workflows may send user-supplied images, audio, or video to external generation APIs. <br>
Mitigation: Confirm the intended provider, review companion skills separately, and avoid uploading media unless the user has permission and understands where it will be processed. <br>
Risk: Generated motion or audio-conditioned clips can fail quality checks through flicker, identity drift, desync, or unintended overlays. <br>
Mitigation: Apply the included pre-send and post-render quality checklists before using outputs in downstream edits or publication. <br>


## Reference(s): <br>
- [Prompt Dramaturgy](references/prompt-dramaturgy.md) <br>
- [Camera and Lighting Vocabulary](references/camera-lighting-vocabulary.md) <br>
- [Physics-Safe Motion](references/physics-safe-motion.md) <br>
- [Clip Chaining](references/clip-chaining.md) <br>
- [Audio-in-Video Prompting](references/audio-in-video-prompting.md) <br>
- [Scene Anchor Pair](references/scene-anchor-pair.md) <br>
- [Scene Anchor Triple](references/scene-anchor-triple.md) <br>
- [p-video Quality Checklist](references/p-video-quality-checklist.md) <br>
- [p-video-avatar Prompting](references/p-video-avatar-prompting.md) <br>
- [p-video-avatar Quality Checklist](references/p-video-avatar-quality-checklist.md) <br>
- [p-video-animate Prompting](references/p-video-animate-prompting.md) <br>
- [p-video-animate Quality Checklist](references/p-video-animate-quality-checklist.md) <br>
- [p-video-replace Prompting](references/p-video-replace-prompting.md) <br>
- [p-video-replace Quality Checklist](references/p-video-replace-quality-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured prompt text, checklists, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model-specific field guidance for video, avatar, animation, replacement, audio, and clip-continuity workflows.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
