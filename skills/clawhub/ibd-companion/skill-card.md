## Description:

AI-assisted, local-first IBD recordkeeping for Crohn's disease and ulcerative colitis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[denniscriss](https://clawhub.ai/user/denniscriss)

### License/Terms of Use:

MIT

## Use Case:

External users managing private IBD records use this skill to organize local symptom logs, infusions, checkups, review episodes, reports, clinician-confirmed assessments, and treatment or review plans for personal tracking and clinic preparation. It is a recordkeeping and planning aid, not a diagnostic, prescribing, or emergency-care tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill maintains sensitive personal health records in a local SQLite database.

Mitigation: Keep the database path private, exclude databases and attachments from Git or public issue trackers, and use access-controlled backups before upgrades or migrations.

Risk: External reminders could disclose health-related timing or treatment information if enabled without care.

Mitigation: Leave external reminder delivery disabled unless the user explicitly approves the channel and timing.

Risk: Medical records or symptoms could be misread as diagnosis, causality, or treatment advice.

Mitigation: Use the skill only for recordkeeping, planning, and descriptive summaries; preserve source wording and escalate urgent symptoms or medical decisions to professional care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/denniscriss/skills/ibd-companion)
- [Data entry workflow](references/data-entry.md)
- [IBD Companion schema](references/schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and natural-language guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update private local SQLite records only when the user explicitly authorizes record changes.]

## Skill Version(s):

0.1.1 (source: server release metadata and CHANGELOG, released 2026-08-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
