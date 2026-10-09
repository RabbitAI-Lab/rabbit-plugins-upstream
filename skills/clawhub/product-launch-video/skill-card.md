## Description:

Turns a product URL, script, or brief into a branded promotional video with a storyboard, narration, and rendered frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to turn product sites, scripts, or briefs into launch videos and site showcases, reviewing the plan and preview before final rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable external tooling can update global skills or install registry components.

Mitigation: Run in a contained workspace and require confirmation before updates or registry additions.

Risk: Capturing commercial URLs and using local provider credentials can expose site content or incur service usage.

Mitigation: Confirm capture targets and credential use before running capture or media generation.

Risk: Preview and rendering execute external tooling and project preferences may persist.

Mitigation: Review proposed changes and obtain confirmation before preview or render; inspect saved preferences.

## Reference(s):

- [Product Launch Video on ClawHub](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Video]

**Output Format:** [Storyboard and script in Markdown, HTML video frames, and rendered MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include narration, captions, and a contact sheet; final render follows review.]

## Skill Version(s):

1.0.50 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
