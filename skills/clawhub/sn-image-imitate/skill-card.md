## Description:

Generates a new image that imitates the style of a reference image while updating content based on user intent through image annotation, caption rewriting, and image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to create a new image from a reference style image and a target content request while preserving the reference image's style and layout where possible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, target prompts, generated captions, and outputs may be sent to configured SenseNova/OpenClaw provider APIs.

Mitigation: Use only provider-approved inputs and avoid confidential images, personal documents, internal-only URLs, or proprietary visuals unless that provider use is approved.

Risk: Intermediate files may be written under /tmp/openclaw/sn-image-imitate/ during execution.

Mitigation: Review local retention expectations and clean task directories when generated artifacts should not remain on disk.

Risk: The generated image is not guaranteed to match the reference at pixel level or pass the layout threshold on every attempt.

Mitigation: Review the selected image and, when needed, adjust max_attempts, layout_threshold, reference clarity, or the target content request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sensenova-skills/skills/sn-image-imitate)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [SenseNova Token Plan](https://platform.sensenova.cn/token-plan)
- [Image Annotation Prompt](artifact/prompts/image_annotate.md)
- [Caption Rewrite Prompt](artifact/prompts/caption_rewrite.md)
- [Layout Review Prompt](artifact/prompts/layout_review.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Friendly text plus a generated image path, or verbose Markdown-style status with structured JSON process artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include reference captions, layout blueprint JSON, rewritten caption, per-attempt review scores, selected generated image path, and timing details.]

## Skill Version(s):

2026.8.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
