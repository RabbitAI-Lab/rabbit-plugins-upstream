## Description: <br>
Use when crafting video or motion prompts for any generative model — dramaturgy, camera, physics-safe motion, frame anchors, and clip chaining. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative technologists, and content teams use this skill to draft and review short video-generation prompts for text-to-video, image-to-video, frame-anchor, audio-led, clip-chaining, avatar, animate, and replacement workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using this prompt-writing skill with related Pruna or API skills may upload user media to external generation services or make paid API calls. <br>
Mitigation: Confirm rights to input media, understand the external service path before use, and review generated outputs before publishing. <br>
Risk: The skill is guidance for prompt construction rather than a standalone generator. <br>
Mitigation: Pair it with the appropriate generation, API, or review workflow and validate outputs against the included quality checklists. <br>


## Reference(s): <br>
- [Video prompt dramaturgy (`p-video`)](artifact/references/prompt-dramaturgy.md) <br>
- [Camera and lighting vocabulary](artifact/references/camera-lighting-vocabulary.md) <br>
- [Physics-safe motion (`p-video`)](artifact/references/physics-safe-motion.md) <br>
- [Clip chaining (multi-scene video)](artifact/references/clip-chaining.md) <br>
- [Audio-in-video prompting (`p-video`)](artifact/references/audio-in-video-prompting.md) <br>
- [Scene anchor pair (visual transitions)](artifact/references/scene-anchor-pair.md) <br>
- [Scene anchor triple (single narrated beat to multi-scene extension)](artifact/references/scene-anchor-triple.md) <br>
- [p-video quality checklist](artifact/references/p-video-quality-checklist.md) <br>
- [p-video-avatar prompting](artifact/references/p-video-avatar-prompting.md) <br>
- [p-video-avatar quality checklist](artifact/references/p-video-avatar-quality-checklist.md) <br>
- [p-video-animate prompting](artifact/references/p-video-animate-prompting.md) <br>
- [p-video-animate quality checklist](artifact/references/p-video-animate-quality-checklist.md) <br>
- [p-video-replace prompting](artifact/references/p-video-replace-prompting.md) <br>
- [p-video-replace quality checklist](artifact/references/p-video-replace-quality-checklist.md) <br>
- [smixs/visual-skills](https://github.com/smixs/visual-skills) <br>
- [inference-sh/skills](https://github.com/inference-sh/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with prompt patterns, checklists, and JSON-like prompt payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; downstream prompts may be used with external video generation services.] <br>

## Skill Version(s): <br>
1.0.7 (source: evidence.release.version and artifact metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
