## Description:

Turns text, photo descriptions, dialogue, diary entries, poems, or knowledge notes into comics, picture-book pages, infographics, or hybrid visual pages using structured storyboards and panel-by-panel rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn stories, dialogue, educational notes, travel notes, diary entries, and photo descriptions into storyboarded visual outputs. It is also useful when users need style recommendations, character consistency, per-panel retries, or targeted single-panel revisions instead of regenerating a full page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private or sensitive source material may be summarized into storyboard and image-generation prompts.

Mitigation: Avoid providing sensitive personal photos or private text unless prompt use is acceptable, and review the storyboard before rendering private or ambiguous material.

Risk: Requests based on substantial copyrighted material or exact living-artist style imitation can create rights or misuse concerns.

Mitigation: Use original or user-owned material, summarize copyrighted inputs before transformation, and avoid exact imitation of a protected living artist's signature style.

Risk: Generated panels can drift in character appearance, scene continuity, readable text, or image cleanliness.

Mitigation: Use the structured panel plan, character bible, per-panel validation, bounded retries, and single-panel repair flow before assembling the final page.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [README](artifact/README.md)
- [Panel plan schema](artifact/schemas/panel-plan.schema.json)
- [Render task schema](artifact/schemas/render-task.schema.json)
- [Style presets](artifact/presets/styles.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, image generation prompts, images, guidance]

**Output Format:** [Markdown explanations with structured JSON artifacts and generated image outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce panel_plan.json, per-panel render task records, retry notes, final panel images, and an assembled page; requires image generation capability and python3 for helper scripts.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
