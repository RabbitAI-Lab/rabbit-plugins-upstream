## Description:

Automates a Farsight Mysteries preparation workflow for timestamped transcription, target-informed image prompt generation, 1080p image file creation, and DaVinci Resolve timeline placement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and media-production agents use this skill to prepare Farsight Mysteries projects by converting an audio source and target sheet into timestamped visual prompts, generated image assets, and DaVinci Resolve timeline updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read the specified audio and target sheet, create generated image files beside them, and modify the currently open DaVinci Resolve timeline.

Mitigation: Confirm the exact input files and active Resolve project before execution, keep backups, and review timeline changes before saving final work.

Risk: The security evidence flags safety-filter bypass language in the image-generation workflow.

Mitigation: Review generated prompts and avoid prompt changes intended to bypass image-model safety restrictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/mysteries-prep)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with file paths, prompts, generated media instructions, and DaVinci Resolve Python API steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create generated image files beside user-provided media and modify the currently open DaVinci Resolve timeline.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
