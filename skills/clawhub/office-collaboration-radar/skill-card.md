## Description:

Office Collaboration Radar (Chinese) turns Chinese workplace chat logs, meeting notes, and project collaboration text into stable collaboration status cards with action items, risks, dependencies, evidence snippets, priorities, radar visualization data, and structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamyeed](https://clawhub.ai/user/yamyeed)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, project managers, and team leads use this skill to convert Chinese collaboration materials into a reusable status card covering progress, confirmed decisions, Owner/DDL action items, risks, dependencies, cross-team relationships, and open confirmations. Developers can also use its JSON schema and export helpers to pass reviewed card data into downstream collaboration systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive workplace chat, meeting notes, names, contact details, and project details.

Mitigation: Review inputs before use, rely on the included redaction workflow, and provide an entities list when personal names should be masked more aggressively.

Risk: Implicit invocation could analyze collaboration text when the user intended a different task.

Mitigation: Use explicit prompts when invocation should be controlled, and confirm the requested output before processing sensitive material.

Risk: Generated action items, Owner/DDL values, or risk summaries can be wrong when the source text is ambiguous or incomplete.

Mitigation: Keep the evidence snippets, treat conflict and unavailable markers as review gates, and verify the status card before using it for decisions or downstream systems.

Risk: Saving or exporting card data can overwrite drafts or move sensitive content into files intended for sharing.

Mitigation: Use explicit output paths such as --out, review exported CSV or mapping JSON before distribution, and avoid sharing unreviewed cards outside the intended team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yamyeed/skills/office-collaboration-radar)
- [Publisher profile](https://clawhub.ai/user/yamyeed)
- [Office Collaboration Radar (English)](https://clawhub.ai/yamyeed/skills/office-collaboration-radar-en)
- [Collaboration status card template](templates/collaboration-status-card.md)
- [JSON output schema](templates/json-output-schema.md)
- [Downstream field mapping](templates/downstream-field-mapping.md)
- [Cross-turn aggregation schema](templates/cross-turn-aggregation-schema.md)
- [Action items schema](templates/action-items-schema.md)
- [Risk dependency schema](templates/risk-dependency-schema.md)
- [Confidence schema](templates/confidence-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown status card, structured JSON, CSV or field-mapping JSON exports, and SVG radar chart output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed seven-module card schema; unknown values are marked as unavailable, conflicts are marked for human confirmation, and user-sourced fields are designed for redaction and evidence retention.]

## Skill Version(s):

0.4.3 (source: server release metadata and artifact agent interface)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
