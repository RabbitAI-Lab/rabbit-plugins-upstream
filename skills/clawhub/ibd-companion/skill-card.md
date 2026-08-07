## Description:

AI-assisted, local-first IBD recordkeeping for Crohn's disease and ulcerative colitis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[denniscriss](https://clawhub.ai/user/denniscriss)

### License/Terms of Use:

MIT

## Use Case:

External users managing personal IBD records use this skill to record, query, and summarize symptoms, infusions, labs, reviews, treatment plans, and clinician-confirmed conclusions in a local private database for visit preparation and personal tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health data is stored in a local SQLite database and may also exist in backups.

Mitigation: Keep the database and backups encrypted or otherwise access-controlled, and keep health data out of Git and ordinary notes.

Risk: Incorrect or unreviewed commands could record inaccurate health facts.

Mitigation: Review proposed commands and source values before saving; leave uncertain information empty instead of guessing.

Risk: External reminders may expose health-related timing or context if enabled unintentionally.

Mitigation: Enable external reminder delivery only after explicitly choosing the channel and timing.

## Reference(s):

- [Data entry workflow](references/data-entry.md)
- [IBD Companion schema](references/schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured recordkeeping guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local SQLite record updates and summaries; database writes require user intent and source-backed details.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
