## Description:

Coordinates Fuxin Office write operations into undoable batches so users can revert a grouped set of Word, Excel, or PowerPoint document changes with one undo action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Office workflow agents use this skill to group multiple document write actions into a single transaction boundary and provide clear one-step undo guidance to users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grouped write operations can change active Office documents as a batch.

Mitigation: Review proposed document changes before confirming write operations, and use the documented one-step undo action to revert the grouped batch if needed.

Risk: The skill is useful only in environments that use the related Fuxin Office bridge and active Office document workflow.

Mitigation: Install and enable it only alongside the related bridge workflow, and run the documented pre-check before starting a batch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-batch-undo)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with concise batch lifecycle and undo instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides transaction boundaries and user confirmation for document write operations; it does not provide a standalone undo tool.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
