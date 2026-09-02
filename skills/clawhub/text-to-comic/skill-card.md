## Description:

Turn text, photo notes, diary entries, poems, or knowledge content into comics, picture-book spreads, infographics, or hybrid visual pages through structured storyboard planning, panel-by-panel rendering, validation, and assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and agent users use this skill to convert stories, diary entries, photo notes, dialogue, poems, or knowledge content into comics, picture-book pages, infographics, or hybrid visual pages. It is useful when the user wants an agent to plan a visual structure, choose a style, generate panels, validate the results, and assemble a finished page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User text, diary entries, photo descriptions, and generated prompts may be processed by the configured image generation system.

Mitigation: Avoid submitting private images, sensitive diary content, or other personal material unless the user is comfortable with that processing.

Risk: Substantial copyrighted third-party material or exact imitation of a living artist's signature style can create rights and misuse concerns.

Mitigation: Use user-owned material, summaries, original educational reframing, or broad non-identifying style directions instead of direct transformation or exact style cloning.

Risk: Image generation can produce embedded numbering, watermarks, unreadable text, or visual defects in individual panels.

Mitigation: Validate each panel for clean images, no numbering, no watermark, text budget, faces, character consistency, and scene continuity, then retry or fall back to a more stable style when needed.

## Reference(s):

- [Text-to-Comic ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [Publisher Profile: bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)
- [README](artifact/README.md)
- [Panel Plan Schema](artifact/schemas/panel-plan.schema.json)
- [Render Task Schema](artifact/schemas/render-task.schema.json)
- [Style Presets](artifact/presets/styles.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance, images]

**Output Format:** [Markdown guidance with structured JSON planning artifacts, generated image files, and assembled comic or infographic pages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and an enabled image generation configuration; supports panel plans, render-task records, retries, style fallback, and page assembly.]

## Skill Version(s):

2.2.0 (source: server release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
