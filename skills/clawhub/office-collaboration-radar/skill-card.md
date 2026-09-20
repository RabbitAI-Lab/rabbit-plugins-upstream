## Description:

Extracts Chinese chat logs, meeting notes, and project collaboration text into evidence-traceable status cards with action items, risks, dependencies, confidence cues, redaction, radar charts, and stable JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamyeed](https://clawhub.ai/user/yamyeed)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, project managers, and team leads use this skill to turn Chinese collaboration materials into structured project status cards, action items, risk/dependency lists, confirmation items, and downstream field mappings. It is intended for evidence-grounded status extraction, not for sending reminders, judging performance, or writing to external project systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive meeting notes or credentials may be present in source collaboration material, and the skill's redaction is not a complete secret scanner.

Mitigation: Clean highly sensitive material before use and review generated cards, JSON, CSV, and SVG files before sharing or importing them elsewhere.

Risk: The skill prepares downstream mappings for systems such as Feishu or Notion, which could be mistaken for automatic external writes.

Mitigation: Treat generated mappings as reviewable output only; perform any external import or write action separately after human review.

Risk: Weak, conflicting, or missing source evidence can lead to conservative placeholders or items requiring human confirmation.

Mitigation: Provide the relevant chat logs, meeting notes, and project records explicitly, then review unknown and conflict markers before acting on the card.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yamyeed/skills/office-collaboration-radar)
- [English companion skill](https://clawhub.ai/yamyeed/skills/office-collaboration-radar-en)
- [Collaboration status card template](artifact/templates/collaboration-status-card.md)
- [JSON output schema](artifact/templates/json-output-schema.md)
- [Downstream field mapping](artifact/templates/downstream-field-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration guidance]

**Output Format:** [Markdown status card with structured JSON, optional CSV or mapping JSON, and optional SVG radar chart files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs retain a stable seven-module card structure, use explicit unknown and conflict markers, and require explicit output paths for local file writes.]

## Skill Version(s):

0.4.4 (source: server evidence release.version and artifact agents/office-collaboration-radar.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
