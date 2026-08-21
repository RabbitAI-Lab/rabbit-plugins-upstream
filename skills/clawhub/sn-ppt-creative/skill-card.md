## Description:

Creative-mode PPT pipeline that generates one full-page 16:9 PNG per slide, using LLM/VLM steps for style, outline, and prompts and a text-to-image path for slide rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-generation agents use this hidden creative-mode sub-skill through sn-ppt-entry to turn prepared deck inputs into visually rich slide images and, when packaging succeeds, a PowerPoint deck. It is intended for workflows that need full-slide generated visuals rather than editable slide components.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deck content and reference images may be sent through the configured model and image-generation pipeline.

Mitigation: Avoid secrets in prompts or reference material, and redact sensitive deck inputs before running the skill.

Risk: Generated slide images can contain incorrect or misleading text or visuals.

Mitigation: Review the generated PNG pages and PPTX before external use, especially for business facts, numbers, and claims.

Risk: Dependency drift in python-pptx can change PPTX packaging behavior.

Mitigation: Pin python-pptx in deployment environments and review packaging output during release validation.

Risk: Prompt sanitization diagnostics or logs may expose sensitive prompt fragments.

Mitigation: Restrict or redact logs for sensitive business decks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-ppt-creative)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown and shell-command guidance for the agent; generated artifacts include style_spec.md, outline.json, per-page prompt text, PNG slide images, and a PPTX file when packaging succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires task_pack.json, info_pack.json, a pages directory, SN_IMAGE_BASE, and PPT_STANDARD_DIR; creative slides are rendered as full-page 16:9 images.]

## Skill Version(s):

2026.8.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
