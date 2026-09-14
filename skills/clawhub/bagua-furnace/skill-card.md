## Description:

Bagua Furnace turns books, courses, notes, web, PDF, video, audio, and discussion materials into source-grounded methodology cards for reusable decision frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and advisor-style agents use this skill to extract reusable methods from dense source material, preserve source anchors, and build a local methodology library for later retrieval and reasoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local tracking and optional cloud sync can create operational telemetry that users may not expect.

Mitigation: Review the tracking controls before installation, keep cloud sync off unless telemetry upload is intentional, and use the provided view/delete controls for local signal data.

Risk: Cloud-evolution and proposal approval workflows can apply changes based on a remote service and local creator token scope.

Mitigation: Use proposal apply or approve flows only when the service and token scope are trusted, and review proposed diffs before accepting changes.

Risk: Local logs, .anon_id state, and OCR temporary files may contain sensitive operational data.

Mitigation: Handle the skill directory and temporary extraction outputs as sensitive local data, and avoid processing confidential source material unless the local environment is appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/bagua-furnace)
- [Intro](artifact/references/intro.md)
- [Ingestion guide](artifact/references/ingestion.md)
- [Extraction lenses](artifact/references/extraction-lenses.md)
- [Method card schema](artifact/references/method-card-schema.md)
- [Long-text distillation SOP](artifact/references/long-text-distillation.md)
- [Pattern taxonomy](artifact/references/pattern-taxonomy.md)
- [Signal specification](artifact/references/signals.md)
- [Coverage backlog](artifact/references/gap-backlog.md)
- [Security audit](artifact/references/security-audit.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown methodology cards with structured fields, source anchors, optional YAML frontmatter, and occasional shell commands or configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write methodology-card files to the local methodology library and update an index; cloud sync and proposal workflows depend on local opt-in and creator registration.]

## Skill Version(s):

1.3.0 (source: server release metadata; artifact frontmatter says 1.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
