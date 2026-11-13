## Description:

Creates code-drawn stickman videos with a jointed figure, timed captions, procedural sound, and optional voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to plan, build, and render animated stickman shorts locally, with optional narration and a code-based SVG rig.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documented install commands do not pin exact package versions, and some files were not fully inspected.

Mitigation: Review the skill and its dependencies before execution, and pin package versions when installing.

Risk: Optional voice generation may send narration text to an external provider.

Mitigation: Do not submit sensitive narration unless you are comfortable sharing it with the selected provider.

## Reference(s):

- [Stickman rig API reference](references/rig.md)
- [VARG how-to](https://varg.ai/how-to)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/stickman-video)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance, Video files]

**Output Format:** [Markdown guidance, JavaScript and HTML source, and rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 1080x1920 at 30 fps with timed captions and sound; may include a contact sheet. Voice generation is optional.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
