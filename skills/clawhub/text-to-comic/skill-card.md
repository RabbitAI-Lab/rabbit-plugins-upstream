## Description:

Text-to-Comic turns user-provided text into visual works such as comics, picture books, or infographics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn diary entries, stories, poems, dialogs, knowledge explanations, or travel notes into storyboarded comics, picture-book scenes, or infographics with style recommendations and character-consistency checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User text or reference photos may be processed by the configured image-generation provider.

Mitigation: Avoid submitting private photos or sensitive text unless the user is comfortable with that processing.

Risk: Copyrighted source text or reference material could be transformed into derivative visual output.

Mitigation: Use original, summarized, or rights-cleared material and avoid directly submitting third-party creative works.

Risk: Generated panels may contain inconsistent characters, scene discontinuities, unwanted text, or visual artifacts.

Mitigation: Review the storyboard and generated panels before release, using the skill's character-consistency, scene-continuity, and clean-image checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-comic)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Files]

**Output Format:** [Markdown storyboard tables, image-generation prompts, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output assembled PNG or JPEG comics from generated panels; requires python3 and image generation to be enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
