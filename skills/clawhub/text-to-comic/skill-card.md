## Description:

Text-to-Comic turns user text, photo descriptions, or knowledge notes into comics, picture-book pages, or infographics through a structured storyboard, panel rendering, validation, and assembly workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and developers use this skill to convert stories, dialog, diary entries, photo notes, or concepts into storyboarded comic, picture-book, infographic, or hybrid visual outputs that can be revised panel by panel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use local Python helpers that read panel plans, bundled assets, and image paths, then write assembled image files.

Mitigation: Review user-supplied panel plans and image paths before execution, especially paths outside the project, and direct generated outputs to an expected workspace location.

Risk: Image generation may produce embedded numbering, watermarks, unreadable text, or inconsistent characters.

Mitigation: Use the render-task validation checks for clean images, no numbering, no watermark, text budget, face quality, character consistency, and scene continuity before accepting panels.

Risk: Requests involving private photos or copyrighted third-party material can change the review needs before rendering.

Mitigation: Confirm sensitive-photo use cases before rendering and summarize or reframe copyrighted source material instead of directly reproducing protected text or art.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [Style Presets](presets/styles.json)
- [Panel Plan Schema](schemas/panel-plan.schema.json)
- [Render Task Schema](schemas/render-task.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON panel plans and render-task records, shell commands for helper scripts, and references to generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Python helpers, bundled presets and schemas, and image generation configuration when producing and assembling panels.]

## Skill Version(s):

2.1.0 (source: server release evidence and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
