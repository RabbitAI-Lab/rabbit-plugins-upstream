## Description:

Extracts evidence-linked collaboration status cards from English chat logs, meeting notes, and project updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamyeed](https://clawhub.ai/user/yamyeed)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, project leads, and operations teams use this skill to convert English collaboration records into evidence-linked status cards with actions, decisions, risks, dependencies, human-review items, a summary, JSON, and optional exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input collaboration records may contain live credentials, customer data, or sensitive HR material that the built-in redactor may not fully catch.

Mitigation: Pre-redact sensitive source material before use and only provide the specific files needed for the task.

Risk: A generated status card can contain incorrect or unsupported owners, deadlines, decisions, or risk descriptions if source evidence is incomplete or conflicting.

Mitigation: Use the skill's evidence-grounding and human-review sections, then have stakeholders confirm unresolved or conflicting fields before acting on the card.

Risk: Downstream exports could be mistaken for authorized writes to external systems.

Mitigation: Treat CSV, Feishu, Bitable, and Notion outputs as mappings only; a user or authorized connector must perform any external write.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yamyeed/skills/office-collaboration-radar-en)
- [Publisher Profile](https://clawhub.ai/user/yamyeed)
- [Related Chinese Package](https://clawhub.ai/yamyeed/skills/office-collaboration-radar)
- [Collaboration Status Card Template](artifact/templates/collaboration-status-card.md)
- [JSON Output Schema](artifact/templates/json-output-schema.md)
- [Downstream Field Mapping](artifact/templates/downstream-field-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown status card with embedded JSON; optional SVG radar chart, CSV, Feishu mapping JSON, or Notion mapping JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence snippets are capped by the skill at 80 characters; file-producing commands require an explicit output path.]

## Skill Version(s):

0.1.2 (source: server release evidence and agent interface metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
