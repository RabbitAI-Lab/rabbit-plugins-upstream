## Description:

Google BigQuery (cloud.google.com). Use this skill for ANY Google BigQuery request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to inspect and operate Google BigQuery projects through an OOMOL-connected account. It supports reading metadata and table data, running SQL queries, managing datasets, tables, routines, models, and moving data with BigQuery jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include an unverified remote installer script.

Mitigation: Before installation, prefer a pinned release or downloaded installer with checksum or signature verification instead of running a pipe-to-shell command blindly.

Risk: The skill operates BigQuery through OOMOL as an intermediary for the user's connected account.

Mitigation: Verify that OOMOL is trusted for the BigQuery account before connecting credentials or running connector actions.

Risk: Write and destructive actions can create, update, overwrite, or delete BigQuery resources and data.

Mitigation: Review and explicitly approve the exact action payload and effect before running write or destructive actions.

## Reference(s):

- [ClawHub Google BigQuery Skill](https://clawhub.ai/oomol/skills/oo-google-bigquery)
- [Google BigQuery Homepage](https://cloud.google.com/bigquery)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may read, write, or delete BigQuery resources depending on the selected connector action.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
