## Description:

Private IBD records, lightweight symptom-and-diet logging, plans, reviews, and trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[denniscriss](https://clawhub.ai/user/denniscriss)

### License/Terms of Use:

MIT

## Use Case:

External users and their agents use this skill to keep a private local IBD record, log daily symptoms and diet notes, organize treatment and review plans, and prepare descriptive summaries for clinical conversations. It is a recordkeeping and planning aid, not a diagnostic, prescribing, or emergency-care tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive IBD-related health records in a local SQLite database.

Mitigation: Keep the database and attachments in a private location, set IBD_DB_PATH when needed, and avoid committing or sharing private health data.

Risk: Record summaries or trend descriptions could be mistaken for medical advice.

Mitigation: Use summaries as recordkeeping support only; do not rely on the skill to diagnose, prescribe, assess disease activity, or handle urgent symptoms.

Risk: Local records may be lost or exposed if backups are not handled carefully.

Mitigation: Make encrypted or access-controlled backups outside the repository and avoid copying the database while commands are writing to it.

## Reference(s):

- [Data entry workflow](references/data-entry.md)
- [IBD Companion schema](references/schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown with optional shell commands and JSON summaries from local CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local SQLite database; bundled scripts do not require third-party Python packages or an external network service.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
