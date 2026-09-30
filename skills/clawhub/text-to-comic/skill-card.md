## Description:

Turns user-provided stories, dialogue, diary entries, photo notes, and knowledge notes into storyboarded comics, picture books, infographics, or hybrid visual pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and other users turn their own text or notes into a visual story or explanation, with an editable storyboard and individual panel revisions before final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private diary entries, photo descriptions, or character details may be sent through the host image-generation workflow.

Mitigation: Share only material you are comfortable sending through that workflow; avoid sensitive real-person details.

Risk: Sensitive traits in a saved custom protagonist card may be reused in later panels or sessions.

Mitigation: Do not save sensitive traits in custom character cards unless that reuse is intentional.

## Reference(s):

- [Text-to-Comic on ClawHub](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [Panel plan schema](artifact/schemas/panel-plan.schema.json)
- [Render task schema](artifact/schemas/render-task.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Images]

**Output Format:** [Storyboard summary and panel plan, with generated panel images or an assembled page when rendering is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports storyboard-only output, style changes, and regeneration of selected panels.]

## Skill Version(s):

2.4.2 (source: ClawHub release, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
