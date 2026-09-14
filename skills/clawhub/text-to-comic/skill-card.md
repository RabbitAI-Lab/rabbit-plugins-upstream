## Description:

Turn text, dialog, diary entries, photo notes, or knowledge notes into a comic, picture book, infographic, or hybrid comic+diagram with a storyboard and panel plan first, then panel-by-panel rendering, style presets, and consistent characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to convert their own stories, dialog, notes, diary entries, photo descriptions, or educational concepts into comics, picture-book spreads, infographics, or hybrid visual pages. The workflow is most useful when the user wants an editable storyboard, structured panel plan, style selection, per-panel rendering, and targeted single-panel repair.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided diary, travel, or photo descriptions may contain sensitive personal details that are sent through an image-generation workflow.

Mitigation: Ask for confirmation before rendering sensitive photo material and tell users to avoid submitting details they are not comfortable processing.

Risk: Requests may try to reproduce copyrighted source material or imitate a living artist's signature style.

Mitigation: Use user-owned or summarized material, refuse near-derivative reproduction, and steer style choices to curated presets or broad visual directions.

Risk: In-image text, especially Chinese dialogue, can become unreadable or layout-breaking.

Mitigation: Keep dialogue short, prefer captions or assembly-layer text, enforce the documented Chinese text budgets, and reserve title areas during assembly.

Risk: Panel rendering can drift in character identity, scene continuity, or visual quality across retries.

Mitigation: Maintain a compact character bible, validate each panel for consistency and clean-image requirements, and use bounded retries with fallback styles instead of silently looping.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Panel plan schema](artifact/schemas/panel-plan.schema.json)
- [Render task schema](artifact/schemas/render-task.schema.json)
- [Style presets](artifact/presets/styles.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional structured JSON artifacts for panel plans, render tasks, prompts, retry notes, and assembled visual-output instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce panel_plan.json, per-panel render task records, compiled prompts, retry notes, and final image or page assembly guidance when useful.]

## Skill Version(s):

2.3.1 (source: server release metadata; artifact changelog top entry is 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
