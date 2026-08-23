## Description:

Extract an evidence-linked collaboration status card from chat logs, meeting notes, and project updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamyeed](https://clawhub.ai/user/yamyeed)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, managers, and project teams use this skill to turn English chat logs, meeting notes, and project updates into an evidence-linked status card with progress, decisions, actions, blockers, dependencies, human-review items, an executive summary, and optional exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collaboration records may contain business-sensitive information.

Mitigation: Use explicit invocation for sensitive chats or meeting notes, and review summarized content before sharing it.

Risk: Generated draft or export files may overwrite existing files when paths are reused.

Mitigation: Provide explicit --out paths and review destination filenames before running export or enforcement commands.

Risk: Unsupported owners, deadlines, decisions, or project facts could be mistaken for confirmed commitments.

Mitigation: Keep unsupported fields as Not provided, preserve evidence snippets, and route conflicts or missing owner-deadline data to human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yamyeed/skills/office-collaboration-radar-en)
- [Chinese counterpart skill page](https://clawhub.ai/yamyeed/skills/office-collaboration-radar)
- [Collaboration status card template](templates/collaboration-status-card.md)
- [JSON output schema](templates/json-output-schema.md)
- [Downstream field mapping](templates/downstream-field-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, SVG, CSV, configuration]

**Output Format:** [Markdown status card with stable JSON; optional SVG radar chart, CSV export, and Feishu or Notion mapping JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs preserve evidence snippets, use Not provided for unsupported fields, redact sensitive personal data, and keep external writes out of scope.]

## Skill Version(s):

0.1.1 (source: server release evidence and agent interface metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
