## Description:

Text-to-Comic turns user-provided text, photo descriptions, dialogue, diary entries, poems, or knowledge notes into structured storyboards and panel-by-panel visual outputs such as comics, picture-book spreads, infographics, or hybrid comic diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to convert stories, dialogue, diary or photo notes, poems, and knowledge content into comics, picture-book spreads, infographics, or hybrid visual pages. The skill helps an agent plan panels, select visual style presets, preserve character and scene continuity, validate panels, retry local failures, and assemble the final visual deliverable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private photos, sensitive diary content, or other personal source material may be used in an image-generation workflow.

Mitigation: Avoid providing private or sensitive material unless the user is comfortable with that processing, and ask for confirmation before rendering sensitive photo-derived content.

Risk: Substantial copyrighted source text or requests to imitate a living artist's distinctive style may create rights or style-cloning concerns.

Mitigation: Use user-owned or summarized material, avoid near-derivative reproduction, and avoid promising exact imitation of protected living-artist styles.

Risk: Chinese captions or examples may be followed when the user's preferred output language is ambiguous.

Mitigation: Ask for or honor the user's preferred output language, and keep generated captions concise enough for readable layout.

## Reference(s):

- [Text-to-Comic ClawHub listing](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [Style preset registry](artifact/presets/styles.json)
- [Panel plan schema](artifact/schemas/panel-plan.schema.json)
- [Render task schema](artifact/schemas/render-task.schema.json)
- [Chinese webtoon example](artifact/examples/chinese-webtoon-demo.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with structured JSON panel plans, render tasks, retry notes, and image-generation prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce panel_plan.json, per-panel render task records, compiled prompts, concise storyboard summaries, and final assembly guidance when useful.]

## Skill Version(s):

2.3.0 (source: server release metadata and artifact CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
