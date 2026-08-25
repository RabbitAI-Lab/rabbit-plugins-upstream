## Description:

福昕 Office 演示助编 helps an agent generate PowerPoint report decks with speaker notes, organize existing slides, and edit selected text or shapes through Fuxin Office PowerPoint tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to turn topics, reference material, or key points into editable PowerPoint presentations, and to clean up or revise an already open Fuxin Office presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad presentation-editing requests may be interpreted as permission to modify the active PowerPoint deck.

Mitigation: Use the skill only when deck edits are intended, review the resulting slides after execution, and use PowerPoint undo when changes are not desired.

Risk: The skill is write-capable and operates on the currently open presentation.

Mitigation: Confirm the correct presentation is active before use and rely on the skill's precheck and post-edit review guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-ppt)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown guidance with structured PowerPoint tool parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can cause write operations in the active PowerPoint presentation; generated changes should be reviewed after execution.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
